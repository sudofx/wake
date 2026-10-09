"""Web discussions route to primary material without acquiring evidence authority."""
import json
import unittest
from urllib.parse import urlsplit

from wake.research import (allowed_url, candidate_source_urls,
                           evidence_role, host_tier, research_urls, web_search_url)


class SearchDiscoveryTests(unittest.TestCase):
    def test_web_and_reddit_searches_are_always_discovery(self):
        for reddit in (False, True):
            url = web_search_url('sensor contradiction', reddit=reddit)
            self.assertEqual(allowed_url(url), url)
            self.assertEqual(evidence_role(url), 'discovery')
            self.assertEqual(host_tier(url), 'discovery')
        with self.assertRaises(ValueError):
            allowed_url('https://www.reddit.com/r/science/comments/123/example/')

    def test_search_links_keep_primary_source_routes_and_ignore_unapproved_hosts(self):
        observation = {'result_urls': [
            'https://arxiv.org/pdf/2401.12345.pdf',
            'https://www.reddit.com/r/science/comments/example',
            'https://127.0.0.1/private']}
        self.assertEqual(candidate_source_urls(observation), ['https://arxiv.org/pdf/2401.12345.pdf'])
        self.assertIn('reddit.com', json.dumps(observation))
        self.assertEqual(candidate_source_urls({'url': web_search_url('curiosity'),
                                               'results': observation}), ['https://arxiv.org/pdf/2401.12345.pdf'])

    def test_all_search_indexes_remain_leads_and_targeted_rotation_excludes_datacite(self):
        for targeted in (False, True):
            routes = research_urls('memory provenance', 'memory', targeted=targeted)
            self.assertTrue(all(evidence_role(url) == 'discovery' for url in routes))
            self.assertIn('www.ebi.ac.uk', {urlsplit(url).hostname for url in routes})
            self.assertIn('export.arxiv.org', {urlsplit(url).hostname for url in routes})
            self.assertEqual(any('api.datacite.org' in url for url in routes), not targeted)
