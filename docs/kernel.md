# Reusable kernel boundary

The kernel remains in `wake/kernel/` in this repository. Research remains the
operational application. A future repository/package split is a separate release
and compatibility decision; moving files alone is not the acceptance criterion.

## Ownership

The kernel owns Record → Context → Proposal → Governance → Transition → Receipt,
serialized durable submission, verified replay, generic invocation accounting,
and storage contracts. Application definitions own deterministic domain policy.
Deployment owns installed application versions, permissions, provider credentials,
process lifecycle, and the selected record. A model proposes; it cannot grant its
own permissions or bypass governance.

`wake/application.py` is the research bridge, not the generic extension interface.
New applications use `wake.kernel.applications`: `ApplicationDefinition`, actions
returning `ApplicationDecision`, an `ApplicationRegistry`, and `ApplicationHost`.
The host exposes application state and revision rather than a database connection.
The trusted runtime constructs the kernel with a record and registry-backed
`Governance`; the evaluator receives only state and JSON input. Importing the
kernel must not import research, GitHub tooling, or another project's package.

## Executable non-research proof

From the checkout, with Python 3.11 or later:

```sh
python -m examples.task_list.run --data /tmp/wake-task-example
```

The example adds a task, rejects completion of a nonexistent task, completes the
real task, and verifies audit replay against current state. All three decisions
produce receipts; only the two accepted transitions advance the revision. Reusing
an already recorded proposal ID raises an error without appending another receipt.
Stale-revision requests are governed rejections. No AI or network is needed.

The example writes `task-list.sqlite`, never the research record `wake.sqlite`.
Use a dedicated directory anyway. This is a contract example, not a replacement
research Console, a task service, or a new commercial product.

`tests/test_kernel_boundary.py` runs the example in a temporary tree containing
only the kernel and example, with site packages disabled. It also exercises
stale requests, duplicate IDs, domain rejections, separate application state,
version mismatch, and generic replay after application removal. An import-boundary
check protects the standard-library-only dependency seam. This proves execution
without the research package; a separately distributed wheel remains future work.

## Durable application contract

Keep application IDs, versions, action names, and historical JSON meaning stable.
An existing application's version cannot be renamed or replaced as a cosmetic
cleanup. A changed interpretation needs an explicit, tested migration. Deterministic
evaluation must not depend on network, wall clock, random values, or side effects;
put such observations in the untrusted input before governed evaluation.

Two supported persistence modes have different guarantees:

| Mode | Recorded meaning | Reconstructing domain state |
| --- | --- | --- |
| `snapshot` | Verified resulting state | Generic replay needs no application code |
| `event_log` | Action input and result digest | Matching evaluator version required; generic replay preserves envelopes |

Research uses event-log storage and verified derived projections to avoid repeated
full domain reconstruction during normal operation. Missing application code must
never be treated as an empty or guessed research state. A generic history audit
and a domain replay check are distinct guarantees.

Applications may coexist in one kernel record, but their state keys are separate
and the record revision is shared. This is not multi-tenant security: trusted
host code can access the kernel. Separate independent installations must have
separate records and volumes, not merely separate application IDs.

Effect requests declare intent only. Installed capabilities and deployment grants
both limit them; declaring a capability is not permission to execute it. Retain the
existing durability-before-effect runtime boundary when adding effects or providers.

## Deployment independence

Use [standalone](standalone.md) for container operation and
[multiple installations](installations.md) for independent records and optional
hostname routing. The kernel and research application run without GitHub. GitHub
transport, public Pages projection, and operator Actions belong to their hosted
adapter, not application authority. See [development](development.md) for source,
image, process, volume, and publication custody.
