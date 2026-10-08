"""Resolve deployment settings with native Compose; never start a service."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InstallationConfigTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which('docker'):
            raise unittest.SkipTest('Docker Compose is not installed')
        result = subprocess.run(['docker', 'compose', 'version'], capture_output=True)
        if result.returncode:
            raise unittest.SkipTest('Docker Compose is not installed')

    def config(self, project, gateway=False, **values):
        env = {key: value for key, value in os.environ.items()
               if not key.startswith(('WAKE_', 'COMPOSE_', 'GEMINI_'))}
        env.update(GEMINI_API_KEY='unrelated-key', WAKE_PAUSED='false', **values)
        files = ['compose.yaml', 'compose.instances.yaml']
        if gateway:
            files.append('compose.proxy-client.yaml')
        args = ['docker', 'compose', '--env-file', os.devnull, '-p', project]
        for file in files:
            args.extend(['-f', str(ROOT / file)])
        return json.loads(subprocess.check_output(args + ['config', '--format', 'json'],
                                                  text=True, env=env))

    def test_projects_have_distinct_volumes_images_and_safe_defaults(self):
        a, b = self.config('wake-test-a'), self.config('wake-test-b')
        self.assertNotEqual(a['volumes']['wake-data']['name'], b['volumes']['wake-data']['name'])
        self.assertNotEqual(a['services']['wake']['image'], b['services']['wake']['image'])
        service = a['services']['wake']
        self.assertNotIn('container_name', service)
        self.assertEqual(service['environment']['GEMINI_API_KEY'], '')
        self.assertEqual(service['environment']['WAKE_PAUSED'], 'true')
        self.assertEqual(service['environment']['WAKE_PROVIDER'], 'fixture')
        self.assertEqual(service['ports'][0]['published'], '0')
        self.assertEqual(service['ports'][0]['host_ip'], '127.0.0.1')

    def test_explicit_installation_settings_and_gateway_alias(self):
        result = self.config('wake-test-a', gateway=True, WAKE_INSTANCE_PORT='8099',
                             WAKE_INSTANCE_PROVIDER='gemini', WAKE_INSTANCE_GEMINI_API_KEY='test-only',
                             WAKE_INSTANCE_PAUSED='false', WAKE_INSTANCE_BIND='0.0.0.0')
        service = result['services']['wake']
        self.assertEqual(service['ports'][0]['published'], '8099')
        self.assertEqual(service['environment']['GEMINI_API_KEY'], 'test-only')
        self.assertEqual(service['environment']['WAKE_PAUSED'], 'false')
        self.assertEqual(service['networks']['gateway']['aliases'], ['wake-test-a'])
        self.assertTrue(result['networks']['gateway']['external'])
