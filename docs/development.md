# Maintainer map

Use [kernel development](kernel.md) for the application seam and
[multiple installations](installations.md) for parallel container operation.

This is the entry point for changing WAKE safely. The repository owns executable
behavior; installations own independent records. A shared source tree does not
imply a shared database, execution process, deployment, or provider quota ledger.
Read [architecture](architecture.md) for invariants, [hosted operation](cloud.md)
for GitHub, and [standalone operation](standalone.md) for Docker.

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
| CLI and installation | `wake/__main__.py`, `wake/standalone.py`, Compose files, `scripts/wake_runner` | Explicit initialization; preserve selected volume; one scheduler |
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
Tapping the activity light shows its explanation. Status remains installation-specific
and read-only. Running is green, paused is yellow, unavailable is neutral; waiting and
blocked states have distinct accessible descriptions. Interactive canvases and drag
controls suppress selection, while record inspectors and reading text remain selectable.

## Console layout and provider phases

All numbered panels use the same workspace grid, including overview and inspection.
The outer Console gutter is 20 px on each side, or 10 px on iPhone. The grid,
docked inspector and dedicated panel windows share that gutter.
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

A populated Console inspector docks only while it remains in the main workspace.
Its pop-out handshake releases the desktop width reservation; closing the pop-out
restores it. Unpopulated inspectors remain ordinary grid modules. Desktop height
resizing is presentation state only. Phones use a lower sheet, and selecting a
record scrolls the invoking control into the unobstructed upper area. Test the sheet
with a mobile browser context and hit testing, not only resized desktop geometry.
The page uses horizontal clipping without creating a body scroll container, so
viewport-sticky navigation can return when scrolling upward.

The seven story sections (#012–#018) share amber borders. Category controls for
#013 belong in its heading action row. Cube rotation is interactive; zoom is not.
Light-mode reading pages must change card backgrounds and text together, including
home hero, topic, discovery, metric and reading surfaces. Do not assume changing
body tokens overrides dark page skins. Verify exported pages in both themes.

With a fresh local activity sample, the process marker follows the reported stage
and historical traveling-dot replay is suppressed. The provider call boundary
reports request-in-flight until response arrival; it cannot distinguish network
upload completion from remote model processing. Hosted static snapshots do not
provide that live capability and must retain their dated interpretation.

## Workspace width and directional masthead

Console fills the viewport rather than inheriting reading-page width caps. Only a
populated, in-page desktop inspector reserves width; popping it out restores the
entire workspace. The grid counts available columns instead of applying a fixed
large-screen column limit. Other reading pages may retain their text-column limits.

The shared masthead spans the viewport. Sticky flow space prevents content jumps:
downward scroll hides it, upward scroll reveals it above inspection overlays.
Keyboard focus and open navigation menus keep it accessible; reduced motion removes
sliding animation. Phone inspection must reserve its height even while hidden,
since upward movement reveals it again. Dark story sections use muted amber borders
and a subtle tint; their layout and durable data remain unchanged.

Private collaboration structure and artifact completion rules are in
[the workbench guide](workbench.md). That guide deliberately describes structure,
not the contents of any installation's private notes.

The shared daylight surface owner is `wake/assets/console-light.css`, despite its
historical filename. It loads after dark page skins through export; cover main-page
cards, help/evidence surfaces and nested reading pages when revising it. Match
geometry across themes and retain signal meaning rather than merely recoloring text.

A modular inspector reserves width at the workspace boundary only; legacy reader
padding is scoped to nonmodular views. Verify the grid content edge as well as the
outer workspace width when testing dock, pop-out and restore. Dedicated panel
windows omit the site masthead and fit their reader inside the window frame;
window resizing replaces in-page position and size controls.
