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
        article = deepcopy(self.article)
        if 'references' in request.get('response_schema', {}).get('properties', {}):
            article['references'] = [{'input_ids': [i['stories'][0]['id'] for i in request['context']['group']['inputs']]}]
            article['body'] = article['body'].replace('\n\nSummary', ' [1]\n\nSummary')
        return json.dumps(article), {}


class StructuredWriter:
    name, model, charged = 'fixture', 'structured-editorial-fixture', False
    def __init__(self):
        self.calls = 0
    def propose(self, request):
        self.calls += 1
        self.request = request
        response = {'title': 'What can a recorded reading tell us?',
            'lede': 'The group keeps a trace of its questions and readings.',
            'lens': 'A record of a reading leaves the scientific question open.',
            'paragraphs': [
                {'text': 'Each worker recorded its own reading and open questions.', 'reference_numbers': [1]},
                {'text': 'Which interpretation could a later reading help distinguish?', 'reference_numbers': [1]}],
            'summary': 'The workers have recorded readings. Their questions remain open.',
            'references': [{'input_ids': [item['stories'][0]['id'] for item in request['context']['group']['inputs']]}]}
        if hasattr(self, 'alter'):
            self.alter(response)
        self.raw = json.dumps(response, indent=2)
        return self.raw, {'fixture': True}


