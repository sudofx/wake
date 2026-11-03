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
  "generated_at": "2026-11-03T20:54:43.259181+00:00",
  "head": "snapshot:aa92eeabd1a079d673c452c2d1114a5b18a40b829605607eda6d9cdee3328270",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-03T20:54:43.210483+00:00",
      "head": "91c34bc9d0cde1c2550d237907236ee80b0a93d1c0b44931b4385126b23ec357",
      "node": "100.wake",
      "snapshot_digest": "a843c3f4b6be372c993e53be2e226e85c3bd806c315c5c2f225596b681c12f4f",
      "version": 0
    },
    "101.wake": {
      "generated": "2026-11-03T20:54:43.259181+00:00",
      "head": "0e9e301f69d1874b6fbdb117aa0084c7eeec736c679f47c1931e70c4adae5c05",
      "node": "101.wake",
      "snapshot_digest": "a92a6489776dc9a0c2755ce27f0d5316ed81e573826226add63fe0cb938ba89a",
      "version": 0
    },
    "102.wake": {
      "generated": "2026-11-03T20:54:28.204153+00:00",
      "head": "9c2c0239b0257ed2ac67b91e7e295c9a9b7a9120da590dadea9d62218de8b42c",
      "node": "102.wake",
      "snapshot_digest": "5cc6109782caf91634f58df6c6409d8762b8f176a89b07fab84f548d4b19b4a6",
      "version": 0
    },
    "103.wake": {
      "generated": "2026-11-03T20:54:43.204564+00:00",
      "head": "54634c97203beaead650eebc0efd44ad1a1956623e8be3c7909a9ee88da26240",
      "node": "103.wake",
      "snapshot_digest": "455f16d4600a89e8a5e4a68478980817d9c25086e6c8ed4094cbf10c28b8cffc",
      "version": 0
    },
    "200.wake": {
      "generated": "2026-11-03T20:54:28.204946+00:00",
      "head": "0267b9521de88008133ccdc30852aceebab41995d4a05c66771fc32ca7c78cd3",
      "node": "200.wake",
      "snapshot_digest": "f671862abaaf4c23d709c34aa6eb4a0228b32d68c6f448073c0f9ef705255abc",
      "version": 0
    },
    "201.wake": {
      "generated": "2026-11-03T20:54:43.181700+00:00",
      "head": "f1b09b05198f1347b144986673a19962c387681637ea2145692faa1f45b75f8c",
      "node": "201.wake",
      "snapshot_digest": "9de89d9307b0282057cdf70c20f5be7897bf30dffc11419c365caa2c90b123ed",
      "version": 0
    },
    "202.wake": {
      "generated": "2026-11-03T20:54:43.250905+00:00",
      "head": "15066623bb483bdf3237bf35f98ba427da540504286ebfc823ad2dd83f24e3bb",
      "node": "202.wake",
      "snapshot_digest": "8a0bcbada9fb52b0301d82df409b099dcffa87edb13448a75154a3ff25c38d7f",
      "version": 0
    },
    "203.wake": {
      "generated": "2026-11-03T20:54:43.174649+00:00",
      "head": "22714f0a92f271296351760e713694a9003f68772b9682be839e1b9680347435",
      "node": "203.wake",
      "snapshot_digest": "d09543e03b39e27544e420d13a1cbc881b12206c994f0de84d1ed00827c7bb7f",
      "version": 0
    },
    "300.wake": {
      "generated": "2026-11-03T20:54:28.202809+00:00",
      "head": "3e244c1a14450479c7968a6a651468112ff10da31f9fe538a7f2fdea63158286",
      "node": "300.wake",
      "snapshot_digest": "651d7696a0378b8fa8fc2c12e3a387d10f1f4ea5ca94346d2ce9c95481174d99",
      "version": 0
    },
    "301.wake": {
      "generated": "2026-11-03T20:54:43.203464+00:00",
      "head": "6aaf74b52e9a524ebb030e727ed6d26af9bf2605db822904decf1a418f032dfe",
      "node": "301.wake",
      "snapshot_digest": "e9cd00b0a9a239b92c10f8fb08c5eb0e8c92c7181519a118d1b3dcd34a32e2af",
      "version": 0
    },
    "302.wake": {
      "generated": "2026-11-03T20:54:28.221385+00:00",
      "head": "56b0ee6620d26e7628129b7e6e611e70a93d8c9bdd8666ab27af01e268f7c753",
      "node": "302.wake",
      "snapshot_digest": "1c791769a08df343098f3acc2a15f27334149b0ffd2dcb6058e9c1b170cf6adc",
      "version": 0
    },
    "303.wake": {
      "generated": "2026-11-03T20:54:43.245800+00:00",
      "head": "fc7b571fb29e39b387ea165f5ce8e6af28165eed8c8969700dfd5c78433adbb1",
      "node": "303.wake",
      "snapshot_digest": "83283cb13c313fe9fc6ee82df6fa9a1da111a54d393059b1b0a0d0acedbd098c",
      "version": 0
    }
  },
  "version": 0,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

No matching bounded example records were available.

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
