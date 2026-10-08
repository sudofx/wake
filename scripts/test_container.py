"""Offline OCI acceptance: recreate containers, preserve volume, audit exact prefix.

Run after building wake-standalone:local. Docker engine and both target images required.
No API keys or network access are used. Only uniquely named test resources are removed.
"""
import argparse
import json
import subprocess
import time
import uuid


def docker(*args):
    return subprocess.check_output(['docker', *args], text=True, stderr=subprocess.PIPE).strip()


def check(image, platform):
    name = 'wake-continuity-' + uuid.uuid4().hex[:12]
    volume = name + '-data'
    container = None
    docker('volume', 'create', volume)

    def start(paused=False):
        args = ['run', '-d', '--name', name, '--platform', platform, '--network', 'none',
                '--read-only', '--tmpfs', '/tmp:mode=1777', '--cap-drop', 'ALL',
                '-v', volume + ':/data', '-e', 'WAKE_PROVIDER=fixture',
                '-e', 'WAKE_INTERVAL_SECONDS=1', image]
        if paused:
            args.append('--paused')
        return docker(*args)

    def audit():
        docker('exec', name, 'python', '-c', "from wake.authority import verify_existing_record; verify_existing_record('/data/wake.sqlite')")
        return json.loads(docker('exec', name, 'python', '-m', 'wake', '--data', '/data', 'audit'))

    def ready(cycles=0):
        deadline = time.monotonic() + 90
        while time.monotonic() < deadline:
            if docker('inspect', '--format', '{{.State.Running}}', name) != 'true':
                raise RuntimeError(docker('logs', name))
            try:
                docker('exec', name, 'python', '-c', "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/runtime.json').read()")
                result = audit()
                if result['cycles'] >= cycles:
                    return result
            except subprocess.CalledProcessError:
                pass
            time.sleep(.5)
        raise RuntimeError('Container readiness timeout')

    try:
        container = start()
        ready(2)
        # Kill PID 1 as an unclean stop, then remove and recreate it.
        docker('kill', name)
        docker('rm', name)
        container = None
        container = start(paused=True)
        before = ready(2)
        prefix = docker('exec', name, 'python', '-c', "from wake.authority import open_authoritative_store; import json; s=open_authoritative_store('/data'); print(json.dumps(s.events()))")
        website = docker('exec', name, 'python', '-c', "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8080/console.html').read().decode())")
        assert 'window.WAKE_STANDALONE=true' in website
        for path in ('/.env', '/wake.sqlite', '/wake.toml', '/../data/wake.sqlite'):
            docker('exec', name, 'python', '-c', f"import urllib.request, urllib.error\ntry: urllib.request.urlopen('http://127.0.0.1:8080{path}'); raise AssertionError('Private file exposed')\nexcept urllib.error.HTTPError as e: assert e.code == 404")
        docker('stop', '--time', '30', name)
        docker('rm', name)
        container = None
        container = start(paused=True)
        after = ready()
        assert after['head'] == before['head'], (before, after)
        assert after['cycles'] == before['cycles']
        docker('stop', '--time', '30', name)
        docker('rm', name)
        container = None
        container = start()
        ready(before['cycles'] + 1)
        docker('stop', '--time', '30', name)
        docker('rm', name)
        container = None
        container = start(paused=True)
        final = ready()
        events = json.loads(docker('exec', name, 'python', '-c', "from wake.authority import open_authoritative_store; import json; s=open_authoritative_store('/data'); print(json.dumps(s.events()))"))
        prior = json.loads(prefix)
        assert events[:len(prior)] == prior
        assert final['cycles'] > before['cycles'] and final['valid']
        print(json.dumps({'platform': platform, 'before': before, 'after': final, 'exact_prefix_preserved': True, 'network': 'none'}))
    finally:
        if container:
            subprocess.run(['docker', 'rm', '-f', name], check=False, capture_output=True)
        docker('volume', 'rm', volume)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--image', default='wake-standalone:local')
    parser.add_argument('--platform', action='append', choices=('linux/arm64', 'linux/amd64'),
                        help='Test selected platform(s); defaults to both')
    args = parser.parse_args()
    for architecture in args.platform or ('linux/arm64', 'linux/amd64'):
        check(args.image, architecture)
