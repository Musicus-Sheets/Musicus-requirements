---
id: R-PROG-003
level: 3
title: Prefetch the sheets of an opened programme
priority: must
status: verified
links:
  refines: [F-PROG-002]
  depends_on: [R-PROG-002]
  conflicts_with:
    - id: R-SEC-001
      note: Sheets are kept in memory only; a reload downloads them again.
  verified_by: [e2e/smoke.mjs]
  implemented_by:
    - crates/musicus-web/src/pages/programmes.rs
    - crates/musicus-web/js/bridge.js
  decided_in: [tech:d-no-client-storage]
---

# R-PROG-003 Prefetch the sheets of an opened programme

## Statement

When a member opens a programme, the web client shall start downloading every readable sheet of it into memory, at most 3 at a time, and show the progress and any failed downloads.

## Acceptance criteria

- Opening a programme shows 'All N sheets ready' once the downloads finished.
- Opening a part of the programme afterwards renders it without a new file request.
