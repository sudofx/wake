# Local evidence hardening validation — 2026-10-07

Work targeted `/Users/rjohnson/Developer/wake` on clean local `master` at
`42c9a530cfefcca006539a7c439482237949a6fa`, origin `sudofx/wake`, and its
running `wake` container with `/workspace` bound to that checkout and `/data`
on the existing named volume. GitHub `master` was separately inspected at
`8cdcb836cf2c83d46f098a7067ece01feec1318a`; no pull, push, runtime promotion,
workflow edit or hosted runner operation was performed. The container was
restarted locally after tests to load the changes and returned to healthy.
These hashes identify observations during this work, not future current state.

| Recommendation | Implemented and verified behavior |
| --- | --- |
| Research evidence | Claim matching ignores scope metadata and counts collector-stamped source works, collapsing known mirrors. Provider context and Console expose concentration/reuse counters; the research projection also exposes possible notebook mismatches. These remain deterministic heuristics, not entailment or novelty guarantees. |
| Live correction | Operator-controlled demonstration in the existing live record seeded a clearly labeled false source count, recorded a new measurement, retracted the belief at confidence zero and superseded the original publication. It made zero API calls. Normal writer locking and Attention policy were respected; early attempts refused without writing demonstration events. |
| Continuity Matrix | Failed checks retain expected and returned values in governed results and Console projections. A forged colliding source test preserves the actual source mismatch. Coverage and passed cells are counted separately. Existing matrix grammar and recorded scores are preserved. |
| History checkpoints | Canonical `wake-checkpoint@1` exports use detached Ed25519 signatures. Creation verifies semantic, provider and access journals in one read transaction. Commands open existing authority read-only, without schema migration. A public key supplied independently establishes signature trust. |
| Replay snapshots | Checkpoints materialize the WAKE application projection, omitting its old replay log from the seed. Resume verifies later semantic hashes/revisions and application result digests; complete original events remain in the authoritative database. Normal runtime startup remains unchanged. |

## Test evidence

- Container: `python -m unittest discover -s tests -v` — 414 tests, passing with
  one Node-dependent test skipped. That same test passed separately using the
  local virtual environment and Node.
- New tests cover mirrored corroboration, collector scope leakage, evidence reuse,
  colliding provenance diagnostics, signed-suffix equivalence, wrong keys,
  snapshot modifications, journal tampering, truncation, prefix/suffix corruption,
  read-only identity rejection, non-overwriting witnesses, interrupted correction
  resumption, withheld-publication preflight and preservation of original receipts.
- JavaScript syntax and whitespace checks passed. Focused correction tests passed
  after the final receipt/preflight changes.
- A live pre-demonstration checkpoint verified from genesis through kernel revision
  1,872 (`8e6f06d28be79331af2ebe2b030f9f7de9c7d6903c49dcbc439f589fe05b6cbe`),
  including provider/access journals. An earlier fast replay verified 22 new
  semantic events in 1,751.88 ms; this is one local measurement, not a throughput
  benchmark or claim about other machines.
- A second signed checkpoint was created after the live correction at kernel revision
  1,955 (`452527a10e56e5983a3942446fa1079db9c1c704c341a58d7353ef5e3a67eaa2`).
  Creation fully reconstructed the record and application and verified all three
  journals. Its detached signature and corrected state also verified on the host
  from the separately retained Documents copy, without accessing the database.
  Signed-seed replay in the container confirmed the zero-confidence retraction
  and supersession pointer. The earlier seed successfully verified 110 semantic
  events through revision 1,959 after the demonstration.
- The restarted local website served the new evidence-quality and per-cell
  failure-diagnostic fields. Website snapshots remain disposable presentation.

## Live correction receipts

The demonstration identifier is `controlled-correction-demo-v1`.

| Transition | Domain event | Kernel receipt | Kernel sequence |
| --- | --- | --- | --- |
| Labeled false count and original publication | 1847 | `78312085-06a0-41d2-87ba-347fc803ed1f` | 1934 |
| Belief retraction and publication supersession | 1853 | `7059e356-3654-44a1-8c96-d3dfc2490863` | 1941 |

