"""Rate pressure cannot exhaust controls or silently retry ambiguous writes."""
from contextlib import redirect_stdout
import io
import unittest
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

from wake.hosted import GitHub


class HostedAPITests(unittest.TestCase):
    def response(self, remaining='900'):
        response = MagicMock()
        response.__enter__.return_value = response
        response.headers = {'X-RateLimit-Limit': '1000', 'X-RateLimit-Remaining': remaining,
                            'X-RateLimit-Reset': '130'}
        response.read.return_value = b'{"state":"active"}'
        return response

    def test_exhausted_safe_read_waits_until_reset_and_keeps_diagnostics_private(self):
        error = HTTPError('https://api.github.com/private', 403, 'Forbidden',
                          {'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '130'},
                          io.BytesIO(b'PRIVATE ERROR BODY'))
        output = io.StringIO()
        client = GitHub('owner/repo', 'SECRET')
        with patch('wake.hosted.urlopen', side_effect=[error, self.response()]) as call, \
             patch('wake.hosted.time.time', return_value=100), \
             patch('wake.hosted.time.sleep') as sleep, redirect_stdout(output):
            self.assertEqual(client.request('actions/workflows/research.yml')['state'], 'active')
        sleep.assert_called_once_with(31)
        self.assertEqual(call.call_count, 2)
        self.assertNotIn('PRIVATE', output.getvalue())
        self.assertNotIn('SECRET', output.getvalue())

    def test_data_budget_reserves_control_capacity_before_next_mutation(self):
        client = GitHub('owner/repo', 'fixture', reserve=100)
        with patch('wake.hosted.urlopen', side_effect=[self.response('100'), self.response()]), \
             patch('wake.hosted.time.time', return_value=100), \
             patch('wake.hosted.time.sleep') as sleep, redirect_stdout(io.StringIO()):
            client.request('releases/assets/1')
            client.request('releases/1/assets', method='POST', body=b'encrypted', upload=True)
        sleep.assert_called_once_with(31)

    def test_permission_denial_and_ambiguous_writes_are_not_retried(self):
        for method, headers in [('GET', {}), ('POST', {'Retry-After': '60'})]:
            with self.subTest(method=method), patch('wake.hosted.urlopen', side_effect=HTTPError(
                    'https://api.github.com', 403, 'Forbidden', headers, None)) as call, \
                 patch('wake.hosted.time.sleep') as sleep, redirect_stdout(io.StringIO()):
                with self.assertRaises(HTTPError):
                    GitHub('owner/repo', 'fixture').request('path', method=method)
                self.assertEqual(call.call_count, 1)
                sleep.assert_not_called()

    def test_secondary_retry_after_and_control_fail_closed_bound(self):
        for allowance in (0, 120):
            with self.subTest(allowance=allowance), \
                 patch('wake.hosted.urlopen', side_effect=[HTTPError(
                     'https://api.github.com', 403, 'Forbidden', {'Retry-After': '60'}, None), self.response()]), \
                 patch('wake.hosted.time.sleep') as sleep, redirect_stdout(io.StringIO()):
                client = GitHub('owner/repo', 'fixture', rate_wait_limit=allowance)
                if allowance:
                    client.request('path')
                    sleep.assert_called_once_with(60)
                else:
                    with self.assertRaises(HTTPError):
                        client.request('path')
                    sleep.assert_not_called()

    def test_secondary_limit_without_header_waits_without_publishing_message(self):
        output = io.StringIO()
        error = HTTPError('https://api.github.com', 403, 'Forbidden', {},
                          io.BytesIO(b'{"message":"You exceeded a secondary rate limit. PRIVATE"}'))
        with patch('wake.hosted.urlopen', side_effect=[error, self.response()]), \
             patch('wake.hosted.time.sleep') as sleep, redirect_stdout(output):
            GitHub('owner/repo', 'fixture').request('path')
        sleep.assert_called_once_with(60)
        self.assertNotIn('PRIVATE', output.getvalue())
        self.assertIn('"secondary_limit": true', output.getvalue())

    def test_upload_headers_do_not_erase_known_budget(self):
        client = GitHub('owner/repo', 'fixture', reserve=100)
        no_headers = self.response()
        no_headers.headers = {}
        with patch('wake.hosted.time.time', return_value=100), patch('wake.hosted.urlopen',
                side_effect=[self.response('102'), no_headers]):
            client.request('releases/assets/1')
            client.request('releases/1/assets', method='POST', body=b'encrypted', upload=True)
        self.assertEqual(client.rate['Remaining'], 101)
        self.assertEqual(client.rate['Reset'], 130)

    def test_workers_share_budget_and_wait_before_upload(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as folder, patch('wake.hosted.time.time', return_value=100):
            path = Path(folder) / 'github-rate.json'
            first = GitHub('owner/repo', 'fixture', reserve=100, rate_file=path)
            first.observe_rate({'X-RateLimit-Remaining':'100','X-RateLimit-Reset':'130'})
            second = GitHub('owner/repo', 'fixture', reserve=100, rate_file=path)
            response = self.response();response.headers['X-RateLimit-Reset']='3730'
            with patch('wake.hosted.urlopen', return_value=response), patch('wake.hosted.time.sleep') as sleep, redirect_stdout(io.StringIO()):
                second.request('releases/1/assets', method='POST', body=b'encrypted', upload=True)
            sleep.assert_called_once_with(31)
            self.assertNotIn('fixture', path.read_text())
            self.assertEqual(second.rate['Remaining'], 900)

    def test_expired_shared_budget_does_not_poison_new_window(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'github-rate.json'
            path.write_text('{"Remaining":0,"Reset":99}')
            client = GitHub('owner/repo', 'fixture', reserve=100, rate_file=path)
            with patch('wake.hosted.time.time', return_value=100), patch('wake.hosted.urlopen', return_value=self.response()), patch('wake.hosted.time.sleep') as sleep:
                client.request('path')
            sleep.assert_not_called()
            self.assertEqual(client.rate['Remaining'], 900)

    def test_malformed_shared_budget_fails_before_network_effect(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'github-rate.json';path.write_text('{"token":"PRIVATE"}')
            with patch('wake.hosted.urlopen') as network:
                with self.assertRaisesRegex(ValueError, 'Invalid shared'):
                    GitHub('owner/repo', 'fixture', rate_file=path).request('path', method='POST')
            network.assert_not_called()

    def test_parallel_workers_debit_the_same_numeric_ledger(self):
        import tempfile,json
        from pathlib import Path
        from concurrent.futures import ThreadPoolExecutor
        with tempfile.TemporaryDirectory() as folder, patch('wake.hosted.time.time',return_value=100):
            path=Path(folder)/'github-rate.json'
            GitHub('owner/repo','fixture',rate_file=path).observe_rate({'X-RateLimit-Remaining':'500','X-RateLimit-Reset':'130'})
            response=self.response();response.headers={}
            with patch('wake.hosted.urlopen',return_value=response),ThreadPoolExecutor(max_workers=8) as pool:
                list(pool.map(lambda _:GitHub('owner/repo','fixture',reserve=100,rate_file=path).request('path'),range(20)))
            self.assertEqual(json.loads(path.read_text())['Remaining'],480)
