# **WAKE✳︎**’s independent research life

> **Current operating specification.** This is the authoritative guide to the GitHub-hosted **WAKE✳︎** runtime: `master` is development, `wake-runtime` is the explicitly promoted executable, and `wake-state` carries the separate authoritative sudofx SQLite record.

**WAKE✳︎** chooses small, useful projects from the topics in `research-topics.toml`. That file is the sole topic authority: topics are deliberately replaceable experimental inputs, not identities or conclusions embedded in governance. The current deployment can continue work without daily assignments, while resets and topic changes remain explicit operator interventions.

## Read or wake it

The public interface is **https://sudofx.github.io/wake/** once GitHub Pages is enabled. Home introduces Bob, the public correspondent, and shows the latest activity, active questions, published notebooks and growth. Blog holds selected source-backed notes. Projects opens each investigation and its notebooks. Journal, Lab, Evidence and History expose the supporting record. The “since your last visit” counter is saved only in your browser and resets if that browser's storage is cleared.

The `WAKE✳︎ — Update website · automatic` workflow is the only Pages publisher. Do not add generic static or Jekyll publishing templates: they publish application source instead of the generated research home and can overwrite the correct site.

`WAKE✳︎ — Internal only: one research cycle` is the only research execution lane. It may execute only when the workflow dispatch ref is `wake-runtime`; each accepted/rejected cycle can dispatch its successor from that same runtime branch and carries the exact runtime commit forward. `WAKE✳︎ — Internal only: keep-running switch` is only the durable on/off latch used by **Start research** and **Stop research**; running it manually does not start research.

Runtime control lives entirely in GitHub Actions. The website's small status light opens the repository Actions page; it flashes green only while a real `wake.yml` run is queued or in progress, and is red when no research run is active. There is no site authentication or control backend. **Start research** opens the keep-running switch and dispatches the first `wake.yml` cycle on `wake-runtime`. **Stop research** closes that switch before cancelling active cycles. **Reset WAKE to 0** requires an explicit `RESET` confirmation and refuses active research. It starts a new active WAKE generation at cycle zero; prior governed sudofx history remains durable and the pre-reset state is also archived by Git reference for operator convenience.

Runtime adoption is explicit. **WAKE✳︎ — Make new code live** verifies a candidate, rechecks that no real `wake-runtime` cycle is queued or running, and only then moves the runtime branch to that exact verified commit. It refuses while research is active: **Stop research → Make new code live → Start research**. CI on `master` is development feedback only; failures there never stop or redefine an already-running research chain.

The Pages shell loads the disposable `wake-live/live.json` projection with `cache: "no-store"` and checks it every ten seconds. New state is applied in place; live research no longer waits for or triggers a Pages deployment.

## One-time repository setup

1. Keep `GEMINI_API_KEY` in repository **Settings → Secrets and variables → Actions**. Use an API project with billing disabled. `free_tier_confirmed` in `wake.toml` is an operator attestation; the application cannot inspect Google billing.
2. In **Settings → Pages**, select **GitHub Actions** as the build source. The workflow attempts automatic enablement; if repository permissions prevent that, this setting is required once.
3. Use **Start research** when you want the promoted runtime to begin a continuous research chain. Website publication is automatic after relevant source changes.

The workflow uses the existing public repository and GitHub Pages. No paid fallback, paid search, or subscription is introduced. The local Pacific-day budget is enforced against durable provider-request reservations. A wake may reserve more than one slot only when an eligible transient failure advances to the next configured Gemini model; interrupted unknown attempts remain conservatively reserved. Manual wakes share the same ledger.

## A wake's work

A trusted collector retrieves a bounded sample before inference. Normal mode uses two requests; the current `observation_mode = true` configuration uses `research_collection_budget = 6`. With active projects, one slot remains broad exploration and the remaining slots prioritize project maturation: readable-source candidates, persistent-identifier promotion, queued follow-ups, then question-led scholarly discovery. Broad index results are discovery leads. Exact Crossref/OpenAlex/Semantic Scholar/DataCite records are metadata-routing receipts, not notebook evidence. Approved readable publisher/full-text/source-controlled text is the qualifying source boundary. PubMed/PMC identifiers can be promoted deterministically to NCBI PMC open-access BioC text when available. Collection remains separate from model authority and is bounded by HTTPS allowlists and redirect validation. Normal web responses are capped at one megabyte. PDFs are capped at eight megabytes and text extraction is bounded to the first 24 pages and 50,000 characters; the provider-facing evidence excerpt remains bounded to 10,000 characters with evidence-bearing sections preferentially retained.

## Changing research topics