Original kernel event hash:
`c31631b1413f1d1e4d9865c4866ca65c79358c75fe60396f9bada0b2c23185e8`.
Correction kernel event hash:
`786fb2132e446d042e4f099f0d3c7d27af54e14c445c092ac2aef7a9d096e2b7`.

The original post remains `controlled-correction-demo-v1-original`, with
`superseded_by = controlled-correction-demo-v1-corrected`. The belief is
retracted, retaining its original evidence plus the new measurement. This proves
operator-controlled live additive correction; it does not prove autonomous model
recognition or correction of scientific mistakes.

## Delivery boundaries

Changes remain local and uncommitted for review. Before publication, reconcile
local and GitHub source state without overwriting either, then use the repository's
existing stopped-research promotion procedure. Hosted runners were not touched.
No paid API account was created or required. No kernel separation was implemented.

Public keys and signed witnesses are retained separately under
`/Users/rjohnson/Documents/WAKE-checkpoints/2026-10-07/`; private signing material
remains in ignored local build output and must not be published. External,
independently controlled witness publication and periodic scheduling remain
operator deployment choices; the implementation does not claim notarization or
protection if an administrator replaces both history and every trusted witness.
Fast replay trusts the signed prefix and attests later semantic events only;
full audit is required for interior prefix corruption and later provider/access
journal verification.

## Routine memory follow-up

The operator subsequently authorized promoting shadows into memory that models use routinely. `wake.toml` explicitly selects `memory_mode = "active"`; the library default stays `shadow`. The same bounded working-set owner now delivers advisory compacts, recent operator observations and selected provenance records on every invocation. Raw shadow receipts remain unchanged and governance stays authoritative. No additional inference call or separate writable memory store is introduced.

The container suite passed 424 tests with one Node-dependent skip; that test passed independently on the host. Ten new active-memory tests cover below-ceiling activation, exact request/memory digests, a single provider call, rollback to shadow, retracted beliefs and human counterevidence, preserved obligations, fail-before-provider budget exhaustion, missing roots/excerpt labels, source role separation, collector prose limits and invalid configuration. The full fresh-process sensor regression also passed in the explicitly active repository configuration, including new counterevidence and retraction across ten fresh processes.

Behavioral equivalence to rich context remains unmeasured; paired evaluation is still needed. Routine active memory is an operator-enabled experimental condition.

The first activation attempt exposed a 52,745-character request from the current record and stopped before inference. Active delivery now removes duplicated evidence prose using explicit content pointers and, under pressure, bounds extended recovery prose while retaining project/frame/observation pointers and hashes. A disposable SQLite backup of the live record produced a 46,151-character request under the unchanged 48,000-character ceiling, with both belief identities and the open commitment preserved. This offline check made no provider call and never mutated live authority. The full 424-test suite passed after the correction.

The restarted local container returned healthy and completed scheduled Gemini invocation `w-10fb67538cc547b2` using active memory at 2026-10-07T23:01:24.977164+00:00. Its start event is domain sequence 1,997, hash `f217fda515eed4f2f48392963f30a3c28f21f7d9d9c88742b36826a0d0d0bd03`. The exact request hash `77736d180fc59c8e7706a21fa5b7515bf8dd57c70cdaa2c446889225e96afe3c` and memory digest `b4a9a2c3a985a41b540e3381cc876dd845f1cf71bcf9c6fab87d22fe38ed1b17` both independently recomputed correctly from the recorded request. It delivered 46,152 request characters, eight retrieved records and two advisory compacts, including the challenged demonstration belief, measured counterevidence and open survey commitment. The continuity sidecar remained in the same request and completed with a passing score. The ordinary research proposal was rejected for insufficient notebook claim support; this verifies delivered memory and retained enforcement, not successful research or behavioral equivalence. No extra inference was requested for memory.

