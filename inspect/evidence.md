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
  "generated_at": "2026-10-30T00:51:44.050795+00:00",
  "head": "snapshot:918f8d9fadcad647faa50fe6a12d7f6db50fa41632b4f1673d894048c4461aec",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T00:51:44.050795+00:00",
      "head": "3d2e6d15680a7f7501fc8b7b3dc8926d3d09f38225b67bacada04533574adc1e",
      "node": "100.wake",
      "snapshot_digest": "79afc626e37c76b3cc73cdab066a7ba3bc1673afb33849a7150ab533086c8d23",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T00:49:04.610360+00:00",
      "head": "7007767bd2998c7758f2092b1e4a945d2d711956686503d8b6d77b09430856f9",
      "node": "101.wake",
      "snapshot_digest": "0ea687ba85ee5fa49ba3cf001c64276fa095b229407aa771b77929eefc768b52",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T00:49:08.584671+00:00",
      "head": "dddd465ce8308c5225767359b04280b37818102b069781ee9df505bfb334e856",
      "node": "102.wake",
      "snapshot_digest": "301d96734eaef7252d3f4716f02be2e73faa4a97a609bb5ba4047c4e677f161b",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T00:49:17.701720+00:00",
      "head": "e447a99840f801ddec924fbaf63c75c02a6886d0978d39cfb3305ff21b09efae",
      "node": "103.wake",
      "snapshot_digest": "67f0a88ed42ef2076ec3528e49f23fcdb4ed1b747c5a27960145244b18c2bc2e",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T00:23:50.595544+00:00",
      "head": "084240f8e81ae2f160befd428925cc5402b428536d546e971610f45bc4395713",
      "node": "200.wake",
      "snapshot_digest": "08ae679b74984ebf7aa5771d7d0c2a3472e61216923f12a05449ab419e7b8a58",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T00:50:06.016330+00:00",
      "head": "084c86796642298f55f2868baa9a98fc8b351d64470ce5bbf5d539c19d446e52",
      "node": "201.wake",
      "snapshot_digest": "97d8f151e393aef6600e124a3f54d5c08f165c631f1df451e22852050477d6f6",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T00:49:09.976258+00:00",
      "head": "5116983ee8a59382f1adcdbffce368e0d2a3aa0381c482259d66ed7e0589369f",
      "node": "202.wake",
      "snapshot_digest": "9b1a3c00dea6c20141f6216ba5062edda77fc3ff2628c2ac784a66634843d53a",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T00:49:11.832668+00:00",
      "head": "fcfaeae646eeb6b1d7474a001fda5becc3d8995191dbe8268ad59ac21ecfa9ee",
      "node": "203.wake",
      "snapshot_digest": "4827390ceb0f2d1b6f86787b78ac2d4059edcc04ee65f40b52b2192424eee594",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T00:49:21.236372+00:00",
      "head": "fb4c2fc2eb4a00efc2dc8b6ca3a369f3280cd27c9234d15a76ba7c70a4c064c5",
      "node": "300.wake",
      "snapshot_digest": "828275f9c322e8592cefeb9e606d7bbcb2d3f92da4264fdc311ca5cc15517e50",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T00:50:06.397657+00:00",
      "head": "603f75bff9d3bca8bc7e40d40351a3160f0ff6df84b1466db523ba241357bff5",
      "node": "301.wake",
      "snapshot_digest": "db858d1134af964613c26b4feabf1ddd2bb98dcf98bc2c234f3ecae990582a6d",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T00:50:02.756674+00:00",
      "head": "6772011f19da0d0c31af5d8212491d3e5281c91d6c88474e9d935a7f7a3e0d84",
      "node": "302.wake",
      "snapshot_digest": "8c3bacbdfe70c56591f2ef6a064a2a7bcf1401a05914927140996df938cc569f",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T00:49:06.811460+00:00",
      "head": "42ddf98b3454b864a9ba0595b97f3bbe856b330a39c7d3e289d33c42d910871a",
      "node": "303.wake",
      "snapshot_digest": "6c2dae4757b7afdc1c7d12a94b669416f0c71d1ad08237dba88df869df30f106",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d38353830343338316432393934313466.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d31306635346539363037303634613463.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
