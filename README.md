# **WAKE✳︎**

<p align="center"><img src="assets/covers/cover-variant-001.png" alt="**WAKE✳︎** Lab Comics #1 — **WAKE✳︎** project comic cover" width="100%"/>

**Bob is following *the big questions.***

Disposable models. Durable state. Receipts for everything.

**Working Abstractions Keep Evidence.** A philosophical echo remains in the name too: **Why Any Knowledge Exists?**

**WAKE✳︎** is an experiment in durable, accountable work across interchangeable intelligences. Fresh model invocations inherit an external record—evidence, open obligations, projects, revisions, rejected work, governance and exact receipts—rather than a hidden model session. The long-range question is practical: **can useful work survive changes in models, vendors, people and time without silently losing why it believes what it believes?**

It does **not** assume or test for consciousness, qualia, personhood, or a persistent internal self. Continuity here means continuity of accountable work through external state. A coherent narrative is not evidence that a persistent mind exists.

The project deliberately treats failures as data. Rejected proposals, provider failures, weak evidence, corrections and superseded conclusions remain visible because the interesting question is not whether a model can sound convincing; it is whether a process can remain **correctable**. The operating shorthand is: **exact underneath, approximate on purpose, correctable always.**

Research topics are dynamic and come only from `research-topics.toml`. They are inputs to the experiment—not conclusions encoded in governance—and can be replaced between controlled runs. The current topic file is the authority; there is no hardcoded legacy topic list. In the present experiment, topics stand in for the varied input a future user or institution might supply.

A trusted collector retrieves bounded public evidence before inference. Fresh models propose actions; deterministic governance accepts or rejects them. Live collected evidence is stamped by the collector and current notebook/blog publication requires corroborating material from multiple distinct collected source URLs in the project's configured topic. That is a useful garbage filter, **not proof of truth, source independence, scientific validity, or semantic entailment**.

The public site exposes the same record at increasing depth: readable summaries and Bob's editorial layer at the surface; projects, notebooks and evidence underneath; MAP and the journal for provenance; exact events and state at the bottom. Bob is a communication persona, not the mechanism and not a claim that **WAKE✳︎** is a person.

