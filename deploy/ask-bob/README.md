# Live Ask Bob API

This dedicated anonymous Worker answers public Bob conversations using Gemini.
Source is owned here; Sites stores only a publication mirror. The live API is
`https://wake-ask-bob.coolgrove68.chatgpt.site`. Preserve the Site identity in
`.openai/hosting.json`; do not register another deployment for updates.

No visitor login, identity provider, browser API key or model download is used.
`GET /v1/capabilities` describes availability. `POST /v1/chat` takes JSON with
`article_id`, `expected_article_hash`, `question` (up to 2,000 characters), and up
to six recent `{question, answer}` turns. It returns newline-delimited JSON:
`delta` events carry `text`; `done` carries the complete `result`, exact article
identity and cited source links; `error` means the partial answer is incomplete.
HTTP failures return JSON error codes. No automatic retry consumes extra quota.

The server fixes the source origin to the WAKE Pages public guide archive and
verifies the displayed article hash and source heads. It sends at most 18,000
characters of source passages, 1,200 output tokens and a 45-second provider limit.
Bob is advisory and has no research, filesystem, database or control capability.
Do not connect it to native record storage or the activity relay.

Runtime values: secret `GEMINI_API_KEY`, secret `IP_SALT`, `BOB_ENABLED=true`,
`GEMINI_MODEL=gemini-3.1-flash-lite`, and the owning `INSTALLATION_ID`.
Set `BOB_ENABLED=false` and redeploy to disable provider access. Use native Sites
environment tools; never put secret values in the source or hosting manifest.

R2 binding `BUCKET` holds one disposable `admission.json`: UTC day, attempt count,
daily salted address hashes, burst counts and expiring concurrency leases. It
contains no questions, answers, raw IP addresses or research state. Hosting-provider
request logs may still include ordinary connection metadata. Conditional
writes serialize admission globally across Worker instances. Defaults: 100 total
attempts/day, 20/address/day, four/address/minute, two in flight. Rejections and
failed provider attempts are not refunded. Interrupted leases expire after 90
seconds. Storage failure fails closed. These controls bound model access; CORS is
not authentication and forged Origin or distributed addresses remain possible.
Hosting requests themselves can still consume hosting resources. Gemini project
quota is shared with other callers; this service does not reserve research quota
or establish a monetary billing cap. Google still processes submitted chat text.

Run `node --test tests/api.test.js`, `bash scripts/build.sh`, then
`node scripts/validate-artifact.mjs`. Publish a copy through the Sites source
helper and saved-version deployment workflow, preserving the public audience.
The exact public blog flow must also be checked after Pages publication.
