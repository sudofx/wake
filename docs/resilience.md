# Check operational resilience

WAKE constrains the effects of unpredictable models with deterministic rules,
durable invocation receipts and bounded operational recovery. These mechanisms
do not prove that a provider will recover, that a queue will always drain, or that
accepted research is scientifically correct.

## Inspect before recovering

```sh
docker exec wake wake-research status
```

Read `research`, node observations and `coordinator` separately. Operator intent,
an active provider grant and an advancing verified record are different evidence.
A public mirror is dated exported evidence, not a recovery control.

If a worker has exited, the explicit operator recovery command is:

```sh
docker exec wake wake-research restart
```

This command resumes research and needs the appropriate operator authorization.
Every surviving worker must acknowledge stopping. A confirmed dead owned process
may instead be reaped; a missing process handle or an undrained live worker blocks
replacement. New workers verify their existing records and recover interrupted
invocations before provider effects. Restart never resets, copies or merges records.
See [operator controls](standalone.md#control-research-from-the-shell).

## Use separate indicators

| Question | Existing evidence | Interpretation limit |
| --- | --- | --- |
| What is pending? | Queue count, active grant and node pending invocation | Waiting, an external effect and an unresolved record operation are different states. |
| What failed? | Invocation outcomes, model attempts and generic application-observability counts | Provider failure, governance rejection, quota deferral and barrier failure remain distinct. |
| What was retried? | Model-attempt receipts and supervisor recovery output | Coordination-message retries do not represent additional provider calls. |
| Is recovery working? | Recovery output, invocation times and subsequent verified heads | Reappearing processes or green status alone do not establish accepted progress. |
| Is the provider available? | Shared model cooldown/access state and failure categories | Local credential blocks differ from remote quota and connection failures. |
| Is state intact? | Native audit/replay of the selected record | Exports and process-health checks are not full integrity checks. |

Generic observability counts complete verified history and independently limits
recent lists. Zero or negative recent limits return empty lists. Pre-effect
checkpoint failures count as `effect_barrier_failure`; older `effect_barrier:…`
details remain recognizable without rewriting historical records. This disposable
projection never governs an effect.

Existing controls already provide serialized grants, expiring queued tickets,
bounded search admission, configured daily caps, eligible fallbacks, quota
cooldowns, context ceilings, transaction rollback and interruption recovery.
The standalone supervisor's rolling restart window is a rate bound, not a
lifetime retry limit. None establishes unconditional backlog stability.

## Understand the failure boundaries

* Lost or truncated acquire/release replies get at most three transport attempts
  with the same request identity and release token, separated by 0.1 and 0.2
  seconds. HTTP rejections are not retried. Provider effects are never replayed.
  An unrecovered ambiguous grant remains held until confirmed worker death;
  it never expires into a potentially overlapping call.
* Incremental provider-body reads check a monotonic deadline and byte caps.
  This stops continuous small payload arrivals in non-chunked responses from
  prolonging one full-body read. A blocked read may exceed the deadline by its
  socket inactivity timeout. Chunk framing can perform additional internal reads;
  DNS and response headers also remain urllib's responsibility. There is no hard
  end-to-end wall deadline. No detached timeout thread can continue an unaccounted
  local request after its grant is freed.
* HTTP 200 without a complete textual answer is `invalid_response`. Bounded
  diagnostic metadata retains status, model version, finish reason and known
  token counts while excluding incomplete prose and redacting known credentials.
  No accepted proposal or successful external outcome is invented.
* A failed pre-effect durability checkpoint prevents the provider call and
  records a barrier failure. Recovered interruptions do not prove whether an
  external request took effect.

## Reproduce the failure checks

Use disposable fixtures from the checkout; these tests never use installation
records or call a live model:

```sh
PYTHONPATH=tests python -m unittest \
  test_installation_provider_gate test_installation_lifecycle \
  test_runtime_supervisor test_generation_failures \
  test_kernel_observability test_kernel_boundary test_system -q
```

| Controlled disturbance | Required evidence |
| --- | --- |
| One dead worker, eleven drained workers | Explicit restart reaches replacement; an unknown live worker still blocks it. |
| Acquire/release reply lost after controller application | Same identities are retried; exactly one provider effect, no overlap. |
| All three acquire replies lost | Zero effects; ambiguous grant remains held. |
| All three release transmissions fail | One effect; grant remains held, release failure visible. |
| Operator pauses during coordination recovery | No effect after pause is observed. |
| HTTP success/error body drips payload below inactivity timeout | Incremental deadline checks stop reading; error response closes. |
| Missing, incomplete or malformed answer | Invalid-response evidence without raw prose or known credentials. |
| Checkpoint fails before inference | No provider call or accepted-cycle advance; one classified barrier failure. |
| Recent diagnostic limit is zero | Empty recent lists, unchanged complete-history counts. |
| Signals, temporary/permanent exits and restart bursts | Only eligible failures restart; rolling cooldown and operator stop remain effective. |

These are correctness comparisons under fixed disturbances, not production
reliability distributions. Loopback timings include host scheduling; regression
bounds are deliberately generous. Existing system tests additionally cover
transaction interruption, governance rejection, quota accounting and replay.

## Assess mathematical applicability

Individual indicators expose different causes. Combining queue length, rejected
proposals and latency into one weighted score would require an operational
decision, normalized inputs and calibrated weights; none is established here.

A useful future queue experiment would specify arrival rate, eligible service
capacity, failure duration and sampling intervals, then compare backlog drift and
recovery-time distributions across repeated disturbances. Stable backlog cannot
be assumed during indefinite provider unavailability or sustained excess demand.
Markov/drift analysis additionally requires a justified state/transition model;
a Console sample omits hidden provider state and changing model behavior. No
Foster–Lyapunov condition is demonstrated for this deployment. See
[Meyn and Tweedie's framework](https://probability.ca/MT/); naming a counter a
Lyapunov function does not establish its assumptions or conclusions.

Langevin algorithms sample from a specified target distribution with a suitable
potential and drift/noise model. This audit establishes none of those objects
for topic selection or recovery. Noise would not repair lost replies or missing
failure classification, so no Langevin mechanism or randomized policy is added.
See [Durmus and Moulines](https://arxiv.org/abs/1507.05021) for that different
problem. Attention remains deterministic application policy, outside the kernel.
Recorded-decision replay is distinct from reproducing remote model behavior;
even a stored random seed would not guarantee the latter.

Maintain the fault tests and examine real recovery episodes before adding another
control. Production recovery distributions, saturation behavior and live-model
comparisons need a defined experiment and appropriate runtime authorization.
Source tests and mirror delivery do not establish resident-runtime adoption.
