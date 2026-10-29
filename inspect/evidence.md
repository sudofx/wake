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
  "generated_at": "2026-10-29T17:31:20.595648+00:00",
  "head": "snapshot:abd0ccc4b2611f6d99478faa51e3d3c14ba1d7a47638e7e68e63563af01c2332",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T17:30:10.729084+00:00",
      "head": "ebf42d5b14b14232c461c2652150278a5a40cfc8f74603f40bde0719ea691c22",
      "node": "100.wake",
      "snapshot_digest": "5d62eaa15105fd64312809646c3f147d8d91fece21be737932eabca30d5f5f39",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T17:29:56.572062+00:00",
      "head": "bf274dcb972e0bb5730191cc86ee87befc76fa3d5a0e2f5f2703647e33194b7f",
      "node": "101.wake",
      "snapshot_digest": "f38e87d54e9dc436a1f214721c7bd446100f417057cb0294c68c3bc47ca5e784",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T17:29:56.017490+00:00",
      "head": "800dcdeabff82334438685d120c0d25581d34ee7defa3521130b08184d08e542",
      "node": "102.wake",
      "snapshot_digest": "13b8329a95125f330926a1020150ac1e5227a7345ac07b46513042bf7fd30f0e",
      "version": 19
    },
    "103.wake": {
      "generated": "2026-10-29T17:30:30.030923+00:00",
      "head": "c7169ce18cbd2a6095308f1c3463e71e9a77debd8427871575cff69c8cf2d620",
      "node": "103.wake",
      "snapshot_digest": "86ac92ed2865ad2127853f091875c1fa3f2d27a9c22b6bcb6b3d08ae754a5194",
      "version": 30
    },
    "200.wake": {
      "generated": "2026-10-29T17:31:20.595648+00:00",
      "head": "24382965de522582513befad61925b14c20c3977e7951b48e207e1d8abf4eaa0",
      "node": "200.wake",
      "snapshot_digest": "7e66036b630ddb087b864a118a53048362347e466aa5b31282473805987082a9",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-29T17:30:04.031259+00:00",
      "head": "9afd1602c305263f682e38bcc02c31a6d14a03b9fa573e4e553894887a2ee790",
      "node": "201.wake",
      "snapshot_digest": "56ba8a43179810793ff78c067522172142c0134b4be015b5f3bec9d937245369",
      "version": 25
    },
    "202.wake": {
      "generated": "2026-10-29T17:14:22.163771+00:00",
      "head": "e5d548629e694530c377f1954efb601aba5ed361de2b8ca957944f68606642a2",
      "node": "202.wake",
      "snapshot_digest": "ef56500dfb2cf2be25180c37b6af0d6b29525183b9ff46e220480a629e1afe1c",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T17:29:58.113718+00:00",
      "head": "50fd377a8a989fe80729006452a19ff0202431c76e5e22850c8832c82d6f4491",
      "node": "203.wake",
      "snapshot_digest": "df5562a5a15282e74a60b8f43377528820ebf6d4dddfbe4ca35b6351f495a10c",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-29T17:30:14.380080+00:00",
      "head": "8ce755628009658eb146baf27f99bcbc17f1cae2b3a93b474a1d5de82f70bdd8",
      "node": "300.wake",
      "snapshot_digest": "0f536489a18e93e0b05519a33972158dc809e4dba7be3e13d07f4f0306975ea5",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T17:30:06.754508+00:00",
      "head": "b2e3a5768f22180de92ede76638e90b33b5ec2d1c7c2d59c5615de2fa014e73a",
      "node": "301.wake",
      "snapshot_digest": "70acd659f307fd74e2d33440efb5a8edb8673025a857e94536cb58afdd21f4b3",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T17:30:08.457054+00:00",
      "head": "d2d10b1c8622deb6b746ce2d27d79d6e5ede88c5e298c8eb211fe97eba73cd48",
      "node": "302.wake",
      "snapshot_digest": "b5b8ea25ce09bb4e323d0ac2479450b5e7e780fc2d09e03eafa882f5449fdb67",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-29T17:14:30.442799+00:00",
      "head": "f755b00ef5faf2dc70e31985ba6bc82628ff5b2b07abe81483fa8fbf70919f2a",
      "node": "303.wake",
      "snapshot_digest": "e4609125e9c209bf8694039e41a64dd13b56946239bb4b04062784ae1e0ab68a",
      "version": 24
    }
  },
  "version": 299,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d37623632313061303761323134346631.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d36383334363662356631363734613833.json)
- [notebooks record](../reader-records/notebooks/3230322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d726573706f6e7369/62696c6974792d666f726d6174696f6e2d30312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
