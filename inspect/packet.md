# WAKE external inspection packet

Canonical resource root: https://sudofx.github.io/wake/inspect/



---

<!-- Source: README.md -->

# Inspect WAKE independently

WAKE is infrastructure for preserving accountable work when the model, process or
person doing that work changes. Its kernel stores a durable record, evaluates
proposed changes under application rules, and returns a receipt. Research is its
current operational application; a small task-list application demonstrates the
same kernel without research concepts, a model or a network.

The central claim to examine is narrow: accepted work has recorded consequences,
rejected proposals remain inspectable, and replay can recover the recorded state.
An accepted proposal is not established scientific truth. A receipt for a rejected
proposal is not an accepted transition. Corrections preserve earlier history.

An application defines meaning and acceptance rules. A runtime selects the record,
installed code, credentials and execution permissions. A model may propose work;
it receives no arbitrary database or filesystem authority. Each research node
owns one operational database. The public website is a derived snapshot and
cannot establish current operational state or change governance.

Start with [architecture](architecture.md), then examine [demo.json](demo.json)
and its [evidence and reproduction procedure](evidence.md). The demonstration
records accepted → rejected → accepted decisions, with revisions 1 → 1 → 2.
The rejection reports “task does not exist”; replay checks the record chain and
reconstructed state. Inspect the actual artifact for identifiers and hashes.

Read [limitations](limitations.md) before drawing broader conclusions. Use the
[independent evaluation questions](evaluate.md) to challenge the design and record
missing evidence. [manifest.json](manifest.json) identifies this inspection bundle;
compare its actual fields with the files rather than assuming a certification.

This static inspection material requires no account or JavaScript. Reading it has
no governance effect. It neither assumes personal identity nor makes a claim about
consciousness, quantum physics or scientific discovery.


---

<!-- Source: architecture.md -->

# Architecture and authority

WAKE separates durable execution mechanics from application meaning.

```text
bounded context → untrusted proposal → application rules → durable decision
                                                      → receipt and derived views
```

The kernel owns record integrity, serialized submission, deterministic replay and
generic invocation accounting. An application supplies its identifier, version,
actions and deterministic acceptance rules. The runtime supplies the selected
record, installed application version, process lifecycle, credentials and
permissions. Those are distinct responsibilities, even in one Python process.

Before a provider call, the application selects bounded context from retained
records. Delivered context and provenance let a reviewer distinguish what was
available from what was actually sent. A compact view may omit detail; recovery
must follow retained source references rather than invent omitted history.
See the canonical retrieval contract:
https://raw.githubusercontent.com/sudofx/wake/master/docs/retrieval.md

In the task-list example, application code decides whether a task exists and may
be completed. The kernel records the decision. Rejection preserves the task state
and application revision while retaining an inspectable receipt. It does not mean
that nothing was recorded. A proposal identifier cannot be reused to manufacture
a second receipt. Replay checks historical meaning against the recorded chain.

In the research application, topics, notebooks, evidence qualification, Attention
and publication policy stay above the kernel. Each container node owns its record
at `/data/nodes/ID/record/wake.sqlite`. GitHub Pages contains filtered exports;
reading a public page is not querying or controlling that database. Bob translates
recorded work for readers and cannot approve research or change its authority.

Human continuity notes are separate, private working context, not another
operational store. Provider questions, private advisory notes and reader
conversation history do not belong in public inspection exports.

The following links describe **moving source on master**, not a release pin or
proof of the installed runtime:

- Kernel contract: https://raw.githubusercontent.com/sudofx/wake/master/docs/kernel.md
- Application interface: https://raw.githubusercontent.com/sudofx/wake/master/wake/kernel/applications.py
- Record implementation: https://raw.githubusercontent.com/sudofx/wake/master/wake/kernel/record.py
- Research boundaries: https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md

Use an identified commit from the bundle's actual provenance, when available, to
inspect an immutable version. Source, installed runtime and uploaded snapshot may
represent different moments; agreement must be verified, not inferred.