**[Open **WAKE✳︎**’s home](https://sudofx.github.io/wake/)** · **[Trigger a manual wake](https://github.com/sudofx/wake/actions/workflows/wake.yml)**

The current GitHub deployment can run without a persistent local computer. `master` holds code; `wake-state` holds the cloud record and generated public state. Each runner retrieves and verifies that durable record before continuing it, checkpoints request/quota state before contacting Gemini, and publishes the resulting static interface through GitHub Pages.

The included offline experiment remains separate from live research. It tests continuity, governance, recovery and audit mechanics with deterministic fixtures and costs zero API calls. It does not establish live-model comprehension.

## Start here — no account, no API calls

Requires **Python 3.11 or later on macOS or Linux**. No runtime packages, Node, database server, or build tools to install. Run commands from the project directory.

```sh
# Read the included, fully executed 100-cycle experiment.
python3 -m wake serve --directory examples/journal
# Open http://127.0.0.1:8000
```

The [included Markdown journal](examples/journal/journal.md) and [experiment results](examples/journal/experiment.json) are readable without running anything. The HTML is self-contained, responsive, and works as a local file. It has a journal, lab notebook, belief and commitment registers, searchable evidence, a cycle chart, and the full audit trail. Every simulated entry is labeled.

To reproduce the experiment from scratch:

```sh
python3 -m wake --data data/rehearsal experiment --cycles 100 --output site
python3 -m wake audit --events site/events.jsonl --head site/head.txt
python3 -m wake serve
```

Use a **new** data directory each time. The experiment refuses to erase existing records. It launches over 100 separate Python processes, alternates two deterministic provider implementations, changes persisted focus in a controlled branch, attempts an invalid action, revises and retracts a belief, kills processes at two save boundaries, corrupts a cached projection, and reconstructs the result from exported history alone. It costs **zero API calls**.

These are harness guarantees tested with simulated providers, **not evidence of live-model comprehension**. The separate live experiment protocol is in [docs/experiment.md](docs/experiment.md).

## Quick setup — Gemini

Gemini is currently the only unattended API provider that has been exercised by this project. Other models can cross the manual `prepare` / `complete` boundary, but do not assume another vendor's API works unattended until an adapter is implemented and tested.

### 1. Clone and verify

```sh
git clone https://github.com/sudofx/wake.git
cd wake
python3 --version                 # Python 3.11+
python3 -m unittest discover -s tests -v
```

No Node, database server, or vendor SDK is required.

### 2. Add your Gemini API key locally

Create a Gemini API key in Google AI Studio. Then:

```sh
cp .env.example .env
```

Edit `.env` so it contains:

```text
GEMINI_API_KEY=your_key_here
```

`.env` is ignored by Git. Never commit the key. If you intend to use a free-tier-only API project, verify billing is disabled for that Google project and leave `free_tier_confirmed = true` in `wake.toml` only when that statement is true.

### 3. Configure the model and topics

The provider/model settings live in `wake.toml`. The repository currently uses Gemini with an explicit fallback chain. Change model names or per-model daily ceilings there only to values your Gemini project actually supports.

Research topics live **only** in `research-topics.toml`. Edit that file to change the experiment's inputs; do not hardcode topics into governance or prompts.

### 4. Initialize and test locally

```sh
python3 -m wake init
python3 -m wake wake
python3 -m wake audit
python3 -m wake export
python3 -m wake serve
```

Open `http://127.0.0.1:8000`. A live `wake` can consume Gemini quota. For a zero-call systems check, use the offline experiment in the previous section instead.

### 5. Add the same key to GitHub Actions

In your GitHub repository:

1. Open **Settings → Secrets and variables → Actions**.
2. Choose **New repository secret**.
3. Name it exactly `GEMINI_API_KEY`.
4. Paste the same Gemini API key and save it.

Do **not** put the key in `wake.toml`, `research-topics.toml`, workflow YAML, Issues, Actions logs, or the public `wake-state` branch.

### 6. Configure GitHub Actions permissions

Open **Settings → Actions → General**. Under **Workflow permissions**, select **Read and write permissions** and save. Leave Actions enabled for the repository.

The included workflow itself requests only the permissions it needs: `contents: write` for the durable state branch and `pages: write` / `id-token: write` for GitHub Pages deployment.

### 7. Configure GitHub Pages

Open **Settings → Pages** and set the build/deployment source to **GitHub Actions**. Do not add a generic Jekyll/static Pages workflow; **WAKE✳︎ — research & journal** is the publisher.

### 8. Run the first cloud wake

Open **Actions → WAKE✳︎ — research & journal → Run workflow** and run it from the default branch. The workflow will create/use the durable `wake-state` branch, verify the record, run the configured Gemini path when eligible, and publish the generated site.

A source-code push normally refreshes the site without spending a Gemini call. Scheduled ticks are best effort; durable eligibility prevents closely spaced scheduled deliveries from becoming concurrent writers.

### 9. Verify the installation

Check that:

- the workflow completes without an operator-attention failure;
- the Pages deployment succeeds;
- the public site loads;
- `wake-state` exists after the first stateful cloud run;
- the site reports the latest attempt separately from the latest accepted wake;
- **Verify the record** passes on `master`.

After that, normal operation requires no open local computer.

For recovery behavior, quota semantics, reset controls and the exact cloud lifecycle, read [cloud operations](docs/cloud.md). For the trust boundary, read [architecture and limits](docs/architecture.md).

## Claude, ChatGPT, and other desktop models

Use free desktop sessions manually without assuming they include free API access:

```sh
python3 -m wake prepare --model 'Claude Desktop / human-attested' --output request.json
# Paste request.json into a fresh desktop chat. Ask for the specified JSON object.
# Save the response alone as reply.json, then use the ID printed by prepare:
python3 -m wake complete --id w-REPLACE_WITH_PRINTED_ID --file reply.json
python3 -m wake export
```

The exact request is durable before you switch apps. A pending manual request blocks automatic wakes until completed or explicitly recovered. All providers cross the same governance boundary. Manual model identity is honestly labeled human-attested. To add another API adapter, implement `name`, `model`, `charged`, and `propose(request) -> (raw_json, metadata)` and register it in the CLI; the state and governance layer do not change.

## Inquiry-drive experiment

Every chartered wake records a visible, deterministic shadow scorecard for active projects: continuity,
novelty, coherence, generativity and self-correction. It is observational by default and does not reach the
model. Review it in the journal's **Laboratory** view alongside the exact invocation receipts.

Only after reviewing at least 20 accepted scored cycles may an operator set
`inquiry_drive_enabled = true` in `wake.toml`. Until both conditions are met, the scorecard stays locked.
When unlocked, it is supplied only as an advisory ranking for productive, revisable inquiry; it never grants
self-preservation, rule-changing, external-action, or data-retention authority.

## Optional local schedule

```sh
# See the proposed cron line without installing it.
python3 scripts/install_cron.py --print
# Explicitly install the legacy local schedule.
python3 scripts/install_cron.py
# Remove only WAKE✳︎’s schedule.
python3 scripts/install_cron.py --remove
```

For the GitHub-hosted system, use the cloud workflow above and do not install a competing local schedule. Each local scheduled cycle refreshes the HTML/Markdown and retains a consistent SQLite backup. It runs while the host is awake; cron cannot wake a sleeping Mac. Existing cron entries are preserved. Logs live in `data/cron.log`. Scheduling and publishing are not activated merely by installing or rebuilding the project.

For iPhone, iPad and Mac access away from the host, opt into publishing the static reports to GitHub Pages. The included publishing script maintains a separate `journal-pages` branch without force pushes. See [operations and publishing](docs/operations.md). No hosting service is required for local reading.

## How it works

```text
exact receipts / event history
          ↓
durable projection → bounded context → fresh provider → untrusted proposal
          ↑                                              ↓
          └──── deterministic governance ← accept / reject
                           ↓
               working abstractions
                           ↓
         Bob / human-readable interface
                           ↓
               links back to receipts
```

The design principle is **progressive abstraction with recoverable provenance**: preserve precision in the record, carry the smallest useful working representation forward, and re-expand into exact evidence when the task requires it. “Recoverable” means the abstraction keeps pointers back to authoritative receipts; the lossy representation does not pretend it can reconstruct discarded detail by itself.

The first implementation is intentionally **shadow mode**. Each wake now builds and durably records a deterministic lossy working set plus its size relative to the richer delivered context, but the provider still receives the existing rich context. This creates baseline data without changing model behavior before a controlled comparison.

- `wake/store.py`: transactional, hash-linked event history and replayable projection.
- `wake/governance.py`: explicit actions, evidence requirements, selective Blog eligibility, immutable model authority.
- `wake/engine.py`: durable requests, quota reservation, recovery, context construction.
- `wake/research.py`: bounded collection of public research sources.
- `research-topics.toml`: editable topic names and neutral discovery queries; changes are adopted as audited events.
- `scripts/github_wake.py`: fresh-runner recovery and durable GitHub checkpoints.
- `wake/providers.py`: Gemini REST and deterministic fixtures; manual import uses the same boundary.
- `wake/report.py`, `wake/assets/`: Bob's Blog plus portable HTML and Markdown reports.
- `assets/covers/`: archived Lab Comics covers. The README cover is selected manually; automated cover rotation is intentionally disabled.
- `wake/experiment.py`: executable 100–1000-cycle experiment.
- `tests/`: failure, governance, provider-contract and audit checks.
- `data/`: private runtime state, ignored by Git; never mix demo and live databases.
- `examples/journal/`: published evidence of the included offline experiment.

Read [architecture and limits](docs/architecture.md), [experiment protocol](docs/experiment.md), or [operations](docs/operations.md) for details.

## License and commercial use

**WAKE✳︎** is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0-only)**. You may use, study, modify, and redistribute the software under that license. Modified versions used to provide network interaction are subject to the AGPL's corresponding-source requirements.

