# WAKE✳︎ hosted operation

Independent container deployments are described in [multiple installations](installations.md).
They do not restore hosted checkpoints or use hosted public data. Hosted controls
in this guide retain their separate authority and release procedure.

The local numbered-group peer-note and source-evidence exchange and hostname
router are created only by `scripts/wake_runner` on a local Docker host. Hosted
workflows and Codespaces do not join those networks or receive peer material.

> **Current operating specification.** This is the authoritative guide to the GitHub-hosted **WAKE✳︎** runtime: `master` is development, `wake-runtime` is the explicitly promoted executable, and `wake-state` carries the separate authoritative WAKE SQLite record.

WAKE✳︎ provides the durable record and governed transition boundary. The hosted research application uses that infrastructure to choose small, useful projects from `research-topics.toml`. Topics are replaceable workload inputs, not WAKE✳︎ identity or kernel policy. The deployment can continue research without daily assignments, while resets and topic changes remain explicit operator interventions.

## Read or wake it

The public interface is **https://sudofx.github.io/wake/** once GitHub Pages is enabled. Home explains the system and surfaces the latest published notebook and Bob post. Research and Read expose the reference workload. Console is the inspection workspace for calls, governance, provenance and record structure. The “since your last visit” counter is browser-local and is never part of the durable record.

The `WAKE✳︎ — Update website · automatic` workflow is the only Pages publisher. Do not add generic static or Jekyll publishing templates: they publish application source instead of the generated research home and can overwrite the correct site.

`WAKE✳︎ — Internal only: one research cycle` is the only research execution lane. It may execute only when the workflow dispatch ref is `wake-runtime`; each accepted/rejected cycle can dispatch its successor from that same runtime branch and carries the exact runtime commit forward. `WAKE✳︎ — Internal only: keep-running switch` is the durable on/off latch used by **WAKE✳︎ - Start** and **WAKE✳︎ - Stop**, with a scheduled lost-handoff check while enabled; running it manually does not start research.

Runtime control lives entirely in GitHub Actions. The website's small status light opens the repository Actions page. It is green while the keep-running switch is open and no daily quota standby is known, purple while a durable API allowance boundary pauses research until midnight Pacific time, and red when the switch is closed. The light reports the durable continuation latch and latest published quota status, not whether a cycle is executing at that exact instant. There is no site authentication or control backend. **WAKE✳︎ - Start** opens the keep-running switch and dispatches the first `wake.yml` cycle on `wake-runtime`. **WAKE✳︎ - Stop** closes that switch before cancelling active cycles. The scheduled continuation check reads quota eligibility from `wake-state`, then dispatches one fresh attempt after the Pacific reset; it never treats `wake-live` as authority or keeps a runner sleeping through the daily wait. **WAKE✳︎ - Reset** is the safe reset workflow: it stops research as needed, verifies/promotes current code when required, archives the prior governed generation, and starts a new active generation at cycle zero using its explicit confirmation input. Prior governed wake history remains durable. **WAKE✳︎ - Enable continuity campaign** is the explicit provider-free opt-in for the shared `continuity@1` matrix. It closes and drains the active research lane, verifies/promotes the candidate runtime, records enablement through the serialized `wake-authority` lane, then restores whether continuous research was running or stopped. The Console may link to this workflow when the live record reports the campaign disabled; it does not gain browser-side mutation authority. While enabled, each ordinary research provider request carries at most one isolated matrix sidecar for the next uncovered coordinate. The same Gemini response supplies both the research proposal and the probe answer, so campaign execution makes no second API request and consumes no extra provider slot. WAKE strips the expected sidecar before research governance, scores it deterministically, and commits only the compact coordinate result through application governance. Research can be accepted or rejected independently of the probe. Any returned response completes the tested coordinate; a missing or malformed sidecar is recorded as a zero-score result, while quota/transport deferral before a response leaves the cell uncovered for retry.

Runtime adoption is explicit. **WAKE✳︎ - promote** verifies a candidate, rechecks that no real `wake-runtime` cycle is queued or running, and only then moves the runtime branch to that exact verified commit. It refuses while research is active: **WAKE✳︎ - Stop → WAKE✳︎ - promote → WAKE✳︎ - Start**. CI on `master` is development feedback only; failures there never stop or redefine an already-running research chain.

The Pages shell loads the disposable `wake-live/live.json` projection with `cache: "no-store"` and checks it every ten seconds. New state is applied in place; live research no longer waits for or triggers a Pages deployment.

