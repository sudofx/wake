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
  "generated_at": "2026-10-25T13:46:34.352007+00:00",
  "head": "snapshot:e7380f7184bcd2394ee29fc6d969c3a4b8be6681fa84d3eca448714393f81ad5",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T13:15:56.070570+00:00",
      "head": "391c18b3f4c93309d37960bcf55c44b565aaf4c1a1b9154de18b77b2557cb7cb",
      "node": "100.wake",
      "snapshot_digest": "4205c8caf1efcf0c8455b15aceaf4b9d503c3ad35f4938ae223d47be2041d77e",
      "version": 26
    },
    "101.wake": {
      "generated": "2026-10-25T13:43:00.244964+00:00",
      "head": "41664c6f34955d6f10a643bfbcb95611dc22c03f02851b4bd1832e3ea6ca09d5",
      "node": "101.wake",
      "snapshot_digest": "2d17d35cd75f689d1700ef3ce8f005bc7f64736c1b72be05564f475428b4d34a",
      "version": 43
    },
    "102.wake": {
      "generated": "2026-10-25T13:40:36.896218+00:00",
      "head": "b622173b56f530fa1f1194845b3cefdcb75f22b690f48131d0b4066d7916170b",
      "node": "102.wake",
      "snapshot_digest": "ceabbc5af98361b39985e9d025f07486e78eafda1d9067aa28c81f8f9d8fd768",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T13:45:48.564872+00:00",
      "head": "9f7302ab60881ce1272aaad97de20f707679370aa840ee39b3222d58c6829a28",
      "node": "103.wake",
      "snapshot_digest": "8fbf2b8c475e46f1f69f9534aff1e329042c2c426025a7bfec3d796d79222302",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T13:44:02.357734+00:00",
      "head": "647d4b7b55bef9b8eda0b3498671cd264c85203551dd96258b8af8e7a826cdbc",
      "node": "200.wake",
      "snapshot_digest": "0ff68fa6ed6c1501ddb88de27ed89b942da92b398a1334ad76f7a86d2fcf537f",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T13:15:58.605518+00:00",
      "head": "6f984a0ad16df48d6b70ce32fe6aa8d2bffe846aeb57e7655244649c9bc51c08",
      "node": "201.wake",
      "snapshot_digest": "488873f417da8f4c647a86cb8de77a0c596b1d70447b35326101495b1f5a65ed",
      "version": 39
    },
    "202.wake": {
      "generated": "2026-10-25T13:44:47.415028+00:00",
      "head": "6091004cc2b386863787270d7adabdb07e4f45fa6c600c07218be8d6d4bfb55b",
      "node": "202.wake",
      "snapshot_digest": "00259a83cbb3637db3553dc7d67e99fc6084611317110751483b766832695e24",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T13:43:49.581782+00:00",
      "head": "063bcd1cd71713a3978e6d78e4a39ac1f44bc93d7e769e3a3bc1d2e160dd8778",
      "node": "203.wake",
      "snapshot_digest": "38c8310a9ea8920c4cec037c9e259661d8c5405f7b3561daee859aaba9011ab8",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-25T13:46:02.791387+00:00",
      "head": "73d2f92a4a58261ed20b2250be9d41fecde188714b3373b3cefbcbaa20815287",
      "node": "300.wake",
      "snapshot_digest": "5085c23506630c5e57d184c637f5d3c5fbac3c755435721dd9aa01a05efaf24e",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T13:39:17.918877+00:00",
      "head": "2099d1ad69e01c4a362571286d11bdb1e42e7601031673ca7ae920215cfcae5d",
      "node": "301.wake",
      "snapshot_digest": "a1fea33f1dc0523d52e957f6099be3b27f0b694bd1bdf36b6073f24988f6c551",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T13:46:34.352007+00:00",
      "head": "374543e0cf4a506188d92d5ed00548b971015d65e83378ae52e0960149ae2953",
      "node": "302.wake",
      "snapshot_digest": "6dec1ca5185c38ada7ec438ca39ad2e9f5c433b4c810ef5b4b284aede0e6d657",
      "version": 38
    },
    "303.wake": {
      "generated": "2026-10-25T13:15:58.292570+00:00",
      "head": "df587691c26600ee970b9a80d95dd8aa5315428e536c0503e4d3be5f8cb89909",
      "node": "303.wake",
      "snapshot_digest": "72d09163cc3355db119a407a08918b7fd512f5b396794e33f13282339145f17a",
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
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d36643661623339646232636434636466.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d39356636616564393736636534316334.json)
- [notebooks record](../reader-records/notebooks/3130332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d637269/74697175652d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
