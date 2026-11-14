---
id: F-FILE-003
level: 2
title: MusicXML sheets
priority: could
status: proposed
links:
  refines: [G-007]
---

# F-FILE-003 MusicXML sheets

## Statement

Librarians can upload MusicXML files in addition to PDF; members can read them.

## Rationale

MusicXML allows reflowing and transposition and can produce all parts from one file.

## Notes

- Storage needs no change: the blob store is format-agnostic; add a processor that validates `.musicxml`/`.mxl` and extracts title, composer and part names.
- Rendering: MusicXML reflows with the screen width. Client options: OpenSheetMusicDisplay (TypeScript, BSD-3-Clause) or Verovio (C++ with an Emscripten JavaScript toolkit, LGPL-3.0).
- Annotations: page coordinates do not work on reflowing layouts. Objects need musical anchors (part, measure, beat, staff) with offsets in staff spaces, as a second annotation kind next to the page-based one.
- Pragmatic intermediate step: render MusicXML to PDF on upload (Verovio or the MuseScore CLI) and treat it like any PDF; the existing annotation model applies unchanged, but reflow and live transposition are lost.
- Benefit: one MusicXML score can produce every part, including transposed ones (e.g. Horn in F as E♭).
