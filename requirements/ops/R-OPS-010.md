---
id: R-OPS-010
level: 3
title: Update by replacing the container image
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-028, R-OPS-004]
  constrains: [R-OPS-003]
  decided_in: [tech:d-update-model]
---

# R-OPS-010 Update by replacing the container image

## Statement

When the administrator replaces the container image of a Docker Compose installation with a newer release (`docker compose pull` followed by `docker compose up -d`), the system shall start on the new release with all data and settings, without any further step.

## Acceptance criteria

- The Compose file of the release refers to a published image with a version tag (no local build needed).
- After `docker compose pull && docker compose up -d` on an installation of an older release, `GET /api/version` reports the new version and the container becomes healthy.
- Every user can log in with the same password, and sees the same pieces, parts, programmes and markings as before the update.
- No command other than the two above is needed, and the user guide's update section lists no other step.

## Notes

The plain program is updated the same way: stop it, replace the program file, start it (R-OPS-026). Today `compose.yaml` builds the image locally (`build: .`, `musicus:latest`); publishing images is R-OPS-028.
