"""Compatibility hints for reusing immutable presentation, never authority."""
from hashlib import sha256
from pathlib import Path


def code_fingerprint():
    root = Path(__file__).parent
    digest = sha256()
    for path in sorted(root.rglob('*.py')):
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


# Freeze the code revision when the renderer is loaded. A bind mount edited
# later must not label an old loaded renderer as executing the new source.
CODE_FINGERPRINT = code_fingerprint()


def renderer_signature():
    digest = sha256(CODE_FINGERPRINT.encode())
    assets = Path(__file__).parent / 'assets'
    for path in sorted(assets.rglob('*')):
        if path.is_file():
            digest.update(path.relative_to(assets).as_posix().encode())
            digest.update(path.read_bytes())
    return digest.hexdigest()
