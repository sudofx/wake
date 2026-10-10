# Standalone WAKE✳︎

For multiple independent installations, dynamic ports and optional hostname routing,
see [multiple installations](installations.md). The original single-installation
Compose defaults remain available below.

One installation owns one authoritative record. This Docker mode creates an independent
WAKE with the existing runtime, research application, governance and website. It does
not download the public installation's record or interact with GitHub operationally.
Internet access is needed for live Gemini and public research sources; fixture mode
can run with networking disabled. Passive repository/documentation links remain links.

Before starting research from a fresh checkout, create and edit the local topic file:

```sh
cp example.research-topics.toml research-topics.toml
```

The custom file is ignored by Git for local use. If it is missing, WAKE prints this
command and stops before running research. Docker builds include the local file when
present. Hosted research uses the exact promoted release commit; explicitly add its
topics file with `git add -f research-topics.toml` before committing and promoting it.

## Code and website changes

Follow the [maintainer map](development.md) before updating an existing installation.
Record its image, working directory, source mount and named data volume. Shared
source edits do not transfer research history between hosted and local installations.
The website is regenerated through `wake.report.export` and the standalone publisher;
raw HTML templates are not complete deployment artifacts. A generated installation
identity keeps Console, maps, homepage and status requests on this server even when
accessed through an IPv4/IPv6 LAN address. Missing identity never enables hosted data.
`deployment.json` identifies export mode; snapshot head/version identify displayed data.

For inspection without API calls, preserve the existing Compose project and volume
and recreate with `WAKE_PAUSED=true`. Do not assume an editor overlay reloads imported
Python. Generated website assets refresh through normal publication; rebuild the
standard image when its source changes. Do not manually overwrite generated pages.

## Start

Install Docker Desktop on macOS/Windows and use Linux containers, or install Docker
Engine and Compose on Linux. From this repository:

```sh
cp .env.example .env
# Put your own GEMINI_API_KEY in .env, or export it in your shell.
docker compose up --build -d
docker compose logs -f wake
```

Open `http://localhost:8080`. Check the model names, quota limits, topics and billing
confirmation in `wake.toml` for your own Gemini project before live operation. The
first start creates `/data/wake.sqlite` in the Compose project's `wake-data` named
volume. No API key enters the image, website or record. The image's build context is
an allowlist excluding `.env`, local databases, Git metadata and hosted machinery.

For an offline systems rehearsal, set `WAKE_PROVIDER=fixture` in `.env` and start as
above. Fixture proposals are simulated. Set `WAKE_PAUSED=true` to serve and inspect
without inference. Changes to environment settings require container recreation:

```sh
docker compose up -d --force-recreate
```

`WAKE_INTERVAL_SECONDS` defaults to 60 seconds between bounded cycles, with durable
quota deferrals respected. `WAKE_MODEL` optionally overrides the primary model.
`WAKE_PORT` changes the host port. Compose publishes on all host network interfaces
by default, including the Mac's LAN address. The read-only website is not an
authenticated remote service.

## Access from an iPhone or another device on the local network

Connect the iPhone to the same local network as the host and open
`http://MAC_LAN_IP:8080/console.html` in Safari. Find the Mac's LAN IPv4 address
in System Settings under Network or Wi-Fi. Keep the existing Compose project name
and volume when recreating an existing installation:

```sh
docker compose -p wake-standalone-preview up -d --force-recreate
```

For the VS Code setup, also include `-f compose.vscode.yaml`. That editor overlay
defaults to paused mode; preserve your live provider and pause settings when
recreating an existing installation. Port changes require recreation.

`compose.lan.yaml` remains available for older checkout instructions but is no longer
needed. The website is read-only and unauthenticated; use it on a trusted network
without opening router ports. Host firewall rules and Wi-Fi client isolation can
affect access.

## Continuity matrix campaign

The 7×7×7 continuity cube is opt-in for each independent installation. Accepted
research cycles alone do not enable it. Set `WAKE_ENABLE_CONTINUITY_MATRIX=true`
in `.env` and recreate the container using the same Compose project and data volume,
or pass `--enable-continuity-matrix` to the standalone launcher. Startup audits and
recovers the existing record before submitting the governed enablement action.
Repeated starts preserve campaign results without recording another enablement.

