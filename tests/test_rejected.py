# =============================================================================
# TESTING INTENT — rejected
#
# This file is executable documentation. Passing cases define behavior WAKE✳︎
# promises to preserve; rejection/failure cases define boundaries that future
# refactors must not weaken merely to make CI green. Assertions should make the
# protected invariant understandable to both human and AI maintainers.
# =============================================================================

# WAKE✳︎ MAINTAINER NOTE
#
# Executable specification for rejected.
# Tests in WAKE✳︎ are part of the explanation of the system: successful cases show what authority is allowed,
# while rejection/failure cases show the boundaries that must remain intact during refactors.
# Prefer assertions that make the invariant obvious to a human or AI maintainer reading this file later.

"""Rejected drafts are readable without being promoted to accepted research."""
import copy
import json
import unittest
from wake.rejected import rejected_html


class RejectedDraftTests(unittest.TestCase):
    def setUp(self):
        self.state = {'invocations': {'w-one': {'provider_requests_sent': 2,
            'provider_attempts': [{'model': 'gemini-3.8-flash', 'http_status': 503,
                                   'result': 'transient_failure', 'elapsed_ms': 1200}]}}}
        self.draft = {'title': 'An unapproved correction', 'summary': 'A proposed summary.',
                      'actions': [{'type': 'blog', 'title': 'Proposed blog', 'body': 'A draft to inspect.',
                                   'evidence': ['unlinked-source'], 'notebooks': ['n']}]}
        self.event = {'kind': 'rejected', 'time': '2026-09-16T08:20:00Z', 'payload': {
            'id': 'w-one', 'reason': 'Blog evidence must be traceable through its referenced notebooks',
            'raw_response': json.dumps(self.draft)}}

    def test_readable_draft_reason_and_calls_do_not_mutate_record(self):
        before = copy.deepcopy((self.state, self.event))
        page = rejected_html(self.state, [self.event])
        for text in ('An unapproved correction', 'A draft to inspect.', 'Why it stopped',
                     'not attached to the notebooks', '2 provider requests', 'gemini-3.8-flash',
                     'No research changes or journal entry', 'Exact recorded reason', 'unlinked-source'):
            self.assertIn(text, page)
        self.assertEqual((self.state, self.event), before)
        self.assertIn('<details><summary>Read the unaccepted draft</summary>', page)

    def test_withheld_blog_preserves_distinction_from_accepted_research(self):
        self.event['kind'] = 'accepted'
        self.event['payload']['editorial'] = {'reason': 'Invalid evidence', 'action': self.draft['actions'][0]}
        page = rejected_html(self.state, [self.event])
        self.assertIn('Blog withheld · research accepted', page)
        self.assertIn('The other research actions were accepted.', page)
        self.assertNotIn('No research changes or journal entry', page)

    def test_phrase_explanation_acknowledges_false_positives(self):
        self.event['payload']['reason'] = 'Blog prose must not present contested synthesis or interpretation as established fact'
        page = rejected_html(self.state, [self.event])
        self.assertIn('not a verdict that the whole draft is false', page)
        self.assertIn('quotations, negations, or attempted corrections', page)
        self.assertIn('recorded first failing check', page)

    def test_malformed_responses_and_unknown_historical_counts(self):
        self.state['invocations'] = {}
        for raw in ('not JSON', 'null', '[]', '{"actions":null}', '{"actions":[null]}'):
            with self.subTest(raw=raw):
                self.event['payload']['raw_response'] = raw
                page = rejected_html(self.state, [self.event])
                self.assertIn('Provider request count not recorded', page)
                self.assertIn('Exact saved response', page)

    def test_untrusted_draft_text_is_escaped(self):
        self.draft['actions'][0]['body'] = '<script>alert("x")</script>'
        self.draft['title'] = '<img src=x onerror=alert(1)>'
        self.event['payload']['raw_response'] = json.dumps(self.draft)
        page = rejected_html(self.state, [self.event])
        self.assertNotIn('<script>', page)
        self.assertNotIn('<img ', page)
        self.assertIn('&lt;script&gt;', page)

    def test_regular_accepted_events_are_not_presented_as_rejected(self):
        self.event['kind'] = 'accepted'
        page = rejected_html(self.state, [self.event])
        self.assertIn('No rejected proposals', page)
        self.assertNotIn('An unapproved correction', page)
