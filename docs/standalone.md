# Standalone WAKE✳︎

For multiple independent installations, dynamic ports and optional hostname routing,
see [multiple installations](installations.md). The original single-installation
Compose defaults remain available below.

One installation owns one authoritative record. This Docker mode creates an independent
WAKE with the existing runtime, research application, governance and website. It does
not download the public installation's record or interact with GitHub operationally.
Internet access is needed for live Gemini and public research sources; fixture mode
can run with networking disabled. Passive repository/documentation links remain links.

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
`WAKE_PORT` changes the host port. Compose binds only the host loopback interface.
The read-only website is not an authenticated remote service.

## Access from an iPhone or another device on the local network

Add `compose.lan.yaml` to publish the website on the host's IPv4 and IPv6 addresses
(Docker Compose 2.24.4 or newer). Keep the existing project name and volume:

```sh
docker compose -p wake-standalone-preview -f compose.yaml -f compose.lan.yaml up -d
```

For the VS Code setup, also include `-f compose.vscode.yaml` before the LAN override.
That editor overlay defaults to paused mode; preserve your live provider and pause
settings when recreating an existing installation. Port changes require recreation.

Connect the iPhone to the same network, then open `http://HOST_IPV4:8080/console.html`
or `http://[HOST_IPV6]:8080/console.html` in Safari. IPv6 literals require brackets.
Use the host's network address rather than the container's internal address.
Host firewall rules and Wi-Fi client isolation can affect access. The website
remains read-only and unauthenticated, and this override listens on all host
interfaces; use it on a trusted network without opening router ports.

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

`./scripts/wake_runner wake` recreates the named editor container using the existing
`wake-standalone:vscode` image and the established preview volume. It executes the
mounted repository, forces live research and matrix enablement, and exposes LAN
port 8080. It also selects a Docker Desktop proxy; inspect that transport before
using it outside that environment. It is not the portable Compose setup above.
Normal invocation retains the data and editor-home volumes. `--reset` permanently
deletes the selected data volume and requires explicit history-loss authorization.
