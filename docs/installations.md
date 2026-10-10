# Multiple independent installations

Each installation has its own record, secrets, configuration, and lifecycle.
The same source checkout may build many installations. GitHub hosted research is
another independent installation; matching versions do not imply matching data.
No container needs GitHub Pages, Actions, public snapshots, or another project.
External AI access is needed only when an external provider is selected.

## Compose projects own installation identity

Requires Docker with Compose 2.24.4 or newer, on a Linux container engine
(including Docker Desktop on macOS or Windows). Native ARM64 and AMD64 image
execution is supported by the Dockerfile; other architectures and alternative
engines need their own acceptance evidence. Do not assume a cross-build proves
runtime operation.

Use a distinct **stable** project name for each installation. Reusing the name
reuses its record volume; changing it creates a different installation. The
`compose.instances.yaml` overlay keeps per-project image tags, asks Docker for
an available port, and starts paused with the offline fixture provider. Its
`WAKE_INSTANCE_*` variables deliberately ignore the checkout's usual provider
credentials and pause controls.

From the repository root:

```sh
docker compose --env-file deploy/instances.env.example -p wake-alpha -f compose.yaml -f compose.instances.yaml up -d --build
docker compose --env-file deploy/instances.env.example -p wake-beta -f compose.yaml -f compose.instances.yaml up -d --build
docker compose --env-file deploy/instances.env.example -p wake-alpha -f compose.yaml -f compose.instances.yaml port wake 8080
docker compose --env-file deploy/instances.env.example -p wake-beta -f compose.yaml -f compose.instances.yaml port wake 8080
```

The reported ports lead to each installation's `/console.html` and `/runtime.json`.
Both defaults are paused: inspecting the website consumes no model calls.
Docker chooses ports without a separate probe-and-bind race. Volumes are
`wake-alpha_wake-data` and `wake-beta_wake-data`; neither is the existing operator
volume `wake-standalone-preview_wake-data`. No fixed container name is imposed.

Copy `deploy/instances.env.example` outside the checkout for each installation
and use its absolute path with `--env-file` consistently. Set
`WAKE_INSTANCE_PAUSED=false` to start work. The `fixture` provider is offline;
selecting `gemini` requires that installation's explicit
`WAKE_INSTANCE_GEMINI_API_KEY`. Do not commit credential files or print resolved
Compose configuration with credentials. Shell environment variables can override
env-file values; inspect the intended settings before starting research.

Use `WAKE_INSTANCE_PORT` for a fixed port. Installations bind to all host network
interfaces by default for trusted LAN access; set `WAKE_INSTANCE_BIND=127.0.0.1`
to restrict one to loopback.
Keep each installed image's architecture compatible with its host; a published
multi-architecture image can be selected with `WAKE_INSTANCE_IMAGE` without a
local build. Such publication is a separate authorized operation.

Stop/recreate using the **same** project, env file, and Compose files. `down`
removes containers and project networks but preserves named volumes. Never add
`--volumes` to ordinary maintenance. Keep one research writer per volume; do not
scale the `wake` service against a shared `/data`.

## Optional hostname gateway

The gateway is optional infrastructure, not a WAKE dependency. It routes explicit
hostnames to installation network aliases without mounting the Docker socket,
record volumes, or API credentials. It can share port 80 across installations.
The checked-in routes are `alpha.wake.test` → `wake-alpha` and
`beta.wake.test` → `wake-beta`; unknown hosts return 404.

```sh
docker network create wake-gateway
docker compose --env-file deploy/instances.env.example -p wake-alpha -f compose.yaml -f compose.instances.yaml -f compose.proxy-client.yaml up -d
docker compose --env-file deploy/instances.env.example -p wake-beta -f compose.yaml -f compose.instances.yaml -f compose.proxy-client.yaml up -d
docker compose -p wake-gateway -f deploy/gateway/compose.yaml up -d
```

If the named network already exists, inspect its ownership before reusing it.
Configure hostname resolution on the accessing device or LAN DNS. Docker network
aliases are not LAN DNS entries. For an iPhone, a Mac-only hosts-file entry is not
enough. Direct assigned ports remain available without DNS setup.

The gateway binds loopback by default; use `WAKE_GATEWAY_BIND=0.0.0.0` for trusted
LAN access and `WAKE_GATEWAY_PORT` if port 80 is occupied. `wake.test` is example
local naming; these settings do not configure public DNS, authentication or TLS.
For public hosting, supply those controls at the deployment boundary before
exposing the gateway. The provided HTTP gateway is intended for local/trusted use.

Edit `deploy/gateway/nginx.conf` for additional explicit hostnames and project
aliases. Nginx resolves Docker DNS during requests, so replacing a container does
not pin its old IP. A stopped installation returns a gateway error, never another
installation's data. The `nginx:stable-alpine` default follows upstream releases;
use `WAKE_GATEWAY_IMAGE` with an approved immutable digest for a repeatable hosted
installation. Gateway failure does not stop research or change any record.

## Verification and maintenance

`python scripts/test_installations.py --image wake-candidate:local` builds no image
and makes no provider calls. It creates uniquely named test resources, advances
only one offline fixture installation, checks the other stays unchanged, recreates
a container with its original volume, and verifies the exact record head and
append-only prefix. It removes only resources it created. Operator installations
and volumes are untouched. Add `--gateway-image nginx:stable-alpine` to test
hostname isolation, unknown/stopped hosts, and replacement behind a running gateway.

`python scripts/test_container.py --image IMAGE` additionally checks interrupted
recovery and recreation on both ARM64 and AMD64. Run those proofs against the
actual candidate image. A bind-mounted checkout test does not certify a packaged
image. Build and CI instructions live in [development](development.md); hosted
release controls remain in [cloud](cloud.md).

Compose's project and port behavior: [project isolation](https://docs.docker.com/compose/how-tos/project-name/),
[service ports](https://docs.docker.com/reference/compose-file/services/#ports).
Gateway behavior: [Nginx proxy module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html).
