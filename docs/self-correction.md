# Ask WAKE to repair its own presentation source

Open [Self-correction](https://sudofx.github.io/wake/self-correction/) from the
Console. It shows current GitHub correction runs and the latest published native
adaptation observations. Workflow status comes directly from GitHub; native
research evidence remains a dated export, with its installation, captured source
revision and per-node heads visible. Missing observations remain unknown.

## Start a real source correction

1. Open [Source self-correction in GitHub Actions](https://github.com/sudofx/wake/actions/workflows/self-correction.yml).
2. Sign in with repository workflow permissions. Choose **Run workflow** on
   **master**.
3. In **request**, describe one concrete problem and its expected behavior in
   10–4,000 characters. In **paths**, enter one to four existing files separated
   by commas. For example: `wake/assets/ant-farm.js, wake/assets/ant-farm.css`.
4. Run the workflow. WAKE captures the source revision and hashes, sends the
   request and selected files to Gemini once, validates its proposed edits, and
   compares the exact base hashes before writing candidate text.
5. Open the resulting run. If syntax and regression checks pass, the workflow
   creates a **draft pull request** with the changed files and evidence links.
   Review the diff and behavior, then merge an acceptable change through GitHub.
   Website publication and research-runtime upgrades use their existing separate
   release paths.

Use only public source context in the request: workflow inputs, proposal artifacts
and review branches are visible to repository readers. Do not include secrets.

The repository needs its existing `GEMINI_API_KEY` Actions secret and the
repository Actions setting **Allow GitHub Actions to create and approve pull
requests**. The workflow creates draft requests, never approvals. If that setting
blocks the review step, the proposal artifact and test logs remain available;
there is no silent merge fallback. A repository owner can enable creation and
rerun the failed review job against the retained proposal.

You do not have to copy suggested source changes by hand: the proposed files are
already written on a branch named `wake-correction/RUN_ID`. A failed test prevents
branch publication. Passing checks qualifies the candidate for human source
review; it does not establish visual quality, answer quality, scientific validity
or runtime compatibility. Pull requests created with the workflow token may not
trigger ordinary PR CI automatically; the explicit candidate test job is the
recorded check, and normal release gates still apply.

## What this capability can modify

The first source-correction contract, `wake-source-correction@1`, allows only
existing top-level `wake/assets/` JavaScript, CSS and HTML files and top-level
`docs/` Markdown files. The operator selects the exact files for each run. At most
four files, 96,000 bytes per file and 220,000 total candidate bytes are accepted.
The model returns complete replacement text with exact prior hashes, not shell
commands. New files, binary assets, traversal paths, symlinks, unchanged content,
stale bases and extra response fields are rejected before source writes.

The model cannot modify Python runtime code, tests/evaluators, kernel, governance,
records, dependencies, workflows, deployment bindings or credentials. It receives
no research authority, source-write token or filesystem tool. The workflow can
create one review branch; it cannot merge it or promote the runtime. A wider
allowance requires a reviewed versioned contract, not a model-supplied permission.

The model-request job, candidate-test job and branch-publication job use separate
runners. Dependencies are installed from trusted source before applying the
candidate. Candidate tests run inside a non-root disposable Docker container
with no network, provider credentials, research records, Docker socket or
writable host mounts, plus resource limits and a read-only root. The later
write-capable job downloads the original immutable proposal artifact into a
fresh base checkout and revalidates it without executing the candidate. Docker
is an isolation boundary, not proof against every runtime vulnerability.

One run makes at most one Gemini request. Missing secrets, provider quota,
malformed/truncated responses and failed checks stop visibly. There is no
provider retry loop or autonomous recurring source-edit trigger. The receipt
artifact records the base revision, exact proposal digest, model, provider-call
count and changed paths. This is source-development evidence, separate from each
node’s append-only native research record; it never increments research progress.

## Automatic changes inside the native runtime

The separate [native context adaptation](autonomous-context.md) capability can
propose, measure, adopt, monitor and roll back the installed context-selector
policy without per-change human review, once a deployment grants permission.
It cannot rewrite arbitrary source. The Self-correction page displays each node’s
reported enablement, current policy and trial/adoption/rollback counts. A missing
field is **not reported**, rather than an invented zero or an inferred grant.

Neither the public page nor a source correction enables that deployment grant.
Changing or promoting hosted runtime policy remains an explicit compatible
runtime operation. Source, CI, a merged change, the public mirror and the actual
executing runtime each need their own evidence.

## Earlier recovery experiment

The earlier static retry-delay/concurrency demonstration is retained under
**Earlier operational recovery experiment** with its exact `result.json`. Those
synthetic-service results made zero production changes. They are not relabeled
as current behavior. [Reproduce that experiment](resilience.md#try-bounded-operational-self-correction-in-isolation).
