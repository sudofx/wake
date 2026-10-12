"""Repository-owned terminal setup and bounded, read-only local statistics."""
import argparse
import json
import os
from pathlib import Path
import pwd
import re
import socket
import sys
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
    if [[ -t 1 && ${TERM:-dumb} != dumb && ! ${NO_COLOR+x} ]]; then
        detail="$(python /workspace/scripts/wake_terminal.py prompt --color 2>/dev/null)"
        PS1="\n\[\e[1;35m\]┌─ \[\e[0m\]${detail:-WAKE | status unavailable} \[\e[1;97m\]\w\[\e[0m\]\n\[\e[1;35m\]└─\[\e[1;36m\]\$\[\e[0m\] "
    else
        detail="$(python /workspace/scripts/wake_terminal.py prompt 2>/dev/null)"
        PS1="\n${detail:-WAKE | status unavailable} \w\n\$ "
    fi
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



def state_color(state):
    text = str(state).lower()
    if 'quota' in text:
        return '1;35'
    if text in ('failed', 'error', 'blocked'):
        return '1;31'
    if text in ('running', 'active') or text.startswith('gateway'):
        return '1;32'
    if text in ('paused', 'waiting', 'stopped'):
        return '1;33'
    return '1;34' if text == 'idle' else '37'


def colorize(value, code, enabled=False, *, prompt=False):
    if not enabled:
        return str(value)
    start, end = f'\x1b[{code}m', '\x1b[0m'
    if prompt:
        # Readline must not count ANSI sequences toward the cursor column.
        start, end = '\\[' + start + '\\]', '\\[' + end + '\\]'
    return start + str(value) + end


def prompt_details(s, colored=False):
    safe = lambda value: re.sub(r"[^A-Za-z0-9 .:_/@|·—-]", "?", str(value))
    paint = lambda value, code: colorize(safe(value), code, colored, prompt=True)
    sep = paint(' | ', '35')
    return sep.join((paint(s['node'], '1;36'), paint(s['state'], state_color(s['state'])),
                     paint('accepted ' + str(s['version']), '1;32'), paint(s['memory'], '1;34')))


def status_details(s, colored=False):
    paint = lambda value, code: colorize(value, code, colored)
    label = lambda text: paint(text, '37')
    authority = (label('Authority: ') + paint('none (read-only gateway)', '1;97')
                 if s['role'] == 'gateway' else
                 label('Workspace: ') + paint('/workspace', '1;97') + '   ' +
                 label('Authority: ') + paint('/data/wake.sqlite', '1;97'))
    return (f"\n{paint('WAKE✳︎', '1;35')}  {paint(s['node'], '1;36')} · {paint(s['role'], '1;35')}\n"
            f"{label('Status: ')}{paint(s['state'], state_color(s['state']))}   "
            f"{label('Accepted cycles: ')}{paint(s['version'], '1;32')}   "
            f"{label('Observed: ')}{paint(s['observed'], '1;97')}\n"
            f"{label('Group: ')}{paint(s['group'], '1;35')}   "
            f"{label('Parent: ')}{paint(s['parent'], '1;36')}   "
            f"{label('Image: ')}{paint(s['image'], '1;34')}\n"
            f"{label('Memory: ')}{paint(s['memory'], '1;34')}   "
            f"{label('Load (host): ')}{paint(s['load'], '1;97')}   "
            f"{label('Uptime: ')}{paint(s['uptime'], '1;97')}\n"
            f"{authority}\n"
            f"{label('Live status refreshes at each prompt. Run wake-status for details.')}\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('install', 'status', 'prompt'))
    parser.add_argument('--home', type=Path, default=Path('/home/wake'))
    parser.add_argument('--node', default='wake')
    parser.add_argument('--image', default='')
    parser.add_argument('--color', action='store_true', help='Enable color for prompt command substitution')
    args = parser.parse_args()
    if args.mode == 'install':
        install(args.home, args.node, args.image)
        return
    s = statistics()
    colored = ((args.color or sys.stdout.isatty()) and os.environ.get('TERM', 'dumb') != 'dumb'
               and 'NO_COLOR' not in os.environ)
    print(prompt_details(s, colored) if args.mode == 'prompt' else status_details(s, colored))


if __name__ == '__main__':
    main()
