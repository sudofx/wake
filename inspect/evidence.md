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
  "generated_at": "2026-10-28T22:02:07.897851+00:00",
  "head": "snapshot:f2f894adfc62cad26c6c469b8f312d2d140190cfbf97cdafefd5fcd7eedf1f2a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T21:55:24.216133+00:00",
      "head": "79df2bf5ed70372ed7f8750fba31b89d7d3e91e54ac12f4f34c7c3e22c0e6487",
      "node": "100.wake",
      "snapshot_digest": "cd94743ef7ffb9c2b48d57379194546b9b0c7621671026d29e111e3119884fb4",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T22:00:44.703058+00:00",
      "head": "91b7b993c5db566cc37ee15aa21080add60cb3250368fd63453c4e02c7945ae1",
      "node": "101.wake",
      "snapshot_digest": "e1df385a46bed74c8c5a5bcd4c9bde30e6135e94ac1c4f5d4c57f75eb181c117",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T22:02:07.897851+00:00",
      "head": "a9299ab8703a541c141cea1cc5e55ba7f6ebae348c3806fd0ddc83a7c3f99064",
      "node": "102.wake",
      "snapshot_digest": "875f786a75aded3b524df3d7458c585f0f8419c51351202492ec48bb10246bc3",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T21:54:59.536531+00:00",
      "head": "8a7bbfa9bf454f054b35e4fb5e999a20e602f03c79027d56c7e67a966bba0d36",
      "node": "103.wake",
      "snapshot_digest": "3592d8fa7f210813130cb692f74d1522815e916775a54a48b3bf6cdc48732078",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T21:55:48.766304+00:00",
      "head": "dd877045980bc51671ca4579d37f98ad2afdfac5ccc13c79caee9f0460dcb46f",
      "node": "200.wake",
      "snapshot_digest": "6272e32d0fa18cacd7e3073da5b0e0584c19a3413af84552cd94fac578c1c56f",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T21:56:58.286587+00:00",
      "head": "49b9d085c7b92de9d11dd05ad9f684621b470e9039edb2e9df5c6b897061b31d",
      "node": "201.wake",
      "snapshot_digest": "662fed494b7f64a61cd491f74a830249768763dded22fe89804b65da1aee5509",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T21:54:44.271901+00:00",
      "head": "946e95b9006dc7d645732d06937e2cf793dad64c60015039b4281f6c70627545",
      "node": "202.wake",
      "snapshot_digest": "94fef864bb91d2d186e2dce6820f9783ba7f7d2dd88b7aee49b7d439eda20dc9",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T22:00:00.727986+00:00",
      "head": "03053988fa02b472d3cd8ffd5d3a08daa479b55b36c77d0a623e9f0541b182b7",
      "node": "203.wake",
      "snapshot_digest": "de6ddcad6afbd64624ddffc1279d20832649ccba804f0252777387fa26948609",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T22:01:21.256431+00:00",
      "head": "2d69f56a1fc63e18a5f6eb233c040ec646d0a355456a4ee3a09971d72ecf182b",
      "node": "300.wake",
      "snapshot_digest": "2612d475a92c9c9681e7420d24d91b3bd2f281e95defbe6437246c897c5cf366",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T21:59:10.571796+00:00",
      "head": "d7131148132159ac7761cc55dc15fbc4f3db160ca882fbd284958ec99ec1456f",
      "node": "301.wake",
      "snapshot_digest": "27898534345bdf38bc4e92313a23146d80f8a107c707e96b5816c4e9820084c2",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T21:58:03.848639+00:00",
      "head": "def5c57b4c5d10401eecc16d607c32d8d76fdb5035904b038fb6b33f2e835ed3",
      "node": "302.wake",
      "snapshot_digest": "f85d4715d6c0587f6ab5fe2b6b48cd2829330db837d4cf2ad1ae78cccdb51add",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T21:54:21.216123+00:00",
      "head": "5416bca82a7fc56e31ecffc32131da702e4837853f6e1e64d73e5aeb78bd0386",
      "node": "303.wake",
      "snapshot_digest": "9c0131b5d0e6d3417cb61df601db0507c67ded0eaabb98aab102a80454153d2a",
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
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d65396536303861313834636634353463.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d35643262346439633633616534323565.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
