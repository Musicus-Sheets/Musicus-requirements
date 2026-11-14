---
id: R-TECH-002
level: 3
title: Client technology
priority: must
status: implemented
links:
  refines: [F-TECH-001]
  implemented_by: [crates/musicus-web]
  decided_in: [tech:d-pdf-rendering]
---

# R-TECH-002 Client technology

## Statement

The web client shall be written in Rust with Dioxus and compiled to WebAssembly; JavaScript is limited to one bridge module for browser features without Rust equivalent.

## Acceptance criteria

- All JavaScript of the client lives in crates/musicus-web/js/.
