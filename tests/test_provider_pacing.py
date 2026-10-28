"""A simulated day verifies global rate, reserves, restart and confirmation safety."""
from copy import deepcopy
from datetime import datetime
import io
import json
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stdout
from zoneinfo import ZoneInfo

from wake.installation_gate import InstallationCallCoordinator
from wake.provider_pacing import CallPacing


LIMITS={'lite-a':500,'lite-b':500,'flash-a':20,'flash-b':20}
POLICY={'enabled':True,'target_hours':24,'reserve_calls':208}


class ProviderPacingTests(unittest.TestCase):
    def setUp(self):
        self.now=datetime(2026,10,28,tzinfo=ZoneInfo('America/Los_Angeles')).timestamp()
        self.pacing=CallPacing(POLICY,LIMITS)
        self.gate=InstallationCallCoordinator(clock=lambda:self.now,queue_ttl=100000,pacing=self.pacing)
    def take(self,index,model='lite-a',purpose='research',confirmed=False):
        key=('wake',str(index%12),str(index))
        return key,self.gate.acquire(key,model,confirmation_required=confirmed,purpose=purpose)
    def release(self,key,grant):
        self.assertTrue(self.gate.release(key,grant['token'],{'result':'success'}))

    def test_full_day_across_twelve_nodes_preserves_208_feature_requests(self):
        started=self.now
        for index in range(832):
            if index:self.now=started+index*self.pacing.interval+.000001
            key,grant=self.take(index,'lite-a' if index<500 else 'lite-b')
            self.assertEqual(grant['status'],'granted')
            self.release(key,grant)
            queued=self.take(10000+index,'lite-b')[1]
            self.assertEqual(queued['status'],'queued')
            self.gate.cancel_request(('wake',str((10000+index)%12),str(10000+index)))
        self.assertGreater((self.now-started)/3600,23.9)
        self.assertEqual(self.pacing.research_used,832)
        self.assertEqual(self.take(20000,'lite-b')[1]['reason'],'research_budget')
        for index in range(208):
            model='lite-b' if index<168 else 'flash-a' if index<188 else 'flash-b'
            key,grant=self.take(30000+index,model,'experiment')
            self.assertEqual(grant['status'],'granted')
            self.release(key,grant)
        self.assertEqual(sum(self.pacing.usage.values()),1040)
        self.assertEqual(self.take(40000,'lite-b','reader')[1]['reason'],'research_budget')

    def test_confirmed_grants_count_once_and_lost_reservations_do_not_count(self):
        key,grant=self.take(1,confirmed=True)
        self.assertEqual(self.pacing.research_used,0)
        self.assertTrue(self.gate.cancel_request(key))
        self.assertFalse(self.gate.confirm(key,grant['token']))
        key,grant=self.take(2,confirmed=True)
        self.assertTrue(self.gate.confirm(key,grant['token']))
        self.assertTrue(self.gate.confirm(key,grant['token']))
        self.assertEqual(self.pacing.research_used,1)
        self.release(key,grant)
        self.assertFalse(self.gate.release(key,grant['token']))
        self.assertEqual(self.pacing.research_used,1)

    def test_restart_and_long_idle_never_create_a_burst(self):
        key,grant=self.take(1);self.release(key,grant)
        packet=self.gate.dump_state()
        gate=InstallationCallCoordinator(clock=lambda:self.now,pacing=CallPacing(POLICY,LIMITS))
        gate.restore_state(packet)
        self.assertEqual(gate.acquire(('wake','b','first'),'lite-b')['reason'],'pacing')
        self.now+=3600
        next_grant=gate.acquire(('wake','b','first'),'lite-b')
        self.assertEqual(next_grant['status'],'granted')
        gate.release(('wake','b','first'),next_grant['token'])
        self.assertEqual(gate.acquire(('wake','c','next'),'lite-b')['reason'],'pacing')
        self.assertEqual(gate.pacing.research_used,2)

    def test_reserved_feature_can_bypass_a_paced_head_without_overlapping(self):
        key,grant=self.take(1);self.release(key,grant)
        self.assertEqual(self.take(2)[1]['reason'],'pacing')
        key,grant=self.take(3,purpose='reader')
        self.assertEqual(grant['status'],'granted')
        self.now+=200
        self.assertEqual(self.take(4)[1]['status'],'queued')
        self.release(key,grant)
        self.assertEqual(self.take(2)[1]['status'],'granted')

    def test_failed_attempts_consume_allowance_and_rollover_preserves_spacing(self):
        self.now=datetime(2026,10,28,23,59,50,tzinfo=ZoneInfo('America/Los_Angeles')).timestamp()
        key,grant=self.take(1)
        self.gate.release(key,grant['token'],{'result':'http_failure','http_status':500})
        self.now+=11
        self.assertEqual(self.take(2)[1]['reason'],'pacing')
        self.assertEqual(self.pacing.research_used,0)
        self.now+=104
        self.assertEqual(self.take(2)[1]['status'],'granted')
        self.assertEqual(self.pacing.research_used,1)

    def test_native_usage_backfill_never_erases_reserved_attempts(self):
        key,grant=self.take(1);self.release(key,grant)
        self.pacing.seed(self.pacing.day,{'lite-a':300,'lite-b':200})
        self.assertEqual(self.pacing.research_used,500)
        self.pacing.seed(self.pacing.day,{'lite-a':200})
        self.assertEqual(self.pacing.research_used,500)
        self.pacing.seed('2000-01-01',{'lite-a':500})
        self.assertEqual(self.pacing.research_used,500)

    def test_malformed_policy_or_state_fails_closed(self):
        for changes in ({'reserve_calls':1040},{'target_hours':0},{'enabled':'true'}):
            with self.assertRaises(ValueError):CallPacing({**POLICY,**changes},LIMITS)
        self.pacing.status(self.now);bad=self.pacing.dump();bad['research_used']=1
        with self.assertRaises(ValueError):self.pacing.restore(bad)
        self.assertEqual(self.pacing.research_used,0)

    def test_both_reserve_and_model_budgets_are_enforced(self):
        self.pacing.status(self.now)
        self.pacing.seed(self.pacing.day,{'flash-a':20})
        self.assertEqual(self.take(1,'flash-a','experiment')[1]['reason'],'research_budget')
        self.assertEqual(self.take(2,'flash-b','experiment')[1]['status'],'granted')

    def test_hosted_policy_updates_the_restored_configuration(self):
        import tomllib
        from scripts.github_research import apply_provider_pacing_policy
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'config').mkdir()
            path=root/'config/wake.toml'
            path.write_text('model_daily_call_limits = { a = 500, b = 500, c = 20, d = 20 }\n[unchanged]\nvalue = "keep"\n')
            with redirect_stdout(io.StringIO()):apply_provider_pacing_policy(root,{'provider_pacing':POLICY})
            data=tomllib.loads(path.read_text())
            self.assertEqual(data['provider_pacing'],POLICY)
            self.assertEqual(data['unchanged'],{'value':'keep'})
            before=path.read_bytes()
            with self.assertRaises(ValueError):apply_provider_pacing_policy(root,{'provider_pacing':{**POLICY,'reserve_calls':1040}})
            self.assertEqual(path.read_bytes(),before)

    def test_persistence_failure_does_not_free_a_confirmed_paced_slot(self):
        key,grant=self.take(1,confirmed=True);self.gate.confirm(key,grant['token'])
        def fail(packet):raise OSError('Synthetic failed scheduling persistence')
        with self.assertRaises(OSError):self.gate.release(key,grant['token'],persist=fail)
        self.now+=1000
        self.assertEqual(self.take(2,'lite-b')[1]['status'],'queued')
        self.assertEqual(self.pacing.research_used,1)

    def test_zero_effect_gate_denials_are_not_charged_requests(self):
        from wake.scheduling import charged_request_slots
        self.assertEqual(charged_request_slots({'provider_attempts':[
            {'result':'research_budget','provider_call_made':False},{'result':'success'},
            {'result':'unknown'}]}),2)
