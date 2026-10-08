# Kernel and independent-container validation — 2026-10-08

This is local candidate evidence, not a hosted release certification. No remote
push, runtime promotion, provider call, or operator-container replacement occurred.
The existing `wake` and unrelated `sudofx` containers were left running unchanged.

## Kernel seam

The non-research task-list application ran through governed submission and full
replay. An isolated subprocess containing only `wake/kernel`, the inert package
initializer and the example ran with Python site packages disabled. No research
package, GitHub, sudofx, or installed third-party dependency was present.

Four durable boundary tests protect dependency isolation, accepted/rejected
receipts, stale requests, duplicate proposal IDs, application-state separation,
version mismatch, and replay without an installed application. This is not a
separately released kernel wheel or a claim of tenant isolation.

## Packaged runtime and deployments

The current Dockerfile built a local ARM64/AMD64 candidate manifest:
`sha256:f9653630347d40cfcf2ab845533d4654590882559e75bcf16f1cbc0ad105c38a`.
Both platform variants passed `scripts/test_container.py`, including unclean
interruption, recreation, verified audit and exact append-only prefix preservation,
with Docker networking disabled. ARM64 was native on the development machine;
AMD64 used emulation. Runtime tests resumed beyond the preserved accepted prefix.

The real Compose overlays passed multi-installation acceptance against this image.
Two random test projects received separate dynamic ports and record volumes. One
advanced to four accepted fixture cycles while the other remained at zero with
an unchanged head. Ordinary `down` and recreation preserved the first record's
exact head and history.

The optional gateway passed using Nginx image
`sha256:0985e772fb9f729e6fa0980da05fca5d9c468e870eed43071545afa9d2e27d94`:
each configured hostname matched its installation's direct public snapshot;
unknown hosts returned 404; a stopped installation returned an upstream error
while the other remained accessible; a replaced container became accessible
through the still-running gateway. The actual gateway Compose file and config
were exercised, with unique temporary route aliases. No Docker socket or record
volume was mounted in the gateway.

All temporary acceptance containers, networks and volumes were removed. The
operator record volume was never selected as test input. Fixture execution made
zero external provider calls. Builds and image pulls used internet access, which
is distinct from a runtime dependency on GitHub or a live model.

## Repository checks and limits

The full suite passed **458 tests**. Compose configuration tests verified distinct
project images/volumes, dynamic loopback ports, paused offline defaults, explicit
installation credentials and unique gateway aliases. Diff whitespace checks passed.

The new container CI workflow is saved locally and has not been run on GitHub.
Docker Desktop on Windows, other container engines, public DNS/TLS/authentication,
and a separately distributed kernel package were not validated by these checks.
The optional HTTP gateway is a trusted-local example; deployment-specific public
access controls remain outside this proof. Hosted research and its data were not
changed or compared as though they were local authority.
