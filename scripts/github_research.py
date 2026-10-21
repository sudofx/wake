#!/usr/bin/env python3
"""Run the existing container installation on GitHub and explicitly hand it on."""
import argparse
import base64
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tempfile
import threading
import time
from urllib.error import HTTPError, URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from wake.hosted import GitHub, HostedState
from wake.installation_cli import NODE_IDS, build_public_artifact, request, upload_public_artifact

WORKFLOW = 'hosted-research.yml'
RUNTIME_POLICY = Path(__file__).resolve().parents[1] / 'hosted-runtime.json'


def api():
    return GitHub(os.environ['GITHUB_REPOSITORY'], os.environ['GH_TOKEN'])


def enabled(client):
    try:
        return client.request(f'actions/workflows/{WORKFLOW}')['state'] == 'active'
    except HTTPError as error:
        if error.code == 404:
            return False
        raise


def runtime_policy(client):
    """A source release does not implicitly upgrade a bound installation's records."""
    if not RUNTIME_POLICY.exists():
        return None
    policy = json.loads(RUNTIME_POLICY.read_text())
    if policy.get('schema') != 1 or not isinstance(policy.get('installations'), dict):
        raise ValueError('Invalid hosted runtime policy; refusing automatic promotion')
    selected = policy['installations'].get(client.repository)
    if selected is None:
        return None
    if (not isinstance(selected, dict)
            or not re.fullmatch('[0-9a-f]{40}', str(selected.get('source_revision', '')))
            or not re.fullmatch('[0-9a-f]{32}', str(selected.get('installation_id', '')))):
        raise ValueError('Invalid hosted installation binding')
    return selected


def checked_revision(client):
    policy = runtime_policy(client)
    query = ('head_sha=' + policy['source_revision']) if policy else 'branch=master'
    runs = client.request('actions/workflows/test.yml/runs?' + query + '&status=success&per_page=20')['workflow_runs']
    for run in runs:
        if (run['event'] in ('push', 'workflow_dispatch') and run['head_branch'] == 'master'
                and (not policy or run['head_sha'] == policy['source_revision'])):
            return run['head_sha']
    raise ValueError('The selected runtime has no successful master CI; refusing automatic promotion')


def control(action):
    client = api()
    operation = 'enable' if action == 'start' else 'disable'
    client.request(f'actions/workflows/{WORKFLOW}/{operation}', method='PUT')
    if action == 'start':
        revision = checked_revision(client)
        client.request(f'actions/workflows/{WORKFLOW}/dispatches', method='POST', body={
            'ref': 'master', 'inputs': {'handoff': 'start-' + os.environ['GITHUB_RUN_ID'],
                                     'runtime_ref': revision}})
    print('Hosted research ' + action + ' requested. Existing records are preserved.')


def continue_chain(predecessor):
    client = api()
    if not enabled(client):
        print('Hosted research is stopped; no successor dispatched.')
        return
    token = 'after-' + str(predecessor)
    previous = client.request('actions/runs/' + str(int(predecessor)))
    if previous['path'] != '.github/workflows/' + WORKFLOW or previous['head_branch'] != 'master':
        raise ValueError('Handoff predecessor is not a master research run')
    # The normal handoff and completion-event recovery share one Actions
    # concurrency group. The dispatch identity makes retries idempotent.
    for page in range(1, 4):
        runs = client.request(f'actions/workflows/{WORKFLOW}/runs?per_page=100&page={page}')['workflow_runs']
        if any(run['run_number'] > previous['run_number'] for run in runs):
            # Run numbers survive static workflow naming and completed successors.
            # A delayed recovery must never restart an obsolete chain.
            print('A newer research run already owns continuation.')
            return
        if any(run.get('display_title') == 'WAKE hosted ' + token for run in runs):
            print('Successor already exists for ' + str(predecessor))
            return
        if any(str(run['id']) != str(predecessor) and run['status'] != 'completed' for run in runs):
            # A manual start or a different recovered chain already owns
            # continuation. An old completion event must not seed another one.
            print('Another research run already owns continuation.')
            return
        if len(runs) < 100:
            break
    revision = checked_revision(client)
    client.request(f'actions/workflows/{WORKFLOW}/dispatches', method='POST', body={
        'ref': 'master', 'inputs': {'handoff': token, 'runtime_ref': revision}})
    print('Dispatched successor from checked source ' + revision)


def ready(root, process, timeout=900):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError('Hosted installation exited during startup')
        try:
            status = request(root, {'action': 'status'})
            if all(node.get('available') and node.get('runtime', {}).get('state') in ('stopped', 'paused')
                   for node in status['nodes']):
                return
        except (OSError, ValueError, KeyError):
            pass
        time.sleep(2)
    raise TimeoutError('Hosted node startup did not finish within fifteen minutes')


