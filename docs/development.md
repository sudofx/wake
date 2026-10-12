# Maintainer map

Use [kernel development](kernel.md) for the application seam and
[multiple installations](installations.md) for parallel container operation.

This is the entry point for changing WAKE safely. The repository owns executable
behavior; installations own independent records. A shared source tree does not
imply a shared database, execution process, deployment, or provider quota ledger.
Read [architecture](architecture.md) for invariants, [hosted operation](cloud.md)
for GitHub, and [standalone operation](standalone.md) for Docker.

Before changing anything, answer three questions:

1. **Which installation are you changing?** Local Docker, Codespace and hosted
   WAKE have separate records and processes.
2. **Which code is actually running there?** A checkout, mounted workspace and
   packaged image can all contain different versions.
3. **What are you authorized to change?** Editing, committing, pushing, promoting
   hosted code and resetting research data are separate actions.

If you only need the key terms, use the [glossary](glossary.md). If you need a
release procedure, go to [hosted operation](cloud.md#authority-maintenance).

## Establish the target before editing

Record the checkout's remote, branch, HEAD and existing changes. Identify whether
it is the intended repository, a bind-mounted checkout, an installed package, or a
reference mirror. Preserve existing edits. Inspect the actual process command,
working directory, image and mounts before assuming which source executes.
`python -c 'import wake; print(wake.__file__)'` reveals the imported package in that
execution environment. Do not print environment variables or container secrets.

For hosted changes, inspect the current GitHub refs and workflows rather than
assuming local remote-tracking refs are current. For standalone changes, identify
the container and its exact data volume before recreation. A container name, an
IP address, and an image tag can change; none identifies a record by itself.

| Surface | Executable source | Authority | Presentation |
| --- | --- | --- | --- |
| Hosted research | Exact promoted `wake-runtime` commit | `wake-state/data/wake.sqlite.gz`, restored as `wake.sqlite` | `wake-live` projections |
| GitHub Pages | Generated shell from `master` | None; reads public views | Pages artifact, independent of research promotion |
| Standard Docker | Image package under `/app` | Selected volume at `/data/wake.sqlite` | Atomic temporary website generations |
| VS Code overlay | Bind-mounted `/workspace` because it sets working directory there | Same selected `/data` volume | Local export, never hosted fallback |
| Codespaces / Dev Container | Mounted workspace source | Checkout `data/devcontainer/record/wake.sqlite` | Paused same-origin preview, private forwarded port |
| CLI / offline fixtures | Imported package in the invoking environment | Explicit `--data` directory | Exported directory |
| Public preview helper | Local assets, public GitHub projections | None | Deliberate mirror of hosted data |

These rows may share code while retaining different histories. Equal cycle counts
are not evidence of shared authority; unequal counts are not a synchronization
failure. Never replace a standalone record with the hosted checkpoint to make its
screen match. Restore or migrate a record only through a separately authorized,
verified operation.

## Source ownership

| Change | Start here | Protected boundary |
| --- | --- | --- |
| CLI and installation | `wake/__main__.py`, `wake/standalone.py`, `runtime_supervisor.py`, Compose files, `scripts/wake_runner` | Explicit initialization; preserve selected volume; one scheduler |
| Hosted lifecycle / persistence | Operator workflows, `scripts/github_wake.py`, `scripts/publish_pages.py` | Drain before promotion; durable reservation before provider effect |
| Record adoption / domain bridge | `wake/authority.py`, `record_store.py`, `application.py`, `domain_events.py`, `event_format.py` | One writable authority; immutable historical meaning and hashes |
| Generic record/runtime | `wake/kernel/` | Deterministic receipt, replay, access and invocation contracts |
| Research orchestration / context | `engine.py`, `prompts.py`, `memory.py`, `retrieval.py`, `trust.py`, `attention.py` | Derived context cannot rewrite record or waive obligations |
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
`WAKE_DEPLOYMENT` before reader scripts in generated pages. Only schema 1 with
mode `hosted` permits public GitHub transport. Standalone mode reads same-origin
JSON and `/runtime.json`, including through LAN addresses. A missing/invalid
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
local scheduler endpoint, so runtime status may be unavailable. The deliberate
hosted preview is different: build its shell with `scripts/publish_pages.py`, then
use `scripts/preview_research.py`. The helper rejects standalone directories.

## Codespaces access and preview

The committed Dev Container starts an independent, paused preview on port 8080.
Keep the forwarded port private; it contains this workspace's disposable local
view, not the hosted research record. Do not populate its record from `wake-state`.
A Codespace must execute the mounted checkout, including uncommitted development
changes, rather than an older image package.

The editor-only Dev Container includes the standard SSH feature for GitHub CLI
maintenance. It does not add an SSH service to the standalone runtime image.
GitHub CLI access to Codespaces requires the `codespace` scope. If listing or
creating a Codespace reports missing scope, use
`gh auth refresh -h github.com -s codespace` and complete the browser authorization.
An existing repository permission does not imply this account-level permission.
Use the smallest suitable machine, set an idle timeout, and stop a development
Codespace when finished. Container validation on another machine does not prove
cloud build, startup, source mounting or port forwarding; verify those in the
actual Codespace before claiming that environment works.

### Managed research in a Codespace

The lifecycle starts a paused fixture preview for a new installation. Use
`python scripts/dev_preview.py research` to drain that preview and start supervised
Gemini research on the same independent record (requires the existing Codespace
secret). Use `python scripts/dev_preview.py pause` for read-only inspection or
`python scripts/dev_preview.py stop` to stop the service. Research intent survives
an environment restart only after that explicit command; Stop removes it and the
next lifecycle starts paused. Normal idle shutdown is a Codespaces platform limit,
not a recoverable process failure; no agent silently upgrades machines or defeats
that limit. Worker recovery remains bounded and never resets the record.

## Release and restart boundaries

Local source edits do not publish GitHub. A push to `master` may immediately deploy
Pages because of path filters, but research remains on `wake-runtime`. An image
rebuild does not promote hosted code. Editing a bind mount changes that checkout;
already imported Python does not automatically reload, and a published website
retains its generation until the next export. Restart the intended process through
its supported operator path, retaining the data volume.

Prepare and test the candidate first. When hosted publication is authorized,
use **Stop**, wait for real research jobs to drain, push the candidate, then use
**Restart**. Verify candidate CI, exact promoted SHA, successful restart, continuation
latch and a new research attempt. Verify its terminal receipt and accepted progress
separately: a green job may record a rejection or quota deferral. Do not start or
stop other installations as a side effect of a release.

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
| `docs/cloud.md` | Canonical hosted controls, transport and recovery |
| `docs/standalone.md` | Docker, LAN, editor, volume and backup operations |
| `docs/retrieval.md` | Memory delivery, omissions and replay-seed guarantees |
| `docs/experiment.md` | What observations mean and how to compare them |
| `.workbench/validation/*.md` (local, ignored) | Dated evidence; preserve historical results |

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

The provider overlay uses current local runtime capability only. `context` means
preparation; `provider` means the context-bearing request is in flight and a proposal
is awaited; `governance` means the response arrived and is being checked. The outbound
and inbound connector effects distinguish those phases. They do not imply visibility
into network bytes or model cognition. Reduced-motion mode uses static emphasis, and
idle/disconnected/hosted snapshot views cannot display an in-flight provider pulse.

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

The shared masthead is fixed to the viewport and stays visible at every scroll
position on desktop and phones. Shared navigation reserves its measured height
above content. Its layer is 12000; same-window popup surfaces use 12001. Dedicated dashboard panel windows hide the masthead.
Dark story sections use muted amber borders and a subtle tint;
their layout and durable data remain unchanged.

Private collaboration structure and artifact completion rules are in
[the workbench guide](workbench.md). That guide deliberately describes structure,
not the contents of any installation's private notes.

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

## First-run publication and Passenger

Grouped installations publish **one model-written Bob article with identical text on every
parent and child**. The elected parent (the first configured parent hostname) obtains a
bounded, dated summary from every member and synthesizes their shared story. A missing
member leaves publication pending. The gateway only transports these summaries and the
result; it has no publication authority. Each member appends its own governed publication
receipt to its authoritative record and exports the article through its normal website
publication path. Worker blog drafts are retained as withheld editorial output; they do
not become separate public voices. Research advances independently of publication.

The gateway's group endpoints admit members from all of that group's parent and
child networks, while rejecting members of other groups. Bob requests provider-enforced article fields, with the Summary inside the body string.
He writes plain paragraphs for the existing blog renderer; Markdown heading and emphasis markers are not rendered.

The shared `group-wake-introduction` identifies WAKE01. On creation the group first
uses one parent model invocation to introduce the initialized records of all members,
even when their accepted research versions are still zero. Children make no research
requests during this startup stage. A failed initial synthesis requires operator repair
and a fresh group; it is not automatically retried. Research starts after publication,
unless the operator pauses the group at this checkpoint. Subsequent group reflections use
the existing stable 15–20 wake quiet window after the shared checkpoint, once every member
has reached it. The article records its checkpoint separately from each member's research
version and publication time. Synthesis and publication do not add research cycles,
journal entries, scientific evidence, notebooks, Attention moves or continuity results.
Public synthesis uses the native invocation lifecycle and the ordinary provider quota;
its bounded input and exact response remain auditable. Passenger is excluded.

For a monitored first-post run, the operator may set
`pause_after_group_introduction: true` alongside `research: "running"` in each
member's local `.wake-runner-control.json` before enabling the batch. Each runtime
consumes this one-use control and pauses immediately after its publication receipt,
before an ordinary research request. Paused members continue importing the shared
article so the entire group can finish publication without additional inference.

The one-time operator exception is limited to the exact digest of the group WAKE01
article. It bypasses that article's editorial gates only, adds no scientific support,
and is consumed once in each member's record. It cannot approve other posts or research
mutations. Normal later articles retain Bob's publication and language gates. If a
completed synthesis is withheld, its durable draft and reason are retained instead of
paying for repeated model calls. To apply an explicitly authorized exception, use the
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

Passenger is a private Markdown workspace for operational observations and inert
change proposals. Its logical interface is `./.passenger.md`, resolved relative
to the explicit installation storage root, never the process working directory.
It is available only inside containers. Solo images use `/data/passenger`; solo
runner nodes use their explicit `/passenger` volume. A named runner group uses
`/workspace/.passenger.md`, which is the actual `.passenger.md` in its host project
root. All parents and children share that document with identity `group-GROUP`.
Independent installations need separate project/storage roots; the persisted
identity rejects accidental reuse. Existing containers retain their original
mapping until explicitly upgraded or recreated while preserving their records.
Never use the runner's container `remove` command for a record-preserving upgrade.

The first successfully exported introductory article appends a factual initialization
receipt with its publication provenance and member heads. This gives the private
file meaningful contents without an extra model call. It is explicitly labelled
as durable facts, not a model assessment or scientific finding. A retry is idempotent;
an operator reset prevents an old publication from restoring cleared text.

Initialization creates an empty document if absent and preserves existing text.
Bob may append observations or add a correction naming an earlier assessment.
Code snippets remain text. File writes use a shared-volume lock, atomic replace
and a one-second contention limit; failures are reported without private content
and never fail primary research. The whole document is limited to 1 MiB, model
context to the last 4,000 characters, and each response to 12,000 characters/three
observations. No automatic compaction erases earlier assessments. A full or
malformed document needs a human decision, not an autonomous cleanup.

Sparse advisory assessments run after accepted research at most once per 15
accepted cycles. They use the existing provider adapter, quota accounting,
pause gate and native durability barrier. They add an occasional model call;
creation needs none, and no update is required each cycle. Private input and
output stay in memory/the advisory volume; the public record retains only a
redacted invocation and outcome. They never share model context with public
research/blog generation. This separation prevents stored advisory instructions
from becoming public content or execution authorization.

Only an explicit human command exposes intentional reset:

```sh
docker exec 100.wake python -m wake passenger-reset --confirm
```

Reset advances a persisted generation before clearing the document. Recovery
finishes an interrupted reset, and an older in-flight assessment cannot restore
cleared text. Operator and developer edits should preserve history; developers
have no separate reset authority. The model contract contains append-only data,
no reset/delete/execute operation or filesystem tools. This is the repository's
human-command authority boundary, not an operating-system restriction on humans
who already have Docker/filesystem access.

Passenger is ignored by Git, excluded from image contexts and frozen source
copies, absent from public exports and blocked by the standalone web handler.
It is not served by the group peer endpoints. Treat its text as lower-trust
advisory data, never policy or instructions. No reset, recommendation or proposed
patch changes the research record, source code, credentials or deployment.

Hosted fresh resets and public Bob prose are described in [hosted operation](cloud.md#fresh-hosted-reset).