---

<!-- Source: evidence.md -->

# Evidence you can inspect and reproduce

[demo.json](demo.json) is a generated, synthetic task-list demonstration. It is
software evidence about recorded decisions and replay, not a scientific result,
a live research record or an assessment from an external model.

Examine its actual receipt identifiers, revisions, reasons, hashes and final state.
Do not infer missing fields. The intended sequence is:

The isolated record begins at revision 0 with an empty task list. Each event
contains the fixture proposal, its base revision, the receipt identity, decision
and reasons. For accepted operations, `proposal.operations[].value.next_state`
shows the resulting task state; the rejected completion leaves that state alone.
`result.state` is the replayed final state. These are actual recorded proposals
and decisions from the supplied run, with no model call.

| Request | Decision | Application revision afterward |
| --- | --- | --- |
| Add the example task | accepted | 1 |
| Complete a nonexistent task | rejected: task does not exist | 1 |
| Complete the example task | accepted | 2 |

All three decisions are recorded. Only the two accepted transitions advance the
application revision. The generator verifies replay of the record chain and
agreement with reconstructed application state. A successful replay establishes
consistency under the selected rules; it does not establish that a task was
performed outside the example or that any scientific claim is true.

## Reproduce from source

Use an inspected checkout and Python 3.11 or later. From its repository root:

```sh
python3 -S -m examples.task_list.inspection --output /tmp/wake-inspection-demo.json
python3 -m unittest tests.test_kernel_boundary -v
```

The generator uses a disposable example record, not an operator's research
installation. `-S` disables Python site-package initialization, helping demonstrate
that this example needs only the repository kernel and standard library. No model,
credentials or network is required. Independently read the output and compare the
semantic decisions, revisions and replay result. Generated IDs or times may vary;
do not require identical bytes unless the generator's documented contract says so.

These links point to **moving source on master**:

- Task-list rules: https://raw.githubusercontent.com/sudofx/wake/master/examples/task_list/app.py
- Inspection generator: https://raw.githubusercontent.com/sudofx/wake/master/examples/task_list/inspection.py
- Kernel boundary tests: https://raw.githubusercontent.com/sudofx/wake/master/tests/test_kernel_boundary.py
- Receipt implementation: https://raw.githubusercontent.com/sudofx/wake/master/wake/kernel/receipts.py
- Replay implementation: https://raw.githubusercontent.com/sudofx/wake/master/wake/kernel/record.py

[manifest.json](manifest.json) describes the delivered bundle. Check any recorded
file digests against downloaded bytes. A digest can detect a difference relative
to that manifest; a manifest delivered beside its files is not independent proof
of authorship or protection against replacing both. Missing provenance, failed
reproduction or unavailable sources should remain explicit findings.


## Captured public presentation

This is dated exported presentation, not a live status query or a second authority. Generation time does not establish upload or serving time. The executing source revision is unknown.

