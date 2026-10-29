# Automatic self-correction

WAKE checks its supported presentation source automatically when code checks,
website publication or a research batch finishes. You do not need to describe a
bug or select files to start those checks. The
[Self-correction page](https://sudofx.github.io/wake/self-correction/) shows the
latest check, repair, publication or review outcome and links to its evidence.
**Run a check now** is an optional extra check; leave its repair fields blank.

This is bounded automation. It checks JavaScript syntax in eligible top-level
presentation files and content-based cache keys for the self-correction page.
It also attempts a reviewed repair when current CI fails after a commit confined
to the allowed source files; failing check-step names are supplied as untrusted
diagnostics, without pretending that they establish a cause.
It is not a general detector of scientific mistakes, visual defects or arbitrary
runtime faults. A failed research workflow without a supported source diagnosis
is reported as outside this repair allowance; it cannot authorize a runtime rewrite.

## What happens automatically

- A stale self-correction asset cache key is replaced with the content digest of
  its existing local asset. This exact mechanical transformation is tested in
  isolation, recomputed in a clean base checkout and applied without human review.
  A normal, non-forced source update rejects concurrent master changes. Independent
  The applied source is recorded before a separate job requests CI; the existing checked
  website publisher then owns delivery. A later automatic check recognizes the exact
  repair tree and recovers a missing CI request. It reports pending delivery checks
  separately from a healthy check or a completed website publication.
- A JavaScript syntax error, or current failing CI after changes confined to
  eligible source, selects its own files and a bounded
  repair request. Gemini gets one attempt. WAKE validates and tests the candidate,
  then opens a draft pull request for source review. It does not require you to
  diagnose the fault or copy the proposed code. Model-authored executable changes
  require review before merging.
- A failed website publication can retry once per source revision per UTC day,
  using the existing website publisher and independently checked current source.
  It does not stop research, restore native records or invent a replacement snapshot.
- A healthy check records that no supported fault was found. Provider waits,
  exhausted attempt capacity, failed checks and faults outside the allowance stay visible.

The workflow uses completion events, not a research cron or a perpetual watcher.
It does not trigger itself. Checks run serially without canceling an active
correction. A candidate is tested at most once per source revision per UTC day;
there are at most four automatic model attempts per UTC day, including failed or
interrupted attempts, and no repeated model attempt for the same source revision
that day. Incomplete attempt history fails closed. Native provider quotas and
billing policy remain unchanged; source requests are separate development calls,
not accepted research or experimental results.

An applied source repair, a passing CI run, website delivery and runtime adoption
are separate evidence. The page reads named outcome jobs, rather than interpreting
any successful workflow as a repair. A mechanical repair is reported as applied
when source advances; it still needs its independent CI and website delivery.
A failed subsequent publication is visible as its own event and bounded recovery.

## Optional advanced request

For a specific source issue beyond the automatic detector:

1. Open [Source self-correction in GitHub Actions](https://github.com/sudofx/wake/actions/workflows/self-correction.yml).
2. Choose **Run workflow** on **master**. In **request**, describe one concrete
   problem and its expected behavior in 10–4,000 characters. In **paths**, enter
   one to four existing files, for example
   `wake/assets/ant-farm.js, wake/assets/ant-farm.css`.
3. A valid, passing model candidate appears on `wake-correction/RUN_ID` as a draft
   pull request. Review it before merging. A failed attempt retains its check and
   any proposal artifacts; it never silently merges a substitute.

The optional model defaults to `gemini-3.5-flash-lite`. Changing this advanced
input does not change research models or installed settings. Explicit requests
are separate operator attempts, rather than automatic retries.
Use public source context only: workflow inputs, artifacts and branches are public.
The page never receives credentials or submits privileged commands.

## Scope and execution boundaries

The model contract remains `wake-source-correction@1`: existing top-level
`wake/assets/` JavaScript, CSS and HTML, and top-level `docs/` Markdown.
At most four files, 96,000 bytes per file and 220,000 total candidate bytes are
accepted. Automatic syntax detection uses the same file allowance and size bound.
The model returns small exact replacements and prior file hashes, never commands.
New files, traversal, symlinks, stale bases, unchanged content and extra fields
are rejected before any source writes. Each edit must match exactly once.

The separate trusted mechanical contract, `wake-automatic-correction@1`, permits
only the two existing local JS/CSS query keys in
`wake/assets/self-correction/index.html`. Candidate text must equal the exact
transformation recomputed from committed source. It cannot add markup, change
asset destinations or grant the model this nested path. The write-capable job
executes trusted code only and never executes candidate source.

No model can edit Python runtime code, kernel, governance, native records,
credentials, dependencies, tests, workflows or deployment bindings. It gets no
write token or filesystem tool. Model generation, testing and branch publication
use separate runners. Dependencies are installed from trusted source before a
candidate is applied. Both the unchanged base and candidate run the complete test suite in separate,
identically restricted containers. Their discovered test identities and counts
must match; no previously passing check may fail, and no new skip is accepted.
Existing restricted-environment failures, including unavailable Docker instruments,
remain explicitly recorded rather than being relabeled as passing. A repair
diagnosed from failing CI must resolve at least one baseline failure. Automatic
source application additionally requires successful full CI for the exact
unmodified base; a failed base can still produce an untrusted reviewed proposal.

Candidate tests run in a non-root disposable Docker
container with no network, credentials, native records, Docker socket or writable
host mounts; the root is read-only with four-GiB memory, three-GiB temporary
filesystem and CPU/process limits. Development reload is disabled.

The proposal uses the existing repository `GEMINI_API_KEY` secret, the kernel
vendor request builder, low reasoning, an 8,192-token output ceiling and a
180-second timeout. Missing credentials, quota failures, malformed responses and
failed tests stop visibly without a provider retry loop. A quota/availability
failure is reported as provider wait, not a successful correction. Draft creation
requires the existing Actions permission to create pull requests; failure leaves
artifacts and never triggers a merge fallback. A wider source allowance needs a
reviewed versioned contract.

## Native automatic context adaptation

The separate [native context adaptation](autonomous-context.md) capability can
propose, measure, adopt, monitor and roll back an installed context-selector
policy without per-change human review when the installation grants permission.
It cannot rewrite arbitrary source. The page shows each node's reported grant,
policy and trial/adoption/rollback counts from one immutable, identified public
snapshot. **Not reported** means unknown. A dated observation is not a live
runtime connection or proof of improvement.

The hosted reader uses the shared public-data transport to select that snapshot;
its explicit revision pin and offline cached-revision rules match other readers.
Refresh reloads the document to select a coherent snapshot, rather than mixing
new data into an old document. GitHub correction metadata is observed separately
and cached for ten minutes, including unavailable responses.

## Earlier recovery experiment

The earlier static retry-delay/concurrency demonstration remains under **Earlier
operational recovery experiment** with its exact `result.json`. Those synthetic
results made zero production changes and are not relabeled as current behavior.
[Reproduce that experiment](resilience.md#try-bounded-operational-self-correction-in-isolation).
