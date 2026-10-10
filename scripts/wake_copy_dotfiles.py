"""Copy selected, staged host dotfiles into a WAKE runner home volume."""

import os
import pwd
import shutil
from pathlib import Path


SOURCE = Path("/run/wake-dotfiles")
TARGET = Path("/home/wake")
DOTFILES = (".bashrc", ".gitignore", ".bash_profile", ".profile", ".bash_aliases", ".inputrc")


def main():
    owner = pwd.getpwnam("wake")
    for name in DOTFILES:
        source = SOURCE / name
        if not source.is_file():
            continue
        target = TARGET / name
        if target.is_symlink():
            target.unlink()
        shutil.copy2(source, target)
        os.chown(target, owner.pw_uid, owner.pw_gid)


if __name__ == "__main__":
    main()
