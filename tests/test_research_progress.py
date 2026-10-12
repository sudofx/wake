import json
import unittest
from wake.research_progress import research_progress


class ResearchProgressTests(unittest.TestCase):
    def test_mirrors_and_rewording_do_not_create_more_support(self):
        passage = 'A conserved reaction network has a multinomial equilibrium distribution.'
        payload = json.dumps({'source_identity': 'arxiv:2205.06313', 'excerpt': passage})
        evidence = {'a': {'actor': 'collector', 'scope': 'collected', 'source': 'https://arxiv.org/abs/2205.06313', 'content': payload},
                    'b': {'actor': 'collector', 'scope': 'collected', 'source': 'https://arxiv.org/pdf/2205.06313', 'content': payload}}
        state = {'version': 10, 'evidence': evidence, 'notebooks': {'n': {'revision': 2, 'claims': [{'statement': 'First wording', 'support': [{'evidence': 'a', 'passage': passage}], 'certainty': 'hypothesis'}, {'statement': 'Reworded', 'support': [{'evidence': 'b', 'passage': passage}], 'certainty': 'hypothesis'}]}}}
        progress = research_progress(state)
        self.assertEqual(progress['distinct_source_works'], 1)
        self.assertEqual(progress['distinct_supporting_passages'], 1)
        self.assertEqual(progress['measured_reproductions'], 0)
        self.assertEqual(progress['activity']['accepted_cycles'], 10)
        self.assertIn('not automatically scored', progress['interpretation'])
