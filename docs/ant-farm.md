# Watch the digital ant farm

Open **Bob’s Ant Farm** in the site menu. **Observe** opens live counts, an
individual-ant selector and colony options. Phone pinch uses normal browser
page zoom, scaling the case, sand, controls and background together. On desktop,
the mouse wheel zooms the habitat at the pointer from 1× to 16×; Ctrl-wheel keeps
normal browser zoom. The plus lens doubles magnification; the minus lens halves it. Both stop at
the 1× and 16× bounds. **Whole farm**
returns to the complete habitat. Observe also provides a continuous magnification
slider. Drag a magnified habitat to explore it; native page pinch remains available.
Ant selection highlights the ant in place. **⛶** enters full screen, and the same button returns to the tabletop.
Touch devices use the available page viewport, with the fullscreen button to
exit; downward drags pan the magnified habitat rather than leaving fullscreen.
Desktop browsers can use native fullscreen. The habitat
fills the available window height; fullscreen soil extends to the bottom.
**Trails** starts off. It shows visited routes as dashed purple marks and
remaining food signals as brighter continuous lines. Signal brightness is scaled
relative to the strongest current signal so faint residual signals remain
visible. An empty colony reports that no trails exist yet; it does not invent
food signals. Play/pause and fullscreen
use labelled icons. Button flashes and glowing food marks show actions immediately.
**Add food** scatters surface crumbs in My farm.

The selector starts with **Bob’s farm**, a shared, maintained, observer-only
colony. **My farm** resumes this browser’s editable personal save. Switching
farms never copies the shared recording over that save. The dated care and
observation record appears in a collapsed **Farm observation record** inside each
blog article, above the collapsed **Sources and records** list. See [shared farm upkeep](bob-ant-farm.md).
If the shared recording is unavailable, the page says so; it never invents a
substitute shared colony.

Default **1×** now runs at the previous **4×** pace: four simulation seconds per
visible elapsed second. The **2×** and **4×** controls multiply that new baseline.
This is a viewing preference, not a biological speed calibration. Reload resumes
movement automatically, including with reduced motion enabled; that preference
reduces painting to ten frames per second. Pause remains available explicitly.
My farm saves locally about every ten seconds and when hidden, then rests
while offscreen. It never invents activity during absence. Another tab writing
the same colony pauses this tab and prevents stale writes. An unreadable save
is preserved untouched; a temporary colony cannot silently replace it.
Delayed or duplicate storage notifications after reload are ignored only when
they match the loaded value or are no longer current. Every write also compares
the stored value with the last known value, so a real competing tab still blocks
stale overwrites.

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
A separate, visibly larger queen lays eggs when nest reserves and nursing
permit. She has no canvas label; gentle body shifts, breathing, leg flexes and
antenna sweeps keep her visibly alive while she stays near the nursery. Pause
freezes her pose, and reduced motion removes the added body and leg movement.
Eggs, larvae and pupae take at least 90, 180 and 180 simulation seconds
respectively, with slower development when care or food is missing. Larvae need
protein as well as sugar. Nurses tend the nursery; newly emerged workers begin
as pale callows. Well-fed colonies can grow while older workers die naturally. Worker lifetimes
are one to two simulation hours, with staggered ages among starting workers.
Food reserves also pay a bounded maintenance cost. These compressed life stages
make population turnover observable; they do not reproduce real colony biology.
There are no predators in this version. Add food to sustain an aging colony.
Food outside and food brought home remain separate counts.

Each worker keeps a non-reused number, scoped by the colony seed. Choose its
number or tap it in the habitat to inspect role, age and activity. The selected
ant is highlighted in place. Nurses, foragers, diggers and resting workers have
separate selector groups. **View up close** magnifies to 12× and follows that ant;
dragging or changing the magnification releases the follow view. Taps use the
same displayed positions as rendering, including nurses tending the brood.
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
moisture, collapse or realistic colony energetics. Brood care is a bounded
role-and-resource rule rather than a biological mechanism. Birth and
natural death follow simplified display rules. The
provided starter nest is excluded from the excavation counter. Progress now takes
minutes to hours. A tunnel segment is a model unit, not a physical measurement.

## Observe and save

**Observe** shows colony counts, recent changes and individual ant IDs.
**Save observation** prepares a download and a copyable text fallback. Colony
replacement requires its inline confirmation; canceling preserves progress.
The former Bob conversation panel is removed. Watching, digging, feeding,
tracking ants and saving observations make no provider calls.

The unzoomed farm is a thin indoor container on a wooden table in front of a
window. At 1× the scenery follows local wall time, with continuous dawn/dusk
lighting; faster speeds add their extra elapsed time to the scenery. The ant
movement baseline remains four times the original simulation pace. Pinch zoom
scales the whole webpage; desktop mouse-wheel zoom stays inside the frame. The purple trails are brighter and
half the previous width. Existing browser saves are preserved.

