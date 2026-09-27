# WAKE✳︎ owner control

This Cloudflare Worker is the confidential authentication and control boundary for
WAKE✳︎'s public GitHub Pages interface. It is intentionally separate from the
Gemini provider and durable record.

Authority is narrow:

- GitHub OAuth proves the configured owner identity.
- The browser receives only a short-lived encrypted session envelope.
- Start enables and bootstraps `wake-runner.yml`.
- Stop disables the runner first, then cancels active runner/research runs.
- Reset disables continuous operation, cancels active runs, then dispatches the
  existing governed reset path in `wake.yml`. It does not edit SQLite directly.
- The Worker never receives `GEMINI_API_KEY`.

Required encrypted Worker secrets:

- `GITHUB_CLIENT_ID`
- `GITHUB_CLIENT_SECRET`
- `SESSION_SECRET` (at least 32 random bytes)

The GitHub App/OAuth installation must grant Actions read/write access to
`sudofx/wake`. Set repository variable `WAKE_CONTROL_URL` to the deployed Worker
origin. The generated site hides owner controls when that variable is absent.
