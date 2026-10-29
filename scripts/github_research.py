#!/usr/bin/env python3
"""Run the existing container installation on GitHub and explicitly hand it on."""
import argparse
import base64
from contextlib import contextmanager
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
import tomllib
import zipfile
from urllib.error import HTTPError, URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from wake.hosted import GitHub, HostedState
from wake.installation_cli import NODE_IDS, build_public_artifact, request, upload_public_artifact

WORKFLOW = 'research-worker.yml'
RUNTIME_POLICY = Path(__file__).resolve().parents[1] / 'hosted-runtime.json'


def api():
    directory = os.environ.get('WAKE_HOSTED_STATE_DIR')
    return GitHub(os.environ['GITHUB_REPOSITORY'], os.environ['GH_TOKEN'],
                  rate_file=Path(directory) / 'github-rate.json' if directory else None)


def enabled(client):
    try:
        return client.request(f'actions/workflows/{WORKFLOW}')['state'] == 'active'
    except HTTPError as error:
        if error.code == 404:
            return False
        raise


def runtime_policy(client):
    """A source release does not implicitly upgrade a bound installation's records."""
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        # Checkout intentionally selects runtime_ref, which cannot contain its
        # own final commit hash. The dispatch's immutable workflow commit owns
        # the operator binding; never substitute the candidate's older pin or a
        # moving master read. A missing/unreadable binding fails before restore.
        revision = os.environ.get('GITHUB_SHA', '')
        if not re.fullmatch('[0-9a-f]{40}', revision):
            raise ValueError('Hosted runtime policy requires its workflow commit')
        blob = client.request('contents/hosted-runtime.json?ref=' + revision)
        if (blob.get('type') != 'file' or blob.get('encoding') != 'base64'
                or not isinstance(blob.get('content'), str) or len(blob['content']) > 32768):
            raise ValueError('Hosted runtime policy is not a bounded file')
        policy = json.loads(base64.b64decode(''.join(blob['content'].split()), validate=True))
    else:
        if not RUNTIME_POLICY.exists():
            return None
        policy = json.loads(RUNTIME_POLICY.read_text())
    if policy.get('schema') != 1 or not isinstance(policy.get('installations'), dict):
        raise ValueError('Invalid hosted runtime policy; refusing automatic promotion')
    selected = policy['installations'].get(client.repository)
    if selected is None:
        return None
    if (not isinstance(selected, dict)
            or (selected.get('source_revision') is not None and not re.fullmatch('[0-9a-f]{40}', str(selected['source_revision'])))
            or selected.get('decision_memory_mode', 'off') not in ('off', 'shadow', 'active')
            or ('research_expansion_enabled' in selected and type(selected['research_expansion_enabled']) is not bool)
            or ('research_candidate_catalog_enabled' in selected and type(selected['research_candidate_catalog_enabled']) is not bool)
            or ('autonomous_context_improvement' in selected and type(selected['autonomous_context_improvement']) is not bool)
            or ('experimental_research_enabled' in selected and type(selected['experimental_research_enabled']) is not bool)
            or (selected.get('autonomous_context_improvement') is True and selected.get('decision_memory_mode') != 'active')
            or not re.fullmatch('[0-9a-f]{32}', str(selected.get('installation_id', '')))):
        raise ValueError('Invalid hosted installation binding')
    if 'provider_pacing' in selected:
        from wake.provider_pacing import CallPacing
        limits=tomllib.loads((Path(__file__).resolve().parents[1]/'wake.toml').read_text())['model_daily_call_limits']
        CallPacing(selected['provider_pacing'],limits)
    return selected


