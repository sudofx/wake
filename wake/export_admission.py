"""Bound installation-wide rendering memory without governing research."""
from contextlib import contextmanager
import fcntl
from pathlib import Path
import time


@contextmanager
def export_slot(directory):
    """Admit at most two full node exports; process death releases the slot.

    Native snapshots contain full history. Twelve simultaneous renderers can
    exhaust a standard hosted runner even when each record is individually
    small enough to load. These locks cover disposable rendering only.
    """
    if directory is None:
        yield
        return
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    streams = []
    selected = None
    try:
        for index in range(2):
            streams.append((directory / str(index)).open('a'))
        while selected is None:
            for stream in streams:
                try:
                    fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError:
                    continue
                selected = stream
                break
            if selected is None:
                time.sleep(.05)
        yield
    finally:
        for stream in streams:
            stream.close()
