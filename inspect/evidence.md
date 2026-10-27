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
  "generated_at": "2026-10-27T05:07:28.616998+00:00",
  "head": "snapshot:db46900c5c350ec7f6f64aa49ab09eed1d8b27c6ee88c76819f97dd6648468ac",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T05:07:28.616998+00:00",
      "head": "ac55ab62299ad82e85244c9debff8756d2c24940baf3a84ae366b89dee097672",
      "node": "100.wake",
      "snapshot_digest": "19b5c6b503f636c3f3d6cadd6e034fcc5d6db96e073f1ce6954ab212d59a8a77",
      "version": 33
    },
    "101.wake": {
      "generated": "2026-10-27T05:00:31.587447+00:00",
      "head": "bd68ba44d16f26bf5f5c7c6d42ece4d0b7e743ce6ae5ee9a00aca7a0e28c36f7",
      "node": "101.wake",
      "snapshot_digest": "95d1e23f4636a46247d3cfb9d153563c5a620b762bd58e2b970c3f66e7299d0e",
      "version": 50
    },
    "102.wake": {
      "generated": "2026-10-27T05:05:07.054879+00:00",
      "head": "549e087472ad9679451779711f26a83601c9e0d38233c0998844c922f1f004b4",
      "node": "102.wake",
      "snapshot_digest": "c77f37a6589b11e0c59f9b0c38000aa93d2dbe10eab31e2f47f864b59083ccc7",
      "version": 64
    },
    "103.wake": {
      "generated": "2026-10-27T05:04:25.948668+00:00",
      "head": "384332805b1d0b25e324514ec540af4fa3c5c5a4dc99d11a86b46473293afab0",
      "node": "103.wake",
      "snapshot_digest": "cd0a3ddc60f5dbb9ec1ec0119dd4c28727c0a36a4fd8fbff845f13dadbfaac3c",
      "version": 46
    },
    "200.wake": {
      "generated": "2026-10-27T05:00:57.691224+00:00",
      "head": "e5f9c8a214b6d7745eef5b8212a60169e88bbe421e4397979f8b5f6f4c87dfd9",
      "node": "200.wake",
      "snapshot_digest": "bdd68c41b48696f41b3d05baf484eb9d878331a26349ab9e218c5a52e23cad3a",
      "version": 47
    },
    "201.wake": {
      "generated": "2026-10-27T04:52:43.150976+00:00",
      "head": "1874030f970dd777ed20b1c110c6732812a9f1fc83f881e7a0f8b62338ce9b2d",
      "node": "201.wake",
      "snapshot_digest": "6e74882ac72df18058c80cba239c2f9de071af78f22ba703c95feea6d804c6fa",
      "version": 47
    },
    "202.wake": {
      "generated": "2026-10-27T04:57:09.340890+00:00",
      "head": "6b2616f4f9e76e5175203381e15053c3eb6f29f3bcf8880f0867a1928aceebb3",
      "node": "202.wake",
      "snapshot_digest": "5402be18206995e73dccf97f70e35788067da67eb89f313bfb0c9949e7a903ff",
      "version": 63
    },
    "203.wake": {
      "generated": "2026-10-27T04:56:56.324918+00:00",
      "head": "61a55cc88514bdc27975cdfb015beda62879136781e644ef57b77abc09bef602",
      "node": "203.wake",
      "snapshot_digest": "4593db25ea62f9861ee3c173b969de030a665710744b9625bb926932609bfca8",
      "version": 40
    },
    "300.wake": {
      "generated": "2026-10-27T05:01:09.028203+00:00",
      "head": "699c18b60f992fd464c5b2d5dfa9a850ac23cdd128ec70042e45252e6a225916",
      "node": "300.wake",
      "snapshot_digest": "7a7ee1edf5deaa0fd165ea65d839dac7ccaeaf20bd6a6853a2ee9766eda3d2e6",
      "version": 41
    },
    "301.wake": {
      "generated": "2026-10-27T05:05:39.533737+00:00",
      "head": "26582e267cb9615a5f005fc8c5d0e61c189af8ebc19c08fdf3e7f29dd51e3184",
      "node": "301.wake",
      "snapshot_digest": "594b95428cab8d9ee2b2c48a488681bafb2243026589365cc6e9889d8b07f194",
      "version": 68
    },
    "302.wake": {
      "generated": "2026-10-27T04:54:40.553719+00:00",
      "head": "d90dc90f34353f14c791fac0b730306453579193bc7d2d8c930d01a82907fef7",
      "node": "302.wake",
      "snapshot_digest": "676f2dfd210884808f6d96c196fef0febc7f23fb40aac03a007af287cfb4f2ec",
      "version": 50
    },
    "303.wake": {
      "generated": "2026-10-27T05:03:00.544961+00:00",
      "head": "127759b7538ee247d419a43aa344e80f55641d96dcdc680924c1537b2e3635f3",
      "node": "303.wake",
      "snapshot_digest": "fcdacc5217060d859c21270c1fbd5403f916816199d900745d037c00ee721e0b",
      "version": 59
    }
  },
  "version": 608,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3139.json)
- [evidence record](../reader-records/evidence/3130302e77616b653a3a736f757263652d353861323232653334633337343037/66.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d38663435306266396261656234356366.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d6761/702d69642d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
