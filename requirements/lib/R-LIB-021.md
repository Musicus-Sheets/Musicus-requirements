---
id: R-LIB-021
level: 3
title: Commit and undo of an import
priority: should
status: accepted
links:
  refines: [F-LIB-004]
  depends_on: [R-LIB-019, R-LIB-001, R-LIB-002, R-FILE-002, R-FILE-004, R-PERF-006]
---

# R-LIB-021 Commit and undo of an import

## Statement

The librarian shall commit reviewed pieces one at a time or all green pieces at once. Each piece shall be created (or its parts added to the confirmed existing piece) in one short write transaction, with the same rules as pieces and parts entered by hand. Committed parts become visible to members by the normal read rule (R-ACL-001). The librarian shall be able to undo a batch: its created pieces and parts are removed, unless annotations exist on them or other parts were added to its pieces since, in which case nothing is removed and the affected pieces are named. Uploaded files stay in the file store (R-FILE-004).

## Acceptance criteria

- After committing, a member of a group granted the part's instrument sees the part; before, he does not.
- Undo of a batch whose parts carry no annotations removes the pieces and parts it created and keeps pieces it only added parts to.
- Undo is refused (HTTP 409) when a member has annotated one of the imported parts.
