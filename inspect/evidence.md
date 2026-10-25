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
  "generated_at": "2026-10-25T14:59:31.719834+00:00",
  "head": "snapshot:01dc1ccc5c7bae306c572866874e7ff02be7c5f8f5d429622e379d9db2557f9c",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T14:50:15.322441+00:00",
      "head": "2f90cc540d0a5a6073d83c54202536bb812dcf7e874a72afa73b34550e61d9bc",
      "node": "100.wake",
      "snapshot_digest": "75fecc035f2087e6163bdee140bac6817445a1c8c97f467c568ea5fd6d4ec205",
      "version": 27
    },
    "101.wake": {
      "generated": "2026-10-25T14:55:38.312913+00:00",
      "head": "6ac4f4391c32363598f71345846de2e8215b38ea888c6c44e12339ce17924f1a",
      "node": "101.wake",
      "snapshot_digest": "ca0a5061099fc3e2439f107854157f52a22fefd803c67e8caab7ec3a026eac6d",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T14:55:12.048947+00:00",
      "head": "99d3b3a05d02c8364257de75d2985e3f98ce04e632a48c445c0903935fc2c1de",
      "node": "102.wake",
      "snapshot_digest": "d811c148c946414cc865e8f9d98b95c91125ca06eeda5e9fcc54821861690a85",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T14:47:45.545121+00:00",
      "head": "05d18a9702662dfa10dfce09202fa06fee3433a0725f7fe232439922527da836",
      "node": "103.wake",
      "snapshot_digest": "d1361ea61250184c7ef857815d35c82704c32722a60f7ab270953b9fbca720c4",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T14:59:31.719834+00:00",
      "head": "0c6d5a7fbcae3f3d4de99b67b6ba347cf6d6887eb1a2b4392897ff6d5cbe8919",
      "node": "200.wake",
      "snapshot_digest": "cea8fc1267ba68d1ddbb03dc50de6fbbe7a9f968c65f6030528f3ab7b6e66992",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T14:53:05.767986+00:00",
      "head": "68d3c367840ffc00d08f5d43dffb508ea2f86eb214d64b1f63814e207039ed66",
      "node": "201.wake",
      "snapshot_digest": "924c025ec3f3ee64957a25d93b268d61f03a385bf6b0320abb9837f8acff4992",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T14:57:33.025690+00:00",
      "head": "ca16882d47d0745b0611e252ad2099100eeb388189665d54ffca1cd312b05da8",
      "node": "202.wake",
      "snapshot_digest": "d3ef2a7548a4072207f8d91c5f3e46f4883dd49cc18c5be2481bdd3a5efbad94",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T14:57:44.749619+00:00",
      "head": "58f214295b3a9607bbd67d7385d3b9c2925e2e616051d690c272b100daffe2c1",
      "node": "203.wake",
      "snapshot_digest": "40014ab699b19dc2666427ee14122cc2736033eb829ae29a78e147f1170580f0",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-25T14:48:55.428616+00:00",
      "head": "37d9bc7a7ab0f39598df345ff043dd4e1f9dfe1ac45e955754916dba41aa79e9",
      "node": "300.wake",
      "snapshot_digest": "8e31620f896350e6e162627efcbd7969e1fab64c5c5571e9ee7feecc1e78c124",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T14:55:01.723962+00:00",
      "head": "db71dd3c348eb7d43b420a7573ebed8d0e5ded238fd199e4e33e3f0a9487cb31",
      "node": "301.wake",
      "snapshot_digest": "0bde2897fd156726bdec42dc9bedfc96d7bb4822e5576e9147c9f91bdc2cb3dd",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T14:52:12.265936+00:00",
      "head": "294a1a3f882b9f4a02d14f96d928954b4cd81ed8ccd146769acf0e8d3354e696",
      "node": "302.wake",
      "snapshot_digest": "0ca5f4646a7b4d07a9f979710c0f0e96aac07402a71346c5d374a08f512739b1",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T14:52:00.964035+00:00",
      "head": "e0a666312bee7731a7f6ea629b66b70914a36f176235121af68417e89917f37c",
      "node": "303.wake",
      "snapshot_digest": "b1d00cb2dcf034e4a814681e0028e7f5f6a82d11623681f4c30f666734b429fd",
      "version": 51
    }
  },
  "version": 508,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d30373836306635356430666634346535.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d65656663373962613566313334326266.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
