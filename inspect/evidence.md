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
  "generated_at": "2026-10-30T19:04:52.024097+00:00",
  "head": "snapshot:334f186cf516e020e1513c8479921c9999edde51097022bf7e9585628d291843",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T19:04:52.024097+00:00",
      "head": "d446cc47b6a9f68eb0f44b13163d87515ff000c52a7e83efa84a2de7b741cf25",
      "node": "100.wake",
      "snapshot_digest": "6d3859c89273a3d45cd06eca90105f22e7c12ab9d4eddde92cffc6de0cb646ed",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T17:19:09.354470+00:00",
      "head": "874b37b3d3021448738fe90b8676e202d6a5eab8a9ea84c0a537d976281bc789",
      "node": "101.wake",
      "snapshot_digest": "56a4aef0ac9727ee86a1242eb3b33d1eeab02789dddd8d39b6d71a2a973a82aa",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T17:19:04.635451+00:00",
      "head": "12c09c9e90c17cd8f38f342381dc2a182e65d48b51ad4859bd6a55bf428f2fea",
      "node": "102.wake",
      "snapshot_digest": "4e8aefbd05c6ae4873c6d1bf3ddfe7da90bea828e8b55fdc361ca2da95cd82e5",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T17:19:22.828707+00:00",
      "head": "49eeb2554173e564fdf9413d50c74dcacc023e81de809f32a2b1938a3d4c54de",
      "node": "103.wake",
      "snapshot_digest": "30da599009aa361f2b2f1b2955abd32e555ae953230caddba849c985361785dc",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T17:19:39.552253+00:00",
      "head": "2066a0dbf676ce1e8b2c8c42592cd70e87c47a0a0b489751a07c535a9eabf1db",
      "node": "200.wake",
      "snapshot_digest": "40e9b818e665d1ab5017d1f3297b1a18ac064f4971e8c9f7a7dca87263a6e751",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T19:01:00.775350+00:00",
      "head": "0abc9bbf9ffaee32d9bb6bdfe4989a38544f99aed73eb5a8b46f0e399bb1f970",
      "node": "201.wake",
      "snapshot_digest": "2c1cbaade3760c2f3bfc730545ed45df59bd919c47587d4f039daa9e4821e174",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T17:19:12.313910+00:00",
      "head": "a9e9ff65ce5e1de9d7147c46c526091fd54fb67c2b7bc66b522d89fe40862ce7",
      "node": "202.wake",
      "snapshot_digest": "7a6c3b43b17da95cfac2c9895986b24b23a287f6b8f0c1ea1dd92c075c620495",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T17:19:12.633046+00:00",
      "head": "5f92cad7d17cdf153221a7b04fa3c4c7477c3dcb44920220e51244b9018ffad2",
      "node": "203.wake",
      "snapshot_digest": "f667bcb6dce5d4d88ec5acf111f5fc52654fded567b0e609266e265861d53541",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T17:19:18.303799+00:00",
      "head": "a2ababf4820852630773cfc893560c389b15b35771c67fa05b21c8e942ba133f",
      "node": "300.wake",
      "snapshot_digest": "493add8fc773a3f3406277f61d13781be0b42560abbcf97056f1bf72754825ca",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T18:59:11.281440+00:00",
      "head": "08ea779ca10c074ada5ec851d44bf59d47cbff579c3b6592316f2c1f06424081",
      "node": "301.wake",
      "snapshot_digest": "96710ac08e6295d4dac6a6ee9b90a19bad79cf59ef1eb2337811645a5cae4b51",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T19:02:56.038012+00:00",
      "head": "967085ebaed2f11f6a6388cb1ca3a769cadbdb46157a2d7972c806868798e3c2",
      "node": "302.wake",
      "snapshot_digest": "0f478baf43badefc2c5a00a703bf8e14de57ce89737c7fa2bb06c29f4103b399",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T17:19:12.744675+00:00",
      "head": "241e9882c68c0a87f8c46414b75edfc90059cfaa616a35247de9a49eac4d5fbc",
      "node": "303.wake",
      "snapshot_digest": "cb38ae4b210b5c0287259231992f507b4b19b38fcf0ee38050656fb8c8a4a047",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d34666532323035376365313434653133.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34636132333034323232623934353834.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