## Authority maintenance

Prepare and test changes locally while hosted research runs. For an authorized code
release, use Stop and verify that real research jobs have fully drained **before
pushing**. A push may deploy the Pages shell immediately. Then use Restart for
candidate verification and promotion, check the exact promoted SHA and continuation,
and inspect a new attempt's terminal receipt. Restart success alone does not prove
accepted research. See the [maintainer map](development.md) for environment boundaries.

**WAKE✳︎ - Stop** keeps the continuation latch closed while waiting for cancellation to finish. GitHub's server-side cancellation can take five minutes; Stop allows at least six minutes of polling within a ten-minute job budget and retains its force-cancel fallback. A cancellation request alone is not proof that research has drained.

**WAKE✳︎ - Restart** is the normal maintenance shortcut for the current wake-backed runtime: stop, verify `master`, promote the verified commit, then start again.

Do not use migration/rehearsal workflows as substitutes for ordinary Start/Stop control.

## One-time repository setup

1. Keep `GEMINI_API_KEY` in repository **Settings → Secrets and variables → Actions**. Use an API project with billing disabled. `free_tier_confirmed` in `wake.toml` is an operator attestation; the application cannot inspect Google billing.
2. In **Settings → Pages**, select **GitHub Actions** as the build source. The workflow attempts automatic enablement; if repository permissions prevent that, this setting is required once.
3. Use **WAKE✳︎ - Start** when you want the promoted runtime to begin a continuous research chain. Use **WAKE✳︎ - Restart** for the normal stop/verify/promote/start maintenance sequence. Website publication is automatic after relevant source changes.

The workflow uses the existing public repository and GitHub Pages. No paid fallback, paid search, or subscription is introduced. The local Pacific-day budget is enforced against durable provider-request reservations. With same-wake research enabled, planning and final proposal reserve separate slots. Each phase may reserve additional slots when an eligible transient failure advances to the next configured Gemini model; interrupted unknown attempts remain conservatively reserved. Manual wakes share the same ledger.

## A wake's work

A trusted collector retrieves a bounded sample before the final proposal inference. Normal mode uses two requests; the current `observation_mode = true` configuration uses `research_collection_budget = 6`. With same-wake research disabled and active projects, one slot remains broad exploration and the remaining slots prioritize project maturation: readable-source candidates, persistent-identifier promotion, queued follow-ups, then question-led scholarly discovery. Broad index results are discovery leads. Exact Crossref/OpenAlex/Semantic Scholar/DataCite records are metadata-routing receipts, not notebook evidence. Approved readable publisher/full-text/source-controlled text is the qualifying source boundary. PubMed/PMC identifiers can be promoted deterministically to NCBI PMC open-access BioC text when available. Collection remains separate from model authority and is bounded by HTTPS allowlists and redirect validation. Normal web responses are capped at one megabyte. PDFs are capped at eight megabytes and text extraction is bounded to the first 24 pages and 50,000 characters; the provider-facing evidence excerpt remains bounded to 10,000 characters with evidence-bearing sections preferentially retained.

## Changing research topics

Create the topic file on `master` with `cp example.research-topics.toml research-topics.toml`, then edit it. Local files are ignored by Git; hosted research uses the exact promoted commit, so explicitly include hosted topics with `git add -f research-topics.toml`, commit and push, then promote that candidate. Restart refuses to promote a release without the file, before it stops the current runtime. Each topic has a stable machine `id`, a public `label`, a neutral discovery `query`, and may have a `seed_question`. Development changes on `master` do not affect live research until that commit is explicitly promoted to `wake-runtime`. After promotion and restart, the next runtime cycle records changed topic configuration as an auditable event before doing research. This is forward-only: existing cycles and projects are not rewritten. Keep an ID unchanged when renaming a topic that already owns projects. Removing a topic prevents new projects in it, while existing projects remain reviewable and can be completed or parked. Durable records and filters keep the stable topic `id`; public journal, notebook, blog, and MAP tags resolve that ID through the configured `label` so internal names are not used as display text.

**WAKE✳︎** can start, update, park and complete projects; queue research; publish or revise notebooks; and use the existing belief/commitment system. At most three projects are active and four model-proposed searches are pending. A notebook may preserve a provisional synthesis from one qualifying substantive source, but project completion requires a notebook backed by at least two substantive distinct underlying source works. Known DOI/arXiv/OpenAlex identities collapse mirrors to one work. Revisions require changed findings and newly collected evidence. Previous revisions remain in the event history.

