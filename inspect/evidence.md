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
  "generated_at": "2026-10-26T02:39:04.327157+00:00",
  "head": "snapshot:7426dbbb8cf65fc37cd8009e5a4a3a6d03c5b5d7522d8bdedddfa078b3f95f08",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T02:39:04.327157+00:00",
      "head": "1e478289a44c6802b7d684446883bb0f947fdf7aee0ca99f6395ab6c5893c1b6",
      "node": "100.wake",
      "snapshot_digest": "f99cfb902c5436fd4469dcf961c6a77485c66b13a02bc2c0f1c17e5b407589fe",
      "version": 29
    },
    "101.wake": {
      "generated": "2026-10-26T02:38:48.666037+00:00",
      "head": "aab619899f2e43de73ca25f0bd9851d51f80261b4f0e514df2e71d21a3871476",
      "node": "101.wake",
      "snapshot_digest": "d7eb672d0e18aac28fe84b30a64dfc5ebc9895d297e8b3d3ac582ddc8126267b",
      "version": 46
    },
    "102.wake": {
      "generated": "2026-10-26T02:26:02.631210+00:00",
      "head": "0c9116d23dca6808a165279c2d0f27e5451ae221dca1681b6dcdbaa309c070c8",
      "node": "102.wake",
      "snapshot_digest": "f7b01ba2ba66a7f778b249abbc4c2875ea4f12999e40b786d2212a4a6344058f",
      "version": 59
    },
    "103.wake": {
      "generated": "2026-10-26T02:37:52.446007+00:00",
      "head": "33e795f4b7e9e16fe904beed0fca497af181f13b1a58ff48d3d30d5d8d884c0d",
      "node": "103.wake",
      "snapshot_digest": "a9ec8223288eee07b5943c6235612cdd7942f01a521f5079a0f082bc0c79297e",
      "version": 41
    },
    "200.wake": {
      "generated": "2026-10-26T02:34:07.421947+00:00",
      "head": "f64192fb8ba765f97005baa4fa2436886d700f138fca395bbe2f8c0d9d6f4b1b",
      "node": "200.wake",
      "snapshot_digest": "0509fdff47b442adbc64d98f980c42daf54714890de1e3c85c9617dd9bb65ad3",
      "version": 37
    },
    "201.wake": {
      "generated": "2026-10-26T02:37:16.623704+00:00",
      "head": "e8cce6893df1b1def996002ae67b0ab0736f779cf34bd33646fe36b52abe1dcb",
      "node": "201.wake",
      "snapshot_digest": "34c52116b5bcac7cc61acb224ed53840a0f3fdab92e5bb7b092b2f4aadbd9b84",
      "version": 42
    },
    "202.wake": {
      "generated": "2026-10-26T02:33:34.387531+00:00",
      "head": "de39c57abb4dd246543434b267ff2cae258eff2b90cbf33651cde89eb7a46ca0",
      "node": "202.wake",
      "snapshot_digest": "5b707a3534428ea26593cd27887c7961c716717e817f8e6495969074a24c2564",
      "version": 56
    },
    "203.wake": {
      "generated": "2026-10-26T02:36:43.999079+00:00",
      "head": "0cdf593e1af12fbcee6b461784ff91c67f0b6cd0bc078183ad505ddb743850d4",
      "node": "203.wake",
      "snapshot_digest": "ec13a0cd71dc19ad581ea5258888e7a485541bcb4e8778c236b637431af109c1",
      "version": 32
    },
    "300.wake": {
      "generated": "2026-10-26T02:35:36.528664+00:00",
      "head": "0a6a4cb79b5ef1ed3b04bf08e7648bac28366554b96eaea80842ca9e1ed668ea",
      "node": "300.wake",
      "snapshot_digest": "dbee56b91f4f43ffb5acd8d42a83707714fd4ac9bb98d97862bd309092f81bb5",
      "version": 36
    },
    "301.wake": {
      "generated": "2026-10-26T02:28:18.309206+00:00",
      "head": "238c7cf13485c7370d597c045bde409eae5e9461217ad2dc28ac7e64ca5fd57b",
      "node": "301.wake",
      "snapshot_digest": "b0fa756673d147c01492119255c6fa18f18b04f6d7d33e248eb40d9655a259c0",
      "version": 58
    },
    "302.wake": {
      "generated": "2026-10-26T02:32:28.928365+00:00",
      "head": "536274866d25fe970cfd70d10c88517b2cc93e46d76c542648d5cf6f61e136aa",
      "node": "302.wake",
      "snapshot_digest": "c85b8aabaaf1fe0594330056eb8dce4e825df3b46498b0048e2e4a1b2c1e4004",
      "version": 41
    },
    "303.wake": {
      "generated": "2026-10-26T02:38:31.684478+00:00",
      "head": "e8adcf538cdddf00cc9aad56446b8980b7f96b261c7496d67b53580529f292c8",
      "node": "303.wake",
      "snapshot_digest": "745a22decb8593ec538d7a283dcdd2b81e5b8e2458efe2ddc291ffbfae30145c",
      "version": 52
    }
  },
  "version": 529,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a722d66356631373239636164306534643962.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d32356331666231333538386634613131.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d726573706f6e736962696c6974792d666f726d/6174696f6e2d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
