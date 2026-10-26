# Develop WAKE✳︎

New to the project? Follow [the setup guide](setup.md) for local Docker, GitHub
Pages, VS Code and Codespaces, then return here for source and verification details.

Use [kernel development](kernel.md) for the application seam and
[multiple installations](installations.md) for parallel container operation.

This is the entry point for changing WAKE safely. The repository owns executable
behavior; installations own independent records. A shared source tree does not
imply a shared database, execution process, deployment, or provider quota ledger.
Read [architecture](architecture.md) for invariants, [mirror publishing](cloud.md)
for GitHub, and [standalone operation](standalone.md) for Docker.

Before changing anything, answer three questions:

1. **Which installation are you changing?** Local Docker and Codespace
   WAKE have separate records and processes.
2. **Which code is actually running there?** A checkout, mounted workspace and
   packaged image can all contain different versions.
3. **What are you authorized to change?** Editing, committing, pushing, restarting containers,
   uploading a public snapshot and resetting records are separate actions.

If you only need the key terms, use the [glossary](glossary.md). If you need a
release procedure, go to [mirror publishing](cloud.md#development-and-release).

Long verification and delivery jobs should run in the background while independent
authorized work continues. Recheck the previous job before its next dependent
publication or runtime operation. Do not repeatedly poll an unchanged job or
rerun unaffected suites to fill the wait. Use the release boundaries in
[hosted upgrades](cloud.md#publish-source-without-upgrading-records) to choose checks;
full history replay is a record-compatibility gate, not a universal UI gate.

For private human checkpoints and fresh-conversation recovery, use the
[continuity workflow](continuity/README.md). It complements the authoritative
research record without adding runtime state or automatic model context.

The former hosted Bob service and activity relay are retired. Public [Ask Bob](ask-bob.md)
uses an opt-in downloaded WebGPU model on the reader’s device; pinned model files
come from Hugging Face, with no conversation sent there. The optional loopback
Gemini reader is separate. Public presentation uses GitHub Pages; runtime research
uses GitHub and Google Gemini.
Any additional service requires the user's explicit approval.

For a real bounded source repair, open **Self-correction** from Console and run
the [source-correction workflow](self-correction.md). WAKE generates selected
presentation/docs edits, tests them in isolation and creates a draft pull request.
Merge, website publication and runtime promotion remain separate decisions.

For research-backed code proposals, disposable-container comparisons and human
review receipts, use the [improvement workflow](improvements.md). `wake improve`
creates an explicit isolated experiment record; it never opens research authority
or applies a proposed patch.

The [autonomous context lane](autonomous-context.md) instead generates and adopts
a bounded policy on the owning native record. Its deployment grant is
`autonomous_context_improvement = true` with active decision memory. The default
is false. `wake improve autonomous-demo --output NEW_DIRECTORY` runs its complete
native-record loop without a model, human proposal or per-change review.

For an isolated, governed operational adjustment with failure and rollback
scenarios, run `wake improve recovery-demo --output NEW_DIRECTORY`; see
[bounded recovery](resilience.md#try-bounded-operational-self-correction-in-isolation).
It changes only synthetic fixture callers, never installed research settings.

For the browser-local digital colony and its bounded Bob observation contract,
see [Ant Farm](ant-farm.md).

## Current development path

Start with [one-container setup](standalone.md#run-one-installation-container).
`scripts/wake_installation build` builds the writable development image;
`start` launches one `wake` container stopped for inspection. Attach VS Code or
use `scripts/wake_installation shell`. Preserve the existing `.bashrc` prompt.
Internal nodes are worker processes, with one server on container port 8080
(host port 8080 by default), not twelve separately operated containers.

The root website is a full unified view of the node snapshots. Its Console retains
the normal panels below an installation overview; individual node views remain
selectable from the fixed masthead on Console pages; the unified option is named
`wake`. Switching retains the current page and view. `wake/installation_projection.py` owns aggregation and attribution;
`wake/installation_site.py` exports the website through the canonical report exporter.
Neither opens authority or requests model output.
Project reframing histories keep their ordered lists in the unified view, with
node-qualified project and evidence links and each frame's captured source head.
The journal overview carries a bounded event tail and compact invocation/evidence
views; complete history remains in `events.jsonl`. Installation comparisons read
small exported summaries, and runtime status reads only worker observations.
Reader pages begin with `reader-data.json`, capped at 256 KiB. Opening an exact
record or loading older entries fetches same-origin `reader-records/` pages; the
complete `wake-data.json` archive is never a routine polling channel. An unavailable
node changes its freshness indicator, not access to its last completed export.
Console similarly separates its overview from optional wake details. See
[browser transport](retrieval.md#browser-views-and-exact-detail).
The unified complete-history stream is merged from node exports, retaining source
heads and local receipt identities. Its sort index holds dates and offsets rather
than full payloads. Inactive automatic-pause controls do not load authority during
the idle loop.

The installed CLI is `wake-research`; operator commands use an installation-specific
Unix socket in `/tmp` with mode 0600. Console access over the LAN is read-only.
Inside the installation, `wake status` reads the same controller status as
`wake-research status`. To inspect one record explicitly, use
`wake --data /data/nodes/100.wake/record status`. Outside the installation,
`wake status` retains the single-record default of `data`.
Source changes do not automatically replace these workers: a container restart returns to stopped
inspection, while `wake-research restart` explicitly resumes research. Commands,
archive verification, quotas, and publication are documented once in the
[standalone guide](standalone.md#control-research-from-the-shell).
Changes to the controller's provider-slot protocol require refreshing the
controller as well as workers. Drain through the operator controls, preserve
`/data`, restart the existing container, then explicitly start research. Verify
fresh process identities, control acknowledgments and accepted progress; a
running control alone does not establish healthy execution. The
[shared queue contract](standalone.md#collect-quickly-through-one-shared-api-queue)
distinguishes cancellable reservations from confirmed provider calls.

The multi-container runner, Compose installations and development preview remain
compatibility paths. The earlier GitHub executor branches remain historical
records. The current [hosted installation](cloud.md#run-research-on-github-without-a-laptop)
uses the same controller in Actions containers and its own encrypted native-record
transport. Do not restart a transferred local installation as a second writer.
For a hosted stall, inspect the failed step and numeric API-limit diagnostics first.
The read-only `inspect` action of `hosted-control.yml` reports enabled intent and
current allowance. Quota waits preserve checkpoints and stop authority; see
[continuation and repair](cloud.md#continuation-and-repair).
The new Codespace path needs its own actual remote acceptance evidence.

## Establish the target before editing

Record the checkout's remote, branch, HEAD and existing changes. Identify whether
it is the intended repository, a bind-mounted checkout, an installed package, or a
reference mirror. Preserve existing edits. Inspect the actual process command,
working directory, image and mounts before assuming which source executes.
`python -c 'import wake; print(wake.__file__)'` reveals the imported package in that
execution environment. Do not print environment variables or container secrets.

For publication, inspect the Pages source and public branch. For container changes, identify
the container and its exact data volume before recreation. A container name, an
IP address, and an image tag can change; none identifies a record by itself.

| Surface | Executable source | Authority | Presentation |
| --- | --- | --- | --- |
| One-container installation | Fixed worker source in `/workspace` | `/data/nodes/ID/record/wake.sqlite`, one writer per node | One server, per-node exports and `installation.json` |
| GitHub Pages | Uploaded artifact on `wake-public` | None | Dated unified website and node snapshots |
| Compatibility Docker | Image package under `/app` | Selected volume at `/data/wake.sqlite` | Atomic temporary website generations |
| Compatibility VS Code overlay | Bind-mounted `/workspace` because it sets working directory there | Same selected `/data` volume | Local export, never hosted fallback |
| Codespaces | Mounted workspace source | `data/installation/nodes/ID/record/wake.sqlite` | One installation site, private forwarded port 8080 |
| CLI / offline fixtures | Imported package in the invoking environment | Explicit `--data` directory | Exported directory |

These rows may share code while retaining different histories. Equal cycle counts
are not evidence of shared authority; unequal counts are not a synchronization
failure. Never replace a standalone record with the hosted checkpoint to make its
screen match. Restore or migrate a record only through a separately authorized,
verified operation.

## Source ownership

| Change | Start here | Protected boundary |
| --- | --- | --- |
| CLI and installation | `wake/installation.py`, `installation_cli.py`, `installation_gate.py`, `scripts/wake_installation`; compatibility: `wake/__main__.py`, `wake/standalone.py`, `runtime_supervisor.py`, Compose files, `scripts/wake_runner` | Explicit initialization; preserve selected volume; one scheduler |
| Public mirror | `wake/installation_cli.py`, `scripts/wake_publish`, `scripts/publish_pages.py` | Filter private data; pin immutable exports; dedicated publication branch |
| Record adoption / domain bridge | `wake/authority.py`, `record_store.py`, `application.py`, `domain_events.py`, `event_format.py` | One writable authority; immutable historical meaning and hashes |
| Generic record/runtime | `wake/kernel/` | Deterministic receipt, replay, access and invocation contracts |
| Research orchestration / context | `engine.py`, `prompts.py`, `memory.py`, `retrieval.py`, `trust.py`, `attention.py` | Derived context cannot rewrite record or waive obligations |
| Decision-relevant recall | `decision_memory.py`, `engine.py`, `comparison.py` | Optional snapshot-bound context; existing eligibility and budgets, no learned policy or second authority |
| Domain policy | `application_policy.py`, `governance.py`, `experimental.py` | Models propose; deterministic policy accepts or rejects |
| Providers / quota | `providers.py`, `scheduling.py`, native kernel lifecycle | Every effect reserved and accounted; no fabricated progress |
| Collection / evidence | `research.py`, `evidence_quality.py` | Untrusted prose, bounded transport, source readiness separate from truth |
| Matrix | `kernel/matrix.py`, `matrix_campaign.py`, `matrix.py` | Frozen coordinates; results append through the application |
| Correction / witnesses | `correction_demo.py`, `checkpoints.py`, `audit.py` | Supersede rather than erase; independent retained witness required |
| Browser export / provenance | `report.py`, `live.py`, `research_projection.py`, `provenance.py`, `feeds.py`, `history.py`, `rejected.py` | Disposable views, never read back as operational authority |
| Shared page chrome | `wake/assets/masthead.css`, `site-theme.js`, `nav.js`; `report.py` export | One geometry owner; themes and descriptions are presentation only |
| Console interaction | `wake/assets/console*.js`, `research*.js/css`, `process-field.*`, shared `nav.js` | Browser preferences and animation do not alter experiments |
| Legacy compatibility | `wake/store.py` | Migration/read-only historical evidence and deliberate fixtures only |

Prefer changes at these owners over a second implementation. Read nearby tests
and current callers before changing a contract. Comments at a seam should explain
why it exists, its failure behavior, and the condition under which it can change.
Avoid duplicating obvious syntax or embedding operator conversation in source.

## Website installation identity

`wake.report.export` defaults to standalone mode and produces a complete artifact: templates, transformed pages,
record views, Console components and `deployment.json`. `_deployment_site` places
`WAKE_DEPLOYMENT` before reader scripts in generated pages. All modes read same-origin JSON. Live containers may read `/runtime.json`,
including through LAN addresses; snapshot-only public exports have no runtime
capability. Only an explicit `hosted_status` presentation binding enables a separate,
read-only public Actions observer for the header light; ordinary mirrors do not poll
GitHub. That observer never feeds the research transport or live canvases. A missing/invalid
identity stays same-origin; Console reports the missing identity instead of
silently substituting public research. Identity is routing configuration, not
an authentication credential or proof that the snapshot is fresh.

Raw `wake/assets/*.html` files are templates. Copying one over a generated page
bypasses installation transforms. Regenerate the full artifact through export;
for the standalone server, use its normal publication/recreation path. The server
builds a complete generation before switching `current` atomically. Do not patch
its temporary generation as an upgrade procedure. `/tmp` disappears on recreation.

`python -m wake --data DATA export --output SITE` creates a same-origin standalone view.
A simple static server can serve that export without provider calls. It has no
local scheduler endpoint, so runtime status may be unavailable. Preview a public artifact with a plain static server. `scripts/publish_pages.py`
only uploads a prepared twelve-node public artifact.

## Codespaces access and preview

Use the [Codespaces walkthrough](setup.md#4-run-and-develop-in-codespaces).
`.devcontainer/devcontainer.json` builds the development image and starts
`scripts/installation_preview.py`, which runs the same twelve-node controller
from the mounted checkout. Records live in `data/installation`; port 8080 stays
private. `wake-research` operates that installation. Stop the controller and wait
for it to drain before starting another process against the same records.

`scripts/dev_preview.py` is an older single-record compatibility tool. It is not
the committed Dev Container lifecycle. Do not mix its record directory or controls
with the current installation.

For desktop VS Code, [attach to the managed container](setup.md#3-develop-in-vs-code).
Verify source mounting, initialization and forwarded access in the actual remote
environment before claiming remote acceptance. An offline build on a laptop does
not prove Codespaces works.

## Release and restart boundaries

Local source edits do not publish GitHub. An authorized source push updates
`master` and runs CI; it does not publish container data or replace running workers.
Build or restart the intended container separately, preserving its data volume.
Already imported Python does not automatically reload. Workers start stopped for
inspection after a container restart; explicitly start research when ready.

Public publishing is a separate upload to `wake-public`. It pins exported
generations, reuses compatible completed pages and rebuilds incompatible pages
without changing research controls. See [capture and compatibility](cloud.md#publish-the-local-installation-mirror).
Verify Pages deployment and the upload date independently of source CI.
Hosted successors honor the installation’s `hosted-runtime.json` binding and
require successful repository CI. Publishing new source does not promote a bound
runtime. Verify record compatibility before changing the binding. Use the
[hosted start/stop workflow](cloud.md#run-research-on-github-without-a-laptop) for
that installation; local container controls do not control it.

## Lightweight website observation

Local pages share one read-only status channel per document; same-origin embedded
panels subscribe to their parent. `/runtime.json` reads bounded worker observation
files and small export-head files, never record databases or research graphs.
The optional `/runtime.events` server-sent stream shares the same sample for up
to one second, supports at most sixteen simultaneous connections, and falls back
to small status requests when unavailable. Worker samples older than five seconds
are unavailable. Visibility changes, disconnects and expired samples clear live
indicators. Public snapshots open no live channel and label uploaded observations
with their dates.
Workers report completed quota waits or provider failures before rebuilding their
website, so slow exports cannot leave the live light green after a known failure.

Console and process views share a single research projection request. Refreshes
check the export head before fetching another projection. Canvas views are created
near the viewport or on interaction, and collapsed views defer initialization.
The installation comparison uses the presentation thread's completed summaries;
an HTTP request does not open twelve research files or wait for workers.
These caches hold disposable presentation only; they cannot accept research or
change provider sequencing. See [inspection boundaries](architecture.md#optional-inspection-activity).

Complete exports reuse their captured state and event history for aggregate
metrics. Record reconstruction passes the same envelope and receipt list through
legacy-prefix and active-head validation instead of decoding the projection
again for each helper. This reuse lasts only for that operation; the next read
still loads current authority, and full startup and audit verification remain.
Historical MAP rendering replays into one private working state, copies each
incoming event, and retains independent node details. It does not copy the full
accumulated invocation history at every event. Creation/revision labels still
use collection membership from before the recorded transition.

`scripts/wake_runner` is a convenience launcher for the named local editor image.
It preserves its selected data volume on normal recreation, forces live mode and
matrix enablement, binds port 8080 to LAN interfaces, and uses a configured Docker
Desktop proxy. Its `--reset` deletes that selected record volume; it is not a
recovery or port-change option. Use Compose for portable configuration and paused
inspection. Never infer that this helper is appropriate on an arbitrary host.

## Verification matched to the boundary

Run `python -m unittest discover -s tests -v` in an environment with project
dependencies installed. CI also runs the offline 100-cycle experiment; both use
fixtures and must not be described as live-model findings. For deployment routing,
execute the browser loaders with standalone, hosted, missing and invalid identity
on loopback, LAN and hosted hostnames. For UI changes, inspect the browser's actual
record head/version and selected trace as well as layout and overflow. Test the
artifact produced by export, not only its source templates.

`python -m wake --data DATA audit` verifies the complete kernel event chain,
provider and access journals, then independently reduces the active application's
history using historical acceptance rules and compares it with the current
projection. `status` uses the fast projection path and is not a full audit.

Container acceptance lives in `scripts/test_container.py`: it uses isolated
resources, no network, and verifies persistence through recreation.
`scripts/test_installations.py` verifies multiple real Compose installations and
the optional gateway. `.github/workflows/containers.yml` runs packaged image
acceptance for ARM64 and AMD64 on pull requests or manual dispatch, without
publishing or changing research authority. Never use the
operator's record as disposable test data. Keep signing keys and provider secrets
out of logs, fixtures, exported sites and Git. Use [checkpoint limits](retrieval.md#verified-replay-seeds)
when interpreting a fast replay versus a full audit.

## Documentation ownership

| Document | Role |
| --- | --- |
| `README.md` | Current overview, setup entry points and feature limits |
| `AGENTS.md` | Repository-local change invariants |
| `docs/development.md` | This navigation and environment map |
| `docs/glossary.md` | Plain-language definitions of WAKE terms |
| `docs/kernel.md` | Reusable application contract and extraction proof |
| `docs/installations.md` | Independent Compose deployments and optional gateway |
| `docs/architecture.md` | Authority, lifecycle, policy and trust boundaries |
| `docs/cloud.md` | Canonical container export and public mirror publication |
| `docs/standalone.md` | Docker, LAN, editor, volume and backup operations |
| `docs/retrieval.md` | Memory delivery, omissions and replay-seed guarantees |
| `docs/experiment.md` | What observations mean and how to compare them |

Update the owning living documents alongside material behavior changes. Keep
command examples aligned with code and distinguish defaults from deployment
configuration. Dated validation results do not certify the current checkout.

## Installed-package and live-inspection checks

Container acceptance runs from `/tmp` so Python imports the installed wheel, not
`/app`'s copied checkout. Nested Console icons/backgrounds and every referenced
script must survive packaging and export. New public activity fields are optional
capabilities; assets cannot assume an older runtime implements them.

Use an isolated, slowed fixture to inspect live phase/cell markers without API
calls. Verify both an active phase and its disappearance after completion or
connection loss. A hosted snapshot cannot establish an in-flight phase. Keep
activity overlays separate from score, selection and recorded historical traces.

## Shared website chrome

Export adds the configured node domain below the logo on every page with the shared
masthead; the browser hostname fills an unconfigured domain. The gateway supplies
Main, Blog and Console links per node. See [runner terminals](standalone.md)
for repository-owned shell setup; no personal host dotfiles are imported.


`masthead.css` owns header geometry, icon sizes, mobile breakpoints and the shared
hover/focus/touch description surface. Load it after page skins. Page styles may
supply color tokens but must not add competing masthead geometry. Export normalizes
the main, map, flat-record and nested reading headers from the index shell, including
relative navigation and accepted-cycle metadata. Verify exported HTML, not raw
reading templates. Console component pages intentionally hide their enclosing header.

`site-theme.js` is the only theme controller: it follows the device until a user
chooses a theme. The choice uses the origin-local `wake-site-theme` key, so legacy
forced-dark values cannot override the default. Header geometry must remain identical
in both themes. The first control is a labelled switch; keyboard focus stays visible.

`nav.js` supplies one description controller. Mouse hover and keyboard focus reveal
it; touch hold reveals other control descriptions without performing their actions.
Tapping the status light shows its explanation. Status is installation-specific and
read-only. Keep its meaning consistent across views: green means running; blue,
idle; yellow, waiting or stopped; purple, provider quota standby; and red, operator
or agent action required. If status cannot be confirmed, show it as unavailable
rather than as a red failure. Interactive canvases and drag controls suppress
selection, while record inspectors and reading text remain selectable.

## Console layout and provider phases

Console modules use the same workspace grid, including the overview and record
inspector (#014). The outer Console
gutter is 20 px on each side, or 10 px on iPhone. The grid and dedicated panel
windows share that gutter.
Panel #001 always fills the available workspace columns. Every other panel has a
one-column minimum; the first load without a saved layout and Reset use that minimum. Restore saved order and width before packing.
Never prepend or expand a special panel afterward: that would discard the preference
on refresh. Reset reorders existing nodes and expands collapsed panels in place; it
must not navigate, reload projections or clear record selections. Buttons belong in
the left-aligned action row directly beneath each heading, including isolated windows.

The provider overlay uses a current native runtime capability, locally or through
the same-origin local runtime channel. `context` means
preparation; `provider` means the context-bearing request is in flight and a proposal
is awaited; `governance` means the response arrived and is being checked. The outbound
and inbound connector effects distinguish those phases. They do not imply visibility
into network bytes or model cognition. Reduced-motion mode uses static emphasis, and
idle, disconnected and unbound snapshot views cannot display an in-flight provider pulse.

## Inspector and public reading presentation

Panel #014 is the record inspector and the third section in the seven-part story.
Its initial and Reset position is after #013 and before #015 in the same workspace
grid. It has the same drag, resize, collapse and pop-out controls as its peers.
Saved user placement is respected. Selection updates only its content. Grid packing
keeps document order instead of backfilling holes with later story panels.
It does not reserve a side column, float over other panels, or use a special z-index.
On iPhone it does not slide up as a sheet. It stays visible in the story with a
short empty state until a record is selected; selecting a record fills the panel in
place. This keeps the space between #013 and #015 stable while scrolling. Selection
must not scroll or zoom the page to another panel. Check this at phone width as well
as desktop width. The page uses horizontal clipping without creating a body scroll
container. The shared masthead behavior is described below.

The seven story sections (#012–#018) share amber borders, including the static
inspector at #014. Category controls for
#013 belong in its heading action row. Cube rotation is interactive; zoom is not.
Light-mode reading pages must change card backgrounds and text together, including
home hero, topic, discovery, metric and reading surfaces. Do not assume changing
body tokens overrides dark page skins. Verify exported pages in both themes.

With a fresh local activity sample, the process marker follows the reported stage
and historical traveling-dot replay is suppressed. The provider call boundary
reports request-in-flight until response arrival; it cannot distinguish network
upload completion from remote model processing. Hosted static snapshots do not
provide that live capability and must retain their dated interpretation.

## Workspace width and masthead scrolling

Console fills the viewport rather than inheriting reading-page width caps. The
record inspector follows the workspace and never reserves width. The grid counts
available columns instead of applying a fixed large-screen column limit. Other
reading pages may retain their text-column limits.

The shared masthead keeps one compact row. The right-hand controls appear in this
order: status light, theme, GitHub, Console, node selector and main menu. The node
selector always uses the network-node icon with an accessible native dropdown.
The website follows the system light or dark theme until a reader uses the always
visible theme switch. That manual choice persists across pages and overrides
later system changes. At 1100 pixels and below,
or tablet touch screens up to 1366 pixels, page links move into the rightmost main
menu; wider desktop screens retain horizontal page links. Explore opens the main
home page, followed by Research, Journal and Bob’s Blog.

The shared masthead is fixed to the viewport and stays visible at every scroll
position on desktop and phones. Shared navigation reserves its measured height
above content. Its layer is 12000; same-window popup surfaces use 12001. Dedicated dashboard panel windows hide the masthead.
Dark story sections use muted amber borders and a subtle tint;
their layout and durable data remain unchanged.

The shared daylight surface owner is `wake/assets/console-light.css`, despite its
historical filename. It loads after dark page skins through export; cover main-page
cards, help/evidence surfaces and nested reading pages when revising it. Match
geometry across themes and retain signal meaning rather than merely recoloring text.

### Storage format upgrades across installations

Each installation upgrades its own record on the next writable open. Updating source
does not synchronize data. Keep user-stopped containers and Codespaces stopped;
retain their volumes and upgrade them when the operator next starts them. Review
[kernel storage compatibility](kernel.md#physical-storage-and-compatibility) before
rolling an executable backward against an upgraded volume.

## Reader experience and editorial continuity

Reader navigation uses separate static documents: `index.html` (Explore),
`research.html`, `journal.html`, `blog.html`, and the remaining named section pages.
Each document contains only its own view, visible before exported data loads.
Legacy `index.html#section/record` links redirect to the corresponding page;
record fragments stay within that page. GitHub Pages needs no rewrite service.
`report.py` owns page generation and `page-routing.js` owns legacy-link compatibility.
The reader-only `reader-theme.css` uses sudofx's light/dark palette and sans/mono
font stacks without changing page geometry. Console and its embedded components
never load that stylesheet or the reader navigation script. The dark reader
background is plain, with no background image.

The homepage opens with a question, Bob's latest accepted story, and links to
recorded open questions. Bob's reading pages preserve the article's words while
separating a flattened body at numbered citation boundaries and exposing its
Summary, sources and adjacent published stories. RSS is the working follow path;
there is no email collection or follower counter. The Console keeps its own layout.
`wake/assets/pet.js` owns the homepage, `app.js` owns blog reading, and scoped rules
in `theme.css` style those views. The exporter owns `blog.xml` and its installation
links; do not add a follow control without exporting its destination.

Later group articles receive bounded excerpts of the previous accepted publication
and per-member comparisons of the supplied story packets. The prior opening is
limited to 700 characters, ending to 900, and lede to 300. Changes identify versions
and supplied story IDs; these are structural differences, not certified scientific
progress. Current member summaries and reference identities have priority over
older prose under the existing provider input ceiling. Earlier prose is omitted
first, then optional continuity context if necessary. Native invocation receipts
retain the exact delivered request. No separate editorial database is introduced.

Writing guidance asks for a concrete opening, a connected question, an explanation
of meaningful recorded changes, and an unresolved question already present in the
supplied work. It cannot invent a discovery, future commitment or publication date.
Readership interest cannot select projects or qualify evidence. These are design
hypotheses informed by curiosity research, not a claim of measured audience growth. The rationale draws on [Kang et al. (2009)](https://www.cmu.edu/dietrich/sds/docs/loewenstein/WickCandleLearning.pdf)
and [Le Quéré and Matias (2025)](https://www.nature.com/articles/s41598-024-81575-9);
their findings do not establish retention outcomes for this site.

## First-run publication

Grouped installations publish **one model-written Bob article with identical text on every
parent and child**. The elected parent (the first configured parent hostname) obtains a
bounded, dated summary from every member and synthesizes their shared story. A missing
member leaves publication pending. The gateway only transports these summaries and the
result; it has no publication authority. Each member appends its own governed publication
receipt to its authoritative record and exports the article through its normal website
publication path. Worker blog drafts are retained as withheld editorial output; they do
not become separate public voices. Research advances independently of publication.

The gateway's group endpoints admit members from all of that group's parent and
child networks, while rejecting members of other groups. Modern Bob requests use
provider-enforced structured paragraphs: each supplies its prose and an explicit
nonempty list of reference numbers. The model supplies a separate summary. The
versioned `group-editorial-paragraphs@1` renderer adds only citation punctuation,
paragraph breaks and the final Summary heading. It never chooses supporting
stories or supplies missing attribution. The exact provider response and a
hash-bound rendering receipt remain in authority; replay verifies that the
published article follows that transformation. Older body-string responses remain
supported unchanged. Their final heading can also be a sentence-boundary `Summary`
followed by a capitalized summary sentence. Retained drafts are reevaluated with
their exact text; an acceptable draft needs no replacement model call. Markdown
heading and emphasis markers are not rendered.

The shared `group-wake-introduction` identifies WAKE01. On creation the group first
uses one parent model invocation to introduce the initialized records of all members,
even when their accepted research versions are still zero. Children make no research
requests during this startup stage. A legacy failed initial synthesis retains its historical single-attempt rule.
New attributed editorial packets use an independent sequence: the next article is
scheduled three times per 100 aggregate accepted wakes (34, 67, 100, then
134, 167, 200, and so on) across all nodes. The last publication’s captured inputs are the durable watermark.
A missed milestone remains due until publication succeeds; one catch-up article
covers accumulated work without fabricating backdated posts. Failed attempts,
wall time and Bob’s receipts do not count. Research never waits for the article.
All twelve dated exports are required, but members need not advance equally or
have a currently running worker. An unavailable worker's existing exported stories
remain usable with their captured date, head and version. Bob's own
receipts and changing export heads cannot manufacture news. Regressing a member's
research version fails closed for operator review; a reset is never inferred from
an editorial cadence.

Each input supplies attributed story IDs, node/record links, notebook revisions,
dates, recorded claim labels and limitations, plus bounded source URLs. The model
returns paragraph reference numbers pointing to those supplied IDs; the renderer
prints them as `[1]` or `[1, 2]`. Legacy body-string responses can use `[1][2]` or
`[1, 2]` unchanged. References must cover
every member. These structural checks support traceability; they do not prove
semantic entailment or scientific validity. A progress article can explain open
questions, provisional readings, corrections, failures and blockers without the
two-source scientific-result gate. Result publication and project completion keep
their existing rules. No article advances research, writes a journal, moves
Attention or fulfills a commitment.

Write for a curious reader with no specialist vocabulary assumptions: explain
terms when they appear, use clearly labelled everyday analogies, and naturally
explain who, what, where, when, how and why. The final Summary uses especially
simple, short sentences without condescension or a public audience label. These
are writing instructions, not mechanical publication vetoes: informal discovery
phrasing, specialist vocabulary, repeated introductions, sentence lengths and
Summary word counts do not withhold an otherwise traceable article. The final
Summary, valid supplied references covering every member, bounded article fields,
and the boundary against attributing personhood to Bob or WAKE remain required.
Bob’s wording cannot qualify evidence or promote a research claim.

Editorial inference uses the existing native invocation and provider quota
boundary. Article structure and attribution are checked before an editorial
invocation can complete. The provider-facing output schema specifies structure
without nested array cardinalities that can exceed provider grammar capacity.
Supplied source IDs remain explicit enum choices. Local validation still enforces all size limits, exact
supplied source IDs, numeric reference ranges and complete member coverage. Invalid responses finish as visible rejections with their
exact bounded response, reason and draft excerpt, rather than falsely reporting a
completed synthesis. Existing withheld drafts and their reasons remain durable.
Bounded repairs include the failure reason and an excerpt, including after a day
boundary. Modern milestone articles retry at most
once per 15 minutes for the same editorial sequence, including quota deferrals.
There is no three-attempt or six-per-day editorial cutoff that can erase a required
post; native provider budgets and quota controls still apply. Legacy packets retain
their historical capacity rules. Exact retained drafts are reevaluated under the
current rules without another model call; no draft text or historical receipt is
rewritten. The configured provider fallback chain retains its own per-model
accounting and reset schedules. No fabricated Bob fallback fills a quota failure.

`wake-research bob` requests one eligible editorial attempt even while research
is paused. It grants only the leader's editorial provider slot, respects quota,
cadence and capacity, and cannot start research. A later pause/stop cancels that
pending capability. Paused members still import an already accepted shared article.
`wake-research bob --revise 'REASON'` records a digest-bound operator request for
an eligible model-written correction of the current article. It can become due
without new research activity, but never bypasses provider quotas, retry spacing
or structural publication checks. A consumed command cannot repeat after
interrupted export. The new article supersedes the earlier one while retaining its text and invocation.
Writing instructions discourage repeated introductions, overstated discovery wording
and unexplained specialist terms; they do not certify semantic accuracy.
Only the leader advances its editorial sequence one step at a time; other members
can import a later accepted shared article after missing an earlier feed update.
No missing historical article or research transition is fabricated.
Public delivery is documented in [mirror publishing](cloud.md).

For a monitored first-post run, the operator may set
`pause_after_group_introduction: true` alongside `research: "running"` in each
member's local `.wake-runner-control.json` before enabling the batch. Each runtime
consumes this one-use control and pauses immediately after its publication receipt,
before an ordinary research request. Paused members continue importing the shared
article so the entire group can finish publication without additional inference.

The one-time operator exception is limited to the exact digest of the group WAKE01
article. It bypasses that article's editorial gates only, adds no scientific support,
and is consumed once in each member's record. It cannot approve other posts or research
mutations. Normal later articles retain Bob's structural publication and identity boundaries. If a
completed synthesis is withheld, its durable draft and reason are retained; new
attributed articles may receive the bounded repairs described above. To apply an explicitly authorized exception, use the
same saved publication packet in each enrolled, paused member:

```sh
PYTHONPATH=/workspace python /workspace/scripts/wake_group_bob.py --data /data \
  --publication /tmp/reviewed-group-introduction.json \
  --confirm-wake01-exception --reason 'Operator authorized this first group introduction only'
```

Restart the paused local service through its normal container control to regenerate its
complete website after an operator publication. Check the authoritative post and served
blog on every member; an accepted draft or HTTP success alone is insufficient.

The older solo `wake-introduction` local recovery contract remains supported for solo
installations and replay of already accepted welcomes. Grouped runtime enrolls before
research and never substitutes that programmed welcome for group synthesis. Initialization
and pending publication remain separate states. No introductory article is a scientific
finding.

Public mirror publishing is described in [publication](cloud.md).

Zero-cycle reset defaults and first-post pause controls are documented in
[standalone operation](standalone.md) and [first-run publication](#first-run-publication).

Group peer JSON and Bob feeds are exported from the same verified state and head
as each worker's website, then served from its atomic snapshot generation. HTTP
requests do not reopen the growing record. A missing snapshot returns unavailable
rather than reconstructing authority in a request handler. These dated views remain
context and presentation; receivers retain their own governance and records.

To run a local group until its next shared Bob post, set each member’s
`pause_after_group_checkpoint` control to its current shared checkpoint plus one,
then set `research` to `running`. The target is a publication lower bound, not a
requested research cycle: Bob follows the aggregate three-per-100-wake cadence above. Each member pauses
once it durably imports the newer shared post, before another research request.

Public hosted activity streaming is retired. Check the direct GitHub status
observer with `node tests/browser/hosted-status-unit.cjs`. Local runtime observation
retains the same-origin privacy and freshness checks.
