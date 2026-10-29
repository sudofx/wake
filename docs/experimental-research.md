# Autonomous experimental research

This implementation extends the research application, not the generic WAKE
kernel. A model proposes a falsifiable hypothesis and an executable protocol;
application governance freezes them, a restricted instrument executes them, and
trusted scoring records measurements separately from model interpretation.

## Implementation plan and acceptance gates

1. Versioned hypotheses, immutable protocols and native lifecycle events. Prove
   stale/replayed/forged transitions fail and supersession preserves predictions.
2. Restricted computational instruments reusing the pinned Docker runner. Prove
   actual execution, resource limits, withheld-label isolation and crash cleanup.
3. Integration into ordinary research proposals and idle invocation boundaries.
   Deterministic work must continue without a provider response. Cap the work
   admitted per wake; preserve the existing writer and effect-checkpoint barriers.
4. Historical correction: paired A/B/C conditions, independently scored answers,
   randomized ordering, varied seeded instances and information-availability
   controls. Report accuracy, false correction, evidence selection, usage and time.
5. Hypothesis revision: fresh hidden-system instances, frozen failed predictions,
   model-selected distinguishing tests and revision on unseen inputs. Do not put
   the hidden mechanism or revised explanation in the model context.
6. Experiment-aware convergence, replication and scientific progress metrics.
   Execution success, measurement validity and interpretation remain distinct.
7. Public question-to-result audit views, canonical documentation, exact-source
   CI, all-node compatibility verification and separately verified runtime adoption.

Deterministic tests currently establish native replay, frozen criteria, real
Docker execution, independent exact scoring, retained negative outcomes,
fixture-driven revision on three hidden-system instances, paired A/B/C
correction trials, replication and interruption recovery. Fixtures validate
machinery and cannot establish live model discovery or comprehension.

Release acceptance also requires live model-authored execution, a retained
contradiction followed by a model-authored revision that improves unseen
predictions, independent replication, and a live paired correction study.
Proposal-format, supersession and instrument-binding failures remain visible;
they are engineering failures, not scientific findings. Hosted execution and
actual runtime adoption require their own verified rollout.

## Run a bounded investigation

Use a new disposable directory; these commands do not replace an existing
installation. Configure the already-supported Gemini project with billing
disabled and use the reviewed image named by `wake.improvement_runner.DEFAULT_IMAGE`.

```sh
python -m wake science investigate --output /tmp/new-investigation --instance 17 --calls 4
python -m wake science resume --output /tmp/new-investigation --calls 2
python -m wake --data /tmp/new-investigation/record science report --output /tmp/scientific-audit.html
```

Each run retains native history, settings and a derived report. `--calls` bounds
planning invocations; a model-comparison protocol separately freezes its
explicit trial allowance. Ordinary computational work continues after the
planning allowance is spent. No fixture is silently substituted for an
unavailable live model. The historical-correction instrument uses six failure
families and randomized paired A/B/C conditions; six cases require 18 task calls.
It cannot alter its frozen tasks, scorer or inference count through generated
preparation code. Usage and monetary cost remain unavailable when not reported.

## Current boundaries

- Scientific actions are opt-in through `experimental_research_enabled`; models
  cannot enable this operator-owned grant.
- `hypothesis`, `experiment`, `experiment_interpretation`, `research_direction`
  and `investigation_decision` use normal proposals and project governance.
  Definition objects follow `wake.science.schemas`; older serialized JSON
  definitions remain readable. The kernel gains no scientific concepts.
- Generic numeric observations remain unvalidated and inconclusive without an
  independent instrument check. Exact sorting and synthetic hidden-system
  oracles validate their finite measurement scope only.
- A changed hypothesis reuses its stable ID with explicit supersession. An
  experiment always receives a new ID; exact replication copies its protocol.
  A hidden-system holdout seed cannot be reused for follow-up optimization.
- Scientific report JSON is generated only when native science state
  exists; the stable audit reader is always exported. They expose recorded results and clearly labelled interpretation.
  They do not establish hosted adoption or physical-device rendering.
- The hosted worker pulls the pinned image and runs the adversarial isolation checks before opening research. Its experimental grant still defaults off and requires explicit installation policy. Docker availability must be established separately on the deployed worker.
  An unavailable capability blocks work explicitly; it never falls back to
  running generated code on the host.

## Reuse and changes

- Reuse `ApplicationHost`, `AuthoritativeStore.append`, native invocation receipts,
  deterministic application policy/reduction and existing research project IDs.
  No new authority database or application-specific kernel rules are needed.
- Reuse the improvement runner's pinned image, no-network/read-only/non-root
  containers, bounded process/output handling and named-container cleanup. Extend
  its transport to a general computational entry point; keep scoring outside.
- Reuse the generation-provider contract, budgets and hosted durability barriers.
  Do not treat the earlier four-case knowledge-selection evaluation as the new
  historical-correction benchmark.
