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
  "generated_at": "2026-10-27T12:22:53.083335+00:00",
  "head": "snapshot:6e765f240f513e0775ff3f86bd94b1c2319ceee22712048a8da803615d34bf9a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T12:22:48.375257+00:00",
      "head": "d332e25e5374bfcdd77a1f67cedf21c8c8521dd28d0a237ec6310a095fcf94d8",
      "node": "100.wake",
      "snapshot_digest": "2635191371f320a30d5348fac7d58bd7b22c78a9f62720ff926ca2f4597205ae",
      "version": 1
    },
    "101.wake": {
      "generated": "2026-10-27T12:22:48.438983+00:00",
      "head": "2c6108e658b6752eb492a976a93dc0385a7a96346035e7829ea5354e3ab0c1f3",
      "node": "101.wake",
      "snapshot_digest": "bd33db6dbb228fced71262428c03d49515e6e4bde762244e84c5c4f185a01769",
      "version": 1
    },
    "102.wake": {
      "generated": "2026-10-27T12:22:48.475087+00:00",
      "head": "2f890196ac0d4203ccb1aae9ccd0a1e09cc7cce274edd46c04df2d3a74cbc412",
      "node": "102.wake",
      "snapshot_digest": "f53917eb28c017f7b816842c468e9444fcbed73a4b3f850a0f610851127b1805",
      "version": 2
    },
    "103.wake": {
      "generated": "2026-10-27T12:22:48.472756+00:00",
      "head": "7145ebe99b9723b04ab0c7f8fbef3991e74879088c93d5bf045b23dc7dda22a7",
      "node": "103.wake",
      "snapshot_digest": "693107c3980fd2806a2a3b1202654f4054ecc5ef84ee250efce1c42f97d67915",
      "version": 2
    },
    "200.wake": {
      "generated": "2026-10-27T12:22:48.524135+00:00",
      "head": "ad025973476e9a0394140b3b791e6b78e4ca68d9640b78f84431b0e7a89edb1b",
      "node": "200.wake",
      "snapshot_digest": "d77172454eff5ceb1bea0a81fcc172669254433a1051f338fd67735802f4bb99",
      "version": 1
    },
    "201.wake": {
      "generated": "2026-10-27T12:22:48.554331+00:00",
      "head": "28e9e56c19ec2cfbd96c444779078091251ee087f70fe1323ea5df073c22a898",
      "node": "201.wake",
      "snapshot_digest": "243ea2024ee2eb1c6df2004a45d622dfc792c307fcb11398d8f1ac2842dbbacd",
      "version": 2
    },
    "202.wake": {
      "generated": "2026-10-27T12:22:48.414243+00:00",
      "head": "0b5aa2119b677d580ef3a90a6a55713737d05d3e7516048e3dfc487b906d2ad8",
      "node": "202.wake",
      "snapshot_digest": "8dace31476cc75408a48a9e485a013874f85ffcbff30c6fa478bb7e19dc4f598",
      "version": 2
    },
    "203.wake": {
      "generated": "2026-10-27T12:22:47.980053+00:00",
      "head": "5c69b645a2d0e2d20e82932fd399b6991c4272786573ffb8526cddc4974f4508",
      "node": "203.wake",
      "snapshot_digest": "9337cc629b85520784d02f223b9b162593ecf9c6dda7b0e80c6920affe6ecdd7",
      "version": 2
    },
    "300.wake": {
      "generated": "2026-10-27T12:22:48.624184+00:00",
      "head": "bc14ec6362aa4a80535566ff5601e1cf112c33978ad5808a0eadefa89187395e",
      "node": "300.wake",
      "snapshot_digest": "4170ac2f4b55049847e6f48161db3f5f6535768b892a1532029b256e70afca12",
      "version": 2
    },
    "301.wake": {
      "generated": "2026-10-27T12:22:48.454089+00:00",
      "head": "01fba2457cadc7e5d576b75f37690b4ec721c01922c4346c46129c2ff083c515",
      "node": "301.wake",
      "snapshot_digest": "1fa316672dbd15b73e1cc51011fab379a8fb371f53783d21096c532ec139bb3c",
      "version": 1
    },
    "302.wake": {
      "generated": "2026-10-27T12:22:53.083335+00:00",
      "head": "933f904037c609e8fb4dce2f03015ab18db0492c0469b610b41453f7679e19f3",
      "node": "302.wake",
      "snapshot_digest": "54a6b4466881c9c0ea5959888dbdf2674c5cdf27d065be72622a813721211846",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-10-27T12:22:48.433488+00:00",
      "head": "fe2fe1a792ae965365782823582a6bd63cf49900826c52fd6f1083507ce652f7",
      "node": "303.wake",
      "snapshot_digest": "b3cd11a3968dd07af4c95f938ce403f3bbc87ca94e0ea09c1208328eaa93ec78",
      "version": 1
    }
  },
  "version": 19,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d656161336465393639376339343337/61.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d63633139643537326266306434336134.json)
- [notebooks record](../reader-records/notebooks/3230322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d6d656d6f72792d69/64656e746974792d30312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