Bob may publish at most one selective Blog post inside that same Gemini response, but the blog is an editorial sidecar rather than part of WAKE✳︎'s research authority. Ordinary publication remains event-driven. On Bob's first accepted wake, and again after a deterministic 15–20 accepted-wake quiet window, the provider response schema requires one top-level Bob editorial checkpoint. WAKE✳︎ materializes that checkpoint as the final blog sidecar before governance. If the checkpoint fails publication governance, only the blog is withheld; valid research may still be accepted, no post becomes durable, and Bob remains due on the next wake. Bob cannot gate an accepted cycle, move Attention, count as research progress, or supply the journal title/summary. Ordinary publication likewise requires support traceable through notebooks from at least two qualifying distinct source works; current verification-required claims must materially overlap those sources. A one-source notebook can therefore remain useful provisional research without becoming completion-ready or automatically publishable. Routine status activity creates no ordinary post. Corrections preserve and supersede earlier writing; the exact wake remains linked.

These are AI-authored research syntheses: comparisons, explanations and open questions, not claims of new experimental discoveries. Discovery and metadata receipts may guide retrieval but do not qualify findings. Readable material can still be incomplete, preprint-only, or otherwise limited; scope and limitations remain visible. Two distinct works do not guarantee independent studies, strong evidence, or correct reasoning, and unidentified mirrors may still evade work-level deduplication. Governance checks provenance and structure, not scientific truth.

## Memory on GitHub

`master` holds development code and may move independently. `wake-runtime` holds the exact promoted executable used by live research. **`wake-state` holds the authoritative cloud `data/wake.sqlite` database and is separate from both code branches.** On the first migration run, the existing `data/wake.sqlite3` chain is verified and archived exactly inside WAKE before any provider call; that legacy file then becomes frozen migration evidence, not an operational store. Each later runtime cycle reconstructs WAKE through the WAKE application contract from `wake.sqlite` alone. A branch missing both database formats is an error, never a reason to silently start over. Missing both database files on an existing authority branch fails before provider access; only creation of the first-ever `wake-state` branch may initialize empty authority. A first-ever cloud bootstrap creates WAKE authority directly and never creates a temporary `wake.sqlite3`. Earlier local records and the offline example remain separate; they are not uploaded or relabeled as cloud research.

Before contacting Gemini, the workflow commits and pushes the request and quota reservation. Checkpointing also enforces the GitHub blob ceiling: when `data/wake.sqlite` reaches 90 MiB, the runner performs verified SQLite compaction before staging it. If the verified compressed checkpoint still reaches GitHub's 100 MiB single-blob limit after compaction, the checkpoint fails closed instead of spending another provider call against state that cannot be persisted. If that push fails, the model is not called. It checkpoints again after the response. A lost runner can waste an attempt, but the next runner recovers the unfinished invocation without refunding it. State publication uses an exact remote-head lease with a parentless checkpoint commit; a competing update fails rather than being overwritten. Workflow concurrency serializes automatic and manual runs.

Archived Lab Comics covers remain under `assets/covers/`. They are static assets; runtime research and Pages publication do not modify them.

Each completed cycle refreshes the disposable `wake-live` projection after the authoritative WAKE SQLite state is checkpointed. Governance rejection and handled provider deferral can therefore update the public record without advancing accepted research. GitHub Pages is independent: it republishes only when website code changes. If the live projection refresh fails, the durable record remains authoritative and the previous public projection stays in place. Eligible transient HTTP 500/502/503/504 and narrowly classified network failures may advance once to each next configured Gemini model; there are no sleeps or same-model retries. Every provider attempt is durably reserved and recorded. Exhausting the eligible model chain defers the wake without advancing research. Expected provider pressure leaves the workflow green; this means the outcome was handled, not that research was accepted. The homepage separately shows the last accepted wake, latest attempt, provider-request accounting, and any known quota reset time.

Console has its own static assets and compact `research-data.json`. Website export writes a local fallback; the runtime publishes the live dashboard JSON alongside the existing map projections. The projection producer changes only after explicit runtime promotion while research is stopped; the Pages shell may deploy independently from `master`. A newer Pages shell can therefore temporarily use its dated fallback until the promoted runtime supplies the new projection. The dashboard refreshes once per minute while visible and preserves the previous snapshot on errors; execution status is separately labeled GitHub Actions infrastructure and checked at most every three minutes. For a deliberate read-only preview of hosted data, build `site/` with `python scripts/publish_pages.py` and run `PYTHONPATH=. .venv/bin/python scripts/preview_research.py --directory site --port 8947`. This helper requires a hosted export and rejects standalone directories. This localhost server checks the public `wake-live/live.json` at most every 30 seconds, retains the last snapshot on transport failure, and never opens authority or invokes workflows. Until runtime promotion supplies native classification and matrix progress, newly received legacy public snapshots explicitly retain unknown classifications and unreported campaign status. External HTTP links in exported pages open separate tabs.