- Extend ordinary research actions/context and the existing public projection.
  Literature collection remains available; experimental execution and replication
  become possible alternatives to another retrieval round.
- Existing context adaptation remains a separate bounded policy capability. It
  is not a scientific investigation and does not confer experimental permissions.

## Authority and evidence

Small code, protocol, input, output and scoring artifacts are retained directly in
bounded native events with content digests. Public and provider projections omit
protected scoring inputs and hidden generative parameters. Any future external
artifact transport must preserve verified retention before accepting a result.
Models cannot submit trusted execution receipts, revise frozen criteria, select
an arbitrary container image, expose hidden inputs, or promote their own verdict
into independently verified evidence.

The existing Docker boundary is an isolation mechanism, not a claim of immunity
to container-runtime or kernel vulnerabilities. Missing capabilities produce an
explicit blocked investigation; there is no host-Python fallback.

## Inspect progress without claiming resolution

The planner and public audit derive convergence evidence from the current
hypothesis revision: pending execution, a retained contradiction, invalid or
inconclusive measurement, a missing independent replication, a bounded completed
comparison, or an execution blocker. They retain execution cost and remaining
uncertainty alongside the next-step decision. These are planning signals, not
scientific verdicts inferred from activity counts. Compare a feasible next test
with its expected information value, cost and frozen stopping rule. A depleted
budget justifies suspension; it does not resolve the question. Administrative
closure preserves the recorded uncertainty.

Paired trial inference uses the normal native provider lifecycle. Each exact
request, response and transport attempt is retained. A crash after one response
preserves that response and the interrupted next attempt; restart closes the
unfinished study without repeating effects or inventing an outcome. The
installation recovers those paid effects into its feature budget if the derived
scheduling cache is lost. Explicit zero-effect queue denials do not consume it.

The installable wheel includes the science application modules. Code CI checks
actual restricted Docker execution on Python 3.11 and 3.13 as part of the full
suite. The pinned image is pulled before those checks. Neither packaging nor CI proves a live model revised a hypothesis or
that the hosted installation adopted the scientific grant.

The hidden-mechanism CLI freezes its selected evaluator and instance through an
operator-owned native binding before any experiment. Governance rejects another
instance rather than allowing a sample protocol to silently replace the question.
The provider context includes exact prior protocol inputs, consumed holdout seeds
and native revision identities; follow-ups must use fresh seeds. No hidden
mechanism or holdout labels accompany that guidance.

The paired instrument accepts an unchanged trial list or the unchanged input
object containing that list; either representation must preserve every task,
condition and ordering. A candidate cannot change them or the paid-call count.
Before each trial, native current-day usage also checks the frozen model's daily
ceiling. A study stopped at that boundary retains completed trial evidence and
has no scientific evaluation for its incomplete measurements.

Execution reviews freeze the trusted runtime identity as well as generated code.
A previously approved attempt is blocked if that environment changes before an
effect starts. New reviews record `typed-scalars@1` comparison semantics; older
reviews retain their original comparison behavior for replay. Native trial
accounting records per-trial time envelopes. Recovery conservatively charges
both Pacific days when an effect envelope crosses midnight, rather than lose a
confirmed or possibly interrupted call after scheduling-cache loss.

Ordinary planning and public request totals include native scientific trial calls;
trial reservations with unknown transport outcomes remain separately unresolved.
The same counts enforce per-model limits before ordinary planning resumes, so a
completed experiment does not restore spent allowance. Failed preparation keeps
its bounded output and digest. Failed container programs retain bounded stdout
and stderr prefixes plus captured-stream digests. Missing historical duration
stays unknown; the audit distinguishes known elapsed time from a complete total.

The website reader leads with plain-language questions, predictions, measured
results, replication status and remaining uncertainty. Raw JSON, code, internal
identities and hashes stay inside explicitly labeled researcher/developer
disclosures, closed by default. The canonical JSON export remains complete.

The website audit reader is delivered with the interface, including before the
first experiment. It reads scientific JSON through the same immutable public
snapshot as the other readers. Source-only presentation refresh also delivers
this reader without enabling experimental execution or inventing reports.
The unified page checks each node report against
that snapshot's record head and retains node-qualified presentation rather than
merging local scientific identities. Data-only uploads therefore expose new
studies without rebuilding Pages. A missing or mismatched node report remains
explicit; it cannot select a different snapshot as fallback. A node's own audit
uses that node's report and checks it against the same installation manifest.

`science investigate` and `science resume` use a bounded benchmark focus. The
request retains the question, projects, scientific state, working memory and
applicable constraints, while its omitted categories and deferred continuity
sidecar are recorded. It offers scientific actions instead of unrelated source
collection or editorial work; this CLI has no external collection caller. This
is context selection inside the existing application invocation, not another
research engine or weaker governance. Ordinary installations retain their full
research routing.