```json
{
  "authoritative": false,
  "generated_at": "2026-10-29T18:43:20.698949+00:00",
  "head": "snapshot:02d03f8fe4f0dfb487a30b076c52cd134513276743c7753e7623bdceaa6b3d0a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T18:32:54.700036+00:00",
      "head": "045519dec4705f8378f85f110f92736ef58bda76efbba352bf4ecd38dff71785",
      "node": "100.wake",
      "snapshot_digest": "7b33c1aee333807d7b5838ff9591bd34cd3823fc73f0fb4e9be7edb494cc271e",
      "version": 22
    },
    "101.wake": {
      "generated": "2026-10-29T18:38:16.708771+00:00",
      "head": "6a340a8fcf376146f4fdb23236a306134926f2415a7d29a74ae9e583576840d3",
      "node": "101.wake",
      "snapshot_digest": "f5fb395ed1c0329c372c9c2e39f7180e2481d776024743824130f81865ab2b58",
      "version": 25
    },
    "102.wake": {
      "generated": "2026-10-29T18:41:52.005725+00:00",
      "head": "e07b5a2b1d2cd70455f4a8b4684cc04c84d931f4dd830630dd39361ece5ce829",
      "node": "102.wake",
      "snapshot_digest": "b047ebd1b33085ca7503c0d4ce5ebd8d3994fe8ed222bdd106c26700f605d947",
      "version": 20
    },
    "103.wake": {
      "generated": "2026-10-29T18:29:30.102256+00:00",
      "head": "ea4bd9fc66656942665cb4439ae5a1d3340de15628010c8545c40fa2ebaeb8ee",
      "node": "103.wake",
      "snapshot_digest": "846e11d6909353d71f4c7c1c77e2ca1f830f86346d97b75bb016fe0ad272c46c",
      "version": 31
    },
    "200.wake": {
      "generated": "2026-10-29T18:43:20.698949+00:00",
      "head": "510d887472b2b6f9eb7bd70ad9b1b509016af7811e8e9e51ff1e84db6602e616",
      "node": "200.wake",
      "snapshot_digest": "3c26f6ea62481e4d55c3a68d5f28aa1ec8178994bad52e591dc1af19d1b4bc1c",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-29T18:35:04.009485+00:00",
      "head": "3a569c7d16bbb8d607b2851157f39b6b81983c75d18c3a116afa616389d3f21e",
      "node": "201.wake",
      "snapshot_digest": "a37798aba1d54410bab787b5a62547a1886f4951eda68c8abb701678b5451927",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-29T18:12:18.436124+00:00",
      "head": "82f28d0317597c3289352c49921c76918f1a548f829ecb5d69ba14b602ed6f2d",
      "node": "202.wake",
      "snapshot_digest": "4f750545b6192158c16295b76e254145299e55052cce61d6dd1b4a80bd25b7d7",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T18:40:10.262733+00:00",
      "head": "a30f38cd94fc4113703408caa922458acbf16a844a845cf24c068ccfc6753d3a",
      "node": "203.wake",
      "snapshot_digest": "40083f03a4db6440a02a2e1f58dd0ecf4ec82b0bc304996ab56993baeb6d94a1",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-29T18:36:32.998490+00:00",
      "head": "8634048d600cd4592f634b081c1c38652d8ed3296e27fd0230ba89da871566e9",
      "node": "300.wake",
      "snapshot_digest": "d2da26d511303ae488fa17fbc8782f1b46dfb0cfc55e95ee286af07002ff7414",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T18:27:59.453515+00:00",
      "head": "ce949dae2b77eb17cade5391ec9993ba5265476372c9a8b8bc7e62e43ee38c52",
      "node": "301.wake",
      "snapshot_digest": "89f7892715ab4715e28f2bbd82e31dbc115d89f44b2fa7ed72c326ab84e07900",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T18:31:22.360173+00:00",
      "head": "1e8895dedb617cbdf5f38b036a1706bf20fc653c4ce60561df2a38479d764625",
      "node": "302.wake",
      "snapshot_digest": "177d3c8445189fe857f7f39d648f07673bcc44bda5567dc8a4386bbaa3c6a2b6",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-29T18:12:25.014528+00:00",
      "head": "46c25e2e79c38bed20f1917b2c13e3c49e3e9d72bbad2c4255079ac023799e85",
      "node": "303.wake",
      "snapshot_digest": "1707d85faf96d2ce0c830347e26f1c0ac0c31419451eb55c472fb9ebfe78a705",
      "version": 24
    }
  },
  "version": 307,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d39643662363762633731653534656166.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d35613335376465613566633834333935.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d696e7472696e7369/632d676f616c2d666f726d6174696f6e2d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.


---

<!-- Source: limitations.md -->

# Limits and open challenges

The task-list demonstration is intentionally small. Three decisions and successful
replay do not establish production resilience, useful research, superior model
reasoning, lower cost or energy savings. Those claims require separate evidence
and appropriate comparisons.

Recorded acceptance means the selected rules accepted a proposal. Poor rules,
incorrect evidence or an unsound interpretation can still produce an accepted
result. Hashes and replay check consistency relative to retained history; they do
not prevent a privileged operator from replacing a record and its reference data.
Independent retained witnesses and trustworthy deployment practices matter.

Kernel/application separation is an architectural constraint, not a sandbox for
arbitrary trusted Python code. A local operator with filesystem access has powers
that an untrusted model proposal does not. The public website has neither those
powers nor authority over research.

A public export is a dated view. It cannot prove that current source is loaded in
a resident process, that research is running, that the hosted page is current, or
that another installation holds equivalent records. Missing information is not
permission to reconstruct a convenient history.

Public research exports omit private/provider bodies and may namespace identifiers
in aggregate views. A retained source-event hash identifies historical provenance;
it is not a hash of the filtered JSON beside it. Do not claim full authoritative
replay from those views alone. The isolated task-list artifact separately retains
its complete recorded proposals for checking that fixture's event hashes.

A compact orientation also omits detail. Inspect the implementation and tests
before relying on compatibility, migration, transaction or failure guarantees.
Successful offline tests do not measure provider reliability or real-world
research quality. No external model evaluation is claimed here.

Model-backed work depends on external providers' availability, quotas and output
quality. Providers may fail or return plausible but unsupported proposals; a
recorded failure or deferral is not accepted progress. The task-list fixture does
not exercise that provider boundary. Compressed context can lose relevant detail
or emphasize the wrong information. References and hashes help identify retained
sources but cannot restore source bytes that were never retained or are missing.
Replay may fail on damaged or incomplete history; reconstructing domain meaning
can require the matching application version and evaluator. The demonstrated
three-decision fixture does not cover every migration or recovery failure.

An independent critic should ask whether ordinary transactional applications,
event logs or workflow engines already meet the need with less machinery. Require
a concrete workload and comparison before accepting the cost of another layer.
Identify both guarantees the kernel enforces and obligations that remain with the
application, runtime, operator and reviewer. Record counterexamples and unsupported
claims alongside any favorable findings.


---

<!-- Source: evaluate.md -->

# Evaluate as an unfamiliar observer

Start without assuming WAKE is useful or deficient. Read only the material needed
to answer each question. Record what you inspected, approximate reading time or
word volume, source locations and unavailable evidence. Do not turn a supplied
explanation into an independently verified finding.

1. **Purpose:** After the orientation alone, can you explain the concrete problem
   WAKE addresses and what the task-list example demonstrates? State remaining
   ambiguity and how much reading the answer required.
2. **Authority:** Can you correctly distinguish kernel rules, application meaning,
   runtime/operator powers, model proposals and public views? Trace one accepted
   and one rejected decision without granting the mirror operational authority.
3. **Traceability:** Can you follow each example decision to its receipt, reason,
   application revision and final state in `demo.json`? Identify missing links
   instead of inventing identifiers or history.
4. **Reproduction:** Can another person run the documented offline command and
   confirm accepted → rejected → accepted, revisions 1 → 1 → 2, and verified
   replay? Separate observed reproduction from merely reading a reported result.
5. **Historical change:** Is it clear how corrections or changed rules preserve
   earlier meaning? Which behavior is demonstrated here and which needs another
   test, migration fixture or independently retained witness?
6. **Claim discipline:** Which claims are supported, unsupported or contradicted
   by the available artifacts? Distinguish record integrity from truth, accepted
   work from external accomplishment, and input size from reasoning quality or
   energy use.
7. **Practical value:** For a specific workload, what does this add over a normal
   transactional application or event log? Identify complexity, trust and privacy
   costs, plus a simpler alternative that deserves comparison.
8. **Independent challenge:** What failure or counterexample would most change
   your assessment? Recommend the smallest discriminating next test and say which
   conclusions remain unknown until it is performed.

## Record the assessment

For each question, use **0 — unsupported or materially wrong**, **1 — partly
supported with a material gap**, or **2 — supported by cited inspected evidence**.
Use **unknown/not examined** instead of assigning a score when evidence or access
is missing. Keep claims, source references and uncertainties beside each rating;
a total alone is not an evaluation. Give reading volume/time separately from
accuracy, traceability and unsupported-claim counts. Do not reward agreeable tone
or penalize warranted criticism.

If a person or another model performs an assessment, preserve its actual dated
response and supplied material privately before deciding whether to publish a
reviewed version. Label evaluator identity as attested when it is not independently
verified. Do not claim an external review occurred, invent quotations, or infer
consensus from one response. No external assessment is included in this bundle.


## Exact offline demonstration artifact

```json
{
  "application": {
    "id": "example-task-list",
    "version": "1"
  },
  "checks": {
    "expected_decisions": true,
    "expected_revisions": true,
    "full_replay_matches_current_state": true,
    "rejected_state_unchanged": true,
    "research_record_absent": true
  },
  "events": [
    {
      "created_at": "2026-10-17 22:15:59",
      "event_hash": "37aed91c7aa29e8bfa1debf0b35ad2174a22458d8d4c2932825cceedacac9f65",
      "previous_hash": "0000000000000000000000000000000000000000000000000000000000000000",
      "proposal": {
        "based_on_revision": 0,
        "operations": [
          {
            "action": "apply_application",
            "key": "example-task-list",
            "value": {
              "action": "add",
              "application_id": "example-task-list",
              "application_version": "1",
              "input": {
                "id": "f49f094b497e4c2684b754b322ee0d0f",
                "title": "Verify independent kernel application"
              },
              "next_state": {
                "f49f094b497e4c2684b754b322ee0d0f": {
                  "completed": false,
                  "title": "Verify independent kernel application"
                }
              }
            }
          }
        ],
        "proposal_id": "db76bf4c83df40ceb83a1761bab108cb",
        "rationale": ""
      },
      "proposal_id": "db76bf4c83df40ceb83a1761bab108cb",
      "provenance": {
        "how": "Deterministic governance and serialized record submission",
        "receipt_schema": "wake-receipt@1",
        "what": "accepted: add (proposal db76bf4c83df40ceb83a1761bab108cb)",
        "when": "2026-10-17T22:15:59.095235+00:00",
        "where": "Execution location not supplied",
        "who": "Caller identity not supplied",
        "why": "Reason not supplied"
      },
      "reasons": [],
      "receipt_id": "3ac67ebe-188a-4c56-9305-ed808a303bed",
      "revision_after": 1,
      "revision_before": 0,
      "sequence": 1,
      "status": "accepted"
    },
    {
      "created_at": "2026-10-17 22:15:59",
      "event_hash": "e1399a6aaf9735e13cb3dfacae08f4fbc4e4a759f5e5ccd2fdca227f5004a6ce",
      "previous_hash": "37aed91c7aa29e8bfa1debf0b35ad2174a22458d8d4c2932825cceedacac9f65",
      "proposal": {
        "based_on_revision": 1,
        "operations": [
          {
            "action": "apply_application",
            "key": "example-task-list",
            "value": {
              "action": "complete",
              "application_id": "example-task-list",
              "application_version": "1",
              "input": {
                "id": "missing-task"
              },
              "next_state": null
            }
          }
        ],
        "proposal_id": "a80245635ce6446ba3a62acdcb993bfd",
        "rationale": ""
      },
      "proposal_id": "a80245635ce6446ba3a62acdcb993bfd",
      "provenance": {
        "how": "Deterministic governance and serialized record submission",
        "receipt_schema": "wake-receipt@1",
        "what": "rejected: complete (proposal a80245635ce6446ba3a62acdcb993bfd)",
        "when": "2026-10-17T22:15:59.098099+00:00",
        "where": "Execution location not supplied",
        "who": "Caller identity not supplied",
        "why": "Reason not supplied"
      },
      "reasons": [
        "task does not exist"
      ],
      "receipt_id": "f41f3313-3a4f-4adb-8418-d5c954fd6db5",
      "revision_after": 1,
      "revision_before": 1,
      "sequence": 2,
      "status": "rejected"
    },
    {
      "created_at": "2026-10-17 22:15:59",
      "event_hash": "021d45f244f9e2de5a21429c031bbef74e9a703582acbfc6c90b4f233475e45a",
      "previous_hash": "e1399a6aaf9735e13cb3dfacae08f4fbc4e4a759f5e5ccd2fdca227f5004a6ce",
      "proposal": {
        "based_on_revision": 1,
        "operations": [
          {
            "action": "apply_application",
            "key": "example-task-list",
            "value": {
              "action": "complete",
              "application_id": "example-task-list",
              "application_version": "1",
              "input": {
                "id": "f49f094b497e4c2684b754b322ee0d0f"
              },
              "next_state": {
                "f49f094b497e4c2684b754b322ee0d0f": {
                  "completed": true,
                  "title": "Verify independent kernel application"
                }
              }
            }
          }
        ],
        "proposal_id": "8929412e447245a28051aeba385bd52a",
        "rationale": ""
      },
      "proposal_id": "8929412e447245a28051aeba385bd52a",
      "provenance": {
        "how": "Deterministic governance and serialized record submission",
        "receipt_schema": "wake-receipt@1",
        "what": "accepted: complete (proposal 8929412e447245a28051aeba385bd52a)",
        "when": "2026-10-17T22:15:59.101065+00:00",
        "where": "Execution location not supplied",
        "who": "Caller identity not supplied",
        "why": "Reason not supplied"
      },
      "reasons": [],
      "receipt_id": "5b1579ba-04ff-4ce5-a604-2babb0f18663",
      "revision_after": 2,
      "revision_before": 1,
      "sequence": 3,
      "status": "accepted"
    }
  ],
  "format": "wake-kernel-inspection@1",
  "generated_at": "2026-10-17T22:15:59.105547+00:00",
  "limits": [
    "Offline synthetic task-list demonstration, not accepted research or a live service.",
    "Application rules and decision semantics are deterministic; UUIDs, receipt timestamps and exact hashes vary between runs.",
    "Hashes detect edits relative to retained bytes and head; they do not authenticate the author or prevent replacement of the entire artifact.",
    "The artifact records checks performed during generation; a static page does not rerun the kernel.",
    "No model or provider is called, and no research record is opened."
  ],
  "reproduction": {
    "command": "python -S -m examples.task_list.inspection --output demo.json",
    "example_command": "python -S -m examples.task_list.run --data FRESH_TEMPORARY_DIRECTORY",
    "requirements": [
      "Python 3.11 or later",
      "standard library only",
      "this source checkout"
    ]
  },
  "result": {
    "head": "021d45f244f9e2de5a21429c031bbef74e9a703582acbfc6c90b4f233475e45a",
    "receipts": [
      {
        "reasons": [],
        "revision": 1,
        "status": "accepted"
      },
      {
        "reasons": [
          "task does not exist"
        ],
        "revision": 1,
        "status": "rejected"
      },
      {
        "reasons": [],
        "revision": 2,
        "status": "accepted"
      }
    ],
    "replay_verified": true,
    "revision": 2,
    "state": {
      "f49f094b497e4c2684b754b322ee0d0f": {
        "completed": true,
        "title": "Verify independent kernel application"
      }
    }
  },
  "scenario": "task-list-three-decisions",
  "source": {
    "dirty": true,
    "files": [
      {
        "path": "wake/__init__.py",
        "sha256": "f78e2a2f3719c327ce7b9979fe3d43f41cf5d1ff63b141b49fb60af94e38c080"
      },
      {
        "path": "wake/kernel/__init__.py",
        "sha256": "0833c3f9440d5e7f5a66732a6536d6724e27550569df359c50533620d2df6955"
      },
      {
        "path": "wake/kernel/applications.py",
        "sha256": "97ed1dfb24f1dd4861210c161cd8a85022072cb9756cab072261cb2417913540"
      },
      {
        "path": "wake/kernel/compression.py",
        "sha256": "ca8ab7e0fbe60a560816db571c2f58b06e0d19bf4de889a0a5812d68222b5efa"
      },
      {
        "path": "wake/kernel/generation.py",
        "sha256": "d6fa548adf8ef3ddc7613a53d984ded775ea7f5651ae86640933e6b57037b406"
      },
      {
        "path": "wake/kernel/governance.py",
        "sha256": "841b57552731a6650ce87d91e715eb2e9817395ae34340fa314a88a201fbd221"
      },
      {
        "path": "wake/kernel/kernel.py",
        "sha256": "23761107a3c71c2aa856ddd97aeae695b34b4cb9c9ba8d3cc856e2afb1f2e0e9"
      },
      {
        "path": "wake/kernel/matrix.py",
        "sha256": "6458eb9ace3e4c071c0e5fdd3d8fd469e3942e1ab5055451ff8260598817a053"
      },
      {
        "path": "wake/kernel/models.py",
        "sha256": "834465849a2d060981fb04eacd0c1ccc96a490566279e43192bcdc705ca89474"
      },
      {
        "path": "wake/kernel/observability.py",
        "sha256": "045034d65e67871ccb21fd24ce9b44ef4c8a0c233388b2a220eac68450a9b2db"
      },
      {
        "path": "wake/kernel/providers.py",
        "sha256": "bed7f832b3dc3dd40d3c8b1797ad547b9e06e59108d7a41bc1fc7aa2fe857220"
      },
      {
        "path": "wake/kernel/receipts.py",
        "sha256": "e9b63f4dc11e4ba0fbf9949c19540614b78965dc063892dfcbd6d3f085c7886a"
      },
      {
        "path": "wake/kernel/record.py",
        "sha256": "c88666ded959426af873c8a6323830eeeb953943d034c3a9eac01b9bc814bf94"
      },
      {
        "path": "wake/kernel/runtime.py",
        "sha256": "a532ee8c3b3c5da944e6f1793e2ee1d5f96955b6d8458bbb2e6a64397319aa5e"
      },
      {
        "path": "wake/kernel/storage.py",
        "sha256": "09b9c5dbdc47193f700b94b6daa5dd1aff876edc91178c2856deea5d47208a0c"
      },
      {
        "path": "examples/task_list/app.py",
        "sha256": "8111a898e01023236849171411d51fb7112488434fa875d27ca18e1b7728848e"
      },
      {
        "path": "examples/task_list/run.py",
        "sha256": "a1894b159cac5067337b2135fb15c7d956b507271c815b3fffa16a1572ded20a"
      },
      {
        "path": "examples/task_list/inspection.py",
        "sha256": "cb74f47bbd490a39a4f1154651ec414adbb6817f64b1749c800b11541478f132"
      },
      {
        "path": "tests/test_kernel_boundary.py",
        "sha256": "c65b932670f30278833e7ff405d39c32de655b86811b079a20c6825f661463c4"
      },
      {
        "path": "tests/test_inspection_demo.py",
        "sha256": "f181f71293536a7d27a894d4eb02ba46c8e78a8c6bcf8fe3441028c473ad3b1a"
      }
    ],
    "git_revision": "fcec49b269b8a7609414683fe923c05019e91a7b",
    "scope": "Exact listed source-file bytes; Git revision is descriptive, not proof that a dirty checkout matches its commit."
  }
}
```