## Implementation and boundaries

`ant-colony.js` owns the seeded tunnel graph, timed work and validated save format.
`ant-drawing.js` draws the same anatomy at normal and enlarged scale. `ant-farm.js`
owns one Canvas2D view with two cached buffers, HTML controls and text observations.
No external libraries or third-party browser assets are needed. The ground uses simple drawn colour fields. Ant bodies, legs and antennae are procedural. See
[art provenance and prompts](ant-farm-art.md). Canvas keeps continuous movement cheap;
HTML keeps controls, focus and counts accessible. Cached terrain redraws after
excavation or resize. Phone rendering is capped at twenty frames per second;
desktop uses twenty-four. Canvas detail tracks the device pixel ratio and native
page zoom, up to an eight-times pixel ratio and four million pixels per buffer.
Pinching in redraws the ants at higher resolution, including while paused;
pinching out releases the larger buffers. Scene coordinates and frame geometry
stay unchanged. Paused views redraw only on change.
The simulation still caps
nodes at 3,000, faces at twelve, food sources at 32 and saved samples at sixty.
Mobile uses the same world and touch controls, without hover or drag requirements.

Browser storage keeps the `wake-ant-colony@2` key; new saves use schema `@4`.
Validated `@2` and `@3` saves migrate in place, preserving tunnels, IDs, counters and
elapsed time. New lifecycle and graph-connection fields receive deterministic defaults. Earlier prototype `@1` saves are left
untouched; they are not imported into the corrected model. The shared farm uses its own read-only GitHub checkpoint, never personal browser
storage or native research records. Personal saves never catch up offline.
Observation downloads contain bounded simulation counts and explicitly identify
their scope; they confer no research or governance authority.

The sand contour and surface workers share one path, including the raised,
cratered entrance mounds. Tunnel caps are clipped below the sand surface. These
are presentation changes; saved paths and colony timing are unchanged. The tunnel
network is painted in one joined stroke, including its extra entrances and
junctions. This avoids the separated stroke caps produced by WebKit.

The exporter ships a dedicated presentation page with deployment binding but no
research masthead, runtime observer, record transport or control plane. Nothing
reads local colony state into native records, research progress, Attention,
governance or autonomous improvement.

Run focused checks from the repository root:

```sh
python -m unittest tests.test_ant_farm tests.test_shared_chrome
node --test tests/browser/ant-colony.cjs tests/browser/ant-storage.cjs tests/browser/bob-ant-farm.cjs
```

Checks cover narrow fixed-width growth, gradual excavation, bounded locomotion,
pauses, connected paths, food conservation, exact save/resume, malformed saves,
filtered exports, caretaker replay and personal/shared isolation. These checks
do not certify physical-phone performance or biology.

## Sand, closer inspection and movement

Packed sand is drawn from seeded angular mineral grains of mixed sizes and tones,
with small highlights and darker inclusions. Grains stay fixed in habitat space:
zooming reveals the same material rather than enlarging screen noise. The broad
soil layers and sparse larger grains remain separate from the finer packed texture.

Passages have spatially varying widths and irregular walls. Chamber contours have
broad lobes and smaller excavated notches. Filled overlapping contours connect
shafts, branches and chambers without drawing cap seams through their openings.
Recessed shoulders, a shaded interior and displaced wall grains suggest depth;
these are viewing effects, not a granular-physics or tunnel-collapse simulation.
Excavation geometry is cached until the graph or viewport dimensions change.

Workers follow the same curved passage centerlines used by the renderer. Display
interpolation includes the simulation's variable walking tempo and load slowdown.
Leg phase follows distance traveled, while the head can turn independently during
steering and stationary antenna checks. These refinements preserve the existing
simulation clock, save format and shared recording, including its pauses and care.

Use the browser’s normal page zoom to inspect the ants. Phone pinch zoom and
desktop browser zoom scale the whole scene together, while the canvas increases
its drawing resolution within a bounded pixel budget. Zooming does not restart
the saved colony or accelerate time. Existing saved colonies retain their graph
and progress.

The renderer advances alternating tripods with distance travelled, keeps feet
planted through the longer stance phase, and uses a quicker lifted return. These
are illustrative choices, not measurements or a calibrated species model.

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
with a lid, base and a small air space above simple drawn soil. The room window shows an outdoor landscape; the habitat itself contains
no outdoor landscape or photographic sand. New colonies have an uneven soil surface; existing
saves keep their original surface and all tunnel coordinates. Model `pellet-tunnels@7`
adds validated graph junctions: workers can complete a connector into a nearby
passage, producing circuits and small junction chambers instead of abandoning
every approaching tunnel. Saved `@3` colonies from model `@6` acquire an empty
junction list without losing population or excavation. The finite habitat and
phone rendering bounds remain unchanged.