def checked_revision(client):
    policy = runtime_policy(client)
    pinned = policy.get('source_revision') if policy else None
    query = ('head_sha=' + pinned) if pinned else 'branch=master'
    runs = client.request('actions/workflows/test.yml/runs?' + query + '&status=success&per_page=20')['workflow_runs']
    for run in runs:
        if (run['event'] in ('push', 'workflow_dispatch') and run['head_branch'] == 'master'
                and (not pinned or run['head_sha'] == pinned)):
            return run['head_sha']
    raise ValueError('The selected runtime has no successful master CI; refusing automatic promotion')


def apply_decision_memory_policy(root, policy):
    """Apply the operator's installation setting before any worker is admitted."""
    if not policy or 'decision_memory_mode' not in policy:
        return
    from wake.report import atomic_write
    mode = policy['decision_memory_mode']
    if mode not in ('off', 'shadow', 'active'):
        raise ValueError('Invalid hosted decision memory mode')
    autonomy = policy.get('autonomous_context_improvement', False)
    if type(autonomy) is not bool or (autonomy and mode != 'active'):
        raise ValueError('Invalid hosted autonomous context grant')
    path = root / 'config/wake.toml'
    original = path.read_text()
    # Change only the root TOML key; preserve per-member topics and all tables.
    lines = original.splitlines(keepends=True)
    found = False
    for index, line in enumerate(lines):
        if line.lstrip().startswith('['):
            break
        if re.match(r'^\s*decision_memory_mode\s*=', line):
            lines[index] = f'decision_memory_mode = "{mode}"\n'
            found = True
    updated = ''.join(lines) if found else f'decision_memory_mode = "{mode}"\n' + original
    lines = updated.splitlines(keepends=True)
    found = False
    for index, line in enumerate(lines):
        if line.lstrip().startswith('['):
            break
        if re.match(r'^\s*autonomous_context_improvement\s*=', line):
            lines[index] = 'autonomous_context_improvement = ' + str(autonomy).lower() + '\n'
            found = True
    updated = ''.join(lines) if found else 'autonomous_context_improvement = ' + str(autonomy).lower() + '\n' + updated
    if tomllib.loads(updated).get('decision_memory_mode') != mode:
        raise ValueError('Hosted decision memory configuration did not validate')
    if tomllib.loads(updated).get('autonomous_context_improvement') is not autonomy:
        raise ValueError('Hosted autonomous context configuration did not validate')
    atomic_write(path, updated)
    print(json.dumps({'decision_memory_mode': mode, 'autonomous_context_improvement': autonomy,
                      'scope': 'hosted-installation'}), flush=True)


def apply_experimental_research_policy(root,policy):
    """Only an explicit operator binding grants isolated scientific execution."""
    from wake.report import atomic_write
    enabled=(policy or {}).get('experimental_research_enabled',False)
    if type(enabled) is not bool:raise ValueError('Invalid hosted scientific grant')
    path=root/'config/wake.toml'
    lines=path.read_text().splitlines(keepends=True)
    replacement='experimental_research_enabled = '+str(enabled).lower()+'\n'
    found=False
    for index,line in enumerate(lines):
        if line.lstrip().startswith('['):break
        if re.match(r'^\s*experimental_research_enabled\s*=',line):lines[index]=replacement;found=True
    updated=''.join(lines) if found else replacement+''.join(lines)
    if tomllib.loads(updated).get('experimental_research_enabled') is not enabled:
        raise ValueError('Hosted scientific grant did not validate')
    atomic_write(path,updated)
    print(json.dumps({'experimental_research_enabled':enabled,'scope':'hosted-installation'}),flush=True)


