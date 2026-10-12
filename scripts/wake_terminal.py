"""Repository-owned terminal setup and bounded, read-only local statistics."""
import argparse
import json
import os
from pathlib import Path
import pwd
import re
import socket
import time
from urllib.request import urlopen


COPIED_DOTFILES = ('.bashrc', '.bash_profile', '.profile', '.bash_aliases', '.inputrc', '.gitignore')
BASHRC = r'''# WAKE terminal; no host dotfiles or private advisory content are loaded.
[[ $- == *i* ]] || return
export PATH="/usr/local/bin:/usr/bin:/bin:$PATH"
export HISTCONTROL=ignoreboth
shopt -s histappend checkwinsize
alias ll='ls -alF'
alias wake-status='python /workspace/scripts/wake_terminal.py status'
_wake_prompt() {
    local detail
    detail="$(python /workspace/scripts/wake_terminal.py prompt 2>/dev/null)"
    PS1="${detail:-WAKE | status unavailable} \w\n\$ "
}
PROMPT_COMMAND=_wake_prompt
python /workspace/scripts/wake_terminal.py status
'''


def install(home, node, image=""):
    """Replace only the known imported shell files, preserving other home data."""
    home.mkdir(parents=True, exist_ok=True)
    for name in COPIED_DOTFILES:
        path = home / name
        if path.is_file() or path.is_symlink():
            path.unlink()
    files = {'.bashrc': '# Node: ' + node + '\n' + BASHRC,
             '.bash_profile': '[ -f "$HOME/.bashrc" ] && . "$HOME/.bashrc"\n',
             '.wake-node': node + '\n'}
    if image:
        files['.wake-image'] = image + '\n'
    owner = pwd.getpwnam('wake') if os.geteuid() == 0 else None
    for name, text in files.items():
        path = home / name
        if path.is_symlink():
            path.unlink()
        path.write_text(text)
        path.chmod(0o644)
        if owner:
            os.chown(path, owner.pw_uid, owner.pw_gid)


def public_json(path):
    with urlopen('http://127.0.0.1:8080/' + path, timeout=1) as response:
        raw = response.read(8 * 1024 * 1024 + 1)
    if len(raw) > 8 * 1024 * 1024:
        raise ValueError('snapshot size')
    return json.loads(raw)


def statistics():
    node_file = Path('/home/wake/.wake-node')
    node = os.environ.get('WAKE_PUBLIC_HOSTNAME') or (node_file.read_text().strip() if node_file.exists() else socket.gethostname())
    role = os.environ.get('WAKE_TERMINAL_ROLE') or ('child' if os.environ.get('WAKE_PARENT_HOSTNAME') else 'parent')
    group = os.environ.get('WAKE_GROUP_ID') or 'standalone'
    state, version = 'unavailable', '—'
    try:
        if role == 'gateway':
            config = json.loads(Path('/run/wake-group-router.json').read_text())
            state = f"gateway · {len(config['routes'])} nodes"
            group = ', '.join(sorted(config['groups']))
        else:
            state = public_json('runtime.json').get('state', 'unavailable')
            try:
                version = public_json('group/bob-input.json')['version']
            except Exception:
                version = public_json('state.json')['version']
    except Exception:
        pass
    memory = '—'
    try:
        current = int(Path('/sys/fs/cgroup/memory.current').read_text())
        memory = f'{current / 1024 / 1024:.0f} MiB'
        maximum = Path('/sys/fs/cgroup/memory.max').read_text().strip()
        if maximum != 'max':
            memory += f' / {int(maximum) / 1024 / 1024:.0f} MiB'
    except (OSError, ValueError):
        pass
    uptime = '—'
    try:
        seconds = int(float(Path('/proc/uptime').read_text().split()[0]))
        uptime = f'{seconds // 3600}h {(seconds // 60) % 60}m (host)'
    except (OSError, ValueError):
        pass
    return {'node': node, 'role': role, 'state': state, 'version': version,
            'memory': memory, 'uptime': uptime, 'load': ' '.join(f'{v:.2f}' for v in os.getloadavg()),
            'group': group,
            'parent': os.environ.get('WAKE_PARENT_HOSTNAME') or '—',
            'image': os.environ.get('WAKE_CONTAINER_IMAGE') or ((node_file.parent / '.wake-image').read_text().strip() if (node_file.parent / '.wake-image').exists() else 'not reported'),
            'observed': time.strftime('%H:%M:%S %Z')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('install', 'status', 'prompt'))
    parser.add_argument('--home', type=Path, default=Path('/home/wake'))
    parser.add_argument('--node', default='wake')
    parser.add_argument('--image', default='')
    args = parser.parse_args()
    if args.mode == 'install':
        install(args.home, args.node, args.image)
        return
    s = statistics()
    if args.mode == 'prompt':
        safe = lambda value: re.sub(r"[^A-Za-z0-9 .:_/@|·—-]", "?", str(value))
        print(f"{safe(s['node'])} | {safe(s['state'])} | accepted {safe(s['version'])} | {safe(s['memory'])}")
    else:
        authority = "Authority: none (read-only gateway)" if s["role"] == "gateway" else "Workspace: /workspace   Authority: /data/wake.sqlite"
        print(f"\nWAKE✳︎  {s['node']} · {s['role']}\n"
              f"Status: {s['state']}   Accepted cycles: {s['version']}   Observed: {s['observed']}\n"
              f"Group: {s['group']}   Parent: {s['parent']}   Image: {s['image']}\n"
              f"Memory: {s['memory']}   Load (host): {s['load']}   Uptime: {s['uptime']}\n"
              f"{authority}\n"
              "Live status refreshes at each prompt. Run wake-status for details.\n")


if __name__ == '__main__':
    main()
