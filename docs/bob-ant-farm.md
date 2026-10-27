# Bob’s shared ant farm

The farm selector offers two different colonies. **My farm** belongs to this
browser and keeps its existing local save. **Bob’s farm** is a shared colony
maintained on GitHub. Visitors can observe its recorded interval but cannot feed,
reset or change its saved state. Playback does not become a new shared history.

The caretaker is a small deterministic policy under Bob’s editorial role. It
checks food availability and nest reserves and adds mixed food at the entrance
when needed. It does not use a model, Gemini key or research authority. Bob’s
notebook describes actual counts and recorded interventions; its explanations
are editorial analogies, not claims that an AI performed a scientific discovery.

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

`WakeBobFarm.mountNotebook(container)` renders a separate dated farm-notebook
section using actual numeric observations and care receipts. It uses text nodes,
not source-provided HTML, and labels the material as simulation observations.
No native blog body, article hash, evidence record, research counter or governance
decision changes. This allows farm notes to appear alongside Bob’s articles
without pretending that an old article originally contained a newer observation.

Model-written inline farm references in the native research blog would require
a reviewed editorial context integration and separately verified runtime adoption.
Publishing the browser notebook does not prove the executing research runtime
has adopted new context or that a model has learned from the farm.

Run the focused checks:

```sh
node --test tests/browser/bob-ant-farm.cjs
```
