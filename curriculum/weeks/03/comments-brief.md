# Excalidraw Comments Track: Reference Brief

This brief supports [Week 3 homework](homework.md). It replaces the earlier one-comment exercise with a substantial review workflow. No commercial-product access is required.

## User Story
A reviewer selects elements in a drawing, leaves a comment, and returns to the thread later without losing the relationship to those elements.

## Core Acceptance Criteria
1. Select one or more drawing elements, choose an explicit comment action, enter non-empty text, and save. Cancel creates nothing.
2. Display an identifiable thread pin and a panel containing its text. Selecting a thread reveals/highlights the associated elements; selecting the pin opens that thread.
3. Add a reply, resolve a thread, and reopen it from a resolved-thread view.
4. Keep the pin associated with the selection during pan/zoom and element movement. Define a deterministic anchor rule for multi-element selections.
5. Define deletion behavior: for example, retain an orphaned thread with a clear label rather than silently attaching it to an unrelated element.
6. Reload the drawing and recover its comments. Switching drawings must not mix comment state.

## Architectural Decisions to Defend
Inspect the project's current patterns before choosing state ownership, storage, and rendering. Explain whether comments belong in drawing elements or separate state; do not assume a universal answer. Define drawing identity, element references, serialization, and behavior when referenced elements disappear. Render user text as text, reject blank input, and recover from malformed stored data without crashing the drawing.

## Validation Evidence
Automated checks for comment association, replies and resolution state, persistence isolation, and missing-element handling. Test coordinate conversion where your implementation introduces it. Manual demo: select elements, comment, reply, pan, zoom, move elements, resolve/reopen, reload, and switch drawings. Confirm normal selection/drawing behavior still works.

## Extensions
Reactions, keyboard shortcuts, search, and import/export. Remote collaboration is outside the required core. Explain limitations instead of implying local persistence is multi-user synchronization.
