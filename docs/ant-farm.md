# Watch the digital ant farm

Open **Bob’s Ant Farm** in the site menu. **Observe** opens live counts, an
individual-ant selector, Bob’s observation desk and colony options. **Closer**
magnifies the habitat without speeding it up. **Trails** toggles visible purple
food signals; **Add food** scatters surface crumbs.

Default **1×** now runs at the previous **4×** pace: four simulation seconds per
visible elapsed second. The **2×** and **4×** controls multiply that new baseline.
This is a viewing preference, not a biological speed calibration. Reload resumes
movement automatically, including with reduced motion enabled; that preference
reduces painting to ten frames per second. Pause remains available explicitly.
The colony saves locally about every ten seconds and when hidden, then rests
while offscreen. It never invents activity during absence. Another tab writing
the same colony pauses this tab and prevents stale writes. An unreadable save
is preserved untouched; a temporary colony cannot silently replace it.

## How the ants build and live

A varied starter shaft, chamber and one to four branches are provided. Workers
extend narrow passages with ten pellet removals per new segment. At most two
workers excavate each face. Blocked faces free their job slots; workers seek
new branch origins instead of permanently exhausting a twelve-tip lifetime
budget. There are at most twelve active jobs and 3,000 graph nodes. Upward jobs
can open additional entrances connected to the surface, with shortest-path
soil return through the available entrances. The habitat remains finite; growth
cannot continue after every viable site or the node budget is exhausted.

The colony begins with 64 workers and supports at most 128 workers plus brood.
Delivered food supports new brood, which matures after three simulation minutes;
well-fed colonies can grow while older workers die naturally. Worker lifetimes
are one to two simulation hours, with staggered ages among starting workers.
Food reserves also pay a bounded maintenance cost. These compressed life stages
make population turnover observable; they do not reproduce real colony biology.
There are no predators in this version. Add food to sustain an aging colony.
Food outside and food brought home remain separate counts.

Each worker keeps a non-reused number, scoped by the colony seed. Choose its
number or tap it in the habitat to inspect role, age and activity. **Follow ant**
centers the enlarged view on that worker; dragging takes camera control back.
The most recent 64 natural deaths remain available for an already-selected ant.
Only the selected ant is labeled on the canvas to limit visual clutter and cost.

The rules are informed by primary ant studies:

- [Buarque de Macedo et al., 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8433525/)
  observed incremental excavation and approximately straight segments, often
  descending, rather than uniform removal of the surrounding soil.
