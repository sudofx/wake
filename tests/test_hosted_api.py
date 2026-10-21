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
