# Validation record

This file preserves a dated validation snapshot from September 11, 2026. It is historical evidence, **not a description of the current test count, current UI, current workflow status, or current live research record**. Current behavior is defined by `master`, its tests, and the latest GitHub Actions results.

| Check | Result |
| --- | --- |
| Behavioral test suite | 62 tests passed |
| Offline longitudinal experiment | 100 accepted cycles; all eight checks passed |
| Cross-provider fixture handoffs | 99 completed obligations; one remains open for cycle 101 |
| Forbidden rule change | Entire proposal rejected; accepted state unchanged |
| Process recovery | After-start exit and mid-transaction exit recovered; corrupt projection rebuilt |
| Independent reconstruction | Exported JSONL reconstructs the exact durable state |
| API calls during validation | Zero real inference calls; Gemini HTTP contract tested with a stub |
| Browser interactions | Bob’s Blog list/detail, project/notebook/evidence/exact-wake links, plain-language panels, search, pagination, event filtering and lab results verified |
| Responsive widths | 375×667 phone, 768×1024 tablet, 1440×900 desktop; one-row navigation and no horizontal overflow |
| Browser console | No errors or warnings in the final inspected page |
| Publishing | Initial publication, unchanged publication and update tested against a disposable local Git remote; no public push |
| Replacement ZIP | Extracted to a clean temporary folder; initialize, fixture wake, audit, export and included 100-cycle audit passed |

The observed experiment is included in `examples/journal/experiment.json`. Its durable head is `4c5f205afe0060e30bf71b9b7e807c99001501dd21dbe16d1206995aa9cc1aad`.

The GitHub workflow is configured to run on Python 3.11 and 3.13; those remote jobs have not been run as part of this local rebuild. Live Gemini inference, free-tier account eligibility, real desktop-model handoffs, cron installation and public hosting remain operator setup steps. The synthetic experiment does not establish live-model comprehension.


## Reading this snapshot now

Since this snapshot, **WAKE✳︎** has continued to change: cloud scheduling, Gemini fallback/accounting, MAP, research-topic configuration, collector boundaries, forward-only claim corroboration, queue lifecycle handling, themes and public UI have all evolved. Do not use the table above as proof that those later changes were covered by the September 11 run. The repository's `Verify the record` workflow is the current regression gate.
