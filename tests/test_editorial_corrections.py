"""Corrections preserve provenance and cannot disguise a new overclaim as a quote."""
import copy
import json
import unittest

import test_research as fixtures
from wake.governance import Rejected, transition
from wake.providers import SCHEMA, schema_for_context, retractable_quotes


class CorrectionTests(unittest.TestCase):
    def setUp(self):
        self.case = fixtures.ResearchTests()
        self.case.setUp()
        self.case.source('s1')
        self.case.source('s2')
        self.case.source('belief-only')
        self.case.propose([fixtures.project(), fixtures.notebook(['s1', 's2']), self.case.blog()])
        self.state = self.case.engine.store.load()
        # Represents an older, historically accepted post without rewriting any durable record.
        self.state['posts']['post-one']['body'] += ' It allows genuine epistemic self-governance.'
        self.quote = 'Retracted wording: "genuine epistemic self-governance". This was an overstatement.'

    def tearDown(self):
        self.case.tearDown()

    def proposal(self, **changes):
        body = self.quote + '\n\n' + self.case.blog()['body']
        action = self.case.blog(id='correction', supersedes='post-one', body=body, **changes)
        return dict(base_version=self.state['version'], title='A correction', summary='Narrowing the earlier claim.', actions=[action])

    def test_exact_explicit_retraction_passes_and_supersedes_atomically(self):
        result = transition(self.state, self.proposal(), 'offline')
        self.assertEqual(result['posts']['post-one']['superseded_by'], 'correction')
        self.assertEqual(result['posts']['correction']['status'], 'current')
        self.assertEqual(result['version'], self.state['version'] + 1)
        self.assertNotIn('superseded_by', self.state['posts']['post-one'])

    def test_unincorporated_belief_citations_still_rejected(self):
        with self.assertRaisesRegex(Rejected, 'traceable'):
            transition(self.state, self.proposal(evidence=['s1', 'belief-only']), 'offline')

    def test_retraction_cannot_hide_new_overclaim_in_any_other_field(self):
        for field in ('title', 'lede', 'body', 'lens', 'reason'):
            with self.subTest(field=field):
                p = self.proposal()
                p['actions'][0][field] += ' This demonstrates genuine epistemic self-governance.'
                with self.assertRaisesRegex(Rejected, 'contested synthesis'):
                    transition(self.state, p, 'offline')

    def test_invented_quote_or_missing_supersedes_is_not_exempt(self):
        for variant in ('invented', 'no_supersedes', 'endorsement', 'arbitrary_quote'):
            with self.subTest(variant=variant):
                p = self.proposal(); a = p['actions'][0]
                if variant == 'invented':
                    a['body'] = a['body'].replace('genuine epistemic self-governance', 'real consciousness')
                elif variant == 'no_supersedes':
                    del a['supersedes']
                elif variant == 'endorsement':
                    a['body'] = a['body'].replace('This was an overstatement.', 'This is correct.')
                else:
                    a['body'] = a['body'].replace('Retracted wording: ', 'As previously stated: ')
                with self.assertRaisesRegex(Rejected, 'contested synthesis'):
                    transition(self.state, p, 'offline')

    def test_retraction_does_not_bypass_quantum_bridge_or_limited_source_policy(self):
        p = self.proposal()
        phrase = 'Quantum physics explains consciousness'
        self.state['posts']['post-one']['body'] += ' ' + phrase
        p['actions'][0]['body'] = f'Retracted wording: "{phrase}". This was an overstatement.\n\n' + self.case.blog()['body']
        with self.assertRaisesRegex(Rejected, 'philosophical metaphor'):
            transition(self.state, p, 'offline')
        for eid in ('s1', 's2'):
            self.state['evidence'][eid]['content'] = json.dumps({'scope': 'incomplete excerpt'})
        p = self.proposal()
        p['actions'][0]['body'] += ' This is conclusive.'
        with self.assertRaisesRegex(Rejected, 'certainty language'):
            transition(self.state, p, 'offline')

    def test_schema_excludes_unincorporated_sources_without_mutating_default(self):
        before = copy.deepcopy(SCHEMA)
        context = {'blog_notebooks': {'p': [{'id': 'n', 'evidence': ['s1', 's2']}]},
                   'beliefs': [{'evidence': ['belief-only']}]}
        schema = schema_for_context(context)
        blog = next(a for a in schema['properties']['actions']['items']['anyOf']
                    if a['properties']['type']['enum'] == ['blog'])
        self.assertEqual(blog['properties']['evidence']['items']['enum'], ['s1', 's2'])
        self.assertEqual(blog['properties']['notebooks']['items']['enum'], ['n'])
        self.assertEqual(blog['properties']['project']['enum'], ['p'])
        self.assertEqual(SCHEMA, before)
        without = schema_for_context({})['properties']['actions']['items']['anyOf']
        self.assertFalse(any(a['properties']['type']['enum'] == ['blog'] for a in without))

    def test_request_carries_citation_enum_and_exact_published_quotes(self):
        with self.case.engine.store.lock():
            invocation, request = self.case.engine.start('fixture', 'offline')
        blog = next(a for a in request['response_schema']['properties']['actions']['items']['anyOf']
                    if a['properties']['type']['enum'] == ['blog'])
        self.assertNotIn('belief-only', blog['properties']['evidence']['items']['enum'])
        self.assertEqual(retractable_quotes(self.state['posts']['post-one']), ['genuine epistemic self-governance'])
        self.assertIn('retractable_quotes', request['context']['recent_blog'][0])
        self.assertIn('A belief\'s evidence list', request['system'])
        self.assertIn('Retracted wording:', request['system'])

    def test_valid_correction_is_durable_and_replayable(self):
        action = self.case.blog(id='correction', supersedes='post-one', body=
            'Retracted wording: "a different part of the problem". This was an overstatement.\n\n' + self.case.blog()['body'])
        result = self.case.propose([action])
        self.assertEqual(result['status'], 'accepted')
        state = self.case.engine.store.load()
        replayed, _ = self.case.engine.store.replay()
        self.assertEqual(replayed, state)
        self.assertEqual(state['posts']['post-one']['superseded_by'], 'correction')
