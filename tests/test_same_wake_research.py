"""One governed wake can plan, fetch, answer and commit without a queued cycle."""
import copy
import json
import socket
import tempfile
import unittest
from unittest.mock import patch, Mock
from wake.engine import Engine
from wake.event_format import digest
from wake.record_store import RecordStore
from wake.research import (allowed_url, collect_planned, _public_connection,
    research_plan_schema, validate_research_plan, Redirects, host_tier, PublicHTTPSConnection)
from support import charter_settings
from test_research import project, notebook


class ImmediateProvider:
    name = 'fixture'
    model = 'immediate-test'
    charged = True
    def __init__(self, bad=False, fail_final=False):
        self.requests = []
        self.bad, self.fail_final = bad, fail_final
    def propose(self, request):
        self.provider_requests_sent = 1
        self.requests.append(copy.deepcopy(request))
        if request['context'].get('research_phase') == 'planning':
            if self.bad:
                return json.dumps({'requests': [dict(query='entropy', domain='entropy', project='', url='https://127.0.0.1/secret')]}), {}
            return json.dumps({'requests': [dict(query='entropy comparison measurement', domain='entropy', project='',
                url='https://research.example.edu/'+name) for name in ('a','b')]}), {'provider_requests_sent': 1}
        if self.fail_final:
            raise OSError('Simulated provider outage')
        evidence = request['context']['same_wake_research']['evidence_ids']
        return json.dumps(dict(base_version=request['context']['version'], title='Immediate evidence-backed answer',
            summary='Entropy comparison measurement findings '+''.join('['+i+']' for i in evidence),
            actions=[project(), notebook(evidence, 'Entropy comparison measurement findings '+''.join('['+i+']' for i in evidence))])), {'provider_requests_sent': 1}


class SameWakeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.store = RecordStore(self.temp.name, initialize_empty=True)
        self.engine = Engine(self.temp.name, charter_settings(same_wake_research=True, memory_mode='active'), store=self.store)
        self.engine.initialize()
    def tearDown(self):
        self.store.close(); self.temp.cleanup()
    def collect(self, engine, requests):
        return collect_planned(engine, requests, fetcher=lambda url: dict(excerpt='entropy comparison measurement findings', url=url))
    def test_two_calls_one_accepted_cycle_sources_available_before_final_request(self):
        provider = ImmediateProvider()
        with patch('wake.research.collect_planned', self.collect):
            result = self.engine.run(provider, collector=lambda e: None, question='What distinguishes entropy measurements?')
        self.assertEqual(result['status'], 'accepted', result)
        self.assertEqual(len(provider.requests), 2)
        self.assertEqual(set(provider.requests[0]['response_schema']['properties']), {'requests'})
        self.assertIn('base_version', provider.requests[1]['response_schema']['properties'])
        self.assertNotIn('Return a JSON object with exactly base_version', provider.requests[0]['system'])
        self.assertEqual(self.store.load()['version'], 1)
        self.assertIsNone(self.store.load()['pending'])
        self.assertEqual(set(self.store.load()['notebooks']['n']['evidence']), set(result['same_wake_research']['evidence_ids']))
        self.assertIn('Entropy comparison', result['answer'])
        for request in provider.requests:
            self.assertEqual(request['context']['operator_question'], 'What distinguishes entropy measurements?')
        final = provider.requests[-1]['context']
        readable = {item['id'] for item in final['evidence'] if item.get('content')}
        self.assertTrue(set(result['same_wake_research']['evidence_ids']) <= readable)
        invocations = self.store.load()['invocations']
        self.assertEqual(sorted(item['status'] for item in invocations.values()), ['accepted', 'research_planned'])
        self.assertEqual(sum(item['provider_requests_sent'] for item in invocations.values()), 2)
        for invocation in invocations:
            stages = [event['stage'] for event in self.store.invocation_history(invocation)]
            self.assertIn('context_delivered', stages)
            self.assertIn('completed', stages)
        replay = self.store.record.full_replay()[1]
        self.assertIn('app:wake', replay)
    def test_invalid_plan_makes_no_network_call_or_transition(self):
        provider = ImmediateProvider(bad=True)
        with patch('wake.research.collect_planned') as collector:
            result = self.engine.run(provider, collector=lambda e: None)
        self.assertEqual(result['status'], 'failed')
        collector.assert_not_called()
        self.assertEqual(self.store.load()['version'], 0)
        self.assertIsNone(self.store.load()['pending'])
    def test_final_failure_preserves_collected_receipts_without_fabricated_answer(self):
        provider = ImmediateProvider(fail_final=True)
        with patch('wake.research.collect_planned', self.collect):
            result = self.engine.run(provider, collector=lambda e: None)
        self.assertEqual(result['status'], 'failed')
        self.assertIn('planning_invocation', result['same_wake_research'])
        self.assertEqual(self.store.load()['version'], 0)
        self.assertEqual(sum(e['actor']=='collector' for e in self.store.load()['evidence'].values()), 2)
        self.assertIsNone(self.store.load()['pending'])
    def test_metadata_route_reaches_readable_source_in_same_pass(self):
        fetched=[]
        def fetch(url):
            fetched.append(url)
            if 'api.crossref.org' in url:
                return dict(excerpt='entropy comparison measurement https://research.example.edu/readable')
            return dict(excerpt='entropy comparison measurement results')
        ids=collect_planned(self.engine, [dict(query='entropy', domain='entropy', project='', url='')], fetcher=fetch)
        self.assertEqual(len(ids), 2)
        self.assertIn('research.example.edu/readable', fetched[-1])
        contents=[json.loads(self.store.load()['evidence'][identifier]['content']) for identifier in ids]
        self.assertEqual([item['evidence_role'] for item in contents], ['discovery','source'])
    def test_bad_domain_and_attention_constraints_are_enforced_before_fetch(self):
        state=self.store.load(); context=self.engine.context(state,'receipt')
        context['attention']={'enforce_selected_topic': True,'selected_topic':'entropy'}
        for domain in ('music', [], 'unknown'):
            with self.subTest(domain=domain), self.assertRaises(Exception):
                validate_research_plan(json.dumps({'requests':[dict(query='q',domain=domain,project='',url='')]}), context, state)
    def test_budget_exhaustion_does_not_send_final_call(self):
        self.engine.config['daily_call_limit']=1
        with patch('wake.research.collect_planned', self.collect):
            from wake.governance import Rejected
            with self.assertRaisesRegex(Rejected, 'Daily call ceiling'):
                self.engine.run(ImmediateProvider(), collector=lambda e: None)
        self.assertEqual(self.store.load()['version'], 0)
        self.assertIsNone(self.store.load()['pending'])