The state branch is public. It contains science-source snapshots, model requests, responses and runtime receipts. It does not contain API keys, environment files or earlier local private observations. Do not enter private material into this cloud record.

Do not run a second independent live loop against the same provider quota. Local CLI commands remain useful for testing and manual records, but the hosted runtime is GitHub Actions plus `wake-runtime`/`wake-state`.

Source qualification and acquisition outcomes are evaluated separately from workflow success. A failed publisher fetch appends a route-failure receipt; only successfully collected readable source material counts as acquisition progress. Current source qualification filters recognizable navigation and response forms. Existing receipts are retained unchanged when runtime policy becomes stricter.

## Maintenance

The replayable history deliberately favors inspectability over unlimited scale. Normal reads validate the hash-bound materialized projection; startup/adoption and explicit audits use full replay where required. Signed replay seeds provide a separate verified-prefix path with the limits described in `retrieval.md`. As years of raw prompts and source excerpts accumulate, storage and replay time will need maintenance; this initial system does not claim indefinite unattended operation. The model's context is bounded and explicitly excerpts old material while preserving the full record. No expertise score, consciousness claim or simulated research result is used as a growth metric.

## Deferred provider additions

The unattended cloud deployment remains Gemini-only and uses the explicit configured Gemini fallback order. Manual handoff to Claude, ChatGPT, or another desktop model remains available through `prepare` / `complete`; a chat subscription is not treated as API billing credit. Paid-provider scheduling and provider shuffling are not part of the current deployment.

The canonical Console address is `console.html`; `research.html` redirects while preserving query and fragment selections. Export emits Console-owned record/map/flat components and their shared routing assets alongside the overview. The old Research dropdown is removed from canonical navigation; Projects under Read opens Console. Compatibility URLs can remain without being Console dependencies. Deep tools are loaded only when opened and released when closed.

## Standalone checkpoint adoption

The runtime has no external product access check. WAKE Start/Stop, the continuation latch, serialized authority workflow, and the record's local access fence remain authoritative. Existing V1 `*.sqlite.gz` checkpoints are restored and fully replay-verified, then published as `data/wake.sqlite.gz`. The previous filename is removed only after the new package verifies. This preserves every receipt and historical research event; it does not reset the experiment. For rollout, use Restart after successful candidate CI, then verify a completed provider cycle and the public projection on the promoted commit.

## Optional independently retained witnesses

The local `checkpoint`, `verify-checkpoint` and `replay-checkpoint` commands create and verify signed replay seeds; they do not dispatch, disable or edit hosted workflows. Signing keys and independently controlled witness publication are operator responsibilities. Existing `wake-state` transport, runtime promotion, writer serialization and research-stop requirements remain authoritative. Keep private signing keys out of source/state branches and public reports. Retain the public key and signed checkpoint outside the database and through an independently controlled channel before asserting administrator rewrite detection.

## Routine memory configuration

`memory_mode = "active"` selects routine derived memory without additional inference calls. `shadow` restores rich delivery and its existing overflow fallback. Configuration is loaded at process startup, and invocation receipts attest the exact delivered memory and activation reason. Local activation does not promote hosted runtime code or dispatch any workflow; hosted adoption still requires the existing stopped-research promotion procedure.

## Same-wake retrieval and wider research access

The promoted configuration enables `same_wake_research = true`. Planning and final proposal are separate quota-accounted inferences within one scheduled wake; allow for roughly two successful API requests per wake, plus existing bounded fallback attempts. Both phases preserve native lifecycle receipts and stop on quota/provider failures. Invalid planning output is a governed rejection, not an operator-attention failure: no collection or final call occurs, and the next scheduled wake remains eligible. Hosted changes still require the stopped-research promotion procedure. Direct local questions use `wake --question` under the same writer lock. Set `same_wake_research = false` and restart to restore the earlier scheduled collection/proposal cadence.