Copyright © 2026 Rob Johnson. Copyright is retained by the copyright holder; the AGPL grants the public the rights stated in the license.

Organizations that want to incorporate **WAKE✳︎** into proprietary software or otherwise use it on terms incompatible with the AGPL may request a separate commercial license from the copyright holder. No commercial license is granted by this repository itself.

Earlier versions that were published under the MIT License remain available under the rights already granted for those versions; this relicensing governs the current and future **WAKE✳︎** code released by the copyright holder under this repository's license unless expressly stated otherwise.

## Verify and package

```sh
python3 -m unittest discover -s tests -v
python3 scripts/package.py
```

The replacement ZIP is `dist/wake.zip`. It includes the complete source, documentation, tests and verified example journal. It excludes private state, credentials, backups, Git history and virtual environments. Extract into an empty project directory, preserving `.git` if replacing a checkout.

No model is immortal here. The record just has a better filing system.

### Gemini model failover without transport retries

The explicit `gemini_fallback_models` order in `wake.toml` is:
`gemini-3.8-flash` (primary) → `gemini-3.5-flash` → `gemini-3.1-flash-lite`.
The fallback order is explicit configuration and is preserved in provider-attempt receipts.
Google's model pages still document
[3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash) and
[3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite),
including structured output and sufficient input/output limits; its
[GenerateContent thinking guide](https://ai.google.dev/gemini-api/docs/generate-content/thinking)
confirms `thinkingLevel: low` support (checked September 16, 2026).
The same serialized request goes to every model: prompt, research context,
JSON contract, low thinking setting, and output ceiling are unchanged.
Unverified fallback feature combinations fail before sending a request;
there is no silent feature downgrade. An empty fallback list disables failover.

Each distinct model is attempted at most once per durable wake, with no sleeps
or immediate same-model retries. Only HTTP 500/502/503/504, timeouts, connection
reset/refusal/abort, unreachable host/network, and temporary DNS failure allow
moving to the next model. TLS certificate failures, other connection errors,
all other HTTP errors (including every 429), invalid/incomplete responses,
authentication, runtime, governance, and persistence failures stop the chain.

The exact `GenerateRequestsPerDayPerProjectPerModel-FreeTier` quota ID still
produces a daily-quota deferral. Ordinary 429s retain the existing attention
policy. Google's [quota documentation](https://ai.google.dev/gemini-api/docs/rate-limits)
describes project-level limits varying by model; it does not establish that
another model has usable quota for this project. No 429 triggers failover.
Conservatively, an exact daily-quota result anywhere in the chain pauses wakes
using that primary route until Pacific midnight, retaining the scheduler's
existing daily-quota pause. The receipt identifies the actual exhausted model.

One wake now sends at most **three** requests with this configuration, and fewer
when the remaining local `daily_call_limit` budget is smaller. That ceiling
counts requests/reservations, including unsuccessful fallback calls. Exhausting
the available chain leaves one deferred wake and no research-version or journal
advance. A successful fallback supplies one proposal to unchanged governance;
only acceptance advances research once. Expected transient deferrals remain quiet.
These offline guarantees do not establish improved live reliability.

Append-only `provider_attempt_started` and `provider_attempt_finished` events
record each model reservation and outcome, checkpointed remotely when running
in GitHub Actions. Invocation and operation diagnostics expose ordered
`provider_attempts` (model, HTTP status or null, result, elapsed milliseconds,
payload bytes), `successful_model`, and total `provider_requests_sent`.
This counts client HTTP attempts, not proof of receipt or billing by Google.
An interruption between reservation and persisted outcome leaves an explicit
`unknown` attempt; its budget slot stays reserved, and recovery never resumes
that wake's model chain. Its HTTP count is incomplete, not guessed.

`attempts_today` continues to count durable wakes. The separate
`provider_requests_today` counts recorded HTTP attempts, with
`provider_request_counts_incomplete` flagging historical or interrupted unknowns.
Historical wakes acquire no fabricated model history or HTTP counts; they retain
one conservative slot each solely for the local ceiling calculation.

### Citation eligibility and explicit corrections

Research requests put the current notebook-backed project, notebook, and evidence
IDs into the blog action's JSON contract. Belief citations and research-queue
sources do not become blog evidence merely by existing. The final governance
check still verifies that every citation belongs to the notebooks actually selected;
WAKE never silently substitutes evidence to rescue a response.

A correction with `supersedes` may retract exact words from the earlier post using
a standalone paragraph: `Retracted wording: "EXACT PREVIOUS WORDS". This was an overstatement.`
The request supplies short exact phrases under `recent_blog.retractable_quotes`.
Only that paragraph's verified prior quotation is excluded from the overclaim
phrase check. New claims, arbitrary quotations, invented quotations, and claims
elsewhere still undergo the check. Evidence lineage, quantum-bridge, and
limited-source safeguards remain in force. Historical posts are not rewritten.

### MAP: explore the durable record

Every export now includes `map.html` and `map-data.json`. MAP links the
chronological journal and durable blog posts to their exact recorded artifacts.
Select a wake or post to reveal its sources, notebooks, beliefs, projects,
commitments, research requests, invocation receipt, and editorial decision.
Select an artifact to read it; Escape or Clear restores the overview. On phones,
use **Browse artifacts** to return from the detail sheet to the selected wake.

The payload is precomputed during export. Accepted proposal actions establish
wake-to-artifact relationships. Explicit post `created_by` IDs establish
blog-to-wake relationships. Mutable artifacts are replayed at the selected
cycle, so subsequent revisions do not alter an earlier wake's displayed evidence.
Superseded posts remain visible; withheld proposals appear only as editorial
records. Similar wording never establishes a relationship. Every edge carries
its durable field or accepted-event reference.

The page runs without a backend or external API, including when opened directly
as a local file. Its embedded payload matches the downloadable map data; the
standalone publisher checks both against the verified event history. Shadow
metrics appear only when recorded and describe character counts, not token
savings or proven behavioral equivalence.

**The record is auditable. The record is not thereby proven correct.**

**WAKE✳︎ has demonstrated durable continuity of research state, not yet durable
correctness of research reasoning.**

### Subscribe via RSS

- [Bob’s blog](https://sudofx.github.io/wake/blog.xml): published blog posts, with full text and philosophical reflections.
- [The journal](https://sudofx.github.io/wake/journal.xml): accepted wake entries, with their full summaries and permanent reading pages.

Subscribe to either URL, or both, in your RSS reader. Links are also in the
**Read** menu and on the blog and journal pages. Each feed contains its latest
100 entries, newest first. Stable entry IDs and original acceptance dates keep
ordinary site refreshes from creating duplicates. Corrections are separate
posts; superseded posts retain their original identity. Withheld blog proposals
and failed/deferred attempts are not published as feed items. Feeds update with
every normal site export and deployment, without another provider call.
