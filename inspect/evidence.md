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
  "generated_at": "2026-10-28T14:44:42.528101+00:00",
  "head": "snapshot:ab431b56f832f559b14adfdb8296d316e7658f06dae7d659ecbd4de590f7b297",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T14:41:49.635635+00:00",
      "head": "1d4b7410a210cc2dbbef1752abf56ab6e28a370b4f138a63d4b4e4f00fb9f5da",
      "node": "100.wake",
      "snapshot_digest": "721fd92f0d65bc996f1c5d25a0cd490d414f0a27dd6a413f6fee241519d694ff",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T14:37:36.014535+00:00",
      "head": "e4c30fcab28e70859c380c7745efaa242b08ac9aa70bb280009a1ff6c7f44cea",
      "node": "101.wake",
      "snapshot_digest": "ee7f49d3b290f5697568cda5b5fd5643d687939ecb72623dd644e275b4bde6ae",
      "version": 19
    },
    "102.wake": {
      "generated": "2026-10-28T14:44:42.528101+00:00",
      "head": "11eb55b9301e205c3931c4df49bf985d362580c345c27ae1c16ac479892b18b3",
      "node": "102.wake",
      "snapshot_digest": "a00d1cf8923eedd27129ed67dadd6387ab198f4654ccecc7a3ab4ce9f0bdd6f8",
      "version": 16
    },
    "103.wake": {
      "generated": "2026-10-28T14:43:24.330448+00:00",
      "head": "9cec25068c38b2772351241d73df3d10a74e9cd065781eec05590974cc061aa7",
      "node": "103.wake",
      "snapshot_digest": "5a54fca03fd16c033ffe044584d7d0d3a6a67e529bd2165c741eff456546574a",
      "version": 26
    },
    "200.wake": {
      "generated": "2026-10-28T14:41:31.597264+00:00",
      "head": "3f9a79f9691ecf44adffc99a740daa64275e4080462459e3251f56a56cbdf411",
      "node": "200.wake",
      "snapshot_digest": "2893ed2bc185a8a6498f2a808f34de2aa20322a4bddde4b53970a9f7b865a931",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T14:41:28.287420+00:00",
      "head": "fae53c48b6356613929bdc76b13ad5e530ea3180e221d8d5b4e5bedfa4a42b09",
      "node": "201.wake",
      "snapshot_digest": "33c49af2bc797aacfdda3713cbb11cadcbe666b4b95694b9c5528c0cf7a22ea6",
      "version": 20
    },
    "202.wake": {
      "generated": "2026-10-28T14:35:36.231073+00:00",
      "head": "b30f8795e081c8c4b475dc12bb134c81be004a534d18650a949eb42ee4318105",
      "node": "202.wake",
      "snapshot_digest": "5dd2d52deacb273fc4d5cf2d27bbf117a95561dbe7320045ccc12d7e97b83ee0",
      "version": 27
    },
    "203.wake": {
      "generated": "2026-10-28T14:38:23.174410+00:00",
      "head": "e5e0abeb343a58535ce05608c69921b0a9473ffdba43f9105ac3731ddd7208c4",
      "node": "203.wake",
      "snapshot_digest": "347ddb1b56c6fa0c51b1b465b789127284c3c2688cfda521cdc8a3ee25bdb971",
      "version": 24
    },
    "300.wake": {
      "generated": "2026-10-28T14:37:57.269740+00:00",
      "head": "0f73ee1eebd6c30dbac1b4c6514afe8190963d331c57d2205cdcc80c2c6778a2",
      "node": "300.wake",
      "snapshot_digest": "38ce7da24a3784d4749def6e7ea6662603d7cb2e182d71587adf17fde66e360a",
      "version": 23
    },
    "301.wake": {
      "generated": "2026-10-28T14:44:35.538312+00:00",
      "head": "8df79a1772e594269e7127293e8a17384ac617cdc7f79a48aab16c891ee1002c",
      "node": "301.wake",
      "snapshot_digest": "1314184fc21f97b36442ed845355cf6faf1d180bbdb144aefbc87d2979d2f1f1",
      "version": 16
    },
    "302.wake": {
      "generated": "2026-10-28T14:44:42.505182+00:00",
      "head": "94f239d988b02f33d470272890b02ddfd955e3d7e00c730e1ddeec3e923c66b9",
      "node": "302.wake",
      "snapshot_digest": "8c63d04f0ae185dd46a4ab40630ff996b3b2b710e7d82196e8d7500a220c381c",
      "version": 22
    },
    "303.wake": {
      "generated": "2026-10-28T14:36:33.478991+00:00",
      "head": "321110c6e38eae8b6a6bc475d68892ae19a0d13474a9e8bb92b5058d86fd4a58",
      "node": "303.wake",
      "snapshot_digest": "c5460aa7a0430dd0935db0eaae0a9abf3c225302f3f2687bd6594c96cda89c88",
      "version": 22
    }
  },
  "version": 257,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32313135323530313965353034653039.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d366236383439306635643537343937/30.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d77616b652d73656c662d737475/64792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