class InternetBreadthTests(unittest.TestCase):
    def test_institutions_publishers_preprints_and_repositories_are_reachable_by_policy(self):
        for host in ('mit.edu', 'research.ox.ac.uk', 'nih.gov', 'data.europa.eu', 'openaccess.thecvf.com',
                     'onlinelibrary.wiley.com', 'zenodo.org', 'hal.science', 'biorxiv.org', 'aclanthology.org',
                     'datasets.huggingface.co', 'ethz.ch', 'journals.sagepub.com'):
            with self.subTest(host=host): self.assertEqual(allowed_url('https://'+host+'/paper'), 'https://'+host+'/paper')
        self.assertEqual(host_tier('https://www.medrxiv.org/content/paper'), 'preprint')
    def test_suffix_spoofing_and_unsafe_transports_remain_blocked(self):
        for url in ('http://mit.edu/', 'https://mit.edu.evil.example/', 'https://evilmit.edu.example/',
                    'https://127.0.0.1/', 'https://[::1]/', 'https://user:pass@mit.edu/', 'https://mit.edu:8000/'):
            with self.subTest(url=url), self.assertRaises(ValueError): allowed_url(url)
    def test_private_dns_addresses_never_get_a_socket(self):
        for ip in ('127.0.0.1', '10.0.0.1', '169.254.169.254', '::1', 'fd00::1'):
            with self.subTest(ip=ip), patch('wake.research.socket.getaddrinfo', return_value=[(socket.AF_INET, socket.SOCK_STREAM, 6, '', (ip,443))]), patch('wake.research.socket.socket') as factory:
                with self.assertRaisesRegex(ValueError,'public Internet'):
                    _public_connection(('research.example.edu',443),10)
                factory.assert_not_called()
    def test_connection_is_pinned_to_checked_public_address(self):
        connection=Mock()
        with patch('wake.research.socket.getaddrinfo',return_value=[(socket.AF_INET,socket.SOCK_STREAM,6,'',('8.8.8.8',443))]) as resolver, patch('wake.research.socket.socket',return_value=connection):
            self.assertIs(_public_connection(('research.example.edu',443),10),connection)
        resolver.assert_called_once()
        connection.connect.assert_called_once_with(('8.8.8.8',443))

    def test_trusted_proxy_cannot_tunnel_to_a_private_research_target(self):
        connection=PublicHTTPSConnection('operator-proxy.internal',3128)
        connection.set_tunnel('research.example.edu',443)
        with patch('wake.research.socket.getaddrinfo',return_value=[(socket.AF_INET,socket.SOCK_STREAM,6,'',('10.0.0.1',443))]), patch('wake.research.socket.create_connection') as connect:
            with self.assertRaisesRegex(ValueError,'public Internet'):
                connection._checked_connection(('operator-proxy.internal',3128),10)
            connect.assert_not_called()
