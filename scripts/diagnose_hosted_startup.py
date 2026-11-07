"""Reproduce the failed node's startup on one verified disposable copy."""
import json
import os
from pathlib import Path
import subprocess
import sys
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wake.hosted import HostedState
from scripts.verify_hosted_upgrade import restore_audit_nodes
from scripts.github_research import (apply_decision_memory_policy,
    apply_provider_pacing_policy, apply_experimental_research_policy)

PROGRAM = r'''
import json,sys,traceback
from pathlib import Path
from wake.standalone import bootstrap, publish, config
root=Path(sys.argv[1]);record=root/'nodes/300.wake/record'
phase='bootstrap'
try:
    settings=config(root/'config/wake.toml')
    settings['provider_managed_limits']=True
    engine=bootstrap(record,settings)
    phase='export'
    site=root/'site';site.mkdir()
    if not publish(engine,site):raise RuntimeError('Startup publication not completed')
except Exception as exc:
    source=Path.cwd()
    frames=[]
    for frame in traceback.extract_tb(exc.__traceback__):
        path=Path(frame.filename)
        if path.is_relative_to(source/'wake'):
            frames.append({'file':str(path.relative_to(source)), 'line':frame.lineno, 'function':frame.name})
    print(json.dumps({'failure':type(exc).__name__,'phase':phase,'frames':frames}),flush=True)
    sys.exit(1)
print(json.dumps({'startup_export':'verified','node':'300.wake'}),flush=True)
'''


def main():
    transport=HostedState.from_environment();transport.open()
    manifest=transport.read_manifest()
    root=Path(os.environ['WAKE_INSTALLATION_DATA'])
    policy=json.loads(Path('hosted-runtime.json').read_text())['installations'][os.environ['GITHUB_REPOSITORY']]
    if manifest['installation_id']!=policy['installation_id']:raise ValueError('Diagnostic identity mismatch')
    restore_audit_nodes(transport,manifest,root,('300.wake',))
    with zipfile.ZipFile(root/'aux.zip') as archive:
        for entry in archive.infolist():
            path=Path(entry.filename)
            if path.parts[:1]!=('config',) or path.suffix!='.toml':continue
            if '..' in path.parts or entry.file_size>1_000_000:raise ValueError('Invalid diagnostic configuration')
            target=root/path;target.parent.mkdir(parents=True,exist_ok=True)
            with target.open('xb') as output:output.write(archive.read(entry))
    apply_decision_memory_policy(root,policy)
    apply_provider_pacing_policy(root,policy)
    apply_experimental_research_policy(root,policy)
    from wake.research_expansion import apply_hosted_configuration
    apply_hosted_configuration(root,policy['research_expansion_enabled'],policy['research_candidate_catalog_enabled'])
    env={key:os.environ[key] for key in ('PATH','LANG','LC_ALL','LD_LIBRARY_PATH') if key in os.environ}
    env.update(PYTHONPATH=str(Path.cwd()),WAKE_GROUP_ID='wake',WAKE_GROUP_INSTANCE='300.wake',
               WAKE_PUBLIC_HOSTNAME='300.wake',WAKE_GROUP_PEERS='100.wake,200.wake,301.wake,302.wake,303.wake',
               WAKE_PARENT_HOSTNAME='',WAKE_GROUP_TOPIC_FILE=str(root/'config/.wake-runner-topics/300.wake.toml'),
               WAKE_INSTALLATION_WORKER='1',WAKE_DEV_RELOAD='false')
    print(json.dumps({'diagnostic_generation':manifest['generation'],'provider_calls':0,'remote_record_writes':0}),flush=True)
    return subprocess.run([sys.executable,'-c',PROGRAM,str(root)],env=env,timeout=180).returncode

if __name__=='__main__':sys.exit(main())
