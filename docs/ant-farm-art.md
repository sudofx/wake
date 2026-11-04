# Ant farm artwork

The built-in image-generation tool produced the synthetic body texture and
room backdrops. The simulation draws the habitat soil and tunnel contours.

## Body texture

`backgrounds/ant-body-v1.png` supplies the chitin texture used by the macro
renderer. The original prompt specified the following:

**Ant:** Transparent dorsal worker-ant body sprite, exactly from above,
orthographic macro, head right and oval gaster left, body perfectly horizontal.
Connected head, elongated mesosoma, two small petiole nodes and segmented gaster;
black lateral compound eyes, mandibles, fine hairs, exoskeleton texture and glossy
chestnut chitin with upper-left highlights. Only the body, without legs or antennae,
which are animated separately. Single centered specimen, transparent padding,
genuine alpha, no detached parts, labels, shadow beneath, extra insects, cartoon
or vector treatment. Photographic entomology appearance and slender adult worker
proportions.

## Drawn ground

The farm uses a procedural, repeating grain tile and shaded tunnel contours.
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

The active renderer combines procedural anatomy from `ant-drawing.js` with
chitin texture from the body PNG. Separate head, thorax and gaster
patches are clipped into live anatomical shapes from one 1024×512 atlas; legs,
antennae, mandibles and carrying poses remain articulated. A failed image load
keeps the procedural body available. The ground combines a repeating grain tile,
restrained strata and shaded chambers. Molded green rails and a clear glass edge
follow the physical-farm references. The vector details redraw at habitat
magnification within the canvas pixel budget.
