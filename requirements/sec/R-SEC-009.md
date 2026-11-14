---
id: R-SEC-009
level: 3
title: Personal watermark
priority: could
status: proposed
links:
  refines: [F-SEC-002]
  conflicts_with:
    - id: R-FILE-004
      note: The personalised copy is generated on delivery and never stored as a blob; the original stays immutable and content-addressed.
---

# R-SEC-009 Personal watermark

## Statement

The system shall be able to add the name of the downloading member to the margin of every delivered sheet.

## Acceptance criteria

- A delivered PDF shows the member's name in the page margin; the stored original is unchanged.

## Notes

Copying cannot be prevented technically (anything on screen can be captured); a watermark is a deterrent. Conflicts with content addressing: a personalised file has its own hash, so it must be generated on delivery and must not replace the blob (R-FILE-004).
