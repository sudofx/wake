"""Only interface changes need a Pages artifact; uncertain comparisons rebuild."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('pages_delivery', Path(__file__).resolve().parents[1] / 'scripts/pages_delivery.py')
delivery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(delivery)


class PagesDeliveryTests(unittest.TestCase):
    def test_skip_only_known_current_or_non_presentation_changes(self):
        current = {'presentation': {'source_revision': 'a' * 40, 'data_transport': 'github-pinned@1'}}
        self.assertFalse(delivery.needs_delivery(current, 'a' * 40))
        comparison = {'status': 'ahead', 'files': [{'filename': 'wake/kernel/record.py'}]}
        self.assertFalse(delivery.needs_delivery(current, 'b' * 40, comparison))
        comparison['files'].append({'filename': 'wake/assets/reader-data.js'})
        self.assertTrue(delivery.needs_delivery(current, 'b' * 40, comparison))
        comparison['files'] = [{'filename': 'elsewhere', 'previous_filename': 'wake/assets/reader-data.js'}]
        self.assertTrue(delivery.needs_delivery(current, 'b' * 40, comparison))
        for invalid in (None, {}, {'status': 'diverged'}, {'status': 'ahead', 'files': [{}] * 300}):
            self.assertTrue(delivery.needs_delivery(current, 'b' * 40, invalid))
        self.assertTrue(delivery.needs_delivery({}, 'b' * 40))
