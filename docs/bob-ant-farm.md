# Bob’s shared ant farm

The farm selector offers two different colonies. **My farm** belongs to this
browser and keeps its existing local save. **Bob’s farm** is a shared colony
maintained on GitHub. Visitors can observe its recorded interval but cannot feed,
reset or change its saved state. Playback does not become a new shared history.

The caretaker is a separate deterministic policy, not Bob’s writing model. It
checks food availability and nest reserves and adds mixed food at the entrance
when needed. It does not use a model, Gemini key or research authority. The
observation record contains counts and interventions. It does not manufacture
first-person Bob prose or repeat a fixed lesson.

## What is shared

The dedicated `bob-ant-farm` Git branch contains one bounded `farm.json` packet.
Each update is an ordinary commit retaining the previous commit as its parent.
The branch never contains native research records or copies of `wake-public`.

The packet identifies `wake-bob-ant-farm@1`, colony `bobs-ant-farm`, its fixed
seed, model `pellet-tunnels@9`, exact source revision and update time. It includes
the saved checkpoint, one recorded interval, food receipts and at most 48 dated
notebook entries. The reader limits the entire packet to 2 MiB and validates
both saved states with the colony model before exposing it.

Readers fetch a fixed raw GitHub URL. They do not discover models, run source
from the state branch, accept a URL from query parameters or send writes.
GitHub delivery may cache an earlier packet; the visible update date identifies
the captured interval. The single JSON object keeps checkpoint, observations and
receipts together even when different visitors see different cached revisions.

## Playback and time

Each upkeep run advances at most 6,000 fixed simulation steps. It does not try to
catch up with all elapsed wall time. If upkeep is delayed, the saved simulation
rests rather than starving because GitHub stopped running jobs. The interface
must show the update time and delayed upkeep instead of implying live execution.

`replay.start` is the save before the run. At every step, apply all `replay.care`
entries whose absolute `tick` equals the colony’s **current** `ticks`, then call
`Colony.step()`. A feed calls `Colony.addFood(x)` once and adds exactly 100 mixed
food units. After `replay.ticks` steps, the result must match `checkpoint` exactly.
The client’s `applyReplayStep` returns the next care-array cursor; `createReplay`
creates an isolated copy. Neither helper publishes or saves the result.

Death or a damaged checkpoint never triggers an automatic replacement colony.
The keeper stops and reports the problem. An extinct colony remains part of its
history; starting another would require an explicit operator choice.

## Bootstrap and verify

First finish code checks on the exact source that includes the reviewed model
and caretaker. Then initialize the dedicated branch once:

```sh
gh workflow run bob-ant-farm.yml --repo sudofx/wake --ref master -f bootstrap=true
```

Subsequent manual upkeep uses the default, with no reset or bootstrap:

```sh
gh workflow run bob-ant-farm.yml --repo sudofx/wake --ref master
```

The workflow selects a successfully checked master revision and serializes all
farm writers under its own concurrency group. Its token can write contents and
read source-check status; it receives no native-state, model or research secrets.
It writes only the fixed farm branch through normal non-forced ref updates.
Conflicting writes fail rather than overwrite another checkpoint. Scheduled
upkeep runs twice an hour, with manual and successful-code-check triggers as
additional opportunities. It never dispatches successors or rebuilds Pages.
GitHub schedules can be delayed or dropped and public-repository schedules can
be disabled after inactivity; the simulation’s paused-clock design handles
that limit. [GitHub scheduling behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

For an isolated local preview with no GitHub writes:

```sh
node scripts/bob_ant_farm.cjs advance --bootstrap --ticks 6000 \
  --source-revision FULL_CHECKED_COMMIT --output /tmp/bob-ant-farm.json
node scripts/bob_ant_farm.cjs advance --input /tmp/bob-ant-farm.json \
  --ticks 6000 --source-revision FULL_CHECKED_COMMIT \
  --output /tmp/bob-ant-farm-next.json
```

An explicitly source-bound local preview may set
`WAKE_DEPLOYMENT.bob_ant_farm.preview_path` to a same-origin
`bob-ant-farm.json` path. The public default is the fixed `sudofx/wake` branch;
an identified hosted deployment may bind its own repository. A page query can
select Bob’s farm, but cannot choose the JSON URL.

## Blog integration and evidence boundary

`WakeBobFarm.mountNotebook(container)` renders a collapsed **Farm observation
record** with dated numeric observations and care receipts. Within an article it sits inside the main
reading container, above **Sources and records**. Both lists start collapsed and
expand on click; article citation links also open the relevant sources list. It uses text nodes,
not source-provided HTML, and labels the material as simulation observations.
No native blog body, article hash, evidence record, research counter or governance
decision changes. This allows farm notes to appear alongside Bob’s articles
without pretending that an old article originally contained a newer observation.

Bob is the central public synthesis voice across the supplied research topics,
recorded self-study and system adaptations, and this farm. His eyes receive
attributed observations; his mouth publishes an interpretation. He has no research,
source-editing, governance or colony-control tools. The caretaker stays separate.

The existing group editorial path receives every member's dated overview, including
the latest notebook interpretation in each studied topic and its limitations.
The leader also reads a bounded public farm packet through two GET requests: resolve
the fixed farm branch once, then read `farm.json` at that immutable commit. The
editorial context retains the revision, raw SHA-256, capture time, model identity,
interval, before/after counts and bounded recent intervals. Metric/receipt
disagreement or unavailable data produces an explicit unavailable observation,
never a fabricated lesson. No untrusted farm prose is delivered to the model.

This source enters the leader's attributed story and the exact native editorial
invocation/publication digest. It is never imported as qualifying research evidence.
The writing model may connect or challenge an interpretation, explain where an
analogy fails, or formulate a useful public question. It must distinguish a
programmed simulation from a biological experiment and a speculative comparison
from a research finding. A connection is optional when the supplied material
does not support one. Previous Bob prose remains reading continuity, not evidence.

Regular publication opportunities require a new notebook/revision or a recorded
system-adaptation change; accepted-cycle counters and routine feedings alone
do not justify another article. Operator editorial revisions remain explicit.
The provider still returns only attributed article fields, and publication changes
no research version, journal, evidence, Attention, commitments or farm state.

The browser observation record may be newer than a displayed article. Its
publication alone does not prove runtime adoption, model comprehension or a
scientific discovery. Source checks, the hosted runtime upgrade and actual
editorial receipts remain separate verification boundaries.

Run the focused checks:

```sh
node --test tests/browser/bob-ant-farm.cjs
```
