"""Full-history renderers share a bounded installation memory admission."""
from concurrent.futures import ThreadPoolExecutor
from contextlib import ExitStack
import tempfile
import threading
import unittest

from wake.export_admission import export_slot


class ExportAdmissionTests(unittest.TestCase):
    def test_independent_renderers_share_two_slots(self):
        with tempfile.TemporaryDirectory() as directory:
            started = threading.Barrier(4)
            lock = threading.Lock()
            occupied = threading.Event()
            release = threading.Event()
            active = peak = 0
            def render():
                nonlocal active, peak
                started.wait(timeout=3)
                with export_slot(directory):
                    with lock:
                        active += 1
                        peak = max(peak, active)
                        if active == 2:
                            occupied.set()
                    release.wait(timeout=3)
                    with lock:
                        active -= 1
            with ThreadPoolExecutor(max_workers=4) as pool:
                futures = [pool.submit(render) for _ in range(4)]
                try:
                    self.assertTrue(occupied.wait(timeout=3))
                    with lock:
                        self.assertEqual(active, 2)
                finally:
                    release.set()
                for future in futures:
                    future.result(timeout=4)
            self.assertEqual(peak, 2)

    def test_failed_export_releases_admission(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, 'render failed'):
                with export_slot(directory):
                    raise ValueError('render failed')
            with ExitStack() as stack:
                stack.enter_context(export_slot(directory))
                stack.enter_context(export_slot(directory))


if __name__ == '__main__':
    unittest.main()
