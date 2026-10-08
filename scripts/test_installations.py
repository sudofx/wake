"""Offline multi-installation acceptance using the real Compose deployment path.

Only unique test projects/volumes are removed. Never targets an operator project.
Build the supplied image first; fixture work makes no external provider calls.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
import urllib.request
import urllib.error
import uuid

ROOT = Path(__file__).resolve().parents[1]


def check(image, gateway_image=None):
    prefix = 'wake-isolation-' + uuid.uuid4().hex[:10]
    names = [prefix + '-a', prefix + '-b']
    gateway = prefix + '-gateway'
    network = prefix + '-network'
    temporary = tempfile.TemporaryDirectory()
    environment = dict(os.environ)
    # Explicit test settings win over checkout .env and shell credentials.
    environment.update(WAKE_INSTANCE_IMAGE=image, WAKE_INSTANCE_PROVIDER='fixture',
                       WAKE_INSTANCE_GEMINI_API_KEY='', WAKE_INSTANCE_PAUSED='true',
                       WAKE_INSTANCE_INTERVAL_SECONDS='1', WAKE_INSTANCE_PORT='0',
                       WAKE_INSTANCE_BIND='127.0.0.1',
                       WAKE_INSTANCE_ENABLE_CONTINUITY_MATRIX='false')
    if gateway_image:
        environment['WAKE_GATEWAY_NETWORK'] = network
        environment.update(WAKE_GATEWAY_IMAGE=gateway_image, WAKE_GATEWAY_PORT='0',
                           WAKE_GATEWAY_BIND='127.0.0.1')

    def gateway_compose(*args):
        return subprocess.check_output(
            ['docker', 'compose', '-p', gateway, '-f', str(ROOT / 'deploy/gateway/compose.yaml'),
             '-f', str(Path(temporary.name) / 'gateway.json'), *args],
            env=environment, text=True, stderr=subprocess.PIPE).strip()

    def compose(name, *args, paused=True):
        env = {**environment, 'WAKE_INSTANCE_PAUSED': str(paused).lower()}
        command = ['docker', 'compose', '--env-file', str(ROOT / 'deploy/instances.env.example'),
             '-p', name, '-f', str(ROOT / 'compose.yaml'),
             '-f', str(ROOT / 'compose.instances.yaml')]
        if gateway_image:
            command.extend(['-f', str(ROOT / 'compose.proxy-client.yaml')])
        return subprocess.check_output(command + list(args), env=env, text=True,
                                       stderr=subprocess.PIPE).strip()

    def ready(name, minimum=0):
        deadline = time.monotonic() + 90
        while time.monotonic() < deadline:
            try:
                runtime = json.loads(compose(name, 'exec', '-T', 'wake', 'python', '-c',
                    "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8080/runtime.json').read().decode())"))
                audit = json.loads(compose(name, 'exec', '-T', 'wake', 'python', '-m',
                                          'wake', '--data', '/data', 'audit'))
                if audit['cycles'] >= minimum:
                    return runtime, audit
            except (subprocess.CalledProcessError, json.JSONDecodeError):
                pass
            time.sleep(.5)
        raise RuntimeError(f'{name}: readiness timed out')

    def events(name):
        return json.loads(compose(name, 'exec', '-T', 'wake', 'python', '-c',
            "import json; from wake.authority import open_authoritative_store; s=open_authoritative_store('/data'); print(json.dumps(s.events()))"))

    try:
        if gateway_image:
            subprocess.run(['docker', 'network', 'create', network], check=True, capture_output=True)
        for name in names:
            compose(name, 'up', '-d', '--no-build', '--pull', 'never')
        _, before_a = ready(names[0])
        _, before_b = ready(names[1])
        assert before_a['cycles'] == before_b['cycles'] == 0
        addresses = [compose(name, 'port', 'wake', '8080') for name in names]
        assert addresses[0] != addresses[1], addresses
        for address in addresses:
            origin = 'http://' + address
            with urllib.request.urlopen(origin + '/deployment.json', timeout=5) as response:
                assert json.load(response) == {'schema': 1, 'mode': 'standalone'}
            with urllib.request.urlopen(origin + '/console.html', timeout=5) as response:
                assert 'window.WAKE_STANDALONE=true' in response.read().decode()
        compose(names[0], 'up', '-d', '--no-build', '--pull', 'never', paused=False)
        ready(names[0], minimum=2)
        compose(names[0], 'up', '-d', '--no-build', '--pull', 'never')
        runtime_a, advanced = ready(names[0], minimum=2)
        prefix_events = events(names[0])
        _, unchanged = ready(names[1])
        assert before_b['head'] == unchanged['head'] and unchanged['cycles'] == 0
        assert runtime_a['state'] == 'paused'
        compose(names[0], 'down')  # Volume survives ordinary maintenance.
        compose(names[0], 'up', '-d', '--no-build', '--pull', 'never')
        _, recreated = ready(names[0], minimum=2)
        assert recreated['head'] == advanced['head']
        assert events(names[0]) == prefix_events
        assert recreated['valid'] and unchanged['valid']
        if gateway_image:
            config = (ROOT / 'deploy/gateway/nginx.conf').read_text()
            config = config.replace('wake-alpha:8080', names[0] + ':8080')
            config = config.replace('wake-beta:8080', names[1] + ':8080')
            config_path = Path(temporary.name) / 'nginx.conf'
            config_path.write_text(config)
            (Path(temporary.name) / 'gateway.json').write_text(json.dumps({'services': {
                'gateway': {'volumes': [{'type': 'bind', 'source': str(config_path),
                                        'target': '/etc/nginx/nginx.conf', 'read_only': True}]}}}))
            gateway_compose('up', '-d', '--pull', 'never')
            address = gateway_compose('port', 'gateway', '8080')

            def fetch(host, path='/wake-data.json'):
                request = urllib.request.Request('http://' + address + path, headers={'Host': host})
                with urllib.request.urlopen(request, timeout=5) as response:
                    return json.load(response)

            deadline = time.monotonic() + 30
            while True:
                try:
                    fetch('alpha.wake.test', '/deployment.json')
                    break
                except (OSError, ValueError):
                    if time.monotonic() >= deadline:
                        raise
                    time.sleep(.5)
            for host, name in zip(('alpha.wake.test', 'beta.wake.test'), names):
                direct = compose(name, 'port', 'wake', '8080')
                with urllib.request.urlopen('http://' + direct + '/wake-data.json') as response:
                    assert fetch(host) == json.load(response)
            try:
                fetch('unknown.wake.test')
                raise AssertionError('Unknown hostname was routed')
            except urllib.error.HTTPError as exc:
                assert exc.code == 404
            # A failed upstream must not fall through to another installation.
            compose(names[0], 'stop')
            try:
                fetch('alpha.wake.test')
                raise AssertionError('Stopped installation returned data')
            except urllib.error.HTTPError as exc:
                assert exc.code in (502, 504)
            assert fetch('beta.wake.test')
            # Keep the gateway running across replacement, allowing its short
            # DNS cache to expire. No configuration reload should be required.
            compose(names[0], 'down')
            compose(names[0], 'up', '-d', '--no-build', '--pull', 'never')
            ready(names[0], minimum=2)
            deadline = time.monotonic() + 30
            while True:
                try:
                    assert fetch('alpha.wake.test')
                    break
                except OSError:
                    if time.monotonic() >= deadline:
                        raise
                    time.sleep(.5)
        result = {'projects': names, 'distinct_dynamic_ports': True,
                  'independent_records': True, 'recreation_preserved_exact_history': True,
                  'advanced_cycles': advanced['cycles'], 'other_cycles': unchanged['cycles'],
                  'provider': 'fixture', 'external_provider_calls': 0}
        result['hostname_gateway_verified'] = bool(gateway_image)
        print(json.dumps(result))
        return result
    finally:
        if gateway_image and (Path(temporary.name) / 'gateway.json').exists():
            gateway_compose('down')
        for name in names:
            # --volumes is restricted here to fresh, random test projects.
            compose(name, 'down', '--volumes')
        if gateway_image:
            subprocess.run(['docker', 'network', 'rm', network], check=True, capture_output=True)
        temporary.cleanup()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--image', required=True)
    parser.add_argument('--gateway-image', help='Also verify explicit hostname routing with this Nginx image')
    args = parser.parse_args()
    check(args.image, args.gateway_image)
