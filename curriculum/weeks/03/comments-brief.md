# Week 3: Local Comments Reference Brief

This is the fixed assignment specification. No commercial-product access is needed.

## User Story
As someone reviewing a drawing, I can leave a note at a canvas location and return to read it after reloading that drawing.

## Core Interaction
1. Choose an explicit **Add comment** action (a toolbar button or context-menu item).
2. Click a canvas location, enter non-empty text, and save. Cancel creates nothing.
3. A clearly distinguishable pin marks the saved scene location.
4. Select the pin to open a text panel. Closing the panel leaves the pin in place.
5. Pan and zoom: the pin follows the scene location, not a fixed screen pixel.
6. Reload the same drawing: the pin and text return. Open a different drawing: the note does not appear there.

One comment is enough for the core assignment. If replacing an existing comment is supported, ask for confirmation or provide an explicit edit action. Use keyboard-accessible controls with labels and visible focus; do not block ordinary drawing interactions outside comment mode.

## Data and Architecture
Store text and scene coordinates in comment state separate from drawing elements. Explain how drawing identity is assigned and how local storage is keyed to it. Define behavior when no saved drawing identity exists. Render comment text as text. Reject empty or whitespace-only input and handle missing or malformed stored data without crashing the drawing.

## Acceptance Evidence
- Automated checks: scene/screen coordinate round trip at non-default pan and zoom; persistence round trip; isolation between drawing IDs; malformed stored data.
- Manual checks: create, cancel, select, close, pan, zoom, reload, switch drawings, and continue drawing normally.
- Record baseline and final relevant upstream test results. Separate pre-existing failures from regressions introduced by the change.

## Extensions
Replies, reactions, resolved threads, multiple comments, element anchoring, and export/import are optional. Local persistence is the core contract; collaboration and remote synchronization are out of scope.
