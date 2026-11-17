---
id: F-READ-003
level: 2
title: System view for small screens
priority: should
status: implemented
links:
  refines: [G-004]
  depends_on: [F-READ-001]
---

# F-READ-003 System view for small screens

## Statement

Besides whole pages, members can read their parts as a sequence of whole music systems: as many systems as fit at a chosen minimum staff size, cropped to the width of the music and continuing across page boundaries, so the notes stay readable on a small tablet. The server finds the systems of every uploaded file automatically; pages it is unsure about are shown whole, and librarians can correct the detection.

## Rationale

A full A4 page on an 8" tablet shrinks the staves to 2–4 mm. Showing only whole systems at the width of the music makes them 2–2.7 times larger (measured in the prototype, `docs/agents/background.md` §6.1), without cutting any system, and the end of one page and the start of the next can be on the screen together.

## Notes

The overlap rule and the staff sizes were decided by the user after the prototype. Splitting a system that is too wide into halves at a barline is a separate, later proposal (R-READ-017).