Edit `research-topics.toml` on `master`. Each topic has a stable machine `id`, a public `label`, a neutral discovery `query`, and may have a `seed_question`. Development changes on `master` do not affect live research until that commit is explicitly promoted to `wake-runtime`. After promotion and restart, the next runtime cycle records changed topic configuration as an auditable event before doing research. This is forward-only: existing cycles and projects are not rewritten. Keep an ID unchanged when renaming a topic that already owns projects. Removing a topic prevents new projects in it, while existing projects remain reviewable and can be completed or parked. Durable records and filters keep the stable topic `id`; public journal, notebook, blog, and MAP tags resolve that ID through the configured `label` so internal names are not used as display text.

**WAKE✳︎** can start, update, park and complete projects; queue research; publish or revise notebooks; and use the existing belief/commitment system. At most three projects are active and four model-proposed searches are pending. A notebook may preserve a provisional synthesis from one qualifying substantive source, but project completion requires a notebook backed by at least two substantive distinct underlying source works. Known DOI/arXiv/OpenAlex identities collapse mirrors to one work. Revisions require changed findings and newly collected evidence. Previous revisions remain in the event history.

Bob may publish at most one selective Blog post inside that same Gemini response. Ordinary publication likewise requires support traceable through notebooks from at least two qualifying distinct source works; current verification-required claims must materially overlap those sources. A one-source notebook can therefore remain useful provisional research without becoming completion-ready or automatically publishable. Routine status activity creates no post. Corrections preserve and supersede earlier writing; the exact wake remains linked.

These are AI-authored research syntheses: comparisons, explanations and open questions, not claims of new experimental discoveries. Discovery and metadata receipts may guide retrieval but do not qualify findings. Readable material can still be incomplete, preprint-only, or otherwise limited; scope and limitations remain visible. Two distinct works do not guarantee independent studies, strong evidence, or correct reasoning, and unidentified mirrors may still evade work-level deduplication. Governance checks provenance and structure, not scientific truth.

## Memory on GitHub

`master` holds development code and may move independently. `wake-runtime` holds the exact promoted executable used by live research. **`wake-state` holds the authoritative cloud `data/sudofx.sqlite` database and is separate from both code branches.** On the first migration run, the existing `data/wake.sqlite3` chain is verified and archived exactly inside sudofx before any provider call; that legacy file then becomes frozen migration evidence, not an operational store. Each later runtime cycle reconstructs WAKE through the sudofx application contract from `sudofx.sqlite` alone. A branch missing both database formats is an error, never a reason to silently start over. Earlier local records and the offline example remain separate; they are not uploaded or relabeled as cloud research.

Before contacting Gemini, the workflow commits and pushes the request and quota reservation. If that push fails, the model is not called. It checkpoints again after the response. A lost runner can waste an attempt, but the next runner recovers the unfinished invocation without refunding it. Non-fast-forward pushes fail; no force pushes are used. Workflow concurrency serializes automatic and manual runs.

Archived Lab Comics covers remain under `assets/covers/`. They are static assets; runtime research and Pages publication do not modify them.

Each completed cycle refreshes the disposable `wake-live` projection after the authoritative sudofx SQLite state is checkpointed. Governance rejection and handled provider deferral can therefore update the public record without advancing accepted research. GitHub Pages is independent: it republishes only when website code changes. If the live projection refresh fails, the durable record remains authoritative and the previous public projection stays in place. Eligible transient HTTP 500/502/503/504 and narrowly classified network failures may advance once to each next configured Gemini model; there are no sleeps or same-model retries. Every provider attempt is durably reserved and recorded. Exhausting the eligible model chain defers the wake without advancing research. Expected provider pressure leaves the workflow green; this means the outcome was handled, not that research was accepted. The homepage separately shows the last accepted wake, latest attempt, provider-request accounting, and any known quota reset time.

The state branch is public. It contains science-source snapshots, model requests, responses and runtime receipts. It does not contain API keys, environment files or earlier local private observations. Do not enter private material into this cloud record.

Do not run a second independent live loop against the same provider quota. Local CLI commands remain useful for testing and manual records, but the hosted runtime is GitHub Actions plus `wake-runtime`/`wake-state`.

## Maintenance

The replayable history deliberately favors inspectability over unlimited scale. Every wake rechecks all events. As years of raw prompts and source excerpts accumulate, storage and replay time will need maintenance; this initial system does not claim indefinite unattended operation. The model's context is bounded and explicitly excerpts old material while preserving the full record. No expertise score, consciousness claim or simulated research result is used as a growth metric.

## Deferred provider additions

The unattended cloud deployment remains Gemini-only and uses the explicit configured Gemini fallback order. Manual handoff to Claude, ChatGPT, or another desktop model remains available through `prepare` / `complete`; a chat subscription is not treated as API billing credit. Paid-provider scheduling and provider shuffling are not part of the current deployment.
