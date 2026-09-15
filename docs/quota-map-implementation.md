# Gemini request accounting and MAP

## Delivered

A charged Gemini invocation now attempts at most one generate-content request.
Transient HTTP 500/502/503/504, timeout, and connection failures defer durably;
a later scheduled wake provides the next opportunity. The exact free-tier daily
quota ID still blocks another request for that provider/model/quota day until
Pacific midnight. Other 429s retain the existing attention policy without being
misclassified as daily exhaustion. Auth, runtime, persistence, integrity,
publication, and proposal rejection behavior remains attention-worthy.

New terminal invocation records carry `provider_requests_sent` when known. The
adapter also supplies it in success metadata and structured error diagnostics.
The count describes the client attempt; it does not establish server receipt or
billing. No historical request counts are inferred or backfilled.

MAP is exported at `map.html`, with a downloadable `map-data.json` and an
identical safely embedded payload. The page works as a local file or on GitHub
Pages without a backend, Gemini, GitHub API, or third-party frontend dependency.
Existing navigation links to MAP, including standalone readable exports.

## Provenance

- Persistent journal nodes come from accepted journal entries. Persistent blog
  nodes come from durable posts, including superseded posts.
- `posts.created_by` establishes blog-to-journal linkage only when the referenced
  invocation belongs to an accepted journal entry. Missing linkage stays missing.
- Each accepted event is replayed under historical rules. Its proposal actions
  establish created, revised, retracted, resolved, or superseded relationships.
- Mutable artifacts carry their values at the selected cycle. Notebook/evidence
  relationships from an older cycle cannot silently change when a notebook is
  revised later. Evidence IDs and artifact references are preserved.
- Belief, notebook, project, commitment, research, source, invocation, runtime
  receipt, and editorial records are supported. Relationships carry exact field
  references or accepted-event sequence/hash references.
- Withheld blog actions appear only as labelled editorial decisions. They are
  never promoted to published blog nodes.
- No relationship is created from prose, keywords, semantic similarity, or a
  guessed timestamp. The map builder does not modify its state or event inputs.
- The standalone publisher regenerates the expected graph from verified history
  and refuses mismatched downloadable or embedded map data.

## Interaction and presentation

The chronological spine keeps stable positions while selection reveals grouped
artifacts beside it. SVG connectors represent only explicit relationships among
visible nodes. A plain-text detail panel provides contents and relationship
receipts. Hover highlights direct visible relationships; click locks context.
Artifact selection preserves the wake context. Escape, Close, Clear, or a map
background click collapses the selection.

Nodes are keyboard-operable buttons with labels, visible focus, and shapes or
border treatments that supplement color. Dark/light themes follow the existing
site preference. Reduced-motion preferences are respected. On phones the layout
stacks and details become a bottom sheet; Browse artifacts returns to the
expanded context without clearing it. At 390px, the page has no horizontal
layout overflow.

Working-set and retrieval metrics appear only when recorded. They are labelled
as observational character counts and ratios, never token savings, cognitive
savings, or proof of behavioral equivalence. Historical prose remains intact;
the display normalizes and bolds the WAKE✳︎ wordmark.

## Compatibility fix found during validation

`wake.audit.verify_history` previously applied current editorial overclaim rules
to historical accepted posts, unlike `Store.replay`. It now uses the same
historical replay mode. Hash-chain verification, structural governance, source
provenance, result hashes, and the retained head are still checked. The cached
20-cycle durable export now reconstructs exactly, without rewriting its events
or state. Current proposal acceptance retains the stricter editorial policy.

## Validation

- Baseline: 84 unit/integration tests passed.
- Final: 88 unit/integration tests passed. Three obsolete retry tests were
  removed/consolidated and seven new tests added.
- Tests assert one network call for successful charged wakes, all four transient
  HTTP statuses, timeout/connection failures, and exact daily quota exhaustion.
  A second same-day real-adapter invocation is blocked before another request.
- Cloud tests verify durable deferral, unchanged research version, recorded
  request count, redacted diagnostics, and existing attention semantics.
- Provenance tests cover historical revisions, exact evidence edges,
  supersession, unrelated but matching prose, absent origin links, withheld
  proposals, missing shadow metrics, static exports, safe embedding, unchanged
  input records, and map publication integrity.
- The 100-cycle offline experiment passed all eight checks: fresh sessions,
  commitment handoff, evidence lifecycle, longitudinal behavior, causal state,
  invalid-transition rejection, crash recovery, and audit reconstruction.
- Independent audit of that experiment passed at 100 cycles.
- Browser checks passed for the cached 20-cycle record and a fixture containing
  superseded posts, a withheld post, and shadow metrics. Checked desktop and
  390px phone layouts, artifact selection, context retention, Escape, mobile
  sheet navigation, dark mode, and absence of browser errors.
- JavaScript syntax check and `git diff --check` passed.
- No live Gemini calls were made for validation.

## Files changed

Provider work:

- `wake/providers.py`
- `wake/engine.py`
- `wake/store.py`
- `tests/test_system.py`
- `tests/test_cloud_workflow.py`
- `.github/workflows/wake.yml`

MAP, compatibility, and documentation:

- `wake/provenance.py`
- `wake/assets/map.html`
- `wake/assets/map.css`
- `wake/assets/map.js`
- `wake/assets/index.html`
- `wake/report.py`
- `wake/audit.py`
- `scripts/publish.py`
- `tests/test_provenance.py`
- `tests/test_publishing.py`
- `tests/test_research.py`
- `README.md`
- `docs/quota-map-implementation.md`

## Limits and delivery

No historical events, research records, or posts were rewritten. No embeddings,
semantic inference, force layout, infinite canvas, annotations, graph search,
heat maps, historical diff animation, or dashboards were added. The desktop
bloom uses deterministic groups beside the timeline rather than a radial
force simulation. Source titles are presentation labels, never edge evidence.

The historical pre-rebuild connection-to-publication rate has not been measured,
and this change does not establish a restored rate. Validation demonstrates the
single-request invariant and provenance behavior with offline checks.

Two local commits are prepared for the provider fix and MAP addition. Nothing
has been pushed or deployed; the final task response gives the commit IDs and
local preview link.