- [Gravish et al., 2013](https://crablab.gatech.edu/pages/publications/pdf/PNAS-2013-Gravish-1302428110.pdf)
  found early fire-ant tunnels comparable in diameter to body length. Over the
  studied interval, nests grew mainly by lengthening tunnels while diameter
  remained approximately stable.
- [Aguilar et al., 2018](https://crablab.gatech.edu/pages/publications/2018-Collective-clog.html)
  studied unequal excavation workloads and retreat behavior that limits clogs.
- [Hunt et al., 2016](https://pubmed.ncbi.nlm.nih.gov/26909181/)
  reported intermittent movement and responses to environmental cues between
  movement bouts in the studied species, informing pauses rather than constant
  jitter.
- [WSU’s identification guide](https://pubs.extension.wsu.edu/product/identification-and-habits-of-key-ant-pests-in-the-pacific-northwest/)
  and [AntWiki’s morphology reference](https://antwiki.org/wiki/Morphology_and_Terminology)
  inform the recognizable waist, gaster and elbowed antennae. The drawing has
  six articulated legs attached to the mesosoma, mandibles and a walking gait.

The implementation is an illustrative 2D model informed by these observations,
not a validated species simulation. Worker fractions, walking pace, grain count,
dig duration, separation rules and branch probability are chosen for this display;
they are not measured biological constants. It does not solve granular mechanics,
moisture, collapse, detailed brood care or realistic colony energetics. Birth and
natural death follow simplified display rules. The
provided starter nest is excluded from the excavation counter. Progress now takes
minutes to hours. A tunnel segment is a model unit, not a physical measurement.

## Ask Bob about what happened

In **Observe**, ask a question at Bob’s observation desk. Each question captures
the current counts and at most twelve recent ten-second samples, plus the total
food added. Bob receives that sample and a bounded recent conversation. He can
compare changes and discuss hypotheses. He does not watch between questions or
control the ants. **Save observation** prepares a download and a copyable text fallback.
Colony replacement focuses an explicit confirmation; canceling preserves progress.

Questions use the existing shared Ask Bob limits. Watching, walking, digging,
saving and local observations make no provider calls. Chat text and the sample
go to the hosted WAKE answer service and Google Gemini only on submission. Recent
chat stays in page memory; the service retains admission counters, not colonies
or conversations. Both website assets and the matching answer-service update
must be published. Local preview does not forward questions remotely.

## Implementation and boundaries

`ant-colony.js` owns the seeded tunnel graph, timed work and validated save format.
`ant-drawing.js` draws the same anatomy at normal and enlarged scale. `ant-farm.js`
owns one Canvas2D view with two cached buffers, HTML controls and text observations.
No external libraries or third-party browser assets are needed. The ground uses simple drawn colour fields. The generated ant-body image is
downsampled once into a small reusable atlas; animated legs and antennae remain
procedural. The fallback drawing remains available if an image cannot load. See
[art provenance and prompts](ant-farm-art.md). Canvas keeps continuous movement cheap;
HTML keeps controls, focus and counts accessible. Cached terrain redraws after
excavation or resize. Phone rendering is capped at twenty frames per second and a 1.25 pixel ratio;
desktop uses twenty-four frames and a 1.5 pixel ratio. Canvas buffers share a
1.5-million-pixel ceiling, independently of zoom. Paused views redraw only on
change, terrain is cropped to the viewport, and off-screen ants are not painted.
The simulation still caps
nodes at 3,000, faces at twelve, food sources at 32 and saved samples at sixty.
Mobile uses the same world and touch controls, without hover or drag requirements.

Browser storage keeps the `wake-ant-colony@2` key; new saves use schema `@3`.
Validated `@2` saves migrate in place, preserving tunnels, IDs, counters and
elapsed time. New lifecycle and graph-connection fields receive deterministic defaults. Earlier prototype `@1` saves are left
untouched; they are not imported into the corrected model. No shared server colony,
URL state or offline catch-up is provided. `wake-ant-observation@1` with model
`pellet-tunnels@2` through `@7` is bounded numeric advisory input. The API strips extra labels,
instructions, URLs and model choices. Samples remain unverified user input. Ant
questions fetch no research articles and use existing admission, cooldown and
provider restrictions.

The exporter ships a dedicated presentation page with deployment binding but no
research masthead, runtime observer, record transport or control plane. Nothing
reads local colony state into native records, research progress, Attention,
governance or autonomous improvement.

Run focused checks from the repository root:

```sh
python -m unittest tests.test_ant_farm tests.test_shared_chrome
node --test tests/browser/ant-colony.cjs deploy/ask-bob/tests/api.test.js
```

Checks cover narrow fixed-width growth, gradual excavation, bounded locomotion,
pauses, connected paths, food conservation, exact save/resume, malformed saves,
filtered exports and advisory streaming through the existing budget. Provider
output is mocked; these checks do not certify live answer quality or biology.

## Sand, closer inspection and movement

A quiet, drawn cream background and lighter tunnel interiors keep dark workers visible,
without photographic sand or enlarged grains.
Use **Closer +** up to 4×, **−** to zoom out, or **Fit** for the whole colony.
Drag to pan; pinch or scroll to zoom around a point. Keyboard users can focus
the habitat, use plus/minus and arrow keys, and press Home to fit. Camera changes
do not restart the saved colony or accelerate time.

Movement model `pellet-tunnels@3` retains the excavation and save format from @2,
with short heading-change pauses and individual walking-speed variation. The
renderer advances alternating tripods with distance travelled, keeps feet planted
through the longer stance phase, and uses a quicker lifted return. Head, gaster
and antenna motion break up the rigid silhouette. These are illustrative choices,
not measurements or a calibrated species model. Existing @2 browser saves resume.

[Zollikofer (1994)](https://pubmed.ncbi.nlm.nih.gov/9317406/) reports alternating
tripods and shortened inside strides during curved walking.
[Deeti et al. (2023)](https://pubmed.ncbi.nlm.nih.gov/37093284/) describes stops,
body turns and fixations during scanning in the studied desert ants. These inform
the movement vocabulary rather than supplying universal timing parameters.

## Varied tunnel layouts

Model `pellet-tunnels@4` uses seeded variation in entrance position, shaft bends
and depth, two to four uneven starter branches, and the angles and timing of later
branches. A seed still reproduces its own history. Existing @2-format saves keep
all their existing nodes, ants and progress; future excavation uses the varied
growth rules. No saved shaft is reshaped and no colony is reset by an update.

## Winding growth

Model `pellet-tunnels@5` keeps the same save envelope and existing tunnel graph.
New colonies begin with one to four irregularly angled branches. Future segments
use a persistent seeded turn and a broad illustrative soil tendency, allowing
winding, lateral and upward passages below the surface. Soil-wall clearance and
fixed excavation length remain enforced. Branch intervals and origins vary, and
returning diggers sometimes switch to a newer face. This adds variation without
per-frame terrain calculations or reshaping a saved colony.

## Living-colony checks

`node --test tests/browser/ant-colony.cjs` covers exact new-save continuation,
legacy-save preservation, rejected invalid identities/connections, abandoned-face
recovery, and four-hour seeded runs with periodic food additions. Those runs
require late excavation, additional entrances, births and deaths together.
Browser interaction and an actual phone’s performance remain separate checks.

## Indoor container and connected passages

The habitat is a thin upright indoor display case viewed through its clear front,
with a lid, base and a small air space above simple drawn soil. It has no outdoor
landscape or photographic sand. New colonies have an uneven soil surface; existing
saves keep their original surface and all tunnel coordinates. Model `pellet-tunnels@7`
adds validated graph junctions: workers can complete a connector into a nearby
passage, producing circuits and small junction chambers instead of abandoning
every approaching tunnel. Saved `@3` colonies from model `@6` acquire an empty
junction list without losing population or excavation. The finite habitat and
phone rendering bounds remain unchanged.
