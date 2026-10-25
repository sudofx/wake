# Watch the digital ant farm

Open **Bob’s Ant Farm** in the site menu. The dedicated page shows 64 digital ants
walking, resting, digging and carrying grains and food. **Observe** opens counts
and recent changes. **Closer** magnifies the habitat without speeding it up.
**Trails** reveals food signals; **Add food** scatters surface crumbs.

Normal speed advances one simulation second per visible elapsed second. Optional
2× and 4× controls accelerate it explicitly. The colony saves locally about every
ten seconds and when hidden, then rests while offscreen. It resumes without
inventing activity during absence. Each browser has its own colony. Clearing
storage loses it; failures are visible. Another tab writing the same colony
pauses this tab and prevents stale writes. Reduced-motion preference starts
paused. Replacing a colony requires confirmation in Colony options.

## How the ants build

A small starter shaft, chamber and three short branches are provided. Digging
extends the tips of narrow passages; it cannot erase side walls into a broad pit.
Twelve workers are potential excavators. At most two work at one face; others
wait or give way. Each worker pauses at the soil, removes a grain and carries it
to the entrance before returning. Ten completed removal trips are required per
new segment. Food is removed from its source once and delivered once at the nest.
Added crumbs are measured as viewer interventions.

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
moisture, collapse, reproduction, brood care or realistic colony energetics. The
provided starter nest is excluded from the excavation counter. Progress now takes
minutes to hours. A tunnel segment is a model unit, not a physical measurement.

## Ask Bob about what happened

In **Observe**, ask a question at Bob’s observation desk. Each question captures
the current counts and at most twelve recent ten-second samples, plus the total
food added. Bob receives that sample and a bounded recent conversation. He can
compare changes and discuss hypotheses. He does not watch between questions or
control the ants. **Save observation** downloads the versioned sample.

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
No external libraries or third-party browser assets are needed. Generated macro
soil and ant-body textures are bundled locally; animated legs and antennae remain
procedural. The fallback drawing remains available if an image cannot load. See
[art provenance and prompts](ant-farm-art.md). Canvas keeps continuous movement cheap;
HTML keeps controls, focus and counts accessible. Cached terrain redraws after
excavation or resize. Frames are capped at thirty per second, pixel ratio at two,
nodes at 3,000, faces at twelve, food sources at 32 and saved samples at sixty.
Mobile uses the same world and touch controls, without hover or drag requirements.

Browser state uses `wake-ant-colony@2`. Earlier prototype `@1` saves are left
untouched; they are not imported into the corrected model. No shared server colony,
URL state or offline catch-up is provided. `wake-ant-observation@1` with model
`pellet-tunnels@2` is bounded numeric advisory input. The API strips extra labels,
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

The pale sand substrate and lighter tunnel interiors keep dark workers visible.
Use **Closer +** up to 8×, **−** to zoom out, or **Fit** for the whole colony.
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
