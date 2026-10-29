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
  "generated_at": "2026-10-29T17:00:45.142683+00:00",
  "head": "snapshot:3ee7d2bab9743f2db24bf678dd0daac52591e8d3a4a00e17ca9a8ec380ae6a69",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T16:57:50.671091+00:00",
      "head": "3a331d4ea4cd397aba0ea95c1930587e3bfcd7c045c5822f8fcf2100cdf1371f",
      "node": "100.wake",
      "snapshot_digest": "a8bfa95de153546dcb9649adcaffc408453c785c9a2d823d61cd839043708b62",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T16:57:28.076383+00:00",
      "head": "cbc5a61af2c5920a7966639d6c8fad63af983fcc98d83ad5c2ebff94cbf99df5",
      "node": "101.wake",
      "snapshot_digest": "b28d23e888128dff465624e79fcfbba2ee54fefb02cc92bed459fe0c6b6c1b92",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T16:57:26.944253+00:00",
      "head": "0d071722eafe48714421f78e1962052d1af6347180034f4f4ed07b9c601a6355",
      "node": "102.wake",
      "snapshot_digest": "b330ec59f88713007cf25faa4dd10c8e2ce0f49b6c459fb968f63f4237d3b28a",
      "version": 18
    },
    "103.wake": {
      "generated": "2026-10-29T16:57:50.761385+00:00",
      "head": "9f3dd4c5a5edee5ef634a88a1c820fc040ad50b3130b59262ee50e9fb274b0ca",
      "node": "103.wake",
      "snapshot_digest": "22dcb466a0995503c7bbcc483bf04bda31d5e4c7f057c68cd6b2e396442ba16c",
      "version": 30
    },
    "200.wake": {
      "generated": "2026-10-29T17:00:45.142683+00:00",
      "head": "e3d725aecbc180846196a24a57d10c5ba8253ba02997e6818ce3b83ce1427153",
      "node": "200.wake",
      "snapshot_digest": "6fee7791b70421f4afa544e34869368b707b3a837660cc09787b17e3d661e935",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-29T16:57:54.961890+00:00",
      "head": "833a3c7eaddad0abd408854ff157b4e5f2fb25ef2e50ea4ffe143066e412f672",
      "node": "201.wake",
      "snapshot_digest": "1a494b24e2cd4f799997229ce7037426e5dac585d161884cd9a47626827e92de",
      "version": 25
    },
    "202.wake": {
      "generated": "2026-10-29T16:57:34.777100+00:00",
      "head": "e5d548629e694530c377f1954efb601aba5ed361de2b8ca957944f68606642a2",
      "node": "202.wake",
      "snapshot_digest": "ffa0c86b88b5e46432f60974938a372f08434de7b3e1dc90b1169e062626096c",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T16:57:23.247630+00:00",
      "head": "a92d0a8e104ed7e717be76ba9d73077f94851261d2fc0818df3e0a0f3c0e1edf",
      "node": "203.wake",
      "snapshot_digest": "d5f0c2fbbd00d4e90235c5d175430a0e9490dd1480e1b37a0750b9d86130dc07",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-29T16:58:01.829419+00:00",
      "head": "eb0d945e2f6730ce2bbbbe491423bd92bb959b533e1dc97a065b2020cf470b88",
      "node": "300.wake",
      "snapshot_digest": "db16628023f953efe02d551d07f7d4f922980d943531444695c6142c86ec6b39",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T16:59:01.373887+00:00",
      "head": "acf5f85f94c1c4f0a5abf288c34e1b0bcd7aaaa69da8eea64dc50d2cd3922089",
      "node": "301.wake",
      "snapshot_digest": "2db38217c8bf9e5050d10eb44b7d95b3d13d0506a0763ea8d0f1b494d2a78462",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T16:57:45.090642+00:00",
      "head": "a09b2318261437447e702d99d4750f9808dfe2704891240f0f443cea35cc2131",
      "node": "302.wake",
      "snapshot_digest": "fcdc75dc7a28140d62b2dbb8c890525df14ed4b4cb3280aabac17383a54f2add",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-29T16:57:35.277681+00:00",
      "head": "f755b00ef5faf2dc70e31985ba6bc82628ff5b2b07abe81483fa8fbf70919f2a",
      "node": "303.wake",
      "snapshot_digest": "34b07cd81d11ebc1d4f07d26178f9b33aa73fa87fd4541afedd23d59f72bdfe9",
      "version": 24
    }
  },
  "version": 298,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d34396232323639633866646434303463.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d373733356534633138656265343531/66.json)
- [notebooks record](../reader-records/notebooks/3230322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d726573706f6e7369/62696c6974792d666f726d6174696f6e2d30312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
