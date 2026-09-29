# WAKE✳︎ owner control

This Cloudflare Worker is the confidential authentication and control boundary for
WAKE✳︎'s public GitHub Pages interface. It is intentionally separate from the
Gemini provider and durable record.

Authority is narrow:

- GitHub OAuth proves the configured owner identity.
- The browser receives only a short-lived encrypted session envelope.
- Start dispatches `wake.yml` on the dedicated `wake-runtime` branch. It never adopts `master`.
- Operator status is a four-state machine backed by GitHub itself: **running** (runner latch enabled + runtime work active), **draining** (latch disabled while work is still cancelling), **stopped** (latch enabled, no runtime work), and **disabled** (latch disabled, no runtime work).
- The `wake-runner.yml` enabled/disabled workflow state is the durable continuation latch; it is never treated by itself as proof that a cycle is running.
- Execution status and Stop consider only non-completed `wake-runner.yml` / `wake.yml` runs whose branch is `wake-runtime`; development/CI debris on `master` is ignored.
- Start is idempotent: it refuses to duplicate active runtime work, enables the continuation latch, then bootstraps the promoted `wake-runtime`.
- Stop disables the continuation latch **before** cancelling active work, preventing a finishing cycle from racing the operator and dispatching a successor.
- Reset is unavailable while runtime work is active. Once idle, it disables the continuation latch and dispatches the governed reset path from `wake-runtime`; it never edits SQLite directly.
- Runtime promotion is outside the Worker and is handled only by the explicit verified promotion workflow.
- The Worker never receives `GEMINI_API_KEY`.

Required encrypted Worker secrets:

- `GITHUB_CLIENT_ID`
- `GITHUB_CLIENT_SECRET`
- `SESSION_SECRET` (at least 32 random bytes)

The GitHub App/OAuth installation must grant Actions read/write access to
`sudofx/wake`. Set repository variable `WAKE_CONTROL_URL` to the deployed Worker
origin. The generated site hides owner controls when that variable is absent.