The expanded anchored host families cover universities, public agencies, scholarly publishers, preprint servers and research repositories. Direct connections pin approved public addresses. Operator-configured proxies are supported as trusted transport after origin DNS checks; onward proxy routing remains a separate trust boundary. Source access limits, classification and claim-support policy still apply. This requires no additional API account, subscription or paid search provider.

Active-memory fitting includes due milestone editorial history so its optional longitudinal window cannot bypass ordinary compaction. The final request is fitted again after collection links are added. Editorial notebook titles are optional delivery prose: under pressure their index hash, eligible notebook IDs, revisions and evidence roots remain, while titles may be omitted. Source excerpts can be shortened further without dropping source identity or provenance. Overflow that remains after safe fitting still pauses before sending the final model call; inspect that recorded reason before restarting. Context fitting never rewrites the hosted authority.

A successful research workflow may contain a rejected or deferred attempt. Compare accepted-cycle progress and terminal reasons rather than the job conclusion alone. Routine requests retain recent rejection guidance and full-record queue capacity so compact memory cannot repeatedly offer mechanically unavailable work. These delivery constraints change neither the authoritative record nor promotion controls.

## Browser data routing

Pages export explicitly selects hosted mode through `wake.report._deployment_site`.
Generated HTML carries `WAKE_DEPLOYMENT` before readers execute and the artifact
includes `deployment.json`. Only explicit hosted identity enables GitHub projection
and Actions-status fetches. Standalone and unconfigured pages use their own origin;
Console warns about missing identity. This routing contract must remain common to
home, Console, maps and generated deep tools. Never use a public projection to
repair a standalone database or treat a successful page response as authority proof.

## Console activity versus published history

The hosted research projection includes `recorded_activity` with the pending
invocation/cell known at export time, a snapshot timestamp and `active: false`.
Console may display that dated pending report. It never treats it as a live
in-flight cell or calls a container endpoint on Pages. Exact live inspection is
shown only when the serving standalone runtime advertises the capability.
No additional hosted workflow dispatches or provider calls are introduced.

## Lost-continuation recovery

While the operator keep-running switch is enabled, its scheduled watchdog checks
roughly every fifteen minutes for a timed-out research run or failed successor
handoff. It dispatches only the currently promoted runtime and only when no actual
research job or operator maintenance is active. It does not use Pages or the public
projection as authority. New cycles perform normal checkpoint verification and
interrupted-invocation accounting. GitHub may delay scheduled checks.

The watchdog does not restart a failed application, governance/configuration block,
or manually cancelled run, and it never enables a closed switch. Use Stop for
intentional maintenance. Optional sidecars can be deferred under context pressure
through the same engine used by containers; receipts explain that omission without
recording an unperformed probe.

Current proposal guidance derives belief-review eligibility from the full record and visible evidence. Existing belief IDs are separate from new-belief creation; a review must cite at least one visible evidence ID outside that belief's durable roots. If no such evidence is delivered, no review alternative is offered. This narrows generation guidance without changing acceptance or historical replay.

When the provider request approaches its context ceiling, belief review alternatives are bounded to one genuinely new visible evidence root per belief before source prose is shortened. Durable belief evidence and deterministic governance remain unchanged. The ceiling now measures exact rendered system/user text shared with the provider adapter; instructions, response rules and enabled probes reserve space before working context. See [provider-ready budgeting](retrieval.md#provider-ready-input-budget) for receipt fields and historical measurement distinctions.

## Lossless storage upgrade

Storage version 12 reduces the SQLite file through per-event zlib encoding and a
binary projection cache. The first writable open performs a verified atomic upgrade
and one-time compaction before ordinary work. Prepare and test the candidate, use
canonical Stop and fully drain research, preserve an immutable `wake-state` backup,
then push and use canonical Restart. Verify the exact runtime, upgraded checkpoint,
and a terminal new attempt. Never manually rewrite the live record or its hashes.

The `.sqlite.gz` transport remains separately compressed and verified. A smaller
SQLite file does not guarantee a smaller gzip package: already compressed individual
payloads can reduce cross-event gzip savings. The existing 100 MiB blob guard still
applies; storage compression does not provide unlimited hosted capacity.

A prior runtime cannot read the newer format. After new work has been appended,
rollback requires a compatible executable or an explicit lossless reverse migration;
restoring the old backup would erase research. Kernel chain verification and
historical application-policy reevaluation are distinct checks. Preserve and report
any preexisting application replay discrepancy rather than weakening policy or
rewriting accepted events to make the upgrade appear clean.
