"""Lossless long-string dictionaries for physical JSON storage, not semantic state."""
from collections import Counter
import re
import struct
import zlib

# Consume ordinary text in spans: per-character alternatives make long saved
# provider strings costly to scan. Escapes retain the exact existing token grammar.
_STRING = re.compile(rb'"[^"\\]*(?:\\.[^"\\]*)*"')
_MIN_BYTES = 128 * 1024


def encode_dictionary(raw: bytes, level: int) -> bytes | None:
    """Intern repeated exact JSON string tokens beyond zlib's sliding window.

    NUL never occurs in valid UTF-8 JSON text: it is the unambiguous reference
    marker. Entries retain original escapes and Unicode bytes, not parsed prose.
    Each stream owns its dictionary; there are no external/missing blob roots.
    """
    if len(raw) < _MIN_BYTES or b'\0' in raw:
        return None
    counts = Counter(m.group() for m in _STRING.finditer(raw)
                     if m.end() - m.start() >= 256)
    entries = [token for token, count in counts.items() if count > 1]
    if not entries:
        return None
    ids = {token: index for index, token in enumerate(entries)}
    def replace(match):
        token = match.group()
        index = ids.get(token)
        return b'\0' + struct.pack('>I', index) if index is not None else token
    body = _STRING.sub(replace, raw)
    packed = (struct.pack('>I', len(entries))
              + b''.join(struct.pack('>I', len(token)) + token for token in entries)
              + body)
    return zlib.compress(packed, level)


def decode_dictionary(packed: bytes) -> bytes:
    """Reject malformed dictionaries/references rather than recovering guessed text."""
    offset = 0
    def integer():
        nonlocal offset
        if offset + 4 > len(packed):
            raise ValueError('truncated dictionary integer')
        value = struct.unpack_from('>I', packed, offset)[0]
        offset += 4
        return value
    count = integer()
    if count > (len(packed) - offset) // 4:
        raise ValueError('invalid dictionary count')
    entries = []
    for _ in range(count):
        size = integer()
        if size < 256 or offset + size > len(packed):
            raise ValueError('invalid dictionary entry size')
        token = packed[offset:offset + size]
        offset += size
        if not _STRING.fullmatch(token) or b'\0' in token:
            raise ValueError('invalid dictionary string token')
        entries.append(token)
    if len(set(entries)) != len(entries):
        raise ValueError('duplicate dictionary entry')
    chunks = []
    while offset < len(packed):
        marker = packed.find(b'\0', offset)
        if marker < 0:
            chunks.append(packed[offset:])
            break
        chunks.append(packed[offset:marker])
        offset = marker + 1
        index = integer()
        if index >= len(entries):
            raise ValueError('invalid dictionary reference')
        chunks.append(entries[index])
    return b''.join(chunks)
