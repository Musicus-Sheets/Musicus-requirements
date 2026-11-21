---
id: R-OPS-025
level: 3
title: No online check for new versions
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  constrains: [R-OPS-010]
---

# R-OPS-025 No online check for new versions

## Statement

The system shall never contact the internet to look for newer releases.

## Acceptance criteria

- The server program and the web client make no request to any host other than the Musicus server itself (certificate requests of the optional Caddy proxy are not made by Musicus).
- There is no setting that enables such a check.

## Notes

Administrators learn about releases from the project's release page or the user guide site. Keeps the server usable on networks without internet access and sends nothing about the ensemble anywhere.
