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
  "generated_at": "2026-10-28T08:10:47.618362+00:00",
  "head": "snapshot:cf23f84c1fdbbae91fffcd5474bfee7e0478c75d31e60e42123d18af19947731",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T08:05:43.797493+00:00",
      "head": "93344312d8520306c4f5fe331b10f13aaca39615434ef4c9add0c8fc1eac7870",
      "node": "100.wake",
      "snapshot_digest": "9de9ba3dde278f72d55fcc5f9643592e2284bc849019b83ac6a282e897780d9d",
      "version": 11
    },
    "101.wake": {
      "generated": "2026-10-28T08:10:14.098889+00:00",
      "head": "b40eea7ce54981c5ae37405e699cb3a18c449cb89077878608771f7f9dde4792",
      "node": "101.wake",
      "snapshot_digest": "74bb05411b3a6772948e6ad150bad658e2495b6389c0037a7dbb0c6ee729b53a",
      "version": 14
    },
    "102.wake": {
      "generated": "2026-10-28T08:09:32.685850+00:00",
      "head": "eef652fd447c50bb7b0738f726f8ee9c2b42fe461afec4c77b0d5c4e74df9cb3",
      "node": "102.wake",
      "snapshot_digest": "8cd8cc67ea156ce0907d13b8902337463cc05181d26f224bcec1a9b0fcceffe5",
      "version": 8
    },
    "103.wake": {
      "generated": "2026-10-28T08:06:17.818992+00:00",
      "head": "0c77bc7b632d1605bd91ad26eb325c7481460c190ebcd6cfccd87b8e68e6a7bd",
      "node": "103.wake",
      "snapshot_digest": "45d282d1035a067b4bc28c5b71d4b9ab3c67811eb25113e924da107923729c9e",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T08:02:12.332546+00:00",
      "head": "1e19dc82a27666695a6a12c297285d56366a6d5b4c5804604066f36385e7c9eb",
      "node": "200.wake",
      "snapshot_digest": "fff75516c98e08e12febb48587574675eebed903c35f2b34fbd1a7d7647a9521",
      "version": 15
    },
    "201.wake": {
      "generated": "2026-10-28T08:06:33.039675+00:00",
      "head": "4de0c53d875ce92b5994677aeffbc2dcf1e9e0cdcefc547bce78064540db432f",
      "node": "201.wake",
      "snapshot_digest": "27dad1f7c2c9ce634fb1d9a0fccb03318a1242d7753002c9d3654581dada17df",
      "version": 14
    },
    "202.wake": {
      "generated": "2026-10-28T08:10:47.618362+00:00",
      "head": "db844cdef1518974b76c2a1522005e893206ca49abd8ed310865e9cf8e2512cd",
      "node": "202.wake",
      "snapshot_digest": "4bdf8eed416e3e3bc875aa64a1267d795948ab925555093f8f9de1c634b11df9",
      "version": 15
    },
    "203.wake": {
      "generated": "2026-10-28T08:09:48.706045+00:00",
      "head": "b5a7d48ada68bb94e796b3e63cb7c0d79edcfc3e796708b273c7f6d75b1e631e",
      "node": "203.wake",
      "snapshot_digest": "2779f44145d1fb59d07292517f775a046edd38e23b0496f69d6af156be73baa7",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-28T08:09:41.662551+00:00",
      "head": "f5acb38049bd962c3c29d37861e19308765c046072141941ba04ff5673030c6c",
      "node": "300.wake",
      "snapshot_digest": "4de16ce35d8baf65381c254b93551364493831582bd0c0138a918f73ff963e4a",
      "version": 16
    },
    "301.wake": {
      "generated": "2026-10-28T08:09:08.989152+00:00",
      "head": "b0543be168105312564b24f498d5e9b4d9fcc4ffaa2e6628ce6fdeae4f67ab9e",
      "node": "301.wake",
      "snapshot_digest": "36b5f16bc83d933a905770f285e3ca68a0be8b22b0468c5a7a70ef0d7c0230e0",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T08:03:43.427464+00:00",
      "head": "e0329e843855a147823a12e0316673510428a77e373e3e47e42519714b11391f",
      "node": "302.wake",
      "snapshot_digest": "e8ec260724d1d039e6344a0d47330716b0950175c26321c1807a78839e6defdc",
      "version": 11
    },
    "303.wake": {
      "generated": "2026-10-28T08:07:25.139919+00:00",
      "head": "cdfab34084d890c24ff4cebc7338da985f4feb885aa7cf57448cef5680f89598",
      "node": "303.wake",
      "snapshot_digest": "1810e7321004a4f764b4ec49cc8b05ddfae0a6cfe60637b4726a5fc850c701be",
      "version": 16
    }
  },
  "version": 168,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d65326333336630386632646434363562.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d31313763353166613230353734633364.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
