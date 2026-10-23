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
  "generated_at": "2026-10-23T21:41:46.342284+00:00",
  "head": "snapshot:f8987b58aa25700d9679822a597a70760459e4ba688b189242763561b7ccb82a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T21:34:51.193257+00:00",
      "head": "3e117333e72bd87a3cf003dde0db988f7855ce08fa6e0a00e820b610da3befe1",
      "node": "100.wake",
      "snapshot_digest": "a27056ed5fc3e251e1bb2f62113f535bb615878fe3c585928fde526ede82c707",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-23T21:41:05.522048+00:00",
      "head": "268c3b51115a829bf9b42a1ec823a05ad698a88fd51aba32c714900dc17f039d",
      "node": "101.wake",
      "snapshot_digest": "9354f9755bbab9771c25ff85448929623349d9878c0642c6a3e8222fc56dab94",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-23T21:39:52.136014+00:00",
      "head": "4351a97df0b5a95897e49ca510444a3a0ed87c2637fedcc3a328bdb3d0aa2ef3",
      "node": "102.wake",
      "snapshot_digest": "ef7a304ca26e3d22c175e906a18dd4d06b0abe2f1a31214c68b370979ea4740e",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-23T21:41:46.342284+00:00",
      "head": "2b8e123e407260fbcdf3488c4ff81c1600145f208526617c77a5112131d0d3bb",
      "node": "103.wake",
      "snapshot_digest": "011491d5fe8995f8a7f9f347dd413635f1e9adfc6e735f851db14a9b9ce84b5e",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-23T21:40:49.510370+00:00",
      "head": "9318a17da8f52ffa07c2ad8fbaa9d62dcf45c611b26e421b6a16d5c583f3819f",
      "node": "200.wake",
      "snapshot_digest": "66d8eef40d7cd94e28009911d02c9557f7df20be68da9c20183c6cfe322879be",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T21:40:33.660157+00:00",
      "head": "b0d10d1c9748f45feec207d7d07dca8aaea1a5f0e7727243f369c9e6eb76cd1b",
      "node": "201.wake",
      "snapshot_digest": "b98b263888b3f564c73fbd6ed30bd4fed9988c44612b576e14afc68393849aec",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-23T21:41:16.398261+00:00",
      "head": "1d0dc50430f67453d11bd2297176e7827dda4c3a9e1fb95fab11902114064924",
      "node": "202.wake",
      "snapshot_digest": "163445dd7994496cccf892eeccf11758bd0fb9e1a608d92b4be4448cfcbbc12b",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-23T21:40:57.714709+00:00",
      "head": "5b0ec0dec5f11a5dacbb98fde5e751d0fbca211b4218483d180653cc0154e549",
      "node": "203.wake",
      "snapshot_digest": "b2203bfe4a6137b5b947ed71cd64d4cd1d402a45e8f0159cdc26ad196dcfd410",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-23T21:41:31.397859+00:00",
      "head": "09331a5e9565ff264f7f2e20b12df6cea6aed0398136fff62fae0e6e7b8fa99a",
      "node": "300.wake",
      "snapshot_digest": "775a402d1572f121d9713e1c1b9d85e941b04b0ee9a668ff5b15769df0c9a039",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-23T21:40:18.431628+00:00",
      "head": "09b2d675844c9bf69e76c4488c30872ee20a1007ecb5114d310ba23f4ae83c76",
      "node": "301.wake",
      "snapshot_digest": "ce2cdaa4e1e868ed46f5ed8359420af4138bc179f73d38a0b3498db1d07ccee7",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-23T21:40:41.769667+00:00",
      "head": "27e7ac775e3d0c286f2aa0f18aa03ebbfdec77c5c08459c32fd27896e2ec6dba",
      "node": "302.wake",
      "snapshot_digest": "f3877c4055292d54bb793aea32c42ccce6ed847ab2d5022f41a7964dd83aebb6",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-23T21:40:26.343845+00:00",
      "head": "da0ec7174e0bb23c5d76e8a174c959cb4dac113d80c077fc328765c515fefb0a",
      "node": "303.wake",
      "snapshot_digest": "ae8b6fcd64471a05df41a3ee8fb717b1557d3bf02c4b28eeab199c5b659bf30f",
      "version": 36
    }
  },
  "version": 337,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d63393466623734616264386434663931.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d31326133333764663834663334613437.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
