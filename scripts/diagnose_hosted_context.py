#!/usr/bin/env python3
"""Build requests on disposable checkpoint copies, with no provider or control capability."""
import argparse
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wake.hosted import HostedState, record_identity
from wake.installation_cli import NODE_IDS
from scripts.verify_hosted_upgrade import SnapshotFiles, restore_audit_nodes

PROGRAM = r'''
import json,socket,sys,ssl
from pathlib import Path
def forbidden(*args,**kwargs):raise RuntimeError('Network disabled for request-capacity diagnostic')
socket.socket=forbidden
import wake.engine as module
from wake.authority import open_authoritative_store
from wake.providers import provider_input_chars
root=Path(sys.argv[1]);settings=module.config(sys.argv[2]);phase=sys.argv[3]
store=open_authoritative_store(root)
engine=module.Engine(root,settings,store=store)
last=[None];parts={}
original=module.provider_input_chars
def counted(request):
    size=original(request);last[0]=size
    parts.clear();parts.update(system=len(request.get('system','')),response_schema=len(module.canonical(request.get('response_schema',{}))),
        context_fields={key:len(module.canonical(value)) for key,value in request.get('context',{}).items()},
        memory_fields={key:len(module.canonical(value)) for key,value in request.get('context',{}).get('memory',{}).items()})
    return size
module.provider_input_chars=counted
result={'phase':phase,'limit':settings['max_context_chars'],'provider_calls':0}
try:
    if store.load().get('pending') is not None:
        result['status']='pending_invocation_not_modified'
    else:
        invocation,request=engine.start('gemini',settings['model'],False,phase=phase)
        result.update(status='fits',input_chars=provider_input_chars(request))
except Exception as error:
    reason=str(error)
    category=('context_ceiling' if 'Context ceiling reached' in reason else
              'decision_memory_budget' if 'Decision memory exceeded' in reason else 'request_build_failed')
    result.update(status=category,error_class=type(error).__name__,input_chars=last[0],parts=parts)
finally:store.close()
print(json.dumps(result,sort_keys=True))
'''


def probe_node(source, record, config, *, node, runner=subprocess.check_output):
    results = []
    original = record_identity(record)
    with tempfile.TemporaryDirectory(prefix='wake-context-probe-') as temporary:
        for phase in ('planning', 'proposal'):
            destination = Path(temporary) / phase
            destination.mkdir()
            with sqlite3.connect(record.resolve().as_uri() + '?mode=ro', uri=True) as before:
                with sqlite3.connect(destination / 'wake.sqlite') as after:
                    before.backup(after)
            env = {key: os.environ[key] for key in ('PATH', 'LANG', 'LC_ALL', 'TZ', 'LD_LIBRARY_PATH', 'DYLD_LIBRARY_PATH') if key in os.environ}
            env.update(PYTHONPATH=str(source.resolve()), PYTHONDONTWRITEBYTECODE='1',
                       HOME=temporary, WAKE_DEV_RELOAD='false', WAKE_GROUP_INSTANCE=node,
                       WAKE_PARENT_HOSTNAME='' if node[:3].endswith('00') else node[0] + '00.wake')
            parent = node[0] + '00.wake'
            topics = config.parent / '.wake-runner-topics' / (parent + '.toml')
            if topics.is_file():
                env['WAKE_GROUP_TOPIC_FILE'] = str(topics)
            try:
                output = runner([sys.executable, '-c', PROGRAM, str(destination), str(config), phase],
                                cwd=source, env=env, text=True, timeout=600, stderr=subprocess.PIPE)
            except (subprocess.SubprocessError, OSError) as error:
                raise ValueError('Isolated request diagnostic stopped: ' + type(error).__name__) from None
            result = json.loads(output)
            if result.get('phase') != phase or result.get('provider_calls') != 0:
                raise ValueError('Invalid isolated capacity result')
            results.append(result)
    if record_identity(record) != original:
        raise ValueError('Diagnostic changed its restored source record')
    return results


def blocked_observation(manifest, policy, run_id):
    """A public warning can trigger investigation, never a record/control change."""
    if (manifest.get('schema') != 1 or manifest.get('live') is not False
            or manifest.get('installation_id') != policy['installation_id']
            or str(manifest.get('hosted_execution', {}).get('run_id')) != str(run_id)
            or not isinstance(manifest.get('nodes'), list)
            or {node.get('id') for node in manifest['nodes']} != set(NODE_IDS)
            or len(manifest['nodes']) != len(NODE_IDS)):
        return []
    return [node['id'] for node in manifest['nodes']
            if node.get('recorded_runtime', {}).get('state') == 'blocked']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot', type=Path, required=True)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--policy', type=Path, required=True)
    parser.add_argument('--node', choices=NODE_IDS, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--candidate', action='store_true', help='Explicit offline candidate comparison; never promotes it')
    args = parser.parse_args()
    repository = os.environ['GITHUB_REPOSITORY']
    policy = json.loads(args.policy.read_text())['installations'][repository]
    revision = subprocess.check_output(['git', '-C', str(args.source), 'rev-parse', 'HEAD'], text=True).strip()
    if revision != policy['source_revision'] and not args.candidate:
        raise ValueError('Diagnostic must use the actual bound runtime source')
    with tempfile.TemporaryDirectory(prefix='wake-context-restore-') as temporary:
        root = Path(temporary)
        transport = HostedState(root / 'transport', repository, 'offline', os.environ['WAKE_HOSTED_STATE_KEY'])
        transport.checkout = args.snapshot.resolve()
        manifest = transport.read_manifest()
        if manifest['installation_id'] != policy['installation_id']:
            raise ValueError('Checkpoint installation differs from policy')
        transport.api = SnapshotFiles(args.snapshot, manifest)
        records = root / 'records'
        restore_audit_nodes(transport, manifest, records, (args.node,))
        with zipfile.ZipFile(records / 'aux.zip') as archive:
            selected = [entry for entry in archive.infolist() if entry.filename == 'config/wake.toml']
            if len(selected) != 1 or selected[0].file_size > 1_000_000:
                raise ValueError('Bounded saved configuration required')
            required = {'config/wake.toml', 'config/research-topics.toml',
                        'config/.wake-runner-topics/' + args.node[0] + '00.wake.toml'}
            found = set()
            for entry in archive.infolist():
                if entry.filename not in required:
                    continue
                if entry.filename in found or entry.file_size > 1_000_000:
                    raise ValueError('Duplicate or oversized saved configuration')
                found.add(entry.filename)
                target = root / entry.filename
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(archive.read(entry))
            configuration = root / 'config/wake.toml'
        result = {'schema':'wake-context-capacity-diagnostic@1','installation_id':manifest['installation_id'],
                  'generation':manifest['generation'],'captured_at':manifest['captured_at'],
                  'node':args.node,'source_revision':revision,'bound_revision':policy['source_revision'],
                  'candidate_probe':args.candidate,'remote_record_writes':0,
                  'boundary':'Disposable checkpoint copies only; no live-worker diagnosis or provider attempt.',
                  'requests':probe_node(args.source, records / 'nodes' / args.node / 'record/wake.sqlite', configuration, node=args.node)}
        args.output.write_text(json.dumps(result, indent=2) + '\n')
        print(json.dumps(result))


if __name__ == '__main__':
    main()
