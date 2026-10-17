# Preserve work between conversations

Use private Markdown checkpoints to keep current understanding, evidence, decisions
and open questions recoverable when a conversation ends. Start with the
[charter](charter.md). These notes complement WAKE's existing durable research
record; they do not change it. This workflow adds no runtime behavior or services.

## Create a checkpoint

From the repository root, run this block with Python 3 available. Set `context` to
`research` for exploratory notes or `implementation` for an engineering assignment.
It creates a unique directory exclusively: an existing directory is never reused.

```sh
context=implementation
checkpoint_dir=$(python3 - "$context" <<'PY'
from datetime import datetime, timezone
from pathlib import Path
import sys
import uuid
context = sys.argv[1]
if context not in {'research', 'implementation'}:
    raise SystemExit('Choose research or implementation')
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
identifier = stamp + '-' + uuid.uuid4().hex
root = Path('.wake-continuity') / context
root.mkdir(parents=True, exist_ok=True)
path = root / identifier
path.mkdir()
(path / 'checkpoint.md').write_bytes(Path('docs/continuity/checkpoint-template.md').read_bytes())
print(path)
PY
)
[ -n "$checkpoint_dir" ] && printf '%s\n' "$checkpoint_dir/checkpoint.md"
```

Open the printed file with your editor and fill its metadata and sections. Use the
folder name as its ID; use an actual timestamp with timezone. Record a baseline
only from verified available information. Write `UNKNOWN` for missing history and
`NONE — baseline` for a genuinely new record's predecessor. An empty template is
not a completed checkpoint. Do not copy private contents into terminal logs.

## Seal and revise

After review, run this block in the same shell, where `checkpoint_dir` names the
new directory. On a later shell, set that variable to the exact directory first.
The exclusive checksum creation refuses to replace an existing seal.

```sh
python3 - "$checkpoint_dir" <<'PY'
import hashlib
from pathlib import Path
import sys
path = Path(sys.argv[1])
digest = hashlib.sha256((path / 'checkpoint.md').read_bytes()).hexdigest()
with (path / 'checkpoint.sha256').open('x') as seal:
    seal.write(digest + '\n')
print('Checkpoint sealed; retain its directory and supporting references privately.')
PY
```

For a correction, changed objective or later session, create another checkpoint.
Cite the previous ID and the digest from its `checkpoint.sha256`, identify any
superseded conclusion and explain why it changed. Preserve the earlier directory.
The checksum detects later accidental modification, not malicious replacement of
both files; retain an independent private backup if stronger assurance is needed.
Create checkpoints at meaningful changes or before ending work, with a manual
periodic reminder if desired. There is no automatic checkpoint process.

## Recover and resume

Set `checkpoint_dir` to the checkpoint you intend to recover, then verify it:

```sh
python3 - "$checkpoint_dir" <<'PY'
import hashlib
from pathlib import Path
import sys
path = Path(sys.argv[1])
expected = (path / 'checkpoint.sha256').read_text().strip()
actual = hashlib.sha256((path / 'checkpoint.md').read_bytes()).hexdigest()
if expected != actual:
    raise SystemExit('Checkpoint checksum mismatch; preserve files and consult the private backup.')
print('Checkpoint checksum verified. Review the note and its references locally.')
PY
```

Read the checkpoint and follow previous IDs/digests to recover decisions and
corrections. Verify each predecessor the same way. If a note, seal or source is
missing, record that gap; do not invent the missing link. Check which checkpoint
supersedes a conclusion before relying on it. Refresh time-sensitive runtime or
publication facts from their proper sources before taking action.

Copy the [resumption template](resumption-template.md) to a new uniquely named
file within the chosen checkpoint directory, for example `resumption-01.md`,
without replacing an earlier summary. Curate a compact summary manually. Include
only necessary scope, selected checkpoint references, decisions, constraints and
unknowns; review private content before sharing it with a new conversation.
The seal covers `checkpoint.md` only: a summary is a disposable, separately dated
view and must be checked against those referenced checkpoints.

## Check privacy and keep a backup

Git ignores the root `.wake-continuity/` folder. Before a source push, check that no
notes were already tracked or force-added:

```sh
git ls-files -- .wake-continuity
```

The output must be empty. A nonempty result needs investigation before pushing;
adding an ignore rule does not remove content from Git history. Docker image
contexts explicitly exclude the folder, Python packaging includes the `wake`
packages, and the canonical mirror copies allowlisted public exports rather than
this workspace. Do not manually copy private notes into public export locations.
The checkout bind mount remains readable to local container processes.

Back up the full private folder to storage with appropriate access controls.
After restoring elsewhere, run the recovery check for each checkpoint and verify
its predecessor references. Git and the hosted mirror intentionally cannot recover
private notes for you. Human review still validates source accessibility, factual
accuracy, correct supersession, summary scope and backup storage privacy.
