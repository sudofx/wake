"""Observer failures expire normally and retry without touching authority."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch
from wake.activity import RuntimeActivity
from wake.standalone import emit_runtime_status

class ObserverRecoveryTests(unittest.TestCase):
    def test_transient_atomic_replace_failure_does_not_kill_heartbeat(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'runtime.json'
            server=SimpleNamespace(runtime_status={'mode':'standalone','state':'running'},activity=RuntimeActivity(),snapshot_generation=2)
            class Stop:
                ticks=0
                def is_set(self):return self.ticks>=2
                def wait(self,_):self.ticks+=1
            import os
            replace=os.replace;calls=[]
            def flaky(*args):
                calls.append(args)
                if len(calls)==1:raise OSError('PRIVATE path')
                return replace(*args)
            output=io.StringIO()
            with patch('wake.standalone.os.replace',side_effect=flaky),redirect_stdout(output):
                emit_runtime_status(server,path,Stop())
            value=json.loads(path.read_text())
            self.assertEqual(value['runtime_id'],server.activity.runtime_id)
            self.assertEqual(value['state'],'running')
            self.assertIn('recovered',output.getvalue())
            self.assertNotIn('PRIVATE',output.getvalue())