def capture_all(transport, root):
    for node in NODE_IDS:
        transport.checkpoint_node(root / 'nodes' / node / 'record')


def publish_hosted_snapshot(client, root, artifact, revision):
    """Publish pinned completed exports without stopping workers or opening records."""
    parent = client.request('git/ref/heads/wake-public')['object']['sha']
    manifest = build_public_artifact(root, artifact, progress=lambda message: print(message, flush=True))
    manifest['hosted_execution'] = {'source_revision': revision,
        'run_id': os.environ.get('GITHUB_RUN_ID'), 'captured_at': datetime.now(timezone.utc).isoformat()}
    for path in [artifact / 'installation.json', *[artifact / 'nodes' / n / 'installation.json' for n in NODE_IDS]]:
        path.write_text(json.dumps(manifest, sort_keys=True))
    from wake.hosted_presentation import bind_hosted_status
    bind_hosted_status(artifact, client.repository, revision)
    authorization = base64.b64encode(('x-access-token:' + client.token).encode()).decode()
    os.environ.update(GIT_CONFIG_COUNT='1', GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
                      GIT_CONFIG_VALUE_0='AUTHORIZATION: basic ' + authorization)
    upload_public_artifact(artifact, 'https://github.com/' + client.repository + '.git',
                           'wake-public', expected_head=parent)
    client.request('pages/builds', method='POST', body={})
    return manifest


class PeriodicPublication:
    """Independent mirror delivery; final publication waits for a healthy upload."""
    def __init__(self, client, root, revision, interval=1800):
        self.client, self.root, self.revision, self.interval = client, root, revision, interval
        self.closed = threading.Event()
        self.thread = threading.Thread(target=self.run, daemon=True)

    def run(self):
        while not self.closed.wait(self.interval):
            try:
                with tempfile.TemporaryDirectory(prefix='wake-hosted-mirror-') as temporary:
                    publish_hosted_snapshot(self.client, self.root, Path(temporary) / 'site', self.revision)
                print(json.dumps({'hosted_mirror': 'published'}), flush=True)
            except Exception as error:
                # A concurrent public refresh or transient upload error cannot
                # stop research. The next interval or final capture retries.
                print(json.dumps({'hosted_mirror': 'unavailable', 'reason': type(error).__name__}), flush=True)

    def close(self, *, wait=True):
        self.closed.set()
        if wait and self.thread.is_alive():
            self.thread.join()


