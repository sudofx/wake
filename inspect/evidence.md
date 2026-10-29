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
  "generated_at": "2026-10-29T08:51:15.314483+00:00",
  "head": "snapshot:7efb713af11f1727db8e31018225e7a5844ff73a2a9c38b338542740eda3b67b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T08:46:08.067478+00:00",
      "head": "29454198919fe096d6bbadd2eda592d99ca24202cf1c2cc18e48f8a1e83e812f",
      "node": "100.wake",
      "snapshot_digest": "6b974e94165916cb39e4c0b5c4ac078a1ba215843248136c225abea878cfdb8f",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T08:20:07.766023+00:00",
      "head": "d1bb77c500b86a2af78fd63d059f85014e75e06e0f91e2a3e741705f662ff5e9",
      "node": "101.wake",
      "snapshot_digest": "0e76b1c9567a2b461ec6cdb4bdccf2fca24639f9deb35350ff3da7650ad2b6c0",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T08:33:57.048767+00:00",
      "head": "a390ed705fb377d1a4ba4de42102d6587a102c80909f2a57da93643a20496f0c",
      "node": "102.wake",
      "snapshot_digest": "751fb9a62603f36e7fec37ba25372a4ea184d5692512770c1bb1c81685aa653f",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T08:44:23.615298+00:00",
      "head": "8ed770a981fa1dab216ae31257aa43c43a80956f0c18bbfb77e9cbf9c9679944",
      "node": "103.wake",
      "snapshot_digest": "bf41f75115aaf50d9453c31b79fdc5016d03cb5c30af57ca2f31375bec04b8c6",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T08:49:33.577276+00:00",
      "head": "a1b082307dec856c7065fae2b7bceb87f223f1d684697ef19c01210a947264f9",
      "node": "200.wake",
      "snapshot_digest": "63c70e6ac9b01ea66b2bb531919e3be1e4dcc72629a141d4efb4047c0d8ef218",
      "version": 24
    },
    "201.wake": {
      "generated": "2026-10-29T08:47:49.561528+00:00",
      "head": "6992c59552dfd5a6f58e27d9c8534b46954745a8c7955a04ede4c8754d02bf62",
      "node": "201.wake",
      "snapshot_digest": "8aae4a64ef88149dd465f92f31611c239bb44b7a56bb0baa4d31e42c2f4e6c06",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T08:37:23.031582+00:00",
      "head": "276df42e28f4aa48ac88f509afceec8b69e1cce13b651f74c0e73953490868fc",
      "node": "202.wake",
      "snapshot_digest": "ec98d5780aaf80aecc22ebf8fcdaa8367d9cd9a574943f7484ba4d215b1527c6",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T08:35:37.579244+00:00",
      "head": "aed4c9aa30c8ea760fe751aac833a9a6aac85c09dba7c3310cd9aa4444fc3d27",
      "node": "203.wake",
      "snapshot_digest": "0ed3da080a0393f7311fef42f671c67c8ae99d8113d53d709a9e8a10cd5d20d1",
      "version": 28
    },
    "300.wake": {
      "generated": "2026-10-29T08:39:12.658417+00:00",
      "head": "0bc06cf33801432aa6572a4f4a6012053cd0ab97d3f8bf1578428597cd0278cc",
      "node": "300.wake",
      "snapshot_digest": "ccce128670764ad7d99622683cc388c29fa87a5d65977c922c1ed4fe74436201",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T08:42:39.367549+00:00",
      "head": "a2b4c7596943e3b92fba4faa2885901410f4fc32e5f7befbd2fcec8f21149da6",
      "node": "301.wake",
      "snapshot_digest": "0ef5cb4143a98c0ad8f6d2d89b1c22d2eb5bbaaf54b05dc938adbdbe7e1dceb3",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T08:51:15.314483+00:00",
      "head": "d1842b8ba7b471e539924e810206b6571d5e94abc6d74a9998045b60287b33cf",
      "node": "302.wake",
      "snapshot_digest": "662b361934c2224e53f932a9c1d8e9994ade2b056922f235840d6b1945e6f935",
      "version": 27
    },
    "303.wake": {
      "generated": "2026-10-29T08:32:16.525650+00:00",
      "head": "7502da172cd2bedea579442381ea6406d51bdb0a7779f317f5690e09cd6ac05b",
      "node": "303.wake",
      "snapshot_digest": "aefd0dbba137296d41266dfec312eb20e4937f7e548698947135a76b3b380ab7",
      "version": 23
    }
  },
  "version": 283,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d633133326462313735313638343530/61.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d663938623233306133373636346666/62.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
