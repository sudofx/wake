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
  "generated_at": "2026-10-26T15:08:46.419738+00:00",
  "head": "snapshot:baf4794cc5e5c5501f77ea8768adbaf3e5ed4455736ac49899d418880afe85ea",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T14:40:28.137111+00:00",
      "head": "97bc43007b6c1065067c4301901841407fdcd6417530f8504faf126d06494d3d",
      "node": "100.wake",
      "snapshot_digest": "5565188567dead2ecd725466f7786bd45d0da7e638fdffc1f8e17ef97c9aa1b5",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T15:05:53.483498+00:00",
      "head": "519ef4c59465bf92c407e99a930a906428390aad29523401ae67a32bed3c295a",
      "node": "101.wake",
      "snapshot_digest": "6a57b5dcc6aed0a857d1230b3956ca816691cf15bfe782fe1ce43f8f64336f04",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T15:02:30.471704+00:00",
      "head": "8288c517bd2503f0c3153b95de6b75d3329623ccdc55c82952db780a471d8284",
      "node": "102.wake",
      "snapshot_digest": "3d052bc8bc6ae4ffe64d4bd71ec660138dd394cce2012b506b8c9f703d57edd0",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T14:40:29.656538+00:00",
      "head": "57283535b207d53954b15072517dfa7ecd8e8d3f7864ef45ccbca9c46c40b915",
      "node": "103.wake",
      "snapshot_digest": "a576c66cd01de3738e51947aa540cacf2a9236c88b919535aea58673f6516d7a",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T15:02:45.529116+00:00",
      "head": "6761b6da38a6033dfddb40ae4964dfb3fcdd39ec478630a6e66046b9cb621bb5",
      "node": "200.wake",
      "snapshot_digest": "b7366be382865f1b86c9213bed1b0889edc71360a24d276f7085b4703bee7d02",
      "version": 43
    },
    "201.wake": {
      "generated": "2026-10-26T14:40:30.018092+00:00",
      "head": "7eee3b1a77e64146fe681881e51787a3deab5a3b0eff1a3f034f182c9573e02a",
      "node": "201.wake",
      "snapshot_digest": "90c904224aac01c3ad7a89558acf278bec410c5bc9eb2b31b1d0c4227a69b9e2",
      "version": 44
    },
    "202.wake": {
      "generated": "2026-10-26T14:40:28.168484+00:00",
      "head": "55bab7e399c14edb9fd7a865183a3775c32dc00f5e61b2c462b90bcc09a9b502",
      "node": "202.wake",
      "snapshot_digest": "85efb4423787696d3d850d9ed5344db47cf50c18d0a1c2da0ec3a371a5342b92",
      "version": 58
    },
    "203.wake": {
      "generated": "2026-10-26T15:05:12.532696+00:00",
      "head": "abd1998d186b994f03dfcdda1fe38ab8d65a82130b7116124393601711013b5b",
      "node": "203.wake",
      "snapshot_digest": "a021aaa4c30d517f2b5516dabefdfc76da8d7e9aa238b8a0adace1e47709d877",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T14:40:28.582136+00:00",
      "head": "8ee4f68dc3f1d663988035bba10ee7b4fbc9b86bd07d45290719f92b0fcbb7fd",
      "node": "300.wake",
      "snapshot_digest": "ddd70cf6921c441288aec7222b831f366c5435f35a1e6792023d699c8998767b",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T15:08:46.419738+00:00",
      "head": "690de83babfc5b2475e0acb081a79b8ecda3f0650b978c325975a57dac7d38fa",
      "node": "301.wake",
      "snapshot_digest": "0df125ab164dbd2934681f5ea809529895f6ab731eecb74498ac756baebc52a2",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T15:04:53.404722+00:00",
      "head": "a98ba4547e2738161df3d84e3580156d8e152f91db55e7c74d538f3b800759c1",
      "node": "302.wake",
      "snapshot_digest": "4dedfeb0480b6cb300bbe20451800a3323ca51bb4c84e21013757d6999be26a7",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T14:40:31.656841+00:00",
      "head": "a4a01dea64b683b869d77963883e7eb90589f502eac7d6c7bacb155161dabced",
      "node": "303.wake",
      "snapshot_digest": "d4a7b091f8d4bd8d57763e591749a2136e0a4798ff2115311ea09fb7acb83720",
      "version": 56
    }
  },
  "version": 574,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d37336531333333646564333434306536.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d39333131613636616432656234616533.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
