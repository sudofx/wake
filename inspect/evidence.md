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
  "generated_at": "2026-10-23T15:40:48.368068+00:00",
  "head": "snapshot:e9088f3651be9966dbb1f620e5b7427d3f20825f7c98c7ed307e05554491c5d5",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T15:31:42.203088+00:00",
      "head": "5fd8e58bfc84d3e1d285a91f1b9de9f0338749012bce89928688adebf0850e73",
      "node": "100.wake",
      "snapshot_digest": "c698871d4c85ec05659a079019938e0dee2ade4cd262857427ba98e037e8c8e8",
      "version": 16
    },
    "101.wake": {
      "generated": "2026-10-23T15:40:48.368068+00:00",
      "head": "9b4a942c70c1494efe4267186a4507a7fc947dc4159709a723712a4b96ea1f5f",
      "node": "101.wake",
      "snapshot_digest": "876b49c1fce7c992f8369277d4eb2e4e57f527865d206f1a5245b1bbc55be4e5",
      "version": 26
    },
    "102.wake": {
      "generated": "2026-10-23T15:38:24.039153+00:00",
      "head": "69cb52c0ec04493c1bbf38f9036bb9ea0049b658f680ba5310fb028756c83270",
      "node": "102.wake",
      "snapshot_digest": "e168b3ed36cae3061fcb2afb295f043d475a5957845ef3a85207dd43cbd4571d",
      "version": 32
    },
    "103.wake": {
      "generated": "2026-10-23T15:23:35.395166+00:00",
      "head": "475bddb553fe3a688f3d237087c0f86ab4ca6771f0bcd4bcd995d175762b0c77",
      "node": "103.wake",
      "snapshot_digest": "e21834700f32bd2bb53a10ed515845892f6a3813e532e748092fb7e41ded4c2b",
      "version": 22
    },
    "200.wake": {
      "generated": "2026-10-23T15:32:37.036477+00:00",
      "head": "19c765452b7fc85ea0ab1ff8dc0eb51a86fded5985763904a4ed7ff81bee1a75",
      "node": "200.wake",
      "snapshot_digest": "98ef0c2be44521e5bf3460285bd3f60e950327b5da2b1df9cbafef4a14ece2b3",
      "version": 21
    },
    "201.wake": {
      "generated": "2026-10-23T15:24:15.176415+00:00",
      "head": "6c6c905df01c940409e69c1475308f90e05238dbaa13f0b9ddc16f4e146601f8",
      "node": "201.wake",
      "snapshot_digest": "543918b9d5604a38b593993b63eb3767ccf53e298e36f0b761ff45cb72f9ed66",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-23T15:40:03.424894+00:00",
      "head": "a3d4d62059850f51dee93bbf636de01e2bacf50b3a011ea8ce62d5d4998a01c0",
      "node": "202.wake",
      "snapshot_digest": "0b666742ce703fd4f647accb2bf1b1e4224840a5275e7e1451db62319981dec4",
      "version": 34
    },
    "203.wake": {
      "generated": "2026-10-23T15:31:55.540201+00:00",
      "head": "1c2a131f5d030ba4e532b137f8bce789f55bb91f7dd71c2ff9734d0eb435971a",
      "node": "203.wake",
      "snapshot_digest": "6ac60d043abf5b552850cd4754ef57132890b8fe8b998917110b82769e40e8bf",
      "version": 14
    },
    "300.wake": {
      "generated": "2026-10-23T15:23:14.462210+00:00",
      "head": "d8b2fdffc24b9ea684085ff20124d5521fa48dce619efb7282d7d58c3739530e",
      "node": "300.wake",
      "snapshot_digest": "0a3578c09573e0f8caec0975d7660653d671584100f537bd7747ca8e42aa3704",
      "version": 19
    },
    "301.wake": {
      "generated": "2026-10-23T15:39:24.000149+00:00",
      "head": "a959a3e74001a9a25836612b1ce9e705145b3e993b352f43bb57b9bfb6615389",
      "node": "301.wake",
      "snapshot_digest": "c3f6daf8c3df68b754d8e5c6d42396d3dc8e623a1489dda203a98268ede3f716",
      "version": 31
    },
    "302.wake": {
      "generated": "2026-10-23T15:33:25.538853+00:00",
      "head": "8072638de0d7d97f4a65073d2ece1e4abf26e880c1c12b6d16fb02e811e8f350",
      "node": "302.wake",
      "snapshot_digest": "b1476f69220dd4a3ff2aa5da1a41cb92b5f7e5c96f98e2d4cff9af74d9bb9895",
      "version": 14
    },
    "303.wake": {
      "generated": "2026-10-23T15:21:43.278885+00:00",
      "head": "23a596764b5b3eda00992e7991ae60e04e602d89595a50cb2e833ea8258c0153",
      "node": "303.wake",
      "snapshot_digest": "b51614ad9bcb11a12868880eba8cf1a7ce5a165225d15b35a2c8c377a5ba1bfc",
      "version": 29
    }
  },
  "version": 280,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d363131313666643138656532346362/34.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d363361383037363838326339343531/62.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
