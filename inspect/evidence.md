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
  "generated_at": "2026-10-25T11:51:14.864957+00:00",
  "head": "snapshot:a44d62e6ad70adfd1439be326b392dbe55af15c97a0b93c75e6229b1795707ae",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T11:51:14.864957+00:00",
      "head": "3b403f2ce4368e504f3d5b96afedf682c707176c7952e11c1d7648b1d09ce0ab",
      "node": "100.wake",
      "snapshot_digest": "df57a1429272d29fa02e2efd22efac7e45224f45d2c4cf0fc6ed7280eab7a5f1",
      "version": 26
    },
    "101.wake": {
      "generated": "2026-10-25T11:42:40.083525+00:00",
      "head": "bf74df851a3386d2905761c7f2d5b7fd04f84c94563da634f3a3660877ebcf72",
      "node": "101.wake",
      "snapshot_digest": "3cc66fe1c5eff67523f5543a22c4884545e99b3fb03224cdf330bc6913635cb4",
      "version": 43
    },
    "102.wake": {
      "generated": "2026-10-25T11:35:03.541710+00:00",
      "head": "89ca866ffdecbeee0e655c73ce9077e6604d4a22d8a6cf643aa846a9da405135",
      "node": "102.wake",
      "snapshot_digest": "6c8be7e6701feefa1a114e6936bfc05828d94526b940b79c5d557cd2d2bd71e5",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T11:45:51.295733+00:00",
      "head": "b284de388eed6f13426c61b892a8e2dc85866323f68ac10f87dd3fed680f7b80",
      "node": "103.wake",
      "snapshot_digest": "02fa50850410702c3554c1dc0abd90686421e5cb9fdac18334727e671e431605",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T11:30:41.022068+00:00",
      "head": "76b4eb775c0ed0f3633d1196ac50197a7e627468350927739553b330cefc6926",
      "node": "200.wake",
      "snapshot_digest": "604dfa356523931e263af9300eaf337804d6870ef578967540da5f1b205f9860",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T11:43:30.663201+00:00",
      "head": "29c6924ef0668bb38fb57b3d74b0572dc4151b91089bb40dca5b32d7de68843a",
      "node": "201.wake",
      "snapshot_digest": "b287dade327958c9ebea9739b10fa86bcd80739ae2d394862133f07006f6ac99",
      "version": 39
    },
    "202.wake": {
      "generated": "2026-10-25T11:41:03.642015+00:00",
      "head": "e485618e9274afe44daeab15b7a38b41acfc5c4921eff02636eb1342269fbb52",
      "node": "202.wake",
      "snapshot_digest": "724bf63ec721833fc97e9ab4eb5e69eb1d47eac86a944e0e74c36a298ca09a30",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T11:38:07.906071+00:00",
      "head": "4fbfb5002ad04160ac533c79544ddc87e4632ed7842f731ccf23057b8e4523e4",
      "node": "203.wake",
      "snapshot_digest": "130e4f8d0e4e6d1fabb792215b8c4de600a3194b95a0b79ccf225769494ce567",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-25T11:40:28.210773+00:00",
      "head": "581c78dc8f9ecf37eb8758b22551169363c90c549e8d79911df5e7c533c28d1d",
      "node": "300.wake",
      "snapshot_digest": "532bd20edc2c40b15bf6e50c1f213415d7e37d246999a05e98b7463b27849363",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T11:36:15.453213+00:00",
      "head": "54af56f6af8fe422710cc43f7c7444960c80b080e4f5d07bb8aa212c703bbc99",
      "node": "301.wake",
      "snapshot_digest": "84d296de67233765a9a150091b43528c0aa93bd1593f8877c29541073d4b89f3",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T11:40:51.358420+00:00",
      "head": "dce86889500aa4d074a3cb14c568055df77f37701505e62efa8d1f07fddc1812",
      "node": "302.wake",
      "snapshot_digest": "8277b34b68f2d65103c38592de5c035856a625c0aadc8661bf193bc542aaff99",
      "version": 38
    },
    "303.wake": {
      "generated": "2026-10-25T11:43:44.532227+00:00",
      "head": "94b6752780c2e274a18e659359ab93521e0e4821d73ef694fb23cdc9e320129c",
      "node": "303.wake",
      "snapshot_digest": "f4928cc12434d57df06ac80faa678f54b3f6eacb358f1f090a4ce739ab8dbb64",
      "version": 50
    }
  },
  "version": 503,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a736f757263652d613661626635326233376565346438/31.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d32366332376532326230363634613363.json)
- [notebooks record](../reader-records/notebooks/3130332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d637269/74697175652d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