def inspect_provider_schedule(transport,policy):
    """Read only the authenticated scheduling file; never restore authority."""
    from wake.provider_pacing import CallPacing
    manifest=transport.read_manifest()
    with tempfile.TemporaryDirectory() as temporary:
        path=Path(temporary)/'aux.zip'
        transport.get_file(manifest['auxiliary'],path)
        with zipfile.ZipFile(path) as archive:
            matches=[e for e in archive.infolist() if e.filename=='provider-schedule.json']
            if len(matches)!=1 or matches[0].file_size>32768:
                raise ValueError('A single bounded scheduling checkpoint is required')
            saved=json.loads(archive.read(matches[0]))
    limits=tomllib.loads((Path(__file__).resolve().parents[1]/'wake.toml').read_text())['model_daily_call_limits']
    pacing=CallPacing(policy['provider_pacing'],limits)
    pacing.restore(saved['pacing'])
    return {'installation_id':manifest['installation_id'],'generation':manifest['generation'],
        'captured_at':manifest['captured_at'],'pacing':pacing.dump(),
        'configured_daily_calls':pacing.total,'reserved_daily_calls':pacing.policy['reserve_calls'],
        'remaining_at_capture_by_model':{m:max(0,n-pacing.usage.get(m,0)) for m,n in limits.items()},
        'feature_remaining_at_capture':max(0,pacing.policy['reserve_calls']-pacing.feature_used),
        'limits':'Dated scheduling evidence; later or outside API use can reduce capacity.'}


def apply_provider_pacing_policy(root,policy):
    """Apply an explicit scheduling grant without rewriting retained records."""
    if not policy or 'provider_pacing' not in policy:return
    from wake.provider_pacing import CallPacing
    from wake.report import atomic_write
    path=Path(root)/'config/wake.toml'
    original=path.read_text();settings=tomllib.loads(original)
    value=policy['provider_pacing']
    CallPacing(value,settings.get('model_daily_call_limits'))
    replacement='provider_pacing = { enabled = '+str(value['enabled']).lower()+', target_hours = '+str(value['target_hours'])+', reserve_calls = '+str(value['reserve_calls'])+' }\n'
    lines=original.splitlines(keepends=True);found=False
    for index,line in enumerate(lines):
        if line.lstrip().startswith('['):break
        if re.match(r'^\s*provider_pacing\s*=',line):lines[index]=replacement;found=True
    updated=''.join(lines) if found else replacement+original
    if tomllib.loads(updated).get('provider_pacing')!=value:raise ValueError('Hosted provider pacing did not validate')
    atomic_write(path,updated)
    print(json.dumps({'provider_pacing':value,'scope':'hosted-installation'}),flush=True)


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
        # Older queued entries can outlive their actual scheduling state.
        # Only a newer run can supersede this predecessor. The workflow's
        # installation-wide concurrency group still serializes every writer.
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


@contextmanager
def measured_stage(name):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(json.dumps({'hosted_stage': name,
                          'elapsed_seconds': round(time.perf_counter()-start, 3)}), flush=True)


def capture_all(transport, root):
    for node in NODE_IDS:
        transport.checkpoint_node(root / 'nodes' / node / 'record')


def publish_hosted_snapshot(client, root, artifact, revision, *, research_start=None):
    """Publish pinned completed exports without stopping workers or opening records."""
    parent = client.request('git/ref/heads/wake-public')['object']['sha']
    manifest = build_public_artifact(root, artifact, progress=lambda message: print(message, flush=True))
    if (root/'experimental-reset.json').exists():
        manifest['experimental_reset'] = json.loads((root/'experimental-reset.json').read_text())
    manifest['hosted_execution'] = {'source_revision': revision,
        'run_id': os.environ.get('GITHUB_RUN_ID'), 'captured_at': datetime.now(timezone.utc).isoformat()}
    if research_start is not None:
        manifest['hosted_execution']['research_start'] = research_start
    for path in [artifact / 'installation.json', *[artifact / 'nodes' / n / 'installation.json' for n in NODE_IDS]]:
        path.write_text(json.dumps(manifest, sort_keys=True))
    from wake.hosted_presentation import bind_hosted_status
    bind_hosted_status(artifact, client.repository, revision)
    authorization = base64.b64encode(('x-access-token:' + client.token).encode()).decode()
    os.environ.update(GIT_CONFIG_COUNT='1', GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
                      GIT_CONFIG_VALUE_0='AUTHORIZATION: basic ' + authorization)
    upload_public_artifact(artifact, 'https://github.com/' + client.repository + '.git',
                           'wake-public', expected_head=parent)
    # Readers discover this immutable public commit directly. Data publication
    # must not queue an interface deployment or fail because Pages is busy.
    return manifest


