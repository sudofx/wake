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
  "generated_at": "2026-10-27T04:18:11.311862+00:00",
  "head": "snapshot:64a93ff75c312347ef19db9ca3d079f8af0c76b2f5b4fe330a51195909a62140",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T04:18:11.311862+00:00",
      "head": "49e2f0f12f349c13a06d331281914be199e4c46df0ef5041c3a11f5d200e6a8b",
      "node": "100.wake",
      "snapshot_digest": "271f747a04c42bec5573c3868c7e536d016e73c7f196159bafde51ab36427abc",
      "version": 33
    },
    "101.wake": {
      "generated": "2026-10-27T04:01:54.723727+00:00",
      "head": "268ee1a073b66b2f62f55ed50a8be2b582e5d067a424d86170b179230da3ac01",
      "node": "101.wake",
      "snapshot_digest": "a47bfd88ef1fa1e02700f0ff032eab59527ccfafbc567f9db95e3febdb9a0f0b",
      "version": 49
    },
    "102.wake": {
      "generated": "2026-10-27T04:01:57.878475+00:00",
      "head": "937955c8a574e0db082a98258a96672eca85e3c7c8dd8a9cbd2deeef3a747d23",
      "node": "102.wake",
      "snapshot_digest": "49d2c0080574c0e4b2bd45b5e50e3eb70a3b79a6cccf2a13c0d0a0dfd076bdad",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-27T04:01:54.249621+00:00",
      "head": "ad68db5d3529983ce3bc1385a9fb0bad47649e370961ee500594b960d224e072",
      "node": "103.wake",
      "snapshot_digest": "ccf5513f048486db33e9b060076a2f6df729939fc05fc698ea78088a0c9a72c6",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-27T04:01:52.703635+00:00",
      "head": "1af3ae00291f83d0b1b9dacbba895f964569604a3f6d66526d280ffc589eaccd",
      "node": "200.wake",
      "snapshot_digest": "1071df1a4cd86f9ee21a85371893888a3553d29eaed345ea804ccadc8bacb162",
      "version": 47
    },
    "201.wake": {
      "generated": "2026-10-27T04:01:52.233447+00:00",
      "head": "9ba512e35c8767d77063fe12b980d07c2152c60099baf2b8bd7c91fdd57e82e6",
      "node": "201.wake",
      "snapshot_digest": "ac16aa19030ee08e3fda440bcc85387939a4ab67806fb32585b6fccf6019ea49",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-27T04:01:51.455529+00:00",
      "head": "2d493580299a1f81a8523bd0ca8dceaba191c0cc9ba315b5c0ed39a6bef1af75",
      "node": "202.wake",
      "snapshot_digest": "11dd2b89b815003645c1743124775ad7cd0a9570594635d502ef6eaf762e4b6b",
      "version": 62
    },
    "203.wake": {
      "generated": "2026-10-27T04:01:54.854498+00:00",
      "head": "9d7de50ee44b1b0f6bbb71b3dc22b6ef8e53107ae7f678ccb6238b0b2e6d63c5",
      "node": "203.wake",
      "snapshot_digest": "e38e16b547224579516f0436dc7455ff0b0567b8a0ff28987ebd8b5fdc48b40d",
      "version": 39
    },
    "300.wake": {
      "generated": "2026-10-27T04:01:54.120931+00:00",
      "head": "fd4299003af3806b9b17663deea9fc7e1227e836294e7699f12dd6f611f1c2cc",
      "node": "300.wake",
      "snapshot_digest": "80c8aa3012e0cafbabe33e4c07eec8198cc385c6a84df2432c1a350c92038efe",
      "version": 40
    },
    "301.wake": {
      "generated": "2026-10-27T04:01:53.734396+00:00",
      "head": "b6f88039e7626701a37dcbb826d2bd94ce5275c535f280af17f07ab3d04a919f",
      "node": "301.wake",
      "snapshot_digest": "714c3badfbef619db7220feb24d7712d0432d1fb41701c2e8cfdd57177f43f2d",
      "version": 68
    },
    "302.wake": {
      "generated": "2026-10-27T04:01:51.005736+00:00",
      "head": "1f41f5d9c7b468756bb852dee10247f8a32e0764f79b63651f571a045fa8e020",
      "node": "302.wake",
      "snapshot_digest": "8f14c8c0a4535d454eff6d7935d7687d1213f7d5f9cd08902e2d2d2340750646",
      "version": 49
    },
    "303.wake": {
      "generated": "2026-10-27T04:01:53.938112+00:00",
      "head": "ed90a3d55a607b51384befac6346429dff4f2ab3bd8c96a7a3f7180969f5ff92",
      "node": "303.wake",
      "snapshot_digest": "2004e9a8781fef85c33f22ff101fc1514e86c5ac6e9c00e5f0af300ea17f0cd7",
      "version": 59
    }
  },
  "version": 600,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3139.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d65366437656635383433373334333936.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d63623733343430373739313634616339.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d6761/702d69642d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
