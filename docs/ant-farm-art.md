# Ant farm artwork

The built-in image-generation tool produced these synthetic assets for the farm;
they are not photographs of observed ants or evidence for the simulation.

- `wake/assets/backgrounds/ant-soil-v1.png`: compact sandy loam substrate.
- `wake/assets/backgrounds/ant-body-v1.png`: transparent dorsal worker body.

Both original PNGs are retained unchanged as artwork provenance. Earlier renderers
cropped the body and used the soil image under excavated paths. The active macro
renderer described below uses vector anatomy and seeded soil grains instead.

The final prompt set used the built-in tool, not the CLI:

**Soil:** Photorealistic orthographic straight-on macro cross-section of compact
natural sandy loam seen flush through clean invisible ant-farm glass. Entire frame
solid unexcavated earth; no tunnels, ants, chambers, sky, plants, text or borders.
Warm medium brown upper earth grading subtly into darker, slightly moist lower
soil. Angular sand grains, mineral flecks, small pebbles, scattered fine roots,
compacted strata and restrained natural mottling at multiple scales. Documentary
macro illumination from upper left, readable texture and soft depth, no blur,
repetitive noise or glossy render. Landscape 3:2. The simulation draws the tunnels.

**Ant:** Transparent dorsal worker-ant body sprite, exactly from above,
orthographic macro, head right and oval gaster left, body perfectly horizontal.
Connected head, elongated mesosoma, two small petiole nodes and segmented gaster;
black lateral compound eyes, mandibles, fine hairs, exoskeleton texture and glossy
chestnut chitin with upper-left highlights. Only the body, without legs or antennae,
which are animated separately. Single centered specimen, transparent padding,
genuine alpha, no detached parts, labels, shadow beneath, extra insects, cartoon
or vector treatment. Photographic entomology appearance and slender adult worker
proportions.

## Pale sand revision

`wake/assets/backgrounds/ant-sand-v2.png` was generated with the built-in image
tool. The original soil asset is retained for compatibility. Final prompt:

> Straight-on orthographic macro cross-section of pale warm ivory/beige fine dry
> quartz sand behind invisible clean glass. Uniformly packed unexcavated fine
> light sand, subtle tiny grains and restrained mineral variation, flat diffuse
> lighting. Low-contrast pale backdrop for dark reddish ants. No roots, clumps,
> large rocks, strata, dark patches, plants, sky, ants, holes, tunnels, text,
> borders, shadows or vignette. The application draws tunnels and ants on top.

## Drawn ground and bounded rendering

The active farm does not load either photographic ground image. Its cream depth
gradient now carries seeded vector grains. The earlier soil, sand and ant body
assets remain provenance for retired treatments.
See [rendering limits](ant-farm.md#implementation-and-boundaries).


## Window and glass treatment

The active room uses generated photographic day and night backdrops,
`backgrounds/ant-room-day-v1.webp` and `backgrounds/ant-room-night-v1.webp`.
They show an empty walnut desk with visible grain, a painted window frame,
a garden and distant hills. Matching geometry permits a stationary local-time
crossfade. They contain no sun/moon disk, case or ants; the application draws
exactly one celestial object and the independent live habitat over them.
The case and canvas above the soil remain transparent with restrained glass-edge
highlights. The procedural anatomical body and articulated legs are the
active ant artwork. These assets ship with Pages; viewing needs no image service.

The day image was generated using the built-in image tool as a front-facing,
photorealistic empty desk and window, with wood grain, fine frame texture, soft
clouds and realistic garden foliage; no text, people, ant farm or celestial disk.
The night edit retained the same framing and material geometry, with a dark blue
sky and warm off-frame interior lighting. Both were encoded as WebP at quality
88 for the static site. Earlier CSS landscape layers remain inert compatibility
markup; they do not add a second horizon, window frame, sun or moon.

## Macro renderer

The active renderer now uses procedural anatomy from `ant-drawing.js`, including
articulated legs and antennae. The earlier body PNG is retained as artwork
provenance and is not loaded by this renderer. Likewise, the ground now uses
seeded vector grains, restrained strata and shaded chambers, rather than the
retired flat colour-only treatment or photographic soil. Day/night room WebP
assets remain active. The vector details redraw at habitat magnification without
a larger full-world raster or an image-service dependency.