To enable an already running installation without restarting or calling a model:

```sh
docker compose exec wake python -m wake --data /data enable-continuity-matrix
```

The command shares the writer lock; retry between cycles if it is busy. Enablement
is durable: removing the setting does not disable or reset the campaign. Paused mode
can enable and display it but never runs probes. Each ordinary answered provider
invocation scores one cell as a sidecar, including rejected research responses;
timeouts and quota deferrals leave the cell pending. The website projects recorded
progress after the cycle. No separate scheduler or extra provider call is needed.

Custom config and topics may be mounted read-only over `/app/wake.toml` and
`/app/research-topics.toml`. Mount both when changing relative topic-file paths.
The image runs as UID/GID 10001; bind-mounted data directories must be writable by
that user. Named volumes acquire the image's data-directory ownership automatically.

## Open the installation in VS Code

With the Dev Containers extension installed, add the optional editor overlay while
keeping the same Compose project name as your existing installation:

```sh
docker compose -p wake-standalone-preview -f compose.yaml -f compose.vscode.yaml up -d --build
```

The current local preview uses `wake-standalone-preview`. Substitute your own existing
project name for another installation; changing that name selects a different data volume.
This overlay keeps research paused and omits the provider credential. It mounts the
local repository at `/workspace` and a persistent, writable VS Code home at `/home/wake`.
Its optional `vscode` image target includes Git and the OpenSSH client and trusts only the `/workspace` bind
mount for Git ownership checks. The default standalone image omits editor tools.
The authority remains `/data/wake.sqlite`; the rest of the image stays read-only.

In VS Code, open the Command Palette and choose **Dev Containers: Attach to Running
Container…**, select `wake-standalone-preview-wake-1`, then open `/workspace`.
Edits there persist in your local repository. `/app` is the packaged image copy.
The overlay sets the working directory to `/workspace`, so `python -m wake.standalone`
imports that mounted source tree. The standard image runs its packaged copy from `/app`.
Confirm the actual imported path before testing. Restart the editor-mode process to
load Python changes; rebuild for dependency or packaged-image changes. Attach again after
recreation if the editor connection closes.

VS Code copies the host Git identity configuration and can forward the host SSH agent.
Use the VS Code integrated terminal for SSH Git operations; ordinary `docker exec`
sessions do not automatically receive the forwarded `SSH_AUTH_SOCK` environment.
Private keys are not mounted or baked into the image. The host agent must have your
GitHub key loaded. Normal SSH host verification still applies on the first connection.

Use both Compose files for subsequent editor-mode operations. To return to the ordinary
runtime, recreate using only `compose.yaml` and explicitly select paused or live mode.
The source mount and editor home are omitted while the same data volume is retained.

## Runtime secret file

The default Compose file passes `GEMINI_API_KEY` at runtime. Alternatively use a
Compose override (stored locally) with a Docker secret:

```yaml
services:
  wake:
    environment:
      GEMINI_API_KEY: ""
      GEMINI_API_KEY_FILE: /run/secrets/gemini_api_key
    secrets:
      - gemini_api_key
secrets:
  gemini_api_key:
    file: ./secrets/gemini_api_key.txt
```

Keep the secret file outside version control, then pass both Compose files with `-f`.
The runtime refuses simultaneous nonempty environment and file credentials. Never
supply credentials as build arguments. Docker's [Compose secrets documentation](https://docs.docker.com/compose/how-tos/use-secrets/)
describes mounted runtime secrets.

## Stop, recreate and audit

```sh
docker compose exec wake python -m wake --data /data audit
docker compose down
docker compose up -d
docker compose exec wake python -m wake --data /data audit
```

`down` preserves the volume. **`down --volumes` deletes your local record.** Keep the
same Compose project name and volume when recreating or upgrading. A new project
name selects a new independent volume. Never run two schedulers against one volume.
Never mount or import the hosted checkpoint as this installation's live authority.