The live terminal receipt recorded 1 provider request(s) and 1 attempt(s) for that invocation.

## Same-wake research and wider Internet access

The operator authorized an additional inference so retrieval and proposal submission can complete without waiting for another scheduled wake. `same_wake_research = true` is enabled locally. A bounded planning inference selects up to two configured-domain questions and optional known source URLs. Deterministic validation enforces Attention, active-project identity and URL policy. The canonical collector then follows bounded routing hops immediately, records evidence, and the final fresh inference receives prioritized source IDs and submits one normal governed proposal. `research_planned` closes retrieval intent without incrementing the research version; only final proposal acceptance advances a cycle. `wake --question` adds a direct operator question and returns the proposed summary/answer with its verdict and linked receipts. Provider/collection failures remain visible and preserve already collected evidence.

Network policy now includes 98 anchored host families plus 55 explicit hosts, covering international university/public-agency families, scholarly publishers, preprints, institutional repositories and datasets. HTTPS/host/port/credential and redirect checks remain. Direct connections pin checked public addresses; operator-configured proxies retain their trusted transport role with origin DNS checked before tunneling. Routing/DNS beyond a configured proxy is an explicit separate trust boundary. Private/loopback/link-local research addresses and suffix spoofing remain blocked. Access expansion does not promote discovery or metadata into scientific evidence.

Final container verification: 435 tests passed with one Node-dependent skip; the same skipped test passed independently on the host. Eleven immediate-research/network tests protect two calls with one accepted cycle, both native lifecycles and quota accounting, new sources visible before the final request, invalid plan refusal before network effects, final failure retaining evidence without a fabricated answer, same-pass metadata-to-readable-source routing, topic/Attention bounds, quota refusal before a second call, anchored domain breadth, private address refusal, pinned direct connections and configured-proxy target checks. Repeated active compaction also preserves the original recovery hash and all open obligation identities.

A disposable backup of live authority generated a 46,076-character final research request below the unchanged 48,000-character ceiling with all beliefs and open commitments preserved. Further bounded source/working excerpts prevent growing prose from forcing silent obligation loss; requests that still exceed the limit stop before inference.

Initial direct-only probes from disposable containers timed out. Inspection of actual runtime transport identified the Docker host proxy; after correcting proxy support, the real container fetched Crossref bibliographic content (2,069 excerpt characters) and newly permitted Zenodo content (6,589 excerpt characters). These are reachability checks, not claim-support validation. Live planning and final inference phases have been recorded, including provider timeouts/deferrals; no successful scientific answer is inferred from those failed attempts. The local provider timeout is now bounded at 45 seconds per attempt to allow current response latency. No hosted runner, workflow, paid account, source branch or public projection was changed.

Live same-wake acceptance was observed: planning invocation `w-9850951c722f405c` completed a validated plan with one API request, then final invocation `w-463711aa60324e17` made one API request and was accepted at research cycle 63. Its start event is sequence 2,071, hash `a60bbbd537dbad2ae57ab9d9ce79d5af9831d165df5b76c33c503fb868242175`; the recorded request hash recomputed correctly and measured 46,954 characters. Immediate collection obtained readable `https://plato.stanford.edu/entries/scientific-objectivity/` content plus an OpenAlex discovery result; two DOI routes failed and were preserved as failed observations. This verifies a real linked plan/collection/final proposal in one wake, not universal source availability or scientific correctness.

A later malformed planning response exposed conflicting inherited ordinary-proposal instructions. The planning phase now has its own untrusted-data system contract and requests-only schema, with existing active-project IDs constrained explicitly. Final proposals retain the ordinary governance contract. Configuration/source changes remain local and uncommitted; local/remote source ancestry still needs reconciliation before publication.

After the planning-contract correction, live plan `w-5a8d8c473ef94b25` validated successfully; linked final invocation `w-0cbeb8cbdf074485` ended as `accepted` with 1 planning request and 1 final request. The final request hash verified, and its size was 46573 characters. Outcome reason: accepted through ordinary governance. The container remained healthy.
