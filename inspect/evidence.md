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
  "generated_at": "2026-10-24T15:38:23.087014+00:00",
  "head": "snapshot:b3585ba16e9aaaff07a48b78265ebb94bd759ce273b760f6e356deee28144f31",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T15:36:16.001288+00:00",
      "head": "d23740c441ff2c5da70d2a56c98f5e9220da05395f404a9bf68c48c563380e76",
      "node": "100.wake",
      "snapshot_digest": "9b42a241bbd62272caf27f8c3c88f31d8cca3dd106ccd970bcebf53de51c2ebd",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-24T15:13:56.491004+00:00",
      "head": "d7c15485d6b5a438af017a8e577111289e7773200711a033e68319d1f912f67f",
      "node": "101.wake",
      "snapshot_digest": "eb9f97db275a25b682d5a81f580be3d9bf15b9374181e3a32e71ef7352d44f34",
      "version": 36
    },
    "102.wake": {
      "generated": "2026-10-24T15:33:56.560742+00:00",
      "head": "6798d3b80f5f93ae474abb012d849cc7f3631c30d7ac308c23c1f1cb6d8195b4",
      "node": "102.wake",
      "snapshot_digest": "63a238ed6c7b804eacf92d33a73bcb9d181c2d4b2b8e667e8f41cc0848c0a27d",
      "version": 46
    },
    "103.wake": {
      "generated": "2026-10-24T15:17:17.509069+00:00",
      "head": "be8baf783ea5b4a2223a0c291e5d44e6a55f0ad12f72fc7ace5f23cfdfb43e36",
      "node": "103.wake",
      "snapshot_digest": "e659c5d14785fae92d806d0ea62c71291161fab434388a9076ba91e7f873fc0b",
      "version": 34
    },
    "200.wake": {
      "generated": "2026-10-24T15:10:35.659233+00:00",
      "head": "ffe2eca31b28b6a16e07cdd563596bdd8e8120f0eb66bd94ed199691a336d6c7",
      "node": "200.wake",
      "snapshot_digest": "5f63496d864530f2e8011044b7f289c00457c199ec35747d2d6be3ef3b93f378",
      "version": 26
    },
    "201.wake": {
      "generated": "2026-10-24T15:34:45.536860+00:00",
      "head": "4d394214b015afd9ee909c793e61e515554998645509053d13076c4e077d57c0",
      "node": "201.wake",
      "snapshot_digest": "e8221ddf8dd15883c7cfbdacf058df58ebc9954d5fd6e05f2580d782cd231684",
      "version": 34
    },
    "202.wake": {
      "generated": "2026-10-24T15:38:23.087014+00:00",
      "head": "24ea811f0808e12832bcd8cb3ca5211dfe28f88be0b8d0c69dbb08cc7f87190f",
      "node": "202.wake",
      "snapshot_digest": "8e040fd692510ac113904980b8c8c9f5bb96f05171bb7ac0a7d9a76d4a5cf534",
      "version": 44
    },
    "203.wake": {
      "generated": "2026-10-24T15:37:09.066681+00:00",
      "head": "b3108933399c0223800e9b52deca032ca144028789e0bf738ee7e53ead3489d2",
      "node": "203.wake",
      "snapshot_digest": "9246a853989167526bae36c12d4d7208e4647b18f87ddcd98f9f6b89ddb99101",
      "version": 25
    },
    "300.wake": {
      "generated": "2026-10-24T15:36:46.531562+00:00",
      "head": "a238daf2637a1a49d31c0de536538bdf849f1b561bd524b7c35428d655996cea",
      "node": "300.wake",
      "snapshot_digest": "c5090bc6c8c0d7d135c1d6ea4e2fc60855d6130a0b11c4d70197408ef917cde0",
      "version": 28
    },
    "301.wake": {
      "generated": "2026-10-24T15:34:16.066123+00:00",
      "head": "53d881d5f228760d0205b037234b225b307adbb9c2d47669ad3361d9ef44cabe",
      "node": "301.wake",
      "snapshot_digest": "81dc4c09c3b1594a3f6d8de8801c8cfc66bbce6f3bf643b2bc8d440d913b499d",
      "version": 47
    },
    "302.wake": {
      "generated": "2026-10-24T15:10:27.271876+00:00",
      "head": "9e3d161cf30fc9cf3a17428d7713d599b08925eec3e3c974f26a6cadde165e5a",
      "node": "302.wake",
      "snapshot_digest": "416cec3029bc2e775a9a98e15c50118aac2f70cff1bad70a5f83913298b30824",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-24T15:04:03.481963+00:00",
      "head": "d4040dbff927ea66a7309c4260e4a6e1035cb2a9c02acd21a98be0935f55ef4e",
      "node": "303.wake",
      "snapshot_digest": "48c602f0ccabb0a5cb30e5ffe824858714bb2d3cf038ef1c6eed660c3b32e841",
      "version": 44
    }
  },
  "version": 413,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d37646336356366666131313634623061.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d39623861663761663334646334383130.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
