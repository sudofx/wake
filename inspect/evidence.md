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
  "generated_at": "2026-10-28T02:13:30.269325+00:00",
  "head": "snapshot:a368cafd84670c7000072284faa0463bc20bbb6afe893d7a3e89669e7e7ccbd6",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T02:13:17.964298+00:00",
      "head": "cbe5b64d0bcac387105e813b8e87767933d97259aaa4e674ed0a9dbe0257877d",
      "node": "100.wake",
      "snapshot_digest": "7030b70212dd1caf61442455b8039aaaf15f94f52c0b5b6566f8705be49bdefd",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T02:13:15.999809+00:00",
      "head": "394141d90a1fbe1495c92c486fb9b50d919cab95f35b1ac0039dce5bf9335c95",
      "node": "101.wake",
      "snapshot_digest": "1b49ec8fefadbd9b76781253b77b529fe615ba1bcb35adc7f3620e126a114373",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T02:13:18.298166+00:00",
      "head": "2e2b8b3f1cd72c35f93c96b694d49839e962ca7c4d2babbf529082009cc74914",
      "node": "102.wake",
      "snapshot_digest": "8f2db495ad1730497ee1383c7eae4b87d6cca3c2df0a2cf58839f7dc9294ad6b",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T02:13:23.565645+00:00",
      "head": "11a6d19366f10a5565175982df35c56ba15534e7a103c73f7d37ba0df819d2b7",
      "node": "103.wake",
      "snapshot_digest": "2d87646b538f061b2cab2b2f5d71cd9974a2f4d2a61a63d13119c8bd0c39920b",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T02:13:28.667437+00:00",
      "head": "5b1ade214b3e195d2e165ff0f7259c1b1f8c91ef996e170f413c4be81057ee33",
      "node": "200.wake",
      "snapshot_digest": "09503a951cd4d6f21252d106a9197ba15039bfcf6f668f96ad167a0ea1a03988",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T02:13:30.269325+00:00",
      "head": "bb5906f8c248c9b84dd82923380c363e0f7217987b91b59f2c0ee9b44c75d38a",
      "node": "201.wake",
      "snapshot_digest": "55fcacc505622bf2cc9fa4d09fae14b5ac214a477ad9858f0bfb68669e4b94f4",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T02:13:16.743421+00:00",
      "head": "fd957b84e9bd0a9734904db667358c23e87cdd136d7e2f187455eef074dd07f4",
      "node": "202.wake",
      "snapshot_digest": "78c1df63b96f08916655bad7cb75e42abaeac03f8d121b1de20aab52306dd757",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T02:13:16.583465+00:00",
      "head": "99fbbf71ed6ea29afe97af1f1511b47367bff0d1af45970de635a569c01ac546",
      "node": "203.wake",
      "snapshot_digest": "eb4d7ff11b670e8cf854b1cd555b74d4d921cf765d75f0fead765b9a5dd6d713",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T02:13:17.272250+00:00",
      "head": "9d63c139be0e448836e6720f39df79e6b78aed96044630f5d201dbe2c9033b15",
      "node": "300.wake",
      "snapshot_digest": "4f1ef0015d0f7f2e5b1b56d081ed33ffd86bbe8aa7ba21d4e90bac6bcde63b66",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T02:13:24.638022+00:00",
      "head": "3110846e3f8106d36217e01348900638a88e2ded23d69592036bf13f81f893aa",
      "node": "301.wake",
      "snapshot_digest": "2f16b443e793cb22fdaf3ff616ee408605c9e03e5deb896e19b0ded94eecac60",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T02:13:07.373361+00:00",
      "head": "f9d6f6440d946f02e1544e9b6aaa4699273093a9ff34626b8ed5aa5bd02af930",
      "node": "302.wake",
      "snapshot_digest": "32051681b44ae11a87cb35f855e2dd23e27161f7bbac3887ca33354b3fdcab43",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T02:13:16.964896+00:00",
      "head": "c336e392f2e825076754d30a39b9ff219ad416a5dfbc792274ea848f0d61eb11",
      "node": "303.wake",
      "snapshot_digest": "0257808b12b68f5583ea51212097de399e1fd57561f096b1940fca1f8cf7d694",
      "version": 15
    }
  },
  "version": 152,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d38663661653636336132613734326266.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d35376338623037663131643834396435.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
