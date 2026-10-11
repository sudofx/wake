"""A storage upgrade must retain authority and recover the original container."""
import unittest
from unittest.mock import patch
from scripts.wake_passenger_upgrade import configuration, upgrade, LABEL


def specification():
    return {
        'Image': 'sha256:fixture',
        'Config': {'User': '10001:10001', 'WorkingDir': '/workspace',
                   'Labels': {LABEL: 'true', LABEL+'.role': 'parent', LABEL+'.hostname': '100.wake'},
                   'Env': ['WAKE_PAUSED=true'], 'Entrypoint': ['python', '-m', 'wake.standalone'], 'Cmd': []},
        'HostConfig': {'ReadonlyRootfs': True, 'Privileged': False,
                       'PortBindings': {'8080/tcp': [{'HostIp': '', 'HostPort': ''}]},
                       'Tmpfs': {'/tmp': ''}, 'RestartPolicy': {'Name': ''}},
        'Mounts': [{'Destination': '/data', 'Type': 'volume', 'Name': 'original-data', 'RW': True},
                   {'Destination': '/workspace', 'Type': 'bind', 'Source': '/checkout', 'RW': True}],
        'NetworkSettings': {'Networks': {'cell': {'Aliases': ['100.wake']}}},
    }


class PassengerUpgradeTests(unittest.TestCase):
    def test_candidate_preserves_existing_data_and_adds_only_cell_advisory_volume(self):
        args, networks = configuration(specification(), '100.wake', '100.wake')
        self.assertIn('original-data:/data:rw', args)
        self.assertIn('100.wake-passenger:/passenger', args)
        self.assertIn('WAKE_PAUSED=true', args)
        self.assertIn('WAKE_PASSENGER_INSTALLATION=100.wake', args)
        self.assertEqual(networks, [])

    def test_failed_replacement_restores_original_without_removing_volumes(self):
        calls = []
        def docker(*args):
            calls.append(args)
            if args[0] == 'create':
                raise RuntimeError('replacement failed')
            if args[0] == 'ps':
                return '' if 'name=^/100.wake-passenger-upgrade-backup$' in args else '100.wake'
            return ''
        with patch('scripts.wake_passenger_upgrade.inspect', return_value=specification()), \
             patch('scripts.wake_passenger_upgrade.runtime', side_effect=[{'state':'paused'}, {'head':'old-head','state':{'pending':None}}]), \
             patch('scripts.wake_passenger_upgrade.docker', side_effect=docker):
            with self.assertRaises(RuntimeError):
                upgrade('100.wake')
        self.assertIn(('rename', '100.wake-passenger-upgrade-backup', '100.wake'), calls)
        self.assertIn(('start', '100.wake'), calls)
        self.assertNotIn(('volume', 'rm', 'original-data'), calls)
        self.assertFalse(any(call[:2] == ('volume', 'rm') for call in calls))


if __name__ == '__main__':
    unittest.main()
