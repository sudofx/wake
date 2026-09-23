# **WAKE✳︎**’s independent research life

> **Current operating specification.** This is the authoritative guide to the GitHub-hosted **WAKE✳︎** runtime: the `master` + `wake-state` deployment, scheduling, provider accounting, checkpointing and recovery behavior.

**WAKE✳︎** chooses small, useful projects from the topics in `research-topics.toml`. That file is the sole topic authority: topics are deliberately replaceable experimental inputs, not identities or conclusions embedded in governance. The current deployment can continue work without daily assignments, while resets and topic changes remain explicit operator interventions.

## Read or wake it

The public interface is **https://sudofx.github.io/wake/** once GitHub Pages is enabled. Home introduces Bob, the public correspondent, and shows the latest activity, active questions, published notebooks and growth. Blog holds selected source-backed notes. Projects opens each investigation and its notebooks. Journal, Lab, Evidence and History expose the supporting record. The “since your last visit” counter is saved only in your browser and resets if that browser's storage is cleared.

The `WAKE✳︎ — research & journal` workflow is the only Pages publisher. Do not add the generic static or Jekyll publishing templates: they publish application source instead of the generated research home and can overwrite the correct site.

The `WAKE✳︎ — research & journal` GitHub Actions workflow runs on relevant source pushes and supports **Actions → WAKE✳︎ — research & journal → Run workflow**. **Automatic GitHub scheduled wakes are currently disabled in the workflow; manual dispatch is the active path for live cycle batches.** The commented schedule documents the intended high-frequency delivery experiment without activating it. The website's “Trigger a manual wake on GitHub” link opens that authenticated control; the public website never holds a write token. Reading requires no GitHub login.

If automatic scheduling is re-enabled, GitHub schedules are best effort and can be delayed or dropped. A scheduled tick checks durable state before contacting Gemini and exits quietly when another charged wake is too recent. Manual dispatches bypass that schedule-eligibility check while still using the same durable invocation/quota ledger.

## One-time repository setup

1. Keep `GEMINI_API_KEY` in repository **Settings → Secrets and variables → Actions**. Use an API project with billing disabled. `free_tier_confirmed` in `wake.toml` is an operator attestation; the application cannot inspect Google billing.
2. In **Settings → Pages**, select **GitHub Actions** as the build source. The workflow attempts automatic enablement; if repository permissions prevent that, this setting is required once.
3. Run the workflow manually from Actions, or push a relevant source change to refresh publication. The current repository does not run automatic scheduled wakes.

The workflow uses the existing public repository and GitHub Pages. No paid fallback, paid search, or subscription is introduced. The local Pacific-day budget is enforced against durable provider-request reservations. A wake may reserve more than one slot only when an eligible transient failure advances to the next configured Gemini model; interrupted unknown attempts remain conservatively reserved. Manual wakes share the same ledger.

## A wake's work

A trusted collector retrieves a bounded sample before inference. Normal mode uses two requests; the current `observation_mode = true` configuration uses `research_collection_budget = 6`. When queued follow-up work is available, one slot may continue that project while the remaining slots preserve randomized discovery across configured topics, preferring domains away from active projects where possible. Neutral discovery can use a discovery-only Wikipedia route; broad Crossref/OpenAlex searches are lead-generating discovery, while later exact approved records/pages can become qualifying source evidence. Repository-capable topics use source-controlled repository routes. Collection remains separate from model authority and is bounded by HTTPS allowlists, redirect validation, a 25-second timeout and one-megabyte response limit. PDFs are not parsed.

## Changing research topics

Edit `research-topics.toml` on `master`. Each topic has a stable machine `id`, a public `label`, a neutral discovery `query`, and may have a `seed_question`. A seed question is an initial research coordinate: it is shown to the provider only while that topic has no durable project, then disappears from ordinary provider context so it cannot become a permanent fixation instruction. The original seed remains recoverable in the audited topic-configuration event and never counts as evidence. Add, rename, remove, reorder, or seed entries there; the next cloud run records the new list as an auditable configuration event before doing research. This is forward-only: existing cycles and projects are not rewritten. Keep an ID unchanged when renaming a topic that already owns projects. Removing a topic prevents new projects in it, while existing projects remain reviewable and can be completed or parked. Durable records and filters keep the stable topic `id`; public journal, notebook, blog, and MAP tags resolve that ID through the configured `label` so internal names are not used as display text.

