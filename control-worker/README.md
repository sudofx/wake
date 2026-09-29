# WAKE✳︎ owner control

This Cloudflare Worker is the confidential authentication and control boundary for
WAKE✳︎'s public GitHub Pages interface. It is intentionally separate from the
Gemini provider and durable record.

Authority is narrow:

- GitHub OAuth proves the configured owner identity.
- The browser receives only a short-lived encrypted session envelope.
- Start dispatches `wake.yml` on the dedicated `wake-runtime` branch. It never adopts `master`.
- Status and Stop consider only non-completed `wake.yml` runs whose branch is `wake-runtime`; development/CI debris on `master` is ignored.
- Reset cancels active runtime cycles, then dispatches the governed reset path from `wake-runtime`. It does not edit SQLite directly.
- Runtime promotion is outside the Worker and is handled only by the explicit verified promotion workflow.
- The Worker never receives `GEMINI_API_KEY`.

Required encrypted Worker secrets:

- `GITHUB_CLIENT_ID`
- `GITHUB_CLIENT_SECRET`
- `SESSION_SECRET` (at least 32 random bytes)

The GitHub App/OAuth installation must grant Actions read/write access to
`sudofx/wake`. Set repository variable `WAKE_CONTROL_URL` to the deployed Worker
origin. The generated site hides owner controls when that variable is absent.