Every startup audits existing authority, recovers unfinished automatic invocations
through the native engine, and retains exact history. Manual proposals require explicit
completion or recovery. An absent database in a used volume is an error; the runtime
will not quietly replace lost history. Stop drains the bounded cycle; forced termination
may leave an invocation for native recovery on the next start.

## Operator commands and backup

Use the existing CLI inside the container:

```sh
docker compose exec wake python -m wake --data /data status
docker compose exec wake python -m wake --data /data focus 'Review the evidence' --reason 'Operator review'
docker compose exec wake python -m wake --data /data backup /tmp/operator-backup.sqlite
docker compose cp wake:/tmp/operator-backup.sqlite ./wake-backup.sqlite
```

Commands share the native writer lock. If a cycle owns it, retry between cycles or
recreate with `WAKE_PAUSED=true` first. The paused website refreshes at the configured
interval. Copy the temporary backup out before removing the container: `/tmp` is disposable.
Keep backups off the live volume; multiple `*.sqlite` authority candidates deliberately
fail closed. To restore, stop the installation, place the verified
backup as `wake.sqlite` in its volume with UID/GID 10001 ownership, then start and audit.

For independent truncation detection, retain the website's `head.txt` and
`events.jsonl` exports outside the volume. A chain audit alone cannot detect deletion
of an otherwise valid historical suffix without an independently retained head.

## Portable images and offline acceptance

The Dockerfile targets Linux without a fixed CPU architecture. Build both targets:

```sh
docker buildx build --platform linux/amd64,linux/arm64 --tag wake-standalone:local --load .
python3 scripts/test_container.py
```

The acceptance script runs both images with **`--network none`**, uses uniquely named
test volumes, kills/removes/recreates containers, verifies an unchanged head while
paused, resumes work, checks the exact event prefix and audits continuity. It also
checks that authority and secrets cannot be fetched through the website. Only its own
test resources are removed.

