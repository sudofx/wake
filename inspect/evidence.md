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
  "generated_at": "2026-10-29T00:33:08.006929+00:00",
  "head": "snapshot:96ebc6ee77cb70d0251d10424b0a3e761a5386ad8258a4dcf99924393a023faa",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T00:31:59.258852+00:00",
      "head": "1e6e765360b016bd801774f32449232e3f04b36f43779f0f704b973bb06d334c",
      "node": "100.wake",
      "snapshot_digest": "e50c347c4618de826b7cc42e614c3300aa7407975d76d136de9ea19a6449e492",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T00:29:47.983603+00:00",
      "head": "cb523bfe064e97ae6e6d8e9b32c28c8d7b2fc8d5202047399d610d2c6e46c9e8",
      "node": "101.wake",
      "snapshot_digest": "0d8cd3e5c0df1244bdb32b05e5a9b6f8b2dd22d36190a8d12f784ef1eab7c2be",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T00:30:32.775857+00:00",
      "head": "1da2d13184184eba83cf2639b05306b4f91f7e79e87cadf508b3b6dbd3510819",
      "node": "102.wake",
      "snapshot_digest": "1171f352b340275cd8eec41c3b906863332bd30a4bb67961499616e2ec8e985d",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T00:31:38.137341+00:00",
      "head": "6eabd64d083284b8b51a69d502ab694388783a8351d889102f67058f4ab14c8f",
      "node": "103.wake",
      "snapshot_digest": "3aea5eca71e1bb1c26e64ef395bc43dfeff9ebb3b5657c574a783236de01180d",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T00:31:57.531303+00:00",
      "head": "d416603262f0ca13d845c9cd082fb8acacafa1d6b4b6c570126670389ed8dcab",
      "node": "200.wake",
      "snapshot_digest": "79476762898b0daddf4c7d6e8af1484237058450fb5a94e6132c68044ce65579",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T00:32:26.649555+00:00",
      "head": "a03e730b78d26face85daf98568a7544f97976ed470253be1a314fff60d5ec45",
      "node": "201.wake",
      "snapshot_digest": "661965c3c7c5bf28f90bdb9306a49b8ff695b7412f506bfcc20f0abb8052e1a0",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T00:31:32.418891+00:00",
      "head": "39f0749bd4b0dbfbbd269fb81e0dd3f425cf220850d5426e2e6407a2e41ac20c",
      "node": "202.wake",
      "snapshot_digest": "a1645c2df80d9fe2bf3485799e76d11bf82f6cb5b53aec223ea26f12b2d29e03",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T00:28:06.064867+00:00",
      "head": "43b9a61857d0a23550769f64d1410087cd2f8fb3be6a2e4f2d7ff5bc10e9710d",
      "node": "203.wake",
      "snapshot_digest": "8f762f51916c704ab0c77f0907888be22e3d8ac06218d74b724d4a705c3b0c81",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T00:30:18.712742+00:00",
      "head": "a3cdd8f77279ccddc6b16db890dafb59a0737e228b359ab4b9f146369f026179",
      "node": "300.wake",
      "snapshot_digest": "de33d4c8f3bb50e9781e2d5e3253aab236b1dd12a96caeadc7537811469b0bcd",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T00:33:08.006929+00:00",
      "head": "ecbf49770585744fde2a744f26e4946e3daf50ad551d1ce3ba7cf79a44106bad",
      "node": "301.wake",
      "snapshot_digest": "8a24168dd79951e36d22735c15f407b510fdf6169ba2550524855a6ca87022da",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T00:32:39.947530+00:00",
      "head": "e5e123e9bcd4ac331b35e308224f3bb70c81de7a683b3edf3963becf759b20b0",
      "node": "302.wake",
      "snapshot_digest": "7ae5485848c1d2eb736cababe62cdcb7278dca508114dd06fe9c6b7195bb6df9",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T00:30:33.792343+00:00",
      "head": "6ef19c326914520705954928f26cd4368f24394c7d8330803ea7b69bf996d6d9",
      "node": "303.wake",
      "snapshot_digest": "00d07682020249b2608c9af1c1f1f277932ca3c8647e5d1165e7093c2a36e254",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d62663264333961356532366234343436.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d66653531613835366236343534316666.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