class PeriodicPublication:
    """Independent mirror delivery; final publication waits for a healthy upload."""
    def __init__(self, client, root, revision, interval=1800):
        self.client, self.root, self.revision, self.interval = client, root, revision, interval
        self.closed = threading.Event()
        self.thread = threading.Thread(target=self.run, daemon=True)

    def run(self):
        # Publish acknowledged startup promptly; the first interval must not
        # hide a healthy restart behind the previous batch's observations.
        while not self.closed.is_set():
            try:
                with tempfile.TemporaryDirectory(prefix='wake-hosted-mirror-') as temporary:
                    publish_hosted_snapshot(self.client, self.root, Path(temporary) / 'site', self.revision)
                print(json.dumps({'hosted_mirror': 'published'}), flush=True)
            except Exception as error:
                # A concurrent public refresh or transient upload error cannot
                # stop research. The next interval or final capture retries.
                print(json.dumps({'hosted_mirror': 'unavailable', 'reason': type(error).__name__}), flush=True)
            if self.closed.wait(self.interval):
                break

    def close(self, *, wait=True):
        self.closed.set()
        if wait and self.thread.is_alive():
            self.thread.join()


def run_batch(minutes, provider, *, reset=False):
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
    if policy and policy.get('source_revision') and revision != policy['source_revision']:
        raise ValueError('This installation requires its pinned runtime; record compatibility must be verified before promotion')
    checks = client.request(f'actions/workflows/test.yml/runs?head_sha={revision}&status=success&per_page=20')['workflow_runs']
    if not any(item['head_sha'] == revision and item['head_branch'] == 'master' for item in checks):
        raise ValueError('Source revision has not passed repository CI')
    transport = HostedState.from_environment()
    transport.open()
    root = Path(os.environ['WAKE_INSTALLATION_DATA']).resolve()
    with measured_stage('restore'):
        before = transport.restore(root, workers=3, fresh_experiment=reset)
    if policy and before['installation_id'] != policy['installation_id']:
        raise ValueError('Restored installation differs from the runtime binding; no controller started')
    apply_decision_memory_policy(root, policy)
    apply_provider_pacing_policy(root,policy)
    apply_experimental_research_policy(root,policy)
    if policy and 'research_expansion_enabled' in policy:
        from wake.research_expansion import apply_hosted_configuration
        apply_hosted_configuration(root, policy['research_expansion_enabled'],
                                   policy.get('research_candidate_catalog_enabled', False))
    print(json.dumps({'restored_installation': before['installation_id'],
                      'generation': before['generation'],
                      'heads': {n: d['head'] for n, d in before['nodes'].items()}}), flush=True)
    stopped = False
    control_error = None
    start_error = None
    research_start = None
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
        mirror = PeriodicPublication(client, root, revision)
        try:
            with measured_stage('startup'):
                ready(root, process)
            print(json.dumps({'hosted_provider_admission':request(root,{'action':'status'}).get('coordinator',{})}),flush=True)
            if reset:
                # Explicit reset restored setup only. The stopped controller
                # bootstrapped fresh records; never restore/audit discarded data.
                print(json.dumps({'experimental_reset': transport.reset(root, 'Operator-requested cycle-zero reset')}), flush=True)
            # Recovery is committed in the owning SQLite record. The batch's
            # final state transfer carries it to the next runner.
            if enabled(client) and not stopped:
                with measured_stage('start-acknowledgment'):
                    start = request(root, {'action': 'start'})
                research_start = {'ok': bool(start.get('ok')),
                    'acknowledged_nodes': sorted(node for node, value in start.get('nodes', {}).items()
                                                 if value.get('state') == 'acknowledged')}
                if not start.get('ok'):
                    # Admission is already running. Preserve healthy workers
                    # while keeping unavailable/late acknowledgments visible.
                    # With no confirmed worker, close this batch and publish
                    # its saved exports; the successor retries from checkpoints.
                    print(json.dumps({'hosted_start': 'degraded',
                                      'nodes': start.get('nodes', {})}), flush=True)
                    # Inspect only bounded operational controls/observations.
                    # No native record, provider body or credential enters logs.
                    controls = {}
                    for node in NODE_IDS:
                        base = root / 'nodes' / node
                        def observation(path, fields):
                            try:
                                with path.open('rb') as stream:
                                    value = json.loads(stream.read(32769))
                                if not isinstance(value, dict):
                                    return {'unavailable': True}
                                return {key: value[key] for key in fields if key in value}
                            except (OSError, ValueError):
                                return {'unavailable': True}
                        controls[node] = {
                            'control': observation(base / 'record' / '.wake-runner-control.json',
                                ('research', 'command_id', 'pause_at', 'pause_after_group_checkpoint', 'pause_after_group_introduction')),
                            'runtime': observation(base / 'runtime.json',
                                ('state', 'control_ack', 'observed_at', 'reason'))}
                    print(json.dumps({'hosted_start_observations': controls}), flush=True)
                    if not any(value.get('state') == 'acknowledged'
                               for value in start.get('nodes', {}).values()):
                        stopped = True
                        start_error = RuntimeError('No research worker acknowledged Start; state and public data were retained')
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
            with measured_stage('drain'):
                drained = request(root, {'action': 'stop'})
            print(json.dumps({'hosted_provider_admission':request(root,{'action':'status'}).get('coordinator',{})}),flush=True)
            if not drained.get('ok'):
                # Stop already closed new-call admission. A slow/dead worker
                # cannot withhold the public mirror indefinitely. Terminate the
                # owned processes below, retain their coherent native journals,
                # and let the next bootstrap recover interrupted invocations.
                print(json.dumps({'hosted_drain': 'bounded-shutdown',
                                  'nodes': drained.get('nodes', {})}), flush=True)
        finally:
            process.terminate()
            try:
                process.wait(timeout=210)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            mirror.close(wait=False)
    if process.returncode != 0:
        raise RuntimeError('Hosted controller did not shut down cleanly')
    with measured_stage('final-checkpoint'):
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
    with measured_stage('data-publication'):
        manifest = publish_hosted_snapshot(client, root, artifact, revision, research_start=research_start)
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
    if start_error is not None:
        # Recovery sees a failed batch after its safe capture/publication,
        # rather than a green workflow that never admitted research.
        raise start_error


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='action', required=True)
    run = commands.add_parser('run')
    run.add_argument('--minutes', type=float, default=120)
    run.add_argument('--provider', choices=('fixture', 'gemini'), default='gemini')
    run.add_argument('--reset', action='store_true', help='Discard experimental results and start at cycle zero; no archive')
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
        if os.environ.get('WAKE_HOSTED_STATE_KEY'):
            with tempfile.TemporaryDirectory(prefix='wake-schedule-inspect-') as directory:
                transport=HostedState(directory,client.repository,client.token,os.environ['WAKE_HOSTED_STATE_KEY'])
                transport.open()
                print(json.dumps({'hosted_provider_schedule':inspect_provider_schedule(transport,runtime_policy(client))}),flush=True)
    elif args.action == 'continue':
        continue_chain(args.predecessor)
    elif args.action == 'control':
        control(args.intent)
    else:
        if not 0 < args.minutes <= 180:
            raise ValueError('Hosted run must have a bounded duration')
        run_batch(args.minutes, args.provider, reset=args.reset)


if __name__ == '__main__':
    main()