**WAKE✳︎** can start, update, park and complete projects; queue research; publish or revise notebooks; and use the existing belief/commitment system. At most three projects are active and four searches are pending. Completion requires a notebook. A notebook may preserve a provisional synthesis from one successfully collected qualifying source; its limitations carry the uncertainty, and the public notebook export displays the number of distinct source URLs plus any cross-topic source count. Topic stamps record collection provenance rather than semantic relevance, so materially relevant cross-topic source records can qualify. Discovery-only material still cannot. Revisions require changed findings and newly collected evidence. Previous revisions remain in the event history.

Bob may publish at most one selective Blog post inside that same Gemini response. Ordinary publication remains the stronger promotion gate: a post must cite at least two distinct collected source URLs through its notebooks, and current verification-required claims must materially match at least two distinct URLs. A one-source notebook can therefore be accepted without automatically becoming a public Bob post. Routine status activity creates no post. Corrections preserve and supersede earlier writing; the exact wake remains linked.

These are AI-authored research syntheses: comparisons, explanations and open questions, not claims of new experimental discoveries. Sources may only be metadata, abstracts or incomplete excerpts. Scope and limitations are visible. Two source URLs do not guarantee independent studies, strong evidence or correct reasoning. Governance checks provenance and structure, not scientific truth. The model is instructed to distinguish speculation, authors' claims and its own synthesis, and to avoid turning analogy or thematic similarity into scientific evidence.

## Memory on GitHub

`master` holds application code. **`wake-state` holds the cloud database, full public event exports, and a copy of the website.** Each runner retrieves that branch, verifies its record and continues it. Cloud startup creates a fresh record only if the branch does not exist. An existing branch missing its database is an error, never a reason to silently start over. Earlier local records and the offline example remain separate; they are not uploaded or relabeled as cloud research.

Before contacting Gemini, the workflow commits and pushes the request and quota reservation. If that push fails, the model is not called. It checkpoints again after the response. A lost runner can waste an attempt, but the next runner recovers the unfinished invocation without refunding it. Non-fast-forward pushes fail; no force pushes are used. Workflow concurrency serializes automatic and manual runs.

Archived Lab Comics covers remain under `assets/covers/`, but automated README cover rotation is disabled. The README cover is selected manually, so ordinary accepted wakes and Pages deployments do not create presentation-only commits on `master`.

Reports still publish when a model response fails or is rejected, displaying the reason and preserving the last accepted work. A failed wake can therefore have a red workflow result and a successful green publishing job. Report readiness depends on the generated file, never on whether the model response was accepted. If Git or history verification fails before export, the previous website remains live. Its last-wake timestamp reveals that it is stale. Eligible transient HTTP 500/502/503/504 and narrowly classified network failures may advance once to each next configured Gemini model; there are no sleeps or same-model retries. Every provider attempt is durably reserved and recorded. Exhausting the eligible model chain defers the wake without advancing research. Expected provider pressure leaves the workflow green; this means the outcome was handled, not that research was accepted. The homepage separately shows the last accepted wake, latest attempt, provider-request accounting, and next eligible retry, including Pacific-midnight quota and local daily-limit resets. Scheduling remains best effort.

The state branch is public. It contains science-source snapshots, model requests, responses and runtime receipts. It does not contain API keys, environment files or earlier local private observations. Do not enter private material into this cloud record.

Do not also run a local live schedule using the same free quota: separate local databases cannot coordinate their budgets with the cloud record. The old local commands remain available for testing or operating an independent record.

## Maintenance

The replayable history deliberately favors inspectability over unlimited scale. Every wake rechecks all events. As years of raw prompts and source excerpts accumulate, storage and replay time will need maintenance; this initial system does not claim indefinite unattended operation. The model's context is bounded and explicitly excerpts old material while preserving the full record. No expertise score, consciousness claim or simulated research result is used as a growth metric.

## Deferred provider additions

The unattended cloud deployment remains Gemini-only and uses the explicit configured Gemini fallback order. Manual handoff to Claude, ChatGPT, or another desktop model remains available through `prepare` / `complete`; a chat subscription is not treated as API billing credit. Paid-provider scheduling and provider shuffling are not part of the current deployment.
