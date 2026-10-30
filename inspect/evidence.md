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
  "generated_at": "2026-10-30T21:21:03.161767+00:00",
  "head": "snapshot:9e31e15fe88f06fcf7fcf62111de7444f45d2e70ae03a8c8ba61af5a0fa56d7b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T21:19:13.386972+00:00",
      "head": "c854555a1dae63df3ae8a77ad69f0c33cc22f61873e03d76de85152f8636b585",
      "node": "100.wake",
      "snapshot_digest": "f1fd61bec39a09567bb2c2bda4ca2357f57a001e84ca9459fa01714de538dbe0",
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
      "generated": "2026-10-30T21:21:03.161767+00:00",
      "head": "225730a53addd5ff7a02e089693dcede201de0d52fdd871fe238ffcb7277098b",
      "node": "201.wake",
      "snapshot_digest": "726c2bdd9815213e88fd07e1d29a881691d6ccd220b19bec997391b2c203f2e5",
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
      "generated": "2026-10-30T21:15:58.529614+00:00",
      "head": "4804df2245d49773aee3b5ed67d2c074d9fbe92e0ba641d2fbb8fc08ab59f514",
      "node": "301.wake",
      "snapshot_digest": "fed0ed99a77ba9480dc30612997f694d5d13120ce45c04d9919253a236dcbb32",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T21:17:39.153097+00:00",
      "head": "c0eccc8c482253aafe26c19178b81030556cae99cb5ccbec6e430a0c2ec8bb5e",
      "node": "302.wake",
      "snapshot_digest": "54c9b115a3e05d4fdc8dbe0a9d3a1f6ea6cdb42bfdd1cd9e7b293f2b1b78ce19",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d34323533663365343634613834386461.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32333661396236643166643434366537.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
