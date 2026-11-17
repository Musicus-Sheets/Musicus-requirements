---
id: R-READ-014
level: 3
title: View setting per user
priority: should
status: verified
links:
  refines: [F-READ-003]
  depends_on: [R-SEC-001]
  verified_by:
    - crates/musicus-server/tests/api.rs::system_layouts_are_detected_in_the_background_and_follow_file_access
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-server/src/routes/auth.rs
    - crates/musicus-web/src/pages/viewer.rs
---

# R-READ-014 View setting per user

## Statement

The reader shall offer a switch between page view and system view and, in the system view, the staff sizes S, M, L and XL (minimum staff height 5, 6, 7 and 8 mm on the screen); the choice shall be stored per user on the server, not on the device.

## Acceptance criteria

- The setting is part of `GET /api/auth/me` and changed with `PUT /api/auth/reader-settings`; another device of the same user starts in the same view.
- Default: page view, size M.

## Notes

Millimetres are physical only for a screen with 132 CSS pixels per inch (iPad; most 8–11" Android tablets have 120–160); browsers do not report the real density.