Multi-platform loading requires a compatible image store, as described in Docker's
[multi-platform build documentation](https://docs.docker.com/build/building/multi-platform/).
For a transferable OCI archive, use a docker-container builder and
`--output type=oci,dest=wake-standalone.oci.tar` instead of `--load`. A registry release
may use `--push` to a registry you choose; neither registry publication nor hosted
runtime promotion is part of local container operation.

## Repository convenience launcher

`./scripts/wake_runner` creates and starts the default `wake` container when it is
absent. It publishes the container on a random host port across host network
interfaces and prints its local and LAN URLs when available;
the suggested `/etc/hosts` entry lets that URL use the container name, such as
`http://wake:8088/`. If the container already exists, the runner leaves it as-is
and reports its research state and continuity progress. `./scripts/wake_runner.sh`
is an equivalent entry point. A named invocation such as
`./scripts/wake_runner wake-dev` follows the same create-if-missing,
report-if-present behavior.
Pass `--paused` when creating a solo container or group to make the website
available without starting research. The flag affects new containers only.

New containers are enrolled in continuity@1 by default. Pass `--campaign none`
when creating a container to omit that enrollment, for example
`./scripts/wake_runner wake-dev --campaign none`. Enrollment cannot be changed by
this runner after creation. Campaign progress is still reported for existing
containers.

When creating a new container, `wake_runner` copies any existing host files from
`~/.bashrc`, `~/.gitignore`, `~/.bash_profile`, `~/.profile`, `~/.bash_aliases`
and `~/.inputrc` into that container's `/home/wake` volume. Missing files are
skipped. This is enabled by default for solo containers and each newly created
group member. Use `--dotfiles=false` (or `--no-dotfiles`) to skip the copy, for
example `./scripts/wake_runner wake-dev --dotfiles=false` or
`./scripts/wake_runner wake.local --count 3 --dotfiles=false`.
`--dotfiles false` is also accepted. This only applies when a container is
created; invoking the runner for an existing container leaves its home volume
unchanged.

Explicit research actions are available as
`--research stop|start|pause|reset|status [container-name]`. These control the
research scheduler while keeping the Docker container and Console available.
Research reset asks the operator to type the container name and starts a new WAKE
generation at zero while preserving append-only history and continuity results.
Container lifecycle is separate: `--container stop|start|pause|remove
[container-name-or-group]`. `remove` deletes the selected container(s) and any
unshared attached Docker data volumes. A group prefix selects its
`001.PREFIX` through `NNN.PREFIX` members when no exact container has that name.

Supplying `--count` makes the positional name a group prefix and requires that
name. For example, `./scripts/wake_runner wake.local --count 3` creates the
`000.wake.local` proxy and Docker containers named `001.wake.local` through
`003.wake.local`, each with an independent volume and a Docker-assigned host
port. The reserved `000.wake.local` hostname opens a directory of numbered members. The
runner creates a private
user-defined Docker bridge for that prefix and sets group membership only on
these numbered containers.
Members exchange bounded, readable source observations and one concise,
attributed notebook finding from each peer.
Each recipient records an imported source locally with its original source URL and
peer provenance, then applies its own source eligibility and claim rules before it
can be cited. A peer notebook finding is an attributed lead, not a local claim or
citation ID. Full notebooks, topic lists, projects and record authority are not
shared, and no prompt prescribes a connection to find. The exchange uses the local
Docker bridge and adds no provider call. The bridge trusts its operator-created
members; it is not cryptographic remote attestation. Every member keeps its own
`/data` record. Solo runner containers, Compose installs, Codespaces and hosted
research do not participate. The numbered sites in a local group show one Bob
feed assembled from posts in every reachable member. Research and durable records
remain independent per member. The feed skips unavailable members and is only a
display path; it does not gate a member's own research loop.

By default all members use the shared `research-topics.toml`. To give members
different topics, create files before creating the group, for example:

```sh
mkdir -p .wake-runner-topics
cp example.research-topics.toml .wake-runner-topics/001.wake.local.toml
cp example.research-topics.toml .wake-runner-topics/002.wake.local.toml
cp example.research-topics.toml .wake-runner-topics/003.wake.local.toml
```

Edit each numbered file before launching. The runner mounts a matching file
read-only into that member. If a matching file is absent, that member uses the
shared `./research-topics.toml`; the runner requires that shared file before it
creates containers. The `000.wake.local` proxy listens on host port 80 across network
interfaces, so port 80 must be available. For Mac browser access by group hostname,
add the following line to the Mac's `/etc/hosts`:

```text
127.0.0.1 000.wake.local 001.wake.local 002.wake.local 003.wake.local
```

Then open `http://000.wake.local/` for the proxy's member directory, or open
`http://001.wake.local/`, `http://002.wake.local/` or
`http://003.wake.local/` directly. `wake_runner` prints the suggested
`/etc/hosts` line, local URLs and Mac LAN URLs. On an iPhone connected to the same
network, open the printed `GROUP PROXY LAN URL`; the gateway serves member buttons
that point directly to the Mac's LAN address and each member's published port. If
the gateway is opened by its group hostname from another device, it compares the
requesting device's IP with the Mac's LAN IP and uses those same direct links for
remote devices. The `/etc/hosts` line only configures the Mac; the iPhone can use the
printed numeric LAN URL unless local DNS provides the group hostname.
One router serves all active groups; it blocks requests between different group
networks. Group networks are removed when their last member is removed. The runner
requires the existing `wake-standalone:vscode` image and selects the Docker Desktop
proxy; it is not the portable Compose setup above. These websites are read-only and
unauthenticated; use them on a trusted network without opening router ports. Only
the explicit `--container remove` action deletes attached data volumes.

## Live Console inspection

The current runtime serves optional activity metadata at `/runtime.json`: record,
context, evidence collection, provider wait, governance, continuity evaluation,
receipt and idle. It advertises `capabilities.live_activity` and an activity schema;
older runtimes need not implement the channel. The endpoint is inspection-only.

Console checks this endpoint every three seconds while visible. Panel #002 reports
the current phase separately from its historical replay. Panel #003 outlines the
exact cell delivered with an active probe; selecting a different cell does not
move that indicator. A phase can finish between polls and may never be displayed.
The pulse stops on idle, failed work, missing capability, connection failure or
sample expiry; it is static under reduced-motion preference. Publication-generation
changes trigger snapshot refresh, including rejected attempts whose accepted-cycle
count did not advance. This still uses atomic complete exports, not mutable pages.

Use an updated installed image to get the activity endpoint. Updating assets alone
cannot add runtime telemetry to a running Python process. Container acceptance now
runs the installed package outside `/app`, so checkout-only asset availability
cannot hide wheel omissions.

## Codespaces and Dev Containers

The committed `.devcontainer/devcontainer.json` builds the optional `vscode`
target of the same Dockerfile. Use **Code → Codespaces → Create codespace** on
the reviewed branch, or **Dev Containers: Reopen in Container** locally. The
lifecycle starts a paused preview on port 8080 and opens the forwarded port.
Keep Codespaces port visibility private; forwarded URLs are managed by GitHub,
not by WAKE. See [GitHub's port-forwarding guidance](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace).

This is a new independent development installation. Source is imported from the
mounted checkout. Its record is `data/devcontainer/record/wake.sqlite`, not the
image's `/data`, a local operator volume, or `wake-state`. Its generated pages
read same-origin data. The lifecycle uses the fixture provider and explicitly
pauses research, even if provider credentials exist in Codespaces. Opening or
rebuilding the editor does not run paid or unattended research.

`scripts/dev_preview.py start` is idempotent: it recognizes its process by command,
working directory and Linux process start-time. `python scripts/dev_preview.py stop`
drains only that preview and retains the record. Stop and start after Python
changes to import the updated source and regenerate pages. A custom local port
can be selected with `start --port PORT`; update the forwarded port correspondingly.
An occupied port is an error, not evidence that WAKE launched.

The ignored `data/` directory survives an editor-container rebuild with the same
workspace. Deleting a Codespace deletes that workspace's local data; export and
retain records separately before deletion when they matter. No lifecycle imports
hosted checkpoints or pushes/restarts hosted research. Authentication, billing,
Codespaces creation and the forwarded-domain access remain GitHub responsibilities.

If your development network requires a build proxy, supply the usual `HTTP_PROXY`
and `HTTPS_PROXY` environment variables when invoking the Dev Containers tool.
The configuration forwards them as build arguments; it contains no machine-specific
proxy address. The runtime preview does not depend on that build transport.

For local configuration acceptance, run the Dev Containers CLI `up` against this
checkout, then verify `/runtime.json` reports paused, the exported installation
identity is standalone, the source import points into the mounted checkout, and
stop/start preserves the exact record head. This proves the container and lifecycle;
a cloud Codespaces launch additionally verifies GitHub's workspace and forwarding.

After `up`, the repository's lifecycle acceptance check runs in that same container:

```sh
npx @devcontainers/cli exec --workspace-folder . python scripts/test_dev_preview.py
```

It checks source identity, repeated launch, PID reuse protection, paused readiness,
port collisions, a changed port, exact record preservation and zero provider
invocations. It leaves the paused preview ready; stop it or close the development
container after verification, retaining the workspace data.

## Automatic execution recovery

Standalone launches a supervising parent and a record-owning worker on Docker,
Codespaces and ordinary supported hosts. An unexpected worker signal or explicitly
temporary operating-system error restarts the worker with increasing delays.
After five restarts in fifteen minutes, recovery waits for that window to expire.
Each worker reopens and verifies the same record and recovers interrupted invocation
receipts before any provider effect. The supervisor never repairs or resets data.
Normal shutdown, intentional pause, configuration errors and integrity failures
are not retryable worker outcomes. Docker's own restart policy may relaunch a
failed container; record verification still fails closed before inference.

If mandatory context still exceeds its ceiling after safe excerpting, an optional
continuity sidecar may be deferred. Delivery receipts identify the coordinate and
recovery reason; no result is recorded and that coordinate remains next. Coverage
can therefore lag research under budget pressure. This preserves research policy,
mandatory records and source roots; an irreducibly oversized request still blocks
before inference rather than dropping obligations or inventing progress.

Permanent provider failures keep the read-only Console available in blocked state.
Known transient outcomes remain deferred and retry through normal eligibility; an
invalid credential or unsupported model must not generate another call every loop.
