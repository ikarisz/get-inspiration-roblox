---
name: roblox-inspiration
description: >-
  Use captured game UI references and auto-generated Super Prompts to implement inspired
  Roblox games, systems, or UI components clean-room in Roblox Studio.
---

# Roblox Inspiration & Reference Skill

This skill allows Antigravity to ingest screenshots and extracted OCR UI metadata gathered by
`get-inspiration-roblox` and turn them into production-ready Roblox games.

## Workflow

1. **Ingest Prompt:** Read the generated `CLONE_SUPER_PROMPT.md` or `LATEST_GAME_CLONE_PROMPT.md`.
2. **Review UI Palette:** Extract colors and layout constraints from the reference breakdown.
3. **Execute Implementation:** Combine with `roblox-game` skill to scaffold `StarterGui`, RemoteEvents, and DataStores.
