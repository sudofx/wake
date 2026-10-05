# Standalone application validation — October 5, 2026

This is a dated emancipation validation snapshot, not a claim that every possible input or external failure has been proved safe.

## Source and operational boundaries

Development began at `ae31ef9cdbb636e82d205564b2d84468b7851cea`; the live runtime matched that source. Remote runtime, state, projection, and archived-state branches were inspected separately. Older standalone source remained accessible through pull request 32 at `0e56af33f6612555432538e0df042939df9f3230`, whose package had no external runtime dependencies and whose engine used WAKE's own store. Current record/runtime source was verified byte for byte against the previously pinned V1 tree `fad1e250e0253fde95c9ca964c7a36beb798240d` before adoption. Existing AGPL licensing remains in force.

WAKE now owns the record, governance, application host, provider generation boundary, invocation lifecycle, matrix grammar, and observability projection. Unrelated applications, CLIs, websites, and external access checks were excluded. Operational repository/account URLs and email addresses remain. Historical V1 format metadata and recorded provenance remain byte-exact data; ownership does not rewrite receipts.

## Local evidence

| Boundary | Result |
| --- | --- |
| Before-change suite | 381 tests passed |
| Fresh standalone environment | Installation contains WAKE, pypdf and installation tooling; no external application package |
| Standalone suite | 383 tests passed; three obsolete external-gate cases retired, five adoption/safety cases added |
| Fresh-process experiment | 100 cycles, 104 independent processes, no API calls; all experiment checks passed |
| Exported history audit | Reconstructed 100 accepted cycles from JSONL and retained head |
| Production-sized checkpoint | 4,514 exact WAKE events, accepted version 143; complete event, state and generic-record digests match before/after |
| Historical checkpoint adoption | Previous archive is restored, verified, canonicalized, reopened and advanced through real Git transport fixtures |
| Failure behavior | Ambiguous, corrupt and unrelated database candidates fail closed; unrelated SQLite is unchanged |
| Provider and recovery contracts | Existing tests cover quota/fallback outcomes, malformed/rejected output, reservation before effects, interruption recovery and pre-commit crashes |
| Operator/domain interfaces | Existing tests cover reset, continuity enablement, Time Dilation, Attention, retrieval, evidence, research, commitments, publication, provenance and manual handoff |
| Public interfaces | Browser checked homepage, Console, receipt inspection, cube, 2D map, 3D map and phone-width layout; attribution removed |

A pre-existing map error was reproduced in-browser: obsolete handlers dereferenced a removed theme switch and falsely reported unavailable data. Both retired handlers were removed; 2D and 3D maps then reported populated version-143 records.

## Performance

Three runs on the same captured 165 MiB record measured the store-opening and live-projection boundaries. Median open time was 6.71 seconds before and 6.07 seconds after; median projection time was 33.74 seconds before and 32.83 seconds after. These local measurements support no regression at those boundaries; they are not a universal latency guarantee. Removing external authority fetches also eliminates that network dependency from each hosted cycle.

## Hosted acceptance boundary

Local evidence does not prove hosted provider or deployment behavior. Acceptance additionally requires successful GitHub CI, Pages publication, stopped-runtime promotion, a completed Gemini cycle on the exact promoted commit, canonical `wake-state` checkpoint publication, live-projection refresh, and continuing operation. Use the Actions results and retained runtime/state refs as authoritative evidence for that rollout.
