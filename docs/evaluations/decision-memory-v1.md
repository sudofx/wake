# Decision-relevant memory: first implementation and evaluation

This local implementation supplies a deterministic selector, snapshot-bound Decision
State Capsule, shadow telemetry and explicitly enabled active delivery. The checked
configuration remains `decision_memory_mode = "off"`. No production record, runtime
selection, container, provider or public site was changed by this work. No model API
calls were made for this evaluation. Earlier unrelated cleanup edits remain intact.

## Architecture and constraints verified before implementation

`Engine.start` already builds a working-set shadow, Trust Compacts and a retrieval
plan, then rehydrates qualifying sources. Rich/active delivery shares final schema
construction, protected obligations/provenance and exact provider-input fitting.
`invocation_started` stores the request/hash and context-delivery receipt; existing
terminal events record proposals, failures and governance outcomes. Application
replay reconstructs these receipts over the native append-only kernel record.
`comparison.py` already restores checked copies of one frozen native backup.

The implementation preserves these owners and their contracts. It does not change
`memory_mode`, kernel record schemas, action schemas, governance, provider adapters,
objectives or historical event bytes. New optional terminal metadata is reconstructed
only on instrumented invocations. Default-off invocations omit the new receipt fields.

## Files and decisions

- `wake/decision_memory.py`: pure bounded candidate generation, contextual ranking,
  exact record/root hashes, source-work deduplication, capsule assembly/validation,
  revision observations and explicit-reference telemetry.
- `wake/engine.py`: mandatory context fits first; optional delivery is built on a
  copy using existing rehydration, allowlists and response schemas. Exact rendering
  decides fit. Shadow returns the original request. Empty or unfit optional recall
  leaves provider input unchanged. Snapshot freshness is checked before recording.
- `wake/domain_events.py`: conditionally reconstruct new terminal observation
  metadata, including provenance-linked prior belief interpretations. Older events
  without those fields retain their original reconstruction.
- `wake/comparison.py` and `wake/__main__.py`: reuse frozen native backups for
  baseline/recall/ablation arms; add an offline labeled-fixture evaluation command.
  Ablation cannot be configured in production and excludes equivalent source copies.
- `wake/installation_cli.py`: omit new capsule/selection/use namespaces from public
  exports, including event metadata. Native receipts remain inspectable.
- `wake.toml`: explicitly disabled default. Policy settings are versioned, bounded
  and operator-controlled; no adaptive ranking exists.
- `tests/test_decision_memory.py` and `tests/fixtures/decision_memory.json`: ten
  labeled scenarios plus native invocation, rejection, replay, independent-record,
  privacy, operator-control and comparison tests.
- README and architecture, retrieval, experiment, glossary, cloud and development
  guides document behavior, configuration, ownership and limitations.

The prior cleanup changes to artwork, unused helpers and navigation comments were
preserved; they are not requirements of decision memory.

## Mechanical comparison results

[Machine-readable fixture results](decision-memory-v1.json) include source/fixture
fingerprints, selection reasons, exclusions, coverage and per-case checks.
All ten predefined cases pass. All positively labeled targets were candidates and
selected; no explicitly labeled irrelevant record was selected. Delivered record
identity/hash errors and incorrect scientific-source eligibility counts are zero.
The incomplete-source case deliberately retains **one missing evidence-root
reference**, visibly labeled rather than invented. Record identity verification is
not the same measurement as completeness of supporting evidence.

Characters below use the existing provider renderer on small synthetic projections.
They are not production context sizes or evidence of cost reduction.

| Scenario | Baseline | Recall | Ablation | Mechanical checks |
| --- | ---: | ---: | ---: | --- |
| repeated failure | 85 | 4087 | 3436 | Pass |
| contradictory evidence | 592 | 4935 | 3924 | Pass |
| distant historical relevance | 85 | 3017 | 2223 | Pass |
| cross topic connection | 85 | 3000 | 2223 | Pass |
| context pressure | 1423 | 3843 | 4161 | Pass |
| unimportant memory | 85 | 2223 | 1491 | Pass |
| superseded memory | 85 | 3950 | 2907 | Pass |
| adversarial content | 247 | 2985 | 2252 | Pass |
| multiple nodes same work | 820 | 3859 | 2958 | Pass |
| missing or ineligible source | 363 | 3513 | 2501 | Pass |

