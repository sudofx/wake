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
  "generated_at": "2026-10-30T20:46:20.493733+00:00",
  "head": "snapshot:aa62022ea79561324bbb71db0dfba724c6ae51badeb0e272bc21c6c0cde748ff",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T20:46:20.493733+00:00",
      "head": "a922a3c41cbdcb6e83994364c83fddf38d6359aad4a046225011705bd87c1b2b",
      "node": "100.wake",
      "snapshot_digest": "79099dd2bf51832fcc71597add174bf1af87cd79c0a1564bc16a23105b606f22",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T19:39:27.718548+00:00",
      "head": "79430282725545efc8ee572785899e79cc41e7d2ba1a778c47d172952a903272",
      "node": "101.wake",
      "snapshot_digest": "cd00c079cba34236a46c6345a8163648d1652201a46b281f19ffbc3c5bfb95ec",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T19:39:26.134199+00:00",
      "head": "fcaf587a5bbb55af9929971d21bd4ae6c4368d0b7259198bd4f5ffab12aa81a1",
      "node": "102.wake",
      "snapshot_digest": "ed54c574de89065d638a27aae1ebdb815323307f90261d68c02f4aa1a4e1a955",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T19:39:29.382639+00:00",
      "head": "945c9860e63a2a14d1867056908d01fa72a251db1f3cbbd6609f3c153c1c7db0",
      "node": "103.wake",
      "snapshot_digest": "8c57f51143b1f26ebf6de89e56192a34fc6946ac6ff9f9e971d0d1d84363f9d3",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T19:39:41.003419+00:00",
      "head": "c76c71ecff4bedbeb3f05b331d2fd6c613bfc8263a850a0034e6df66cdf916f1",
      "node": "200.wake",
      "snapshot_digest": "dfc767363a49f39f217f9ed7f78f957fc0db11a67601a72d99b9abf890ca39bf",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T20:44:36.568090+00:00",
      "head": "7cc3de755f446471827792694555b1e3789fc1c2dfeb4f864cfbf3ae5084e773",
      "node": "201.wake",
      "snapshot_digest": "5edcfdaace9226f002d887d6e173609b9873a0d7dac632751601cfff78f12540",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T19:39:26.673167+00:00",
      "head": "f0adb9d2e7d3fdb04d8238f8d7779688f7776c8bcc5a2b064c5054511bff62f8",
      "node": "202.wake",
      "snapshot_digest": "c85b4b9c1e594e1df7b9a1f6d7eddbbd57491b426c5a22ae70f50890973a8148",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T19:39:30.730857+00:00",
      "head": "6402c7f9667747ab49aa8e4391be3f647c4c280cd69ef2dd4371f4d68c28cb10",
      "node": "203.wake",
      "snapshot_digest": "5b991fff3ce32e0cbfbcb01e7737177954f7f73e790b8a4a3592209d2f0413a3",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T19:39:36.170610+00:00",
      "head": "44f21b3d653d826aec25f1bf4b0b85749b049204879b7be1aca0f6df5a6865ec",
      "node": "300.wake",
      "snapshot_digest": "0b1ba7a9fd8705cf8c782190eee6407b2c4fdceea9a1f29f2bf1816ff7f5948b",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T20:42:54.824995+00:00",
      "head": "74145706708201e18ffa67e5a681cb352947e4fd28a3c0d340f9cc55639d2a9e",
      "node": "301.wake",
      "snapshot_digest": "28a18ccfff18ab6f0f58b1a28f2aee780e5bd0391e85266a31036f54f338b693",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T20:46:00.449055+00:00",
      "head": "541e08506a78fa6f1420f4482ede7c3c95b2618aa2392962ace6b275a1451dd6",
      "node": "302.wake",
      "snapshot_digest": "55d75c0eadd419ea19604ffe79d7aaa25cf75860e2603b7fc2ae240ddae79bf0",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T19:39:29.485068+00:00",
      "head": "673c4c2c7870f8e1170c1c83d58105e852736502fc513e11fbe57e953f5a257d",
      "node": "303.wake",
      "snapshot_digest": "de03cecf9220a00a5d6115fad56377b82cf15b9be037806e4f4ebe4de0231527",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d30383330376139626133363934666437.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32373633373035353739656434336161.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