class GroupEditorialTests(unittest.TestCase):
    def test_editorial_continuity_keeps_attributed_changes_and_prior_text_bounded(self):
        from wake.group_editorial import request
        prior = self.draft()
        packet = deepcopy(self.packet)
        packet['inputs'][0]['version'] += 1
        packet['inputs'][0]['stories'][0]['statement']['version'] += 1
        before = deepcopy(packet)
        result = request(packet, 2, previous=prior)
        continuity = result['context']['continuity']
        self.assertEqual(continuity['previous_post']['id'], prior['id'])
        self.assertEqual(continuity['previous_post']['ending_excerpt'], prior['article']['body'][-900:])
        self.assertEqual(continuity['recorded_changes'][0]['changed_story_ids'], [packet['inputs'][0]['stories'][0]['id']])
        self.assertEqual(continuity['recorded_changes'][1]['changed_story_ids'], [])
        self.assertEqual(result['context']['group'], packet)
        self.assertEqual(packet, before)

    def test_tight_editorial_budget_preserves_every_current_member(self):
        from wake.group_editorial import request
        from wake.providers import provider_input_chars
        prior = self.draft()
        repair = {'reason': 'Explain the unresolved question more plainly.', 'article': prior['article']}
        for correction in (None, repair):
            with self.subTest(repair=bool(correction)):
                base = request(self.packet, 2, correction)
                limit = provider_input_chars(base) + 20
                result = request(self.packet, 2, correction, previous=prior, max_context_chars=limit)
                self.assertLessEqual(provider_input_chars(result), limit)
                self.assertEqual(result['context']['group'], self.packet)
                self.assertEqual(result['context']['repair'], base['context']['repair'])

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

    def test_summary_sentence_draft_releases_while_paused_without_another_model_call(self):
        for item in self.packet['inputs']: item.pop('editorial_schema')
        from wake.group_editorial import synchronize
        for engine, member in zip(self.engines,self.members):
            engine.store.reset(); engine.initialize()
            engine.store.append('group_bob_enrolled',{'actor':'operator','group_id':'wake','members':self.members,'leader':self.members[0],'member':member})
        self.packet['inputs']=[input_snapshot(engine,'wake',member) for engine,member in zip(self.engines,self.members)]
        for item in self.packet['inputs']: item.pop('editorial_schema', None)
        writer = Writer()
        writer.article['body'] = writer.article['body'].replace('\n\nSummary\n\n',' Summary. ')
        p = self.draft(writer)
        engine = self.engines[0]
        engine.store.append('group_bob_drafted', {'publication':p})
        # Fixture carries the prior policy's dated withholding receipt.
        engine.store.append('group_bob_withheld', {'publication_digest':digest(p),
            'reason':'Bob posts must end with a final Summary section in plain language'})
        before = deepcopy(engine.store.load())
        with patch.dict(os.environ, {'WAKE_GROUP_ID':'wake','WAKE_GROUP_COORDINATOR_URL':'http://controller/group/coordinator','WAKE_PUBLIC_HOSTNAME':self.members[0]}), \
             patch('wake.group_editorial.fetch', return_value=None):
            self.assertTrue(synchronize(engine, None))
        after = engine.store.load()
        self.assertEqual(after['posts'][INTRO_ID]['body'],p['article']['body'])
        self.assertEqual(after['invocations'],before['invocations'])
        self.assertEqual(after['version'],before['version'])
        self.assertNotIn('withheld',after['group_bob'])
        self.assertEqual(engine.store.audit()[0],after)

    def test_retained_inline_summary_releases_exact_draft_without_inference(self):
        from wake.group_editorial import synchronize
        class InlineWriter(Writer):
            def propose(self, request):
                raw, metadata = super().propose(request)
                article = json.loads(raw)
                article['body'] = article['body'].replace('\n\nSummary\n\n', '. Summary ')
                return json.dumps(article), metadata
        draft = self.draft(InlineWriter())
        leader = self.engines[0]
        leader.store.append('group_bob_drafted', {'publication': draft})
        leader.store.append('group_bob_withheld', {'publication_digest': digest(draft),
            'reason': 'Bob posts must end with a final Summary section in plain language'})
        before = deepcopy(leader.store.load())
        with patch.dict(os.environ, {'WAKE_GROUP_COORDINATOR_URL': 'http://controller/group/coordinator',
                                    'WAKE_PUBLIC_HOSTNAME': self.members[0]}), patch('wake.group_editorial.fetch', return_value=None):
            self.assertTrue(synchronize(leader, None))
        after = leader.store.load()
        self.assertEqual(after['posts'][INTRO_ID]['body'], draft['article']['body'])
        self.assertEqual(after['invocations'], before['invocations'])
        for key in ('version', 'journal', 'evidence', 'notebooks', 'attention', 'commitments', 'projects'):
            self.assertEqual(after[key], before[key])
        self.assertNotIn('withheld', after['group_bob'])
        self.assertEqual(leader.store.audit()[0], after)

    def test_attempt_packets_follow_dates_instead_of_dictionary_order(self):
        state = deepcopy(self.engines[0].store.load())
        state['invocations'] = {key:{'id':key, 'time':date, 'phase':'research', 'status':'failed'}
            for key,date in (('z-old','2026-01-01'),('a-new','2026-10-14'),('m-middle','2026-09-01'))}
        packet = input_snapshot(None, 'wake', self.members[0], record_snapshot=(state, 'a' * 64))
        self.assertEqual([i['id'] for i in packet['stories'][0]['statement']['attempts']], ['m-middle','a-new'])

    def test_member_packet_bounds_prose_without_truncating_source_urls(self):
        state = deepcopy(self.engines[0].store.load())
        state['research_topics'] = [{'label':'A research topic', 'seed_question':'q' * 800} for _ in range(3)]
        state['evidence'] = {f'e{i}': {'id':f'e{i}', 'source':'https://example.com/' + 's' * 600,
                                    'time':'2026-10-14T00:00:00+00:00'} for i in range(2)}
        state['notebooks'] = {'n': {'id':'n', 'title':'t' * 250, 'summary':'s' * 1000,
            'limitations':'l' * 1000, 'next_questions':'q' * 1000, 'revision':3,
            'evidence':['e0','e1'], 'claims':[{'statement':'a' * 450,
                'certainty':'hypothesis', 'support':[{'evidence':'e0'}]}]}}
        packet = input_snapshot(None, 'wake', self.members[0], record_snapshot=(state, 'a' * 64))
        self.assertLessEqual(len(json.dumps(packet)), 3500)
        story = packet['stories'][-1]
        self.assertEqual(story['notebook_id'], 'n')
        self.assertEqual(story['revision'], 3)
        self.assertEqual(story['claims'][0]['certainty'], 'hypothesis')
        self.assertTrue(all(source['source'] == '' and source['record_url'] for source in story['sources']))

    def test_accessibility_rejects_repeated_intro_and_undefined_terms(self):
        from wake.group_editorial import validate_accessibility
        article = deepcopy(Writer().article)
        article['lede'] = 'I am Bob, your translation voice for checkpoint one.'
        with self.assertRaisesRegex(Rejected, 'introduction'): validate_accessibility(article, 2)
        article['lede'] = 'Notes about memory.'
        article['body'] = 'Members studied thermodynamic entropy production in dissipative substrates.'
        with self.assertRaisesRegex(Rejected, 'first use'): validate_accessibility(article, 2)
        article['body'] = 'Prebiotic simply means before life. We are reading papers about early chemistry.'
        validate_accessibility(article, 2)
        article['body'] = 'We found that storing memory always costs energy.'
        with self.assertRaisesRegex(Rejected, 'discovery'): validate_accessibility(article, 2)

    def test_new_accessibility_checks_preserve_prior_accepted_group_prose(self):
        initial = self.draft()
        leader = self.engines[0]
        leader.store.append('group_bob_published', {'publication':initial})
        writer = Writer(); writer.article['lede'] = 'Welcome to WAKE, checkpoint one.'
        with leader.store.lock(): r = leader.synthesize_group(writer, self.packet, 2)
        prior = publication(self.packet, 2, r['article'], r['id'], {'name':'fixture','model':writer.model})
        with patch('wake.group_editorial.validate_accessibility'):
            leader.store.append('group_bob_published', {'publication':prior})
        self.assertEqual(leader.store.audit()[0], leader.store.load())

    def test_operator_revision_supersedes_without_research_changes_or_repeat_command(self):
        from wake.group_editorial import editorial_due
        p = self.draft()
        for engine in self.engines: engine.store.append('group_bob_published', {'publication':p})
        leader = self.engines[0]
        before = deepcopy(leader.store.load())
        command = {'actor':'operator', 'command_id':'a' * 32, 'publication_digest':digest(p),
                   'reason':'Explain unfamiliar terms in everyday words.'}
        leader.store.append('group_bob_revision_requested', command)
        with self.assertRaises(Rejected): leader.store.append('group_bob_revision_requested', command)
        self.assertTrue(editorial_due(leader.store.load()['group_bob'], self.packet))
        writer = Writer(); writer.article['title'] = 'A clearer explanation of our notes'
        with leader.store.lock(): r = leader.synthesize_group(writer, self.packet, 2)
        correction = publication(self.packet, 2, r['article'], r['id'], {'name':'fixture','model':writer.model}, supersedes=p['id'])
        for engine in self.engines: engine.store.append('group_bob_published', {'publication':correction})
        after = leader.store.load()
        self.assertEqual(after['posts'][p['id']]['status'], 'superseded')
        self.assertEqual(after['posts'][correction['id']]['supersedes'], p['id'])
        for key in ('version','journal','evidence','notebooks','attention','commitments','projects'):
            self.assertEqual(after[key], before[key])
        self.assertNotIn('revision_requested', after['group_bob'])
        self.assertEqual(leader.store.audit()[0], after)

    def test_progress_cadence_requires_three_per_hundred_without_time_expiry(self):
        from datetime import datetime, timedelta, timezone
        from wake.group_editorial import editorial_due
        now = datetime.now(timezone.utc)
        packet = deepcopy(self.packet)
        group = {'publication': {'inputs': deepcopy(packet)}, 'published_at': now.isoformat()}
        packet['inputs'][0]['stories'][0]['statement']['topic_overview'] = [
            {'domain':'memory', 'notebook_id':'n', 'revision':1}]
        self.assertFalse(editorial_due(group, packet, now=now + timedelta(hours=2)))
        # Two existing wakes: neither 32 nor 33 is due; 34 is, with an idle peer.
        packet['inputs'][0]['version'] += 30
        self.assertFalse(editorial_due(group, packet, now=now))
        packet['inputs'][0]['version'] += 1
        self.assertFalse(editorial_due(group, packet, now=now + timedelta(days=2)))
        packet['inputs'][0]['version'] += 1
        self.assertTrue(editorial_due(group, packet, now=now))
        # One catch-up at 97 covers earlier milestones; next obligation is 100.
        packet['inputs'][0]['version'] += 63
        self.assertTrue(editorial_due(group, packet, now=now))
        group['publication']['inputs'] = deepcopy(packet)
        self.assertFalse(editorial_due(group, packet, now=now))
        packet['inputs'][0]['version'] += 2
        self.assertFalse(editorial_due(group, packet, now=now))
        packet['inputs'][1]['version'] += 1
        packet['inputs'][0]['stories'][0]['statement']['topic_overview'][0]['revision'] = 2
        self.assertTrue(editorial_due(group, packet, now=now))
        packet = deepcopy(group['publication']['inputs'])
        packet['inputs'][0]['activity']['attempt_digest'] = 'new failed attempt'
        self.assertFalse(editorial_due(group, packet, now=now + timedelta(days=2)))
        packet['inputs'][0]['version'] = -1
        with self.assertRaises(Rejected): editorial_due(group, packet, now=now)

    def test_three_publication_opportunities_in_each_hundred_accepted_wakes(self):
        from wake.group_editorial import editorial_due
        packet = deepcopy(self.packet)
        packet['inputs'][0]['version'] = 1
        packet['inputs'][1]['version'] = 1
        group = {'publication': {'inputs': deepcopy(packet)}}
        milestones = []
        for total in range(3, 201):
            packet['inputs'][0]['version'] = total - 1
            packet['inputs'][0]['stories'][0]['statement']['topic_overview'] = [
                {'domain':'memory', 'notebook_id':'n', 'revision':total}]
            if editorial_due(group, packet):
                milestones.append(total)
                group['publication']['inputs'] = deepcopy(packet)
        self.assertEqual(milestones, [34, 67, 100, 134, 167, 200])

    def test_counters_and_routine_care_alone_do_not_manufacture_a_story(self):
        from wake.group_editorial import editorial_due
        packet = deepcopy(self.packet)
        group = {'publication': {'inputs': deepcopy(packet)}}
        packet['inputs'][0]['version'] += 100
        statement = packet['inputs'][0]['stories'][0]['statement']
        statement['farm_observation'] = {'feedings': 12, 'food_added': 1200}
        self.assertFalse(editorial_due(group, packet))
        statement['topic_overview'] = [{'domain':'wake_self_study', 'notebook_id':'new-note', 'revision':1}]
        self.assertTrue(editorial_due(group, packet))
        group['publication']['inputs'] = deepcopy(packet)
        packet['inputs'][0]['version'] += 100
        self.assertFalse(editorial_due(group, packet))
        statement['self_observation']['revision'] += 1
        self.assertTrue(editorial_due(group, packet))

    def test_overview_includes_older_topics_and_observation_is_bound_to_publication(self):
        from wake.group_editorial import with_farm_observation
        state = deepcopy(self.engines[0].store.load())
        state['projects'] = {f'p{i}': {'id':f'p{i}', 'domain':domain}
                             for i,domain in enumerate(('memory','preferences','wake_self_study','inquiry'))}
        state['notebooks'] = {f'n{i}': {'id':f'n{i}', 'project':f'p{i}', 'title':domain,
            'summary':'A recorded interpretation of '+domain, 'limitations':'The comparison is provisional.',
            'revision':1, 'updated_version':i, 'evidence':[], 'claims':[]}
            for i,domain in enumerate(('memory','preferences','wake_self_study','inquiry'))}
        summary = input_snapshot(None, 'wake', self.members[0], record_snapshot=(state, 'a'*64))
        self.assertEqual({n['domain'] for n in summary['stories'][0]['statement']['topic_overview']},
                         {'memory','preferences','wake_self_study','inquiry'})
        observation = {'schema':'bob-farm-observation@1','status':'available','scope':'programmed-simulation-only',
            'revision':'b'*40,'source':'https://raw.githubusercontent.com/sudofx/wake/'+('b'*40)+'/farm.json',
            'captured_at':'2026-10-27T17:00:00Z','before':{'ants':64},'after':{'ants':65}}
        packet = with_farm_observation(self.packet, observation)
        self.assertNotIn('farm_observation', self.packet['inputs'][0]['stories'][0]['statement'])
        writer = StructuredWriter(); engine = self.engines[0]; before = deepcopy(engine.store.load())
        with engine.store.lock():
            result = engine.synthesize_group(writer, packet, 1)
        self.assertEqual(result['status'], 'editorial_completed')
        supplied = writer.request['context']['group']['inputs'][0]['stories'][0]
        self.assertEqual(supplied['statement']['farm_observation'], observation)
        self.assertEqual(supplied['sources'][0]['source'], observation['source'])
        p = publication(packet, 1, result['article'], result['id'], {'name':'fixture','model':writer.model})
        self.grant(engine,p); engine.store.append('group_bob_published', {'publication':p})
        after = engine.store.load()
        for key in ('version','journal','evidence','notebooks','attention','commitments','projects'):
            self.assertEqual(after[key], before[key])
        self.assertEqual(engine.store.audit()[0], after)

    def test_full_installation_keeps_topic_overviews_and_farm_within_provider_budget(self):
        from wake.group_editorial import request, with_farm_observation
        from wake.providers import provider_input_chars
        state = deepcopy(self.engines[0].store.load())
        domains = ['assumptions','preferences','objectives','memory','continuity','responsibility','judgment','wake_self_study']
        state['research_topics'] = [{'id':d,'label':'Research into '+d,'seed_question':'Which observations challenge this interpretation?'} for d in domains]
        state['projects'] = {'p'+d:{'id':'p'+d,'domain':d} for d in domains}
        state['notebooks'] = {'n'+d:{'id':'n'+d,'project':'p'+d,'title':'An interpretation of '+d,
            'summary':'A bounded recorded interpretation. '*20, 'limitations':'Independent confirmation is missing. '*20,
            'next_questions':'What evidence would change this?', 'revision':2,'updated_version':i,
            'claims':[],'evidence':[]} for i,d in enumerate(domains)}
        members = [str(parent*100+child)+'.wake' for parent in (1,2,3) for child in range(4)]
        packet = {'schema':1,'group_id':'wake','members':members,'leader':members[0],
            'inputs':[input_snapshot(None,'wake',member,record_snapshot=(state,'a'*64)) for member in members]}
        observation = {'schema':'bob-farm-observation@1','status':'available','scope':'programmed-simulation-only',
            'source':'https://raw.githubusercontent.com/sudofx/wake/'+('b'*40)+'/farm.json',
            'revision':'b'*40,'sha256':'c'*64,'model_source_revision':'d'*40,
            'captured_at':'2026-10-27T17:00:00Z','before':{'ants':64,'dug':10,'delivered':3},
            'after':{'ants':65,'dug':12,'delivered':4},'recent_intervals':[
                {'from_tick':i*6000,'to_tick':(i+1)*6000,'workers':64,'deliveries':3,'new_tunnels':2,'feedings':1} for i in range(4)]}
        packet = with_farm_observation(packet,observation)
        result = request(packet,2,max_context_chars=48000)
        self.assertLessEqual(provider_input_chars(result),48000)
        for item in result['context']['group']['inputs']:
            self.assertEqual({row['domain'] for row in item['stories'][0]['statement']['topic_overview']},set(domains))
        self.assertEqual(result['context']['group']['inputs'][0]['stories'][0]['statement']['farm_observation']['status'],'available')
        self.assertNotIn('actions',result['response_schema']['properties'])

    def test_retained_grouped_citations_and_informal_language_publish_without_inference(self):
        from wake.group_editorial import synchronize, validate_grounding
        class ExactWriter(Writer):
            def propose(self, request):
                return json.dumps(self.article), {}
        article = deepcopy(Writer().article)
        article['body'] = ('We found that quantum memory is an interesting question. '
                           + 'Long sentences are editorial guidance ' * 50
                           + '[1, 2]\n\nSummary\n\n' + 'There is more to read. ' * 30)
        article['references'] = [{'input_ids':[item['stories'][0]['id']]} for item in self.packet['inputs']]
        leader = self.engines[0]
        with leader.store.lock(): result = leader.synthesize_group(ExactWriter(article), self.packet, 1)
        p = publication(self.packet, 1, result['article'], result['id'], {'name':'fixture','model':Writer.model})
        leader.store.append('group_bob_drafted', {'publication':p})
        leader.store.append('group_bob_withheld', {'publication_digest':digest(p), 'reason':'Every story paragraph needs valid numeric references'})
        before = deepcopy(leader.store.load())
        with patch.dict(os.environ, {'WAKE_GROUP_COORDINATOR_URL':'http://controller/group/coordinator',
                                    'WAKE_PUBLIC_HOSTNAME':self.members[0]}), patch('wake.group_editorial.fetch', return_value=None):
            self.assertTrue(synchronize(leader, None))
        after = leader.store.load()
        self.assertEqual(after['posts'][INTRO_ID]['body'], article['body'])
        self.assertEqual(after['invocations'], before['invocations'])
        for key in ('version','journal','evidence','notebooks','attention','commitments','projects'):
            self.assertEqual(after[key], before[key])
        self.assertEqual(leader.store.audit()[0], after)
        for bad in ('[0]', '[1, 3]', '[1, invented]'):
            invalid = deepcopy(article); invalid['body'] = invalid['body'].replace('[1, 2]', bad)
            with self.assertRaises(Rejected): validate_grounding(invalid, self.packet)
        invalid = deepcopy(article)
        invalid['lede'] = 'I am conscious and sentient.'
        with self.assertRaises(Rejected): validate_grounding(invalid, self.packet)

    def test_progress_references_reject_invented_sources_and_missing_members(self):
        from wake.group_editorial import validate_grounding
        p = self.draft()
        validate_grounding(p['article'], p['inputs'])
        p['article']['references'][0]['input_ids'] = ['invented']
        with self.assertRaises(Rejected): validate_grounding(p['article'], p['inputs'])
        p['article']['references'][0]['input_ids'] = [self.packet['inputs'][0]['stories'][0]['id']]
        with self.assertRaises(Rejected): validate_grounding(p['article'], p['inputs'])

    def test_invalid_progress_rejection_is_retained_and_repaired_with_bounded_calls(self):
        from wake.group_editorial import synchronize
        leader = self.engines[0]
        writer = Writer()
        writer.article['body'] = writer.article['body'].replace('Summary', 'Closing')
        def response(url):
            return self.packet if url.endswith('bob-inputs.json') else None
        with patch.dict(os.environ, {'WAKE_GROUP_COORDINATOR_URL':'http://controller/group/coordinator',
                                    'WAKE_PUBLIC_HOSTNAME':self.members[0]}), \
             patch('wake.group_editorial.fetch', side_effect=response):
            synchronize(leader, writer)
            group = leader.store.load()['group_bob']
            self.assertNotIn('draft', group)
            rejected = [item for item in leader.store.load()['invocations'].values()
                        if item.get('phase') == 'group_editorial'][-1]
            self.assertEqual(rejected['status'], 'rejected')
            self.assertIn('Summary', rejected['reason'])
            self.assertTrue(rejected['editorial']['draft_excerpt'])
            self.assertEqual(leader.store.record.incomplete_invocations(), ())
            before = deepcopy(leader.store.load())
            synchronize(leader, writer)
            self.assertEqual(leader.store.load()['invocations'], before['invocations'])
            # Capacity persists in receipts, including a failed publication.
            from datetime import datetime, timedelta, timezone
            future = datetime.now(timezone.utc) + timedelta(minutes=16)
            writer.article = Writer().article
            with patch('wake.group_editorial.datetime') as clock:
                clock.now.return_value = future
                clock.fromisoformat.side_effect = datetime.fromisoformat
                synchronize(leader, writer)
            self.assertEqual(writer.request['context']['repair']['reason'], rejected['reason'])
            self.assertTrue(writer.request['context']['repair']['previous_draft_excerpt'])
            self.assertEqual(leader.store.load()['group_bob']['checkpoint'], 1)
            self.assertEqual(leader.store.load()['version'], before['version'])
            self.assertEqual(leader.store.audit()[0], leader.store.load())

    def test_required_post_survives_more_than_three_failed_drafts_in_a_day(self):
        from datetime import datetime, timedelta, timezone
        from wake.group_editorial import synchronize
        leader = self.engines[0]
        writer = Writer()
        writer.article['body'] = writer.article['body'].replace('Summary', 'Closing')
        def response(url):
            return self.packet if url.endswith('bob-inputs.json') else None
        before = deepcopy(leader.store.load())
        with patch.dict(os.environ, {'WAKE_GROUP_COORDINATOR_URL':'http://controller/group/coordinator',
                                    'WAKE_PUBLIC_HOSTNAME':self.members[0]}), \
             patch('wake.group_editorial.fetch', side_effect=response):
            synchronize(leader, writer)
            future = datetime.now(timezone.utc) + timedelta(minutes=16)
            with patch('wake.group_editorial.datetime') as clock:
                clock.now.return_value = future
                clock.fromisoformat.side_effect = datetime.fromisoformat
                for _ in range(6):
                    synchronize(leader, writer)
                writer.article = Writer().article
                synchronize(leader, writer)
        after = leader.store.load()
        self.assertEqual(after['group_bob']['checkpoint'], 1)
        self.assertEqual(sum(i.get('phase') == 'group_editorial' for i in after['invocations'].values()), 8)
        for key in ('version','journal','evidence','notebooks','attention','commitments','projects'):
            self.assertEqual(after[key], before[key])
        self.assertEqual(leader.store.audit()[0], after)

    def test_structured_article_renders_explicit_refs_and_summary_with_exact_raw_receipt(self):
        from wake.group_editorial import PARAGRAPH_CONTRACT
        leader, child = self.engines
        writer = StructuredWriter()
        before = deepcopy(leader.store.load())
        draft = self.draft(writer)
        self.assertEqual(writer.request['context']['output_contract'], PARAGRAPH_CONTRACT)
        schema = writer.request['response_schema']
        self.assertEqual(set(schema['required']), {'title', 'lede', 'lens', 'paragraphs', 'summary', 'references'})
        self.assertNotIn('body', schema['properties'])
        # Provider grammar stays structural; local rejection tests below retain
        # exact source membership, numeric ranges and all-member coverage.
        def structural(value):
            if isinstance(value, dict):
                self.assertFalse(set(value) & {'minItems', 'maxItems', 'minimum', 'maximum'})
                for child in value.values(): structural(child)
            elif isinstance(value, list):
                for child in value: structural(child)
        structural(schema)
        self.assertEqual(schema['properties']['references']['items']['properties']['input_ids']['items']['enum'],
                         [story['id'] for item in self.packet['inputs'] for story in item['stories']])
        body = draft['article']['body']
        self.assertIn('distinguish? [1]\n\nSummary\n\n', body)
        receipt = leader.store.load()['invocations'][draft['invocation']]
        self.assertEqual(receipt['output_transform']['contract'], PARAGRAPH_CONTRACT)
        event = next(e for e in leader.store.events() if e['kind'] == 'editorial_completed')
        self.assertEqual(event['payload']['raw_response'], writer.raw)
        self.assertEqual(receipt['output_transform']['response_digest'], digest(json.loads(writer.raw)))
        for engine in (leader, child):
            engine.store.append('group_bob_published', {'publication': draft})
            self.assertEqual(engine.store.load()['posts'][INTRO_ID]['body'], body)
            self.assertEqual(engine.store.audit()[0], engine.store.load())
            self.assertEqual(engine.store.record.incomplete_invocations(), ())
        for key in ('version', 'journal', 'evidence', 'notebooks', 'attention', 'commitments', 'projects'):
            self.assertEqual(leader.store.load()[key], before[key])
        self.assertEqual(writer.calls, 1)

    def test_structured_attribution_errors_are_terminal_rejections_without_progress(self):
        leader = self.engines[0]
        before = deepcopy(leader.store.load())
        alterations = (
            lambda r: r['paragraphs'][1].update(reference_numbers=[]),
            lambda r: r['paragraphs'][1].update(reference_numbers=[0]),
            lambda r: r['paragraphs'][1].update(reference_numbers=[2]),
            lambda r: r['paragraphs'][1].update(reference_numbers=[True]),
            lambda r: r['paragraphs'][1].pop('reference_numbers'),
            lambda r: r['references'][0].update(input_ids=['invented']),
            lambda r: r['references'][0].update(input_ids=[self.packet['inputs'][0]['stories'][0]['id']]),
        )
        for alter in alterations:
            writer = StructuredWriter(); writer.alter = alter
            with self.subTest(alter=alter), leader.store.lock():
                result = leader.synthesize_group(writer, self.packet, 1)
                self.assertEqual(result['status'], 'rejected')
                self.assertIsNone(leader.store.load()['pending'])
                self.assertEqual(leader.store.record.incomplete_invocations(), ())
                self.assertEqual(writer.calls, 1)
        after = leader.store.load()
        for key in ('version', 'posts', 'journal', 'evidence', 'notebooks', 'attention', 'commitments', 'projects'):
            self.assertEqual(after[key], before[key])
        self.assertEqual(leader.store.audit()[0], after)

    def test_structured_failure_repairs_on_next_day_with_original_reason_and_no_extra_calls(self):
        from datetime import datetime, timedelta, timezone
        from wake.group_editorial import synchronize
        leader = self.engines[0]
        writer = StructuredWriter()
        writer.alter = lambda response: response['paragraphs'][1].update(reference_numbers=[])
        def response(url):
            return self.packet if url.endswith('bob-inputs.json') else None
        with patch.dict(os.environ, {'WAKE_GROUP_COORDINATOR_URL': 'http://controller/group/coordinator',
                                    'WAKE_PUBLIC_HOSTNAME': self.members[0]}), \
             patch('wake.group_editorial.fetch', side_effect=response):
            self.assertTrue(synchronize(leader, writer))
            rejected = [i for i in leader.store.load()['invocations'].values()
                        if i.get('phase') == 'group_editorial'][-1]
            self.assertEqual(rejected['status'], 'rejected')
            synchronize(leader, writer)
            self.assertEqual(writer.calls, 1)
            del writer.alter
            with patch('wake.group_editorial.datetime') as clock:
                clock.now.return_value = datetime.now(timezone.utc) + timedelta(days=1)
                clock.fromisoformat.side_effect = datetime.fromisoformat
                self.assertTrue(synchronize(leader, writer))
        repair = writer.request['context']['repair']
        self.assertEqual(repair['reason'], rejected['reason'])
        self.assertEqual(repair['previous_draft_excerpt'], rejected['editorial']['draft_excerpt'])
        self.assertEqual(writer.calls, 2)
        self.assertEqual(leader.store.load()['group_bob']['checkpoint'], 1)
        self.assertEqual(leader.store.record.incomplete_invocations(), ())
        self.assertEqual(leader.store.audit()[0], leader.store.load())

    def test_repair_uses_latest_attempt_by_date_when_projection_reorders_ids(self):
        from wake.group_editorial import synchronize
        leader = self.engines[0]
        state = deepcopy(leader.store.load())
        state['invocations'] = {
            'a-new': {'id': 'a-new', 'phase': 'group_editorial', 'editorial_checkpoint': 1,
                      'time': '2025-02-01T00:00:00+00:00', 'quota_day': '2025-02-01',
                      'reason': 'Latest reference error', 'editorial': {'draft_excerpt': 'Latest failed draft'}},
            'z-old': {'id': 'z-old', 'phase': 'group_editorial', 'editorial_checkpoint': 1,
                      'time': '2025-01-01T00:00:00+00:00', 'quota_day': '2025-01-01',
                      'reason': 'Older summary error', 'editorial': {'draft_excerpt': 'Older failed draft'}}}
        def response(url):
            return self.packet if url.endswith('bob-inputs.json') else None
        with patch.dict(os.environ, {'WAKE_GROUP_COORDINATOR_URL': 'http://controller/group/coordinator',
                                    'WAKE_PUBLIC_HOSTNAME': self.members[0]}), \
             patch('wake.group_editorial.fetch', side_effect=response), \
             patch.object(leader.store, 'load', return_value=state), \
             patch.object(leader, 'synthesize_group', return_value={'status': 'rejected'}) as synthesize:
            self.assertTrue(synchronize(leader, StructuredWriter()))
        self.assertEqual(synthesize.call_args.kwargs['repair'], {
            'reason': 'Latest reference error', 'article': {'body': 'Latest failed draft'}})

    def test_structured_rendering_receipt_rejects_changed_prose_or_transformation_on_replay(self):
        from wake.domain_events import reduce_event
        leader = self.engines[0]
        self.draft(StructuredWriter())
        events = leader.store.events()
        target = next(i for i, event in enumerate(events) if event['kind'] == 'editorial_completed')
        # Reconstruct the pending state immediately before the terminal receipt.
        from wake.domain_events import empty
        state = empty()
        for event in events[:target]:
            state = reduce_event(state, event, historical=True)
        for change in ('article', 'output_transform', 'raw_response', 'remove_transform'):
            event = deepcopy(events[target])
            payload = event['payload']
            if change == 'article': payload['article']['body'] += ' Invented prose.'
            elif change == 'output_transform': payload['output_transform']['contract'] = 'invented@1'
            elif change == 'raw_response': payload['raw_response'] = payload['raw_response'].replace('open questions', 'proven findings')
            else: payload.pop('output_transform')
            for historical in (False, True):
                with self.subTest(change=change, historical=historical), self.assertRaises(Rejected):
                    reduce_event(deepcopy(state), event, historical=historical)
        self.assertEqual(leader.store.audit()[0], leader.store.load())

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
            self.assertTrue(synchronize(e,writer))
            synchronize(e,writer)
        self.assertEqual(writer.calls,1)
        self.assertEqual(e.store.load()['version'],0)
        self.assertEqual(e.store.load()['posts'],{})
        self.assertEqual(e.store.record.incomplete_invocations(),())
    def test_exception_cannot_publish_changed_article_research_actions_or_another_checkpoint(self):
        for item in self.packet['inputs']: item.pop('editorial_schema')
        p=self.draft(Writer({'title':'Short first post','lede':'Welcome.','body':'This welcome is intentionally short.','lens':'Open questions.'}))
        e=self.engines[0]; self.grant(e,p)
        changed=deepcopy(p); changed['article']['body']='A changed article.'
        with self.assertRaises(Rejected): e.store.append('group_bob_published',{'publication':changed})
        with self.assertRaises(Rejected): e.store.append('group_bob_published',{'publication':p,'actions':[{'type':'research'}]})
        e.store.append('group_bob_published',{'publication':p})
        with self.assertRaises(Rejected): self.grant(e,p)
        with self.assertRaises(Rejected): e.store.append('group_bob_published',{'publication':p})

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
        cycle=2
        packet=deepcopy(self.packet)
        for i in packet['inputs']: i['version']=cycle
        writer=Writer(); writer.article['title']='A later shared reflection'
        with e.store.lock(): r=e.synthesize_group(writer,packet,cycle)
        p2=publication(packet,cycle,r['article'],r['id'],{'name':'fixture','model':'group-editorial-fixture'})
        e.store.append('group_bob_published',{'publication':p2})
        self.assertEqual(e.store.load()['group_bob']['checkpoint'],cycle)
        self.assertEqual(e.store.audit()[0],e.store.load())
