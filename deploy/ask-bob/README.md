# Live Ask Bob API

This dedicated anonymous Worker answers public Bob conversations using Gemini.
Source is owned here; Sites stores only a publication mirror. The live API is
`https://wake-ask-bob.coolgrove68.chatgpt.site`. Preserve the Site identity in
`.openai/hosting.json`; do not register another deployment for updates.

No visitor login, identity provider, browser API key or model download is used.
`GET /` serves the stable standalone chat. It remains available when an older
research batch republishes older Pages assets during release adoption.
`GET /v1/articles` returns a bounded list from the fixed public reader overview;
neither route calls Gemini. Standalone history lives only in tab memory.
`GET /v1/capabilities` describes availability. `POST /v1/chat` takes JSON with
`article_id`, `expected_article_hash`, `question` (up to 2,000 characters), and up
to six recent `{question, answer}` turns. It returns newline-delimited JSON:
`delta` events carry `text`; `done` carries the complete `result`, exact article
identity and cited source links; `error` means the partial answer is incomplete.
Record chat uses `mode: "record"`, an allowlisted `collection`, `record_id`,
`expected_head`, and an optional enrolled `node`. It fetches only a fixed public
record shard (512 KiB maximum) or bounded page overview (256 KiB maximum), refuses
changed identities/heads, and supplies at most 18,000 characters from twelve
sources. Journal shards use invocation IDs to preserve cross-node identity.
`GET /v1/articles?collection=...&record=...&head=...` initializes that context in
the same popup; it makes no model call. Arbitrary source URLs, models and tools
remain unavailable to visitors.

HTTP failures return JSON error codes. Provider quota failures include `retry_at`
and `quota_scope`. Only a structured, positive, model-specific daily free-tier
quota failure permits trying the next configured compatible model (at most two
fallbacks, before any text is streamed). Minute, project, unknown and zero quotas
stop the whole service temporarily. Transport failures and partial answers never
trigger fallback. An explicit transient HTTP 500/502/503/504 permits one short,
bounded retry on the same model before streaming; that attempt is also charged
to the existing admission budget and shares the 45-second provider deadline. Every provider attempt consumes admission budget.

Quota cooldowns are shared across workers. Daily cooldowns last until Pacific
midnight; shorter limits respect bounded Google RetryInfo. Availability checks
make no Gemini call. The chat shows a waiting message after ten seconds, distinguishes timeouts from
user stops, and labels failed delivery as no completed reply. It retains failed drafts, creates Bob's bubble only
when text arrives, and reuses the pending user bubble on an explicit retry.
Availability recovery never automatically resends a question.

The server fixes the source origin to the WAKE Pages public guide archive and
verifies the displayed article hash and source heads. It sends at most 18,000
characters of source passages, 1,200 output tokens and a 45-second provider limit.
Bob is advisory and has no research, filesystem, database or control capability.
Do not connect it to native record storage or the activity relay.

Ant Farm questions use `mode: "ant-farm"` and a validated numeric-only
`wake-ant-observation@1` sample instead of an article binding. They share all
admission and provider limits. No research sources, record access or continuous
watching are granted. Farm replies use a separate snapshot instruction with no
research-citation examples; active digging sites do not establish branch counts. See [the farm guide](../../docs/ant-farm.md).

Runtime values: secret `GEMINI_API_KEY`, secret `IP_SALT`, `BOB_ENABLED=true`,
`GEMINI_MODEL=gemini-3.1-flash-lite`, and the owning `INSTALLATION_ID`.
Optional `GEMINI_FALLBACK_MODELS=gemini-3.5-flash-lite,gemini-3.6-flash` is honored
only with `BOB_FREE_TIER_CONFIRMED=true`. Recheck availability and free-tier pricing
before changing this allowlisted model pool; this flag does not alter billing.
Set `BOB_ENABLED=false` and redeploy to disable provider access. Use native Sites
environment tools; never put secret values in the source or hosting manifest.

R2 binding `BUCKET` holds one disposable `admission.json`: UTC day, attempt count,
daily salted address hashes, burst counts, sanitized provider quota cooldowns
and expiring concurrency leases. It
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

The chat inherits the main reader’s theme through its launch URL, follows the system
when opened directly, and offers a local light/dark switch. The shared WAKE theme
tokens and safe Markdown formatter are in `wake/assets/`. The build embeds them
without fetching browser dependencies. Publication mirrors carry exact generated
copies as `worker/theme-tokens.css` and `worker/bob-markdown.js`; update those from
the canonical assets before packaging. Formatted replies use allowlisted DOM
elements, never source HTML. Raw reply text remains the conversation context.

The header avatar embeds the canonical vector favicon from
`wake/assets/icons/wake.svg`, so its gradient mark remains sharp on high-density
displays. The publication mirror carries an exact copy at `worker/wake.svg`;
the build embeds it without an external image request.
