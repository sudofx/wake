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
  "generated_at": "2026-10-29T20:17:25.343716+00:00",
  "head": "snapshot:d932d28d470e56dfebd508a8c029b74b038673536faf3acd8055555d96a1f67d",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T20:17:25.343716+00:00",
      "head": "68ce56f0f5116009256b76d06c427f1db2436214c17776fd3c83e76aa9396feb",
      "node": "100.wake",
      "snapshot_digest": "beecb57bd6f66dbf361bc03582995ae96b0f14ded84c076174fcc994012e1b19",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-29T19:14:32.501960+00:00",
      "head": "e1136b8f0e80b14730f69e352075d5a3175af2a2b422af7fbcb8e733721ad7be",
      "node": "101.wake",
      "snapshot_digest": "48c9f85092ec79f29713d4943d33e1a8ed0de50e7f51f66dd853eff03e8d0780",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-29T19:15:52.993859+00:00",
      "head": "d0af59fc2c96d1fbbb0185032616166bfc6a59edf950526c3c6a8fe08291eb2e",
      "node": "102.wake",
      "snapshot_digest": "cbc86882eb9239f6c228f203634ba0be26ed2e42e765306dcfcf276491a9028f",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-29T20:06:36.997572+00:00",
      "head": "9d7f6a9bd43a5dd8397d1b0f0cc91607a2f933e55a86dd62622b79ebe2bf4f30",
      "node": "103.wake",
      "snapshot_digest": "214437652dee3eac4f75c1cad1ea9993a916a4137c65ce8234dd7926ba2b4394",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-29T20:16:57.167028+00:00",
      "head": "705903158d17a99858e72ace069c1b6c9c49e42e6e58d0256972ecc7ae0d703e",
      "node": "200.wake",
      "snapshot_digest": "f491d87c71c91ff22b9aa7746a0a0d75dd96bff1e2c8a78a8ed0b40b5f99a30e",
      "version": 28
    },
    "201.wake": {
      "generated": "2026-10-29T20:15:44.804432+00:00",
      "head": "2e4c8c026918e7a4991381f63dfcd9131c8f2e4048a7197091bb7c1c94233128",
      "node": "201.wake",
      "snapshot_digest": "b36e4909198c2c810bb3a5f0840d83f78484f9ba646f555f9272992f7c79d55d",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-29T20:14:39.182886+00:00",
      "head": "45138bfaf231134fffb39c149d4b922051efeaf68dc46b858f80589f4138dfe9",
      "node": "202.wake",
      "snapshot_digest": "689425b0afd5aa3ca3d9760e340dbfc7a7a0d2fa2980a6d89b1d6711aa453f23",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T19:38:12.376728+00:00",
      "head": "75ecf106896a3b90fb644308ee8a90be4872b04058722cbaa38cd8e01daf23e0",
      "node": "203.wake",
      "snapshot_digest": "8017f88d9901a06f44651c295f50681c2325b996cd7a803fde43a7848e315af8",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-29T20:09:52.545976+00:00",
      "head": "70143e423544bc0513ead54496df02756457f16de3ea3172e8c965b503043826",
      "node": "300.wake",
      "snapshot_digest": "17717af15b6523511d35a913d72fc70175c5f630ad35f318e908c77e9785f545",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-29T20:14:32.193872+00:00",
      "head": "bd8a579ee3ffee18d177e72434c1f77ed845ce293fc87740cde191e3380d0722",
      "node": "301.wake",
      "snapshot_digest": "9959061efa493b60e3a3589ccb32c0883620facab8a134aef4db12466535675b",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-29T20:15:38.309294+00:00",
      "head": "281d6455bdc13e4b5ffa32020515e0399578f7c981fbdfbde266fbe3f188b37c",
      "node": "302.wake",
      "snapshot_digest": "4da3755e7d3544547ef980bdd2e3b37c2b8a63acda6b124536866066bbffa3e4",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-29T20:14:42.888153+00:00",
      "head": "4cff53f5fd2c1df22014bc9969d523c8f26d0633a640b355fa9a8c2fe1596600",
      "node": "303.wake",
      "snapshot_digest": "f96a8ee9613768c1c83f65f57343e7cc8dae6785665f5294810cfd877a8b3820",
      "version": 24
    }
  },
  "version": 325,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d30343834383037343339336334646664.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d61346137633132386337336134653038.json)
- [notebooks record](../reader-records/notebooks/3230332e77616b653a3a6e622d6d656d6f72792d6964656e746974792d30322d/3031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
