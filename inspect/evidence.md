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
  "generated_at": "2026-10-23T19:59:48.440478+00:00",
  "head": "snapshot:5d1e3f98d4936a132d70fdf59b9ad515bd5f3a72aa0882db1ba573c06e55c31d",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T19:54:44.378331+00:00",
      "head": "75970800bfa30ad8a9fcc2cd002111af92f8313bfbf980087c5d18f48331f9a7",
      "node": "100.wake",
      "snapshot_digest": "470af8432766f421c89b84a24dc6bd2935e90a69be0e2346680d961607cd6c54",
      "version": 18
    },
    "101.wake": {
      "generated": "2026-10-23T19:59:48.440478+00:00",
      "head": "190ea79644a9accf284065ee5040f508d99c9b753cd50f296900f77a47d35ebc",
      "node": "101.wake",
      "snapshot_digest": "d06ecebadb205405e864865ea46aae175628979646c29ac45ed2ddc9869edca6",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-23T19:57:40.604235+00:00",
      "head": "e7a8940399bddecd6c0d8d692bb50d653b653b8a58eed168914c81a49ddb6e4b",
      "node": "102.wake",
      "snapshot_digest": "b94347261df9a62048d13797db928e2f658a6bdc0319c0096c8a8f29116fb3ce",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-23T19:58:07.229948+00:00",
      "head": "9970aaf24856c24dcf3a5ead0866677855b177ee918f05b7e5708c20cb0c004e",
      "node": "103.wake",
      "snapshot_digest": "3538c084e61476bc4cd0023ca06333f98299d1f3f37179852adc1f3995200aa0",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-23T19:57:33.196130+00:00",
      "head": "ee5e4561b2d65b520f2ea89072c18b766e738f897adceb444021ea38ccf97b03",
      "node": "200.wake",
      "snapshot_digest": "521a0bdcb4ea67f9fc09b0baf9b63b11767a40a777fa5a27ff850a30cc8df69f",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T19:59:31.938237+00:00",
      "head": "87a9296ec6686e03220fe7acb1dd8d1b1a954e3f68ab34d4304106e4b097e252",
      "node": "201.wake",
      "snapshot_digest": "d835d7bf6c10907797c18cf571d334785b909f64c30aa1e87cc91597f1b4d2b0",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-23T19:58:24.986488+00:00",
      "head": "4e81a910422f71079fd4f1e83eacc022c97e86278e011b6c0c639f19e5bf89e3",
      "node": "202.wake",
      "snapshot_digest": "06fadc776dc5afb42d4dd67e94765dcdd12b97f54d4f46c643b6ecd8d070b6bc",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-23T19:56:40.287642+00:00",
      "head": "29987e4d71f3932f3c0b51434b832b9341fe27b7b79d5c201f16e75ec8af85f6",
      "node": "203.wake",
      "snapshot_digest": "8d7e565b5983d1e74839d35dd73a3ed5991466abe717c7cc6b275f490735c090",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-23T19:59:25.510814+00:00",
      "head": "4825d55fc48939db7a523e9dba132af108caa5a2359767f43d56f4bb5959a1d4",
      "node": "300.wake",
      "snapshot_digest": "13546404938dbb89ff873a79889ded0ca9795bc81ad812f5bac10968d24d8c52",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-23T19:56:05.128404+00:00",
      "head": "08557f8252073f7c800f2cc9679eaa325f08f5a6eeb01625402389a780546ebd",
      "node": "301.wake",
      "snapshot_digest": "1cfc7cbcf953bdde934b3d69bcd26980108fad1495087ca27048335697991f7c",
      "version": 38
    },
    "302.wake": {
      "generated": "2026-10-23T19:55:49.843967+00:00",
      "head": "4d2d5c53de834606fec25dbac7528ae8aedd2696ae37e869c73ed9ed137d385f",
      "node": "302.wake",
      "snapshot_digest": "8f8ab5665127cc48e1488368f04e5769932b8abfe001349652e3b89ecd3a45e8",
      "version": 18
    },
    "303.wake": {
      "generated": "2026-10-23T19:54:37.580859+00:00",
      "head": "578f91b188075cc33893581bdce6b52fbe11a87406394486021b78d1c5836d03",
      "node": "303.wake",
      "snapshot_digest": "c2194a1747a6e8a566373690c5ba45b0f688867545f1858b0e106f79b4fa3fa9",
      "version": 35
    }
  },
  "version": 333,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d626661333830633939323439343339/65.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d61616531373532346435326134353836.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
