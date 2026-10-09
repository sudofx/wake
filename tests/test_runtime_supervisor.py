"""Recovery restarts execution only; deliberate and permanent stops remain stops."""
import os
from pathlib import Path
import signal
import sys
import tempfile
import threading
import unittest
from wake.runtime_supervisor import supervise


class RuntimeSupervisorTests(unittest.TestCase):
    def attempt(self, first):
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / 'attempts'
            code = ("from pathlib import Path; import os,signal; "
                    f"p=Path({str(marker)!r}); n=int(p.read_text()) if p.exists() else 0; "
                    "p.write_text(str(n+1)); " + first + " if n==0 else None")
            result = supervise([sys.executable, '-c', code], retry_delay=.01)
            return result, int(marker.read_text())

    def test_temporary_exit_recovers(self):
        result, calls = self.attempt('os._exit(75)')
        self.assertEqual((result, calls), (0, 2))

    def test_unexpected_signal_recovers(self):
        self.assertEqual(self.attempt('os.kill(os.getpid(), signal.SIGKILL)'), (0, 2))

    def test_normal_exit_and_fatal_failure_do_not_retry(self):
        self.assertEqual(self.attempt('os._exit(0)'), (0, 1))
        self.assertEqual(self.attempt('os._exit(1)'), (1, 1))

    def test_stop_during_recovery_delay_does_not_restart(self):
        stop = threading.Event()
        timer = threading.Timer(.3, stop.set)
        timer.start()
        try:
            self.assertEqual(supervise([sys.executable, '-c', 'import os; os._exit(75)'],
                                       stop=stop, retry_delay=30), 0)
        finally:
            timer.cancel()

    def test_restart_burst_observes_cooldown(self):
        from unittest.mock import patch
        process = unittest.mock.Mock()
        process.poll.return_value = 75
        process.wait.side_effect = [75, 75, 0]
        stop = unittest.mock.Mock()
        stop.is_set.return_value = False
        stop.wait.return_value = False
        with patch('wake.runtime_supervisor.subprocess.Popen', return_value=process), \
             patch('wake.runtime_supervisor.time.monotonic', return_value=0):
            supervise(['fixture'], stop=stop, retry_delay=1, window_seconds=900, restart_limit=1)
        waits = [call.args[0] for call in stop.wait.call_args_list]
        self.assertEqual(waits, [1, 900])
