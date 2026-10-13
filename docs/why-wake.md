# Why WAKE✳︎

WAKE✳︎ is infrastructure for durable, accountable work across interchangeable
models, runtimes, and people. Research is its first application. Its name asks
us to consider what remains after an interaction ends:

> A wave describes possibilities. A wake carries the consequences of what has occurred.

This is the starting image for the **Quantum Wake Function** metaphor. The
architecture gives that image a practical expression: work can leave an
inspectable history that survives the intelligence that produced it.

## Waves and wakes

Imagine a boat crossing a quiet lake. Its wake is the disturbance left by its
passage. The boat may be gone while that disturbance continues to spread,
interact with other disturbances, and affect another boat's passage.

A wake is both evidence of the past and an influence on the future.

The distinction concerns what we are looking at: a wave's form and propagation,
or a disturbance in relation to the passage that produced it. A wake contains
waves; ordinary water waves also have causes and consequences. The opening
sentence is a metaphor, not a physical classification of waves as possibilities
and wakes as facts. Nor does a water wake preserve a complete, permanent account
of its cause. WAKE's software record supplies deliberate persistence and
provenance that water does not.

## The quantum inspiration and its limits

In quantum mechanics, a wavefunction mathematically describes a quantum state.
It provides complex probability amplitudes from which measurement probabilities
can be calculated. For discrete outcomes in the chosen measurement basis, those
probabilities are the squared magnitudes of the corresponding amplitudes. It is
not an ordinary wave in water. See IBM's
[introduction to quantum states](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/single-systems/introduction)
and [measurement examples](https://quantum.cloud.ibm.com/learning/en/courses/utility-scale-quantum-computing/bits-gates-and-circuits).

Quantum measurement does not require a conscious observer. A measuring apparatus
can interact with a system and register an outcome without a person watching it;
see Yu and Nikolić's discussion of
[why consciousness is not required](https://arxiv.org/abs/1009.2404).

The metaphor borrows the relationship between possibilities and consequences:

> The wavefunction describes what might happen. The wake function describes how what happened shapes what can happen next.

This compresses an idea for reflection; it is not a complete account of quantum
states or measurement. **Quantum Wake Function is not an established mathematical
object or physical law.** Here, “function” names a conceptual role, not an
equation, algorithm, or software interface. WAKE does not claim to perform
quantum computation. Its operation is explained by ordinary software contracts,
not by quantum measurement. The metaphor implies no consciousness, subjective
experience, or persistent personal identity in WAKE or its models.

## How the architecture carries consequences

WAKE's concrete lifecycle is:

```text
Record → Context → Proposal → Governance → Transition → Receipt
```

| Metaphorical idea | Concrete architectural role |
| --- | --- |
| Possibility | A model receives bounded context derived from the record and produces a proposal for potential next actions. |
| Interaction | Governance deterministically evaluates the untrusted proposal against applicable policies and current governed state. |
| Consequence | Accepted transitions change governed state. A governed rejection produces a receipt without applying the rejected changes or advancing the accepted revision. |
| Wake | The durable record preserves events, decisions, receipts, provenance, and corrections. Deferrals and failures remain visible through their recorded outcomes. |
| Continuity | Subsequent work receives bounded context derived from recorded history, allowing earlier interactions to inform future proposals. |

The arrows describe the lifecycle, not a promise that every attempt makes a
transition. A provider failure before a proposal exists is recorded through the
invocation lifecycle; it does not fabricate a proposal receipt. See
[architecture and limits](architecture.md) and the [kernel contract](kernel.md)
for the actual guarantees.

For example, a rejected suggestion can help a later model understand a policy
boundary. Its receipt establishes that the rejection occurred, not that the
suggested change was made. An accepted change can establish governed work that
the next model must account for, even if that model never encountered the
original interaction.

The significant property is that consequences can persist independently of the
intelligence that produced them. A model may disappear, be replaced, or begin
again without remembering earlier work. The governed record carries forward
what was actually established within the system.

**The intelligence is replaceable. The accountable history remains.**

## Memory without model authority

The record influences future work through bounded context, not by giving a model
control over history or policy. Context may summarize or omit detail; recoverable
provenance keeps links back to the exact recorded material. A later proposal
still passes through governance. Neither a confident model nor a repeated claim
can authorize its own acceptance. See [context and retrieval](retrieval.md).

Recording evidence establishes that material was recorded with particular
provenance. It does not establish the truth of every associated claim. Even an
accepted research transition means that the proposal passed applicable rules,
not that its conclusions became unquestionable facts. Scientific support must
still be assessed, uncertainty retained, and claims open to correction.

Corrections and supersession add accountable history rather than rewriting what
happened. A later correction can change which conclusion is current while
preserving the earlier claim and why it was revised. Append-only history and
hash verification support inspection; their [audit limits](architecture.md#recovery-and-audit-limits)
still apply. Persistence alone is not proof of truth or protection against every
form of tampering.

The wake metaphor therefore belongs in WAKE's design language: it explains why
durable consequences matter. The append-only record, governed transitions, and
recoverable provenance are its concrete software realization.