def run_batch(minutes, provider):
    client = api()
    # An unreadable stop latch closes admission promptly. Checkpoint transport
    # may wait for quota after draining, but research cannot assume intent.
    client.rate_wait_limit = 0
    if not enabled(client):
        print('Hosted research disabled; no records or providers opened.')
        return
    revision = os.environ['WAKE_SOURCE_REVISION']
    if not re.fullmatch('[0-9a-f]{40}', revision):
        raise ValueError('Hosted source must be a complete commit identity')
    policy = runtime_policy(client)
    if policy and revision != policy['source_revision']:
        raise ValueError('This installation requires its pinned runtime; record compatibility must be verified before promotion')
    checks = client.request(f'actions/workflows/test.yml/runs?head_sha={revision}&status=success&per_page=20')['workflow_runs']
    if not any(item['head_sha'] == revision and item['head_branch'] == 'master' for item in checks):
        raise ValueError('Source revision has not passed repository CI')
    transport = HostedState.from_environment()
    transport.open()
    root = Path(os.environ['WAKE_INSTALLATION_DATA']).resolve()
    before = transport.restore(root, workers=3)
    if policy and before['installation_id'] != policy['installation_id']:
        raise ValueError('Restored installation differs from the runtime binding; no controller started')
    print(json.dumps({'restored_installation': before['installation_id'],
                      'generation': before['generation'],
                      'heads': {n: d['head'] for n, d in before['nodes'].items()}}), flush=True)
    stopped = False
    control_error = None
    def stop_signal(*_):
        nonlocal stopped
        stopped = True
    signal.signal(signal.SIGTERM, stop_signal)
    signal.signal(signal.SIGINT, stop_signal)
    log_path = root / 'controller.log'
    manifest = None
    with log_path.open('ab') as log:
        process = subprocess.Popen([sys.executable, '-m', 'wake.installation', '--data', str(root),
            '--config', str(root / 'config/wake.toml'), '--host', '127.0.0.1', '--port', '0',
            '--provider', provider], stdout=log, stderr=log,
            env=dict(os.environ, WAKE_DEV_RELOAD='false'))
        from wake.hosted_activity import HostedActivityPublisher
        activity = HostedActivityPublisher(root, before['installation_id'], os.environ.get('GITHUB_RUN_ID'), revision)
        mirror = PeriodicPublication(client, root, revision)
        activity.start()
        try:
            ready(root, process)
            # Bootstrap can recover interrupted native invocations. Persist that
            # recovery before admitting any new provider call.
            capture_all(transport, root)
            if enabled(client) and not stopped:
                start = request(root, {'action': 'start'})
                if not start.get('ok'):
                    # Admission is already running. Preserve healthy workers
                    # while keeping unavailable/late acknowledgments visible.
                    # With no confirmed worker, close this batch and publish
                    # its saved exports; the successor retries from checkpoints.
                    print(json.dumps({'hosted_start': 'degraded',
                                      'nodes': start.get('nodes', {})}), flush=True)
                    if not any(value.get('state') == 'acknowledged'
                               for value in start.get('nodes', {}).values()):
                        stopped = True
            if not stopped:
                mirror.thread.start()
            deadline = time.monotonic() + minutes * 60
            next_intent_check = 0
            while not stopped and time.monotonic() < deadline:
                if process.poll() is not None:
                    raise RuntimeError('Hosted controller exited unexpectedly')
                if time.monotonic() >= next_intent_check:
                    try:
                        continuing = enabled(client)
                    except (HTTPError, URLError, TimeoutError) as error:
                        control_error = error
                        print(json.dumps({'hosted_control': 'unavailable',
                                          'reason': type(error).__name__}), flush=True)
                        break
                    if not continuing:
                        break
                    next_intent_check = time.monotonic() + 60
                time.sleep(1)
            drained = request(root, {'action': 'stop'})
            if not drained.get('ok'):
                # Stop already closed new-call admission. A slow/dead worker
                # cannot withhold the public mirror indefinitely. Terminate the
                # owned processes below, retain their coherent native journals,
                # and let the next bootstrap recover interrupted invocations.
                print(json.dumps({'hosted_drain': 'bounded-shutdown',
                                  'nodes': drained.get('nodes', {})}), flush=True)
        finally:
            activity.close()
            process.terminate()
            try:
                process.wait(timeout=210)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            mirror.close(wait=False)
    if process.returncode != 0:
        raise RuntimeError('Hosted controller did not shut down cleanly')
    capture_all(transport, root)
    # Native recovery is saved before waiting for independent delivery. Do not
    # race a final publication against a healthy periodic uploader.
    mirror.close()
    if control_error is not None:
        # Preserve all drained records and finish a healthy upload before
        # reporting the control failure to the independent recovery workflow.
        raise control_error
    # Publication is derived and independently recoverable. Preserve authority
    # before a rendering/upload error can fail the run.
    artifact = Path(os.environ['WAKE_HOSTED_ARTIFACT'])
    manifest = publish_hosted_snapshot(client, root, artifact, revision)
    with transport.lease():
        transport.prune()
    after = transport.read_manifest()
    print(json.dumps({'status': 'checkpointed-and-published', 'installation_id': manifest['installation_id'],
                      'generation': after['generation'], 'source_revision': revision,
                      'record_heads': manifest['record_heads']}), flush=True)
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a') as stream:
            stream.write('Native records checkpointed; public snapshot uploaded. Pages builds separately.\n')
            stream.write('Source: `' + revision + '`\n')
            for node, value in manifest['record_heads'].items():
                stream.write(f'- {node}: version {value["version"]}, head `{value["head"]}`\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='action', required=True)
    run = commands.add_parser('run')
    run.add_argument('--minutes', type=float, default=120)
    run.add_argument('--provider', choices=('fixture', 'gemini'), default='gemini')
    chain = commands.add_parser('continue')
    chain.add_argument('--predecessor', required=True)
    commands.add_parser('inspect')
    command = commands.add_parser('control')
    command.add_argument('intent', choices=('start', 'stop'))
    args = parser.parse_args()
    if args.action == 'inspect':
        client = api()
        state = enabled(client)
        print(json.dumps({'hosted_enabled': state, 'api_rate': client.rate}), flush=True)
    elif args.action == 'continue':
        continue_chain(args.predecessor)
    elif args.action == 'control':
        control(args.intent)
    else:
        if not 0 < args.minutes <= 180:
            raise ValueError('Hosted run must have a bounded duration')
        run_batch(args.minutes, args.provider)


if __name__ == '__main__':
    main()
