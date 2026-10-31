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
  "generated_at": "2026-10-31T13:00:02.285090+00:00",
  "head": "snapshot:e0808e075bcbc5f036c76210c99efc32eb51db7a70491ab9cbc8d72811e7e2ef",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-31T13:00:02.285090+00:00",
      "head": "f4d0d6cf68a9c52f3ce010702fb4bec02e58a4ebf318013461dc6a78fa67e3a1",
      "node": "100.wake",
      "snapshot_digest": "7a9e52af084f81021380f9b1c79f0b15aa0428d6859dae6e80ae4b8aac61b765",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-31T11:49:47.026039+00:00",
      "head": "8550b59a6c266a8e76112989fed1df0bbc0a98fc5aaf23cfce24d53f30fc169a",
      "node": "101.wake",
      "snapshot_digest": "4e504e279a0273e8048cf8de3abebfd158244af957dcaaf179cfd9125b71e8d2",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-31T11:49:48.444913+00:00",
      "head": "ec816d2a76c695f29cc2b503738b5d106326059f77fbe2b8fe5a97fc4aacaa2c",
      "node": "102.wake",
      "snapshot_digest": "ab8835edbfbbb8ddfca2102883adbd14b2e2ea24c6c76776a9c81bbda033d11d",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-31T11:50:01.291558+00:00",
      "head": "71a27853a1ab9b8483492dda796d8ca61b68d239165af28bd51f14c9c50f397c",
      "node": "103.wake",
      "snapshot_digest": "b797f9a3376d8066e2f2dc35d8e847e4e19d4111dde1d3d9b2a5ca40aad34616",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-31T11:50:09.487428+00:00",
      "head": "31eda186069e5d5de1c9fbc366537bc8d5d53cccd8fe70f575bfca4ced989ee0",
      "node": "200.wake",
      "snapshot_digest": "40e02f0943b86aa94f545be86f1744dd118c7449c3569e50f2269ad26d7da61c",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-31T12:56:12.963080+00:00",
      "head": "d6c0124074208b5a05ddaca715a244e8e451aef4c6e1fd9be278f9e9bd58be37",
      "node": "201.wake",
      "snapshot_digest": "9dd7001996b81b3b75285473e4f810d2d9859eaf829e0abd78c74164b9b867a4",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-31T11:49:55.440194+00:00",
      "head": "03382250fd3620bcd0b0c54d5f35b2531000dbf05b1129f72fd5fdc7ea616811",
      "node": "202.wake",
      "snapshot_digest": "b2fa1499438b79565970d8d90fbe2b6a1f94a11c8e8089700c4bc445a82067bc",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-31T11:49:48.532107+00:00",
      "head": "3914e262f58c43f789fd26d74286c9f267769daf9b51d07608d5906286aab135",
      "node": "203.wake",
      "snapshot_digest": "39f0f055b16d2cfda1d8a3b306f6b7ba412e427371f2a760d9d9d5f4662a8db5",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-31T11:50:06.070211+00:00",
      "head": "5baca6742121dd913ac9ac5b898aba15276323b04b4ed4a659ab0190901805f0",
      "node": "300.wake",
      "snapshot_digest": "566fd868035a3a1055d898e01bc6fa77b33ecf8c65c490c5b9518c130e2950db",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-31T12:54:45.359111+00:00",
      "head": "ef175412a2cfd466f4571cc4890552aaff69ef58eeccd5fc3cfa23a59c759304",
      "node": "301.wake",
      "snapshot_digest": "eb5065dd964d3839fefbcf1c4beeb2f7cbe96c85c1a9e743dcffb0ef608d5b7b",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-31T12:58:07.459227+00:00",
      "head": "afb18c6b45584c4eff5f44370dc2026215b16dbf3f29efa45ed5e430fde228c8",
      "node": "302.wake",
      "snapshot_digest": "575c66a194eab5fe0182b9e6ec29cce2a6b74e1fbbc3d6adb5687093d25072ac",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-31T11:49:47.574554+00:00",
      "head": "b3d68b0171ecab764a4feaa416e1b7aa5592054cc79de5dbf0fd60c258a6df24",
      "node": "303.wake",
      "snapshot_digest": "5e5462df9046f16ff6e6300df27d5ff2dddc07c0ca30d895eee939d332c5d9ce",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d32306265613161316233353834386261.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d30303331663432633062633634633539.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
