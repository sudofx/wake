"""Start intent is observable before slow preparation; drainage is never implied."""
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from wake.standalone import acknowledge_research_start


class StartAcknowledgmentTests(unittest.TestCase):
    def test_start_receipt_does_not_wait_for_editorial_or_provider_work(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, '.wake-runner-control.json').write_text(json.dumps({'research':'running','command_id':'start-1'}))
            server=SimpleNamespace(runtime_status={'state':'stopped'})
            acknowledge_research_start(server,d,'running',None,None)
            self.assertEqual(server.control_ack,'start-1')
            self.assertEqual(server.runtime_status['state'],'waiting')
            server.runtime_status={'state':'running','reason':'Working'}
            acknowledge_research_start(server,d,'running',None,None)
            self.assertEqual(server.runtime_status['reason'],'Working')

    def test_stop_or_pending_reset_cannot_be_acknowledged_as_drained(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, '.wake-runner-control.json').write_text(json.dumps({'research':'running','command_id':'start-1'}))
            server=SimpleNamespace(runtime_status={'state':'stopped'})
            acknowledge_research_start(server,d,'stopped',None,None)
            acknowledge_research_start(server,d,'running','reset-1',None)
            self.assertFalse(hasattr(server,'control_ack'))