## Clear glass, room scenery and feeding

The air space above the soil is transparent: the room window and scenery remain
visible through the glass. The window follows local device time with one sun in
the daytime or one moon at night. Clouds, distant hills, trees, a houseplant and
wood grain give the room depth. Matching generated photographic day/night
backdrops now supply these room materials and scenery; the case, soil and
individually animated ants remain independent live layers.

Model `pellet-tunnels@8` adds food dependence to the existing aging and brood
cycle. Workers share the nest reserve. Once it is empty, hungry diggers and
resting workers join the search for food; prolonged hunger reduces walking speed.
After 20–40 simulation minutes without replenishment, workers can die of
starvation. Individual tolerances vary deterministically. Food brought to the
nest lets surviving workers recover; it cannot revive ants that have died.
Brood is started only with enough food to retain a small reserve. Briefly visible
bodies have folded legs; Observe separates total deaths from starvation losses.
These timings and population rules are illustrative, compressed life history,
not a calibrated biological model. Feed using **Add food** and allow foragers
time to carry it home. Hidden pages still pause, so absence never starves a colony.

Existing colony saves retain their tunnels, identities and counters; previously
saved colonies begin the new nutrition tracking with no assumed hidden hunger.
`node tests/browser/ant-farm.cjs` checks real browser glass transparency, day/night
visibility, native whole-page pinch zoom, canvas/frame alignment, increasing ant
detail, bounded buffers, browser wheel handling, fullscreen and phone layout. A physical
phone remains a separate acceptance check.

## Queen, nursery and task balance

Model `pellet-tunnels@9` and save schema `wake-ant-colony@4` add a separate
queen, staged developing young, nursing, protein reserves and food-trail
recruitment. Existing tunnels, worker IDs and counters remain intact on migration.
Age and distance bias nursing allocation, while low food reserves retain an
available collector even with one worker left. Larger hungry colonies keep
nurses and foragers together. These are illustrative compressed rules, not
measured population dynamics or a validated Lasius simulation.

`node tests/browser/ant-tunnels.cjs` checks rendered tunnel connectivity in Chromium
and WebKit at desktop, phone and bounded pinch-resolution scales. It flood-fills
the actual terrain pixels from the nest and verifies that underground nodes remain
connected. An optional argument supplies a captured shared-farm JSON packet.

## Close viewing

The habitat lens redraws the visible terrain at its current magnification rather
than enlarging a low-resolution picture. A fixed seeded field of fine grain relief and angular grains,
subtle strata, curved passages and uneven shaded chambers provides increasing
detail while retaining the excavated graph. Spatial buckets limit texture work
to the visible soil. Ants use textured chitin on articulated six-leg anatomy, distance-driven tripod
strides, frame-time turning and smoothed positions. Macro views resolve antenna
joints, tarsal claws, fine setae, compound-eye highlights and shell texture. Nurses
have small tending motions beside the brood, separate from the queen. These are
illustrative visual behaviors, not a calibrated biological model.

Rendering preserves the four-million-pixel buffer limit at every lens setting.
Shared recordings and personal saves use the same unmodified simulation contract;
visual detail does not rewrite colony checkpoints. Browser tests cover nurse
selection and taps, 12× following, 16× viewing, return to the whole farm, native
page pinch and Chromium/WebKit tunnel connectivity. Physical iPad performance
and the subjective feel of holding a real farm still require device observation.

Mandibles are separate toothed blades hinged at the front of the head. Their
tips meet near the mouth: excavation and nursing open and close them, while a
carried crumb or soil pellet holds a narrower grip. Idle ants move them
intermittently; pause freezes the pose. The head texture excludes its baked-in
jaws, and its photographed eyes are used without a second drawn pair.

## Coordination follow-up tasks

These questions extend the farm's current reinforcement, decay and local task
rules. They are planned comparisons, not demonstrated collective capabilities.

- [ ] Compare repeated seeded runs with trail reinforcement enabled and disabled,
  holding food placement and simulation duration fixed. Measure delivery, travel
  and congestion rather than judging the pattern by appearance.
- [ ] Deplete or relocate a food patch and measure how quickly traffic leaves the
  old route and reaches the available patch. Keep past visits distinct from the
  current decaying food signal.
- [ ] Compare local task adaptation and recovery when workers or resources become
  unavailable, with identical initial conditions and an explicit intervention log.
- [ ] Let Bob discuss those dated comparisons alongside attributed research and
  source observations when supplied, including null results and limits. His
  writing does not control the colony or certify emergence.

The broader matched-budget WAKE comparisons are listed in
[the experiment guide](experiment.md#planned-adaptive-coordination-comparisons).
Body bridges and rafts from the discussion are a different physical workload;
they are not represented by this sand-nest model.
