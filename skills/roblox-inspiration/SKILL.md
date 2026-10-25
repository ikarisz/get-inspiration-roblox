---
name: roblox-inspiration
description: >-
  Use captured game UI references and auto-generated Super Prompts to implement inspired
  Roblox games, systems, or UI components clean-room in Roblox Studio using roblox-game and roblox-studs-ui.
---

# Roblox Inspiration & Reference Skill

This skill allows Antigravity to ingest screenshots and extracted OCR UI metadata gathered by
`get-inspiration-roblox` and turn them into production-ready Roblox games.

## Chaining with Game Creation Skills

When a user provides a `CLONE_SUPER_PROMPT.md` or a folder of captured reference images:

1. **Visual Reference Inspection**:
   - For each screen in the table, open and view the reference image link (e.g. `[ref_01.png](file:///...)`).
   - Extract the exact visual layout: button placement, aspect ratios, background textures, and color codes.

2. **UI Construction with `roblox-studs-ui`**:
   - For each modal and HUD screen, follow the **Layer Stack**:
     `Aura/Shadow` -> `Outer Rim (UIStroke)` -> `Base Plate (Frame + UICorner)` -> `Header Inset` -> `Content Grid/List` -> `Buttons`.
   - Use the dominant hex colors specified in the prompt.
   - Execute procedural UI scripts in Studio via MCP `execute_luau`.

3. **Game Systems & Architecture with `roblox-game`**:
   - Reference `templates/game-scaffold.md` and the detected genre template (`genre-simulator.md`, `genre-tycoon.md`, etc.).
   - Implement `ServerScriptService.DataManager` using `ProfileService` with session locking.
   - Wire all `ReplicatedStorage.Remotes` listed in the contract table with strict server-side validation.
