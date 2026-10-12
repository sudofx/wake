"""Shared model editorial publication, complete membership and narrow exception."""
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch
import os
from support import charter_settings
from wake.authority import open_authoritative_store
from wake.engine import Engine
from wake.event_format import digest
from wake.governance import Rejected
from wake.group_editorial import input_snapshot, publication, validate_inputs, INTRO_ID
from wake.providers import Fixture


class Writer:
    name, model, charged = 'fixture', 'group-editorial-fixture', False
    def __init__(self, article=None):
        self.article = article or {'title':'Our shared beginning', 'lede':'Bob introduces the group.',
            'body':('We are investigating physical memory and prediction. These are open questions, not proven results. '
                    'The record shows what each worker attempted, and the Console lets readers inspect receipts. ' * 9)
                   + '\n\nSummary\n\nWe are beginning together. Questions remain open.',
            'lens':'A shared story must include every worker and retain uncertainty.'}
    def propose(self, request):
        self.request = request
        return json.dumps(self.article), {}


class GroupEditorialTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.engines = []
        self.members = ['100.wake', '101.wake']
        for n in self.members:
            root = Path(self.temp.name)/n
            e = Engine(root, charter_settings(), store=open_authoritative_store(root, allow_initialize=True))
            e.run(Fixture())
            e.store.append('group_bob_enrolled', {'actor':'operator', 'group_id':'wake', 'members':self.members,
                                                'leader':self.members[0], 'member':n})
            self.engines.append(e)
        self.packet = {'schema':1, 'group_id':'wake', 'members':self.members, 'leader':self.members[0],
                       'inputs':[input_snapshot(e,'wake',n) for e,n in zip(self.engines,self.members)]}
    def tearDown(self):
        for e in self.engines: e.store.close()
        self.temp.cleanup()
    def draft(self, writer=None):
        e = self.engines[0]; writer = writer or Writer()
        with e.store.lock(): r=e.synthesize_group(writer,self.packet,1)
        self.assertEqual(r['status'],'editorial_completed')
        return publication(self.packet,1,r['article'],r['id'],{'name':writer.name,'model':writer.model})
    def grant(self,e,p):
        e.store.append('group_bob_exception_granted', {'actor':'operator','checkpoint':1,'publication_digest':digest(p),
                                                     'reason':'Explicit one-time operator WAKE01 permission.'})
    def test_identical_article_all_members_no_research_progress_and_replay(self):
        p=self.draft()
        for e in self.engines:
            before=deepcopy(e.store.load()); self.grant(e,p)
            e.store.append('group_bob_published',{'publication':p})
            after=e.store.load()
            for key in ('version','journal','evidence','notebooks','attention','commitments','projects'):
                self.assertEqual(after[key],before[key])
            self.assertEqual(after['posts'][INTRO_ID]['body'],p['article']['body'])
            self.assertEqual(after['posts']['wake-introduction']['status'],'superseded')
            self.assertEqual(e.store.audit()[0],after)
            self.assertEqual(e.store.record.incomplete_invocations(),())
            from wake.report import export
            export(e.store, Path(self.temp.name)/('site-'+after['group_bob']['member']))
    def test_fresh_group_first_wake_uses_model_synthesis_without_static_welcome(self):
        for e,n in zip(self.engines,self.members):
            e.store.reset(); e.initialize()
            e.store.append('group_bob_enrolled',{'actor':'operator','group_id':'wake','members':self.members,'leader':self.members[0],'member':n})
            self.assertEqual(e.store.load()['posts'],{})
        self.packet['inputs']=[input_snapshot(e,'wake',n) for e,n in zip(self.engines,self.members)]
        p=self.draft()
        for e in self.engines:
            e.store.append('group_bob_published',{'publication':p})
            self.assertEqual(e.store.load()['version'],0)
            self.assertNotIn('wake-introduction',e.store.load()['posts'])
            self.assertEqual(e.store.audit()[0],e.store.load())

    def test_partial_inputs_rejected_before_call(self):
        packet=deepcopy(self.packet); packet['inputs'].pop()
        with self.assertRaises(Rejected): validate_inputs(packet)
    def test_startup_synthesizes_zero_progress_children_and_never_repeats_failed_inference(self):
        from wake.group_editorial import synchronize
        for e,n in zip(self.engines,self.members):
            e.store.reset(); e.initialize()
            e.store.append('group_bob_enrolled',{'actor':'operator','group_id':'wake','members':self.members,'leader':self.members[0],'member':n})
        self.packet['inputs']=[input_snapshot(e,'wake',n) for e,n in zip(self.engines,self.members)]
        class Bad(Writer):
            calls=0
            def propose(self,r):
                self.calls+=1
                return '{bad',{}
        writer=Bad(); e=self.engines[0]
        def response(url):
            return self.packet if url.endswith('bob-inputs.json') else None
        with patch.dict(os.environ, {'WAKE_GROUP_COORDINATOR_URL':'http://000.wake/group/coordinator',
                                    'WAKE_PUBLIC_HOSTNAME':self.members[0]}), patch('wake.group_editorial.fetch',side_effect=response):
            synchronize(e,writer)
            synchronize(e,writer)
        self.assertEqual(writer.calls,1)
        self.assertEqual(e.store.load()['version'],0)
        self.assertEqual(e.store.load()['posts'],{})
        self.assertEqual(e.store.record.incomplete_invocations(),())
    def test_exception_cannot_publish_changed_article_research_actions_or_another_checkpoint(self):
        p=self.draft(Writer({'title':'Short first post','lede':'Welcome.','body':'This welcome is intentionally short.','lens':'Open questions.'}))
        e=self.engines[0]; self.grant(e,p)
        changed=deepcopy(p); changed['article']['body']='A changed article.'
        with self.assertRaises(Rejected): e.store.append('group_bob_published',{'publication':changed})
        with self.assertRaises(Rejected): e.store.append('group_bob_published',{'publication':p,'actions':[{'type':'research'}]})
        e.store.append('group_bob_published',{'publication':p})
        with self.assertRaises(Rejected): self.grant(e,p)
        with self.assertRaises(Rejected): e.store.append('group_bob_published',{'publication':p})

    def test_later_shared_publication_requests_one_leader_private_note(self):
        from wake.group_editorial import synchronize
        from wake.governance import _bob_quiet_window
        initial = self.draft()
        for engine in self.engines:
            self.grant(engine, initial)
            engine.store.append('group_bob_published', {'publication': initial})
        leader = self.engines[0]
        due = 1 + _bob_quiet_window({**leader.store.load()['posts'][INTRO_ID], 'created_version': 1})
        for item in self.packet['inputs']:
            item['version'] = due
        def response(url):
            return self.packet if url.endswith('bob-inputs.json') else None
        from wake.passenger import Workspace
        workspace = Workspace(Path(self.temp.name) / 'private-notes', 'group-wake')
        class ReflectingWriter(Writer):
            private_calls = 0
            def propose(inner, request):
                if 'advisory_assessments' in request.get('context', {}):
                    inner.private_calls += 1
                    note = {key: 'A useful private reflection' for key in
                            ('title', 'assessment', 'evidence', 'candidate_change', 'verification')}
                    note.update(status='hypothesis', confidence='low')
                    return json.dumps({'observations': [note]}), {}
                return super().propose(request)
        writer = ReflectingWriter()
        writer.article['title'] = 'Our later shared reflection'
        with patch.dict(os.environ, {'WAKE_GROUP_COORDINATOR_URL': 'http://000.wake/group/coordinator',
                                    'WAKE_PUBLIC_HOSTNAME': self.members[0]}), \
                patch('wake.group_editorial.fetch', side_effect=response), \
                patch('wake.passenger.resolve', return_value=workspace):
            synchronize(leader, writer)
            synchronize(leader, writer)
        self.assertEqual(leader.store.load()['group_bob']['checkpoint'], due)
        self.assertEqual(writer.private_calls, 1)
        self.assertIn('A useful private reflection', workspace.path.read_text())
        notes = [i for i in leader.store.load()['invocations'].values() if i.get('phase') == 'passenger']
        self.assertEqual(notes[-1]['group_checkpoint'], due)
        child = self.engines[1]
        with patch.dict(os.environ, {'WAKE_GROUP_COORDINATOR_URL': 'http://000.wake/group/coordinator',
                                    'WAKE_PUBLIC_HOSTNAME': self.members[1]}), \
                patch('wake.group_editorial.fetch', side_effect=response), \
                patch.object(child, 'assess_passenger') as child_assess:
            synchronize(child, Writer())
        child_assess.assert_not_called()
    def test_private_quota_deferral_retries_on_a_new_pacific_day(self):
        from wake.group_editorial import _assess_group_note
        from datetime import datetime, timedelta
        from zoneinfo import ZoneInfo
        engine = self.engines[0]
        state = engine.store.load()
        today = datetime.now(ZoneInfo(engine.config['timezone'])).date()
        deferred = {'phase': 'passenger', 'group_checkpoint': 19,
                    'time': '2026-01-01T00:00:00+00:00', 'quota_day': today.isoformat(),
                    'quota_exhausted': 'free_tier_daily', 'status': 'deferred'}
        state['invocations'] = {'private': deferred}
        published = {'checkpoint': 19, 'inputs': self.packet}
        with patch.object(engine.store, 'load', return_value=state), \
                patch.object(engine, 'assess_passenger') as assess:
            _assess_group_note(engine, Writer(), published)
            assess.assert_not_called()
            deferred['quota_day'] = (today - timedelta(days=1)).isoformat()
            _assess_group_note(engine, Writer(), published)
            assess.assert_called_once()

    def test_malformed_output_keeps_rejection_and_completes_native_invocation(self):
        class Bad(Writer):
            def propose(self,r): return '{bad',{}
        e=self.engines[0]
        with e.store.lock(): r=e.synthesize_group(Bad(),self.packet,1)
        self.assertEqual(r['status'],'rejected'); self.assertIsNone(e.store.load()['pending'])
        self.assertEqual(e.store.record.incomplete_invocations(),())
        self.assertNotIn(INTRO_ID,e.store.load()['posts'])
    def test_group_research_does_not_materialize_static_welcome_or_publish_worker_draft(self):
        e=self.engines[0]
        before=e.store.load()
        result=e.run(Fixture())
        self.assertEqual(result['status'],'accepted')
        self.assertEqual(e.store.load()['posts'],before['posts'])
        self.assertEqual(e.store.audit()[0],e.store.load())
    def test_normal_later_group_reflection_uses_publication_gates(self):
        p=self.draft(); e=self.engines[0]; self.grant(e,p)
        e.store.append('group_bob_published',{'publication':p})
        from wake.group_editorial import _bob_quiet_window
        cycle=1+_bob_quiet_window({**e.store.load()['posts'][INTRO_ID],'created_version':1})
        packet=deepcopy(self.packet)
        for i in packet['inputs']: i['version']=cycle
        writer=Writer(); writer.article['title']='A later shared reflection'
        with e.store.lock(): r=e.synthesize_group(writer,packet,cycle)
        p2=publication(packet,cycle,r['article'],r['id'],{'name':'fixture','model':'group-editorial-fixture'})
        e.store.append('group_bob_published',{'publication':p2})
        self.assertEqual(e.store.load()['group_bob']['checkpoint'],cycle)
        self.assertEqual(e.store.audit()[0],e.store.load())
