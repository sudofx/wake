# Continuity charter

Continuity notes let a person or a new conversation recover what was understood,
why decisions were made, and what remains unknown. They preserve working
understanding without turning an interpretation into an established result.

## Keep the authoritative record authoritative

These are human-authored Markdown notes, not runtime checkpoints or instructions
to WAKE. Each node's `record/wake.sqlite` remains its operational authority.
Existing journals, notebooks, evidence, event heads and supersession links retain
the research history. Reference them; do not copy a database, reconstruct missing
history, or change a research result through a continuity note.

[Signed replay checkpoints](../retrieval.md#verified-replay-seeds) serve a different
purpose: they verify recorded bytes. A note's checksum detects accidental edits;
it proves neither authorship nor the truth of its claims.

## Separate the contexts

Keep actual notes in the ignored repository-root `.wake-continuity/` directory:

- `research/`: exploratory observations, assumptions, hypotheses and interpretations.
- `implementation/`: assigned engineering objectives, constraints and validation.

One checkpoint belongs to one context. Reference another context only when it is
necessary and explicitly selected by the human preparing the handoff. Do not
paste unrelated research into developer instructions. No loader, provider request
or public export automatically consumes these notes.

## Record what is known and what is missing

Every checkpoint has an immutable unique ID, a timezone-bearing timestamp, its
context and objective. Keep observations and supporting sources separate from
hypotheses and interpretations. Record decisions with their reasons, open
questions, changes and recommended next actions. For an operational observation,
include the node/installation, observed time and record head/version when actually
available. A link to a public mirror is dated presentation evidence, not current
operational truth. Label unavailable evidence and missing context as unknown.
Never infer a historical decision merely to complete a template.

## Preserve earlier understanding

Finish and seal a checkpoint before using it as a historical reference. Never
edit or delete a sealed checkpoint as routine revision. Create a new ID; cite the
previous ID and SHA-256 digest, say what is being superseded and why, and retain
older files and evidence references. A previous link records lineage; it does not
assert that the earlier conclusion remains valid. Branches may name their chosen
predecessor explicitly. Do not choose an active objective solely by filename date.

A resumption summary is a curated view of named checkpoints, not another source
of truth. Date it, include checkpoint IDs/digests and necessary constraints, and
state which evidence must be refreshed before action. Conversation summaries do
not grant permission to deploy, reset records or perform other operations.

## Keep private notes private and recoverable

Only blank templates and this workflow belong in Git. Actual notes and resumption
summaries stay in `.wake-continuity/`; do not put them in `docs/`, `wake/assets/`,
site output, logs, issue bodies or commit messages. Do not force-add them to Git.
Repository ignore rules are not encryption or access controls: the development
container's checkout bind mount can see them. Human review is required before
sharing selected text with a model or another person.

Keep a separately secured copy of the complete private folder, including previous
checkpoints, checksums, summaries and any privately held supporting material.
Preserve relative paths and verify checksums after copying. Local ignores exclude
notes from Git backups; losing the checkout without a separate backup loses them.
Retain references to unavailable sources and mark them unavailable during recovery.
