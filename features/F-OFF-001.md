---
id: F-OFF-001
level: 2
title: Encrypted offline app
priority: should
status: proposed
links:
  refines: [G-007]
  conflicts_with:
    - id: F-SEC-001
      note: 'F-SEC-001 applies to the web client. The app stores data only encrypted, with a key in the OS keystore and a time-limited offline lease.'
---

# F-OFF-001 Encrypted offline app

## Statement

A native app stores the member's sheets and markings encrypted on the device, works without network, and synchronises when online.

## Rationale

Venues without reliable network; see G-007.
