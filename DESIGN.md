---
version: alpha
name: WAKE reader and digital colony
description: Evidence readers and an optional field-note experiment beside a simulated habitat.
colors:
  primary: "#d8ddba"
  field-background: "#171b16"
  field-text: "#f3eedf"
  field-muted: "#bdc6b6"
  field-action: "#d8ddba"
  field-focus: "#edc77b"
typography:
  body:
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
  experiment-title:
    fontFamily: "Georgia, serif"
  measurements:
    fontFamily: "ui-monospace, monospace"
omitted:
  - section: spacing
    reason: Existing page owners define geometry; no new global spacing scale.
  - section: rounded
    reason: Existing page owners define shapes; no global radius migration.
---

# WAKE presentation context

## Overview

The reader explains recorded work. The digital colony invites observation. The
optional experiment is a small field notebook beside that colony, usable by a
curious teenager on a phone. It must reach a natural ending without requiring an
account, personal data, another activity or a return visit. Feature completion
does not establish improved human reasoning.

## Colors

Existing runtime CSS remains canonical (ownership model B). `wake/assets/theme.css`
owns reader themes. `ant-farm.css` owns the immersive colony's established dark
palette and native controls. `ant-experiment.css` maps that palette to scoped
`--field-paper`, `--field-ink`, `--field-muted`, `--field-accent` and
`--field-focus` variables. The frontmatter mirrors these roles; it does not
generate a second theme. Keep experiment results understandable without color.

## Typography

Use the existing system sans for instructions and controls. A restrained Georgia
title marks the optional field-note page; monospaced counts distinguish actual
measurements. Keep meaningful limitations readable, not hidden in tiny footnotes.

## Layout

The farm retains its full-height habitat. The experiment is a separate, naturally
scrolling document, bounded at 740px with 18px phone margins. Its signature is the
visitor's frozen prediction immediately above the measured comparison. Native
radio buttons, progress and a two-row table carry the interaction. No dashboard
shell, overlay or decorative chart is needed.

## Elevation & Depth

Keep the existing habitat layers. The experiment uses plain dividers and document
flow, with no new floating panels or fixed navigation.

## Shapes

Inherit the farm's native pill actions. Use ordinary table rows and an understated
left rule for the optional outside observation. Do not rebrand the reader.

## Components

The experiment's native radio group owns prediction selection; platform keyboard
behavior is intentional. Its form locks the seed and choice during execution.
The page-local status region carries progress/failure/completion. Stop cancels
remaining work, a completed result stays inspectable, and leaving ends the task.
The farm's Observe panel remains a nonmodal drawer and links to the experiment.
`ant-experiment.css` owns visible document scrollbars with forced-color fallback.
No shared CRUD, notification service, account, or locale framework is introduced.

## Do's and Don'ts

- Explain a result through visible counts and its frozen method.
- Preserve keyboard access, touch targets, reflow and a clear return link.
- Label simulation, fixture, model interpretation and human-study evidence distinctly.
- Never present a completion click as proof of learning or an invitation to surveillance.
- Preserve personal colonies and native authority; this instrument owns only temporary copies.
