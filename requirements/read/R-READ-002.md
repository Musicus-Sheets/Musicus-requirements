---
id: R-READ-002
level: 3
title: Turning pages
priority: must
status: verified
links:
  refines: [F-READ-001]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/src/pages/viewer.rs]
---

# R-READ-002 Turning pages

## Statement

In reading mode, the web client shall turn to the next page on a tap in the right third or on Arrow Right, Arrow Down, Page Down or Space, and to the previous page on a tap in the left third or on Arrow Left, Arrow Up or Page Up.

## Acceptance criteria

- Arrow Right shows '2 / 4'; Page Up returns to '1 / 4'.
- A Bluetooth foot pedal that sends Page Down turns the page.
