"""A data-only evaluation publisher cannot dispatch jobs or replace another ref."""
import subprocess
import unittest
from unittest.mock import patch
from scripts.publish_evaluation import publish


class EvaluationPublicationTests(unittest.TestCase):
    def test_only_fixed_data_branch_advances_without_forcing(self):
        calls = []
        def api(repo, resource, method='GET', body=None):
            calls.append((resource, method, body))
            if resource == 'git/ref/heads/wake-evaluations':
                return {'object': {'sha': 'a'*40}}
            return {'sha': 'b'*40}
        with patch('scripts.publish_evaluation.api', api):
            publish('example/repo', {'schema': 'wake-evaluation@1', 'result_id': 'test'})
        self.assertEqual(calls[-1], ('git/refs/heads/wake-evaluations', 'PATCH',
                                    {'sha': 'b'*40, 'force': False}))
        self.assertFalse(any('actions' in resource or 'pages' in resource for resource, _, _ in calls))
        tree = next(body for resource, _, body in calls if resource == 'git/trees')
        self.assertEqual([row['path'] for row in tree['tree']], ['latest.json'])

    def test_creation_requires_explicit_initialization_and_a_missing_branch(self):
        def denied(*args, **kwargs):
            raise subprocess.CalledProcessError(1, 'gh', stderr=b'HTTP 403')
        with patch('scripts.publish_evaluation.api', denied):
            with self.assertRaises(subprocess.CalledProcessError):
                publish('example/repo', {'schema': 'wake-evaluation@1', 'result_id': 'test'}, initialize=True)