Median evaluation time was **0.762 ms** on this local run. That measurement
covers the report's ranking, repeated capsule construction, ablation and checks;
it is not a production overhead benchmark. The native invocation receipt records
its own computation time. Large-record sorting/verification costs remain unmeasured.

## Native frozen-record integration

[Native preparation results](decision-memory-v1-native.json) bind all arms to the
same baseline head/state hash and record their actual request hashes.

| Arm | Provider-input characters | Capsule records |
| --- | ---: | --- |
| baseline | 15601 | None |
| recall | 19602 | comparison-baseline, comparison-counterexample, comparison-sensor |
| ablation | 18978 | comparison-counterexample, comparison-sensor |

These are prepared requests with **zero submitted model responses**, not behavioral
results. This fixture already exposes the counterexample in baseline memory, so
its capsule ablation is weak evidence about causal recall. It establishes native
snapshot isolation, actual delivery differences and protected-context retention.
Decision change and independent outcome improvement remain unknown. Full synthetic
requests, source capture and frozen backup remain recoverable at `/tmp/wake-decision-memory-final-evidence-20261021`.

## Executed verification

- `python -m unittest discover -s tests -v`: **830 tests run; OK, three skipped**
  (103.978 seconds). This completed the engine/selector integration regression.
- Final focused decision-memory checks after refining report metric definitions:
  `python -m unittest discover -s tests -p 'test_decision_memory.py' -q`:
  **21 tests passed** (1.641 seconds).
- Existing active-memory suite: **25 tests passed**. Existing comparison suite:
  **three tests passed**; both are also covered by full discovery.
- The offline comparison CLI above ran successfully, generated the linked report
  and used zero provider calls. Documentation path checks and `git diff --check`
  passed.

Environment: repository `.venv`, Python 3.14.8 on macOS. The three skips are Linux
process identity proof, Linux worker parent-death behavior, and the opt-in browser
acceptance needing Node plus `PLAYWRIGHT_MODULE`. This work does not claim those
platform/device checks ran, nor that remote CI or deployment occurred.

## Limits and remaining hypotheses

- Relevance is project/topic association plus explicit question terms and recorded
  events. It is not semantic understanding or universal importance. Matching words
  do not establish contradictions, causality or scientific surprise.
- Default windows inspect at most 252 projection payloads plus 64 existing retrieval
  references; sorted keys still cost work proportional to projection size. Coverage
  and exclusions expose the bounded search. Dormant projected records can return
  without an age cutoff, but immediate recall of every historical event is not promised.
- Current retractions, notebook revisions, source reviews and limitations remain
  visible. Newly observed belief revisions carry their prior interpretation/hash.
  Older pre-instrumentation belief prose is still in exact history, but this
  prototype does not reconstruct every prior revision from the event archive.
- A capsule can add context cost. Optional memories yield to mandatory obligations,
  roots and the final provider ceiling. The fixture results do not establish a
  production throughput or context-efficiency improvement.
- A referenced identifier is only an explicit mention. Acceptance is not scientific
  correctness. No independent behavioral quality, beneficial decision change or
  long-term adaptive improvement was measured; model sample size is **zero**.
- No ranking policy updates itself. The feature can be disabled without migration;
  existing receipts remain immutable. Bob and private advisory assessments acquire
  no research authority through memory.

## Recommended next experiment

Use repeated held-out frozen cases whose relevant optional fact is absent from
baseline input, including delayed corrections and specific prior limitations.
Predeclare A/B/C controls, match model/settings/budget, blind independent scoring,
retain failures and report sample size, uncertainty, cost and correctness separately.
Do not enable routine active delivery on this mechanical evidence alone. Any live
provider experiment or production activation requires explicit operator authorization.
