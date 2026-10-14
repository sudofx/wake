"""Public layout preserves model-written prose and never invents a summary."""
import unittest
from wake.report import _blog_body_html, _blog_display_title, _blog_html


class BlogPresentationTests(unittest.TestCase):
    def test_explicit_sentence_marker_becomes_summary_heading_without_mutation(self):
        post = {'body': 'Exact introduction. Summary. Exact concluding words <kept>.', 'created_version': 1}
        before = post.copy()
        self.assertEqual(_blog_body_html(post, {}), '<p>Exact introduction.</p><h3>Summary</h3><p>Exact concluding words &lt;kept&gt;.</p>')
        self.assertEqual(post, before)

    def test_summary_mentions_and_empty_markers_do_not_create_a_section(self):
        for body in ('A Summary. might be mentioned mid-sentence.', 'A useful explanation. Summary.   ', 'A useful explanation without a summary.'):
            with self.subTest(body=body):
                rendered = _blog_body_html({'body': body, 'created_version': 1}, {})
                self.assertNotIn('<h3>', rendered)

    def test_shared_checkpoint_metadata_does_not_use_leader_accepted_cycle(self):
        post = {'id': 'shared', 'title': 'Shared work', 'lede': 'A plain introduction.',
                'body': 'Exact prose. Summary. Exact summary.', 'created_version': 10,
                'created_by': 'leader-invocation', 'notebooks': [], 'evidence': [],
                'group_publication': {'checkpoint': 1, 'members': ['100.wake']}}
        before = post.copy()
        self.assertEqual(_blog_display_title(post), 'Shared work')
        self.assertIn('SHARED CHECKPOINT 01', _blog_html(post, {}))
        self.assertEqual(post, before)
