# Sample Generated Super Prompt

This is an example of what `get-inspiration-roblox` outputs after capturing screenshots while playing.

```markdown
# MASTER CLONE IMPLEMENTATION SPECIFICATION (SUPER PROMPT)
<!-- Synthesized by get-inspiration-roblox | Ready for roblox-game & roblox-studs-ui skills -->

> **Reference Game:** Pet Clicking Mania
> **Detected Genre:** Simulator (Clicker / Pet Hatching / Progression)
> **Captured Reference Screens:** 4
> **Reference Folder (Absolute):** `file:///C:/Users/USER/Desktop/references/captured_ui/PetClickingMania_20261025_120000`

---
## 1. Visual Reference & Screen Mapping Table

| Screen | Visual Preview | Classification | Target Instance in Studio | Dominant Colors | Key Extracted Texts |
|---|:---:|---|---|---|---|
| `ref_01.png` | [ref_01.png](file:///C:/Users/USER/Desktop/references/captured_ui/PetClickingMania_20261025_120000/ref_01.png) | **Main HUD & Currency Bar** | `StarterGui.HUD_ScreenGui` | `#16213e` `#e94560` `#0f3460` | "Coins: 1,500", "Rebirths: 2", "Shop", "Pets" |
| `ref_02.png` | [ref_02.png](file:///C:/Users/USER/Desktop/references/captured_ui/PetClickingMania_20261025_120000/ref_02.png) | **Shop / Upgrade Modal** | `StarterGui.ShopGui.MainFrame` | `#1a1a2e` `#e94560` `#0f3460` | "UPGRADES", "Buy 1 (+5 Taps) - 100", "Buy Max", "Close [X]" |
| `ref_03.png` | [ref_03.png](file:///C:/Users/USER/Desktop/references/captured_ui/PetClickingMania_20261025_120000/ref_03.png) | **Pet Hatching & Gacha System** | `StarterGui.HatchGui.HatchModal` | `#0f3460` `#533483` `#e94560` | "Common 60%", "Rare 30%", "Legendary 9%", "Hatch 1", "Auto Hatch" |
| `ref_04.png` | [ref_04.png](file:///C:/Users/USER/Desktop/references/captured_ui/PetClickingMania_20261025_120000/ref_04.png) | **Rebirth & Progression Modal** | `StarterGui.RebirthGui.RebirthFrame` | `#16213e` `#e94560` `#0f3460` | "REBIRTH", "Cost: 1,000,000 Coins", "Reward: +100% Multiplier", "Rebirth Now" |

---
## 2. Screen-by-Screen UI Reconstruction Specifications

### Visual Reference: [ref_02.png](file:///C:/Users/USER/Desktop/references/captured_ui/PetClickingMania_20261025_120000/ref_02.png) — Shop / Upgrade Modal
- **Studio Placement:** `StarterGui.ShopGui.MainFrame`
- **Role:** Item purchasing grid with ScrollingFrame, price cards, and purchase CTA buttons.
- **Color Palette:** Primary BG: `#1a1a2e`, Accent: `#e94560`
- **OCR Detected Labels & Controls:**
  - `UPGRADES`
  - `Buy 1 (+5 Taps) - 100`
  - `Buy Max`
  - `Close [X]`

**UI Construction Layer Stack (Texture-First / Studs Style):**
1. **Container / Shadow:** Outer canvas frame with anchor `(0.5, 0.5)`, position `(0.5, 0, 0.5, 0)`, size scale `0.65, 0, 0.75, 0`.
2. **Outer Rim & Border:** `UIStroke` (Color: `#e94560`, Thickness: `2.5px`, ApplyStrokeMode: `Border`).
3. **Base Plate:** `Frame` (BackgroundColor3: `#1a1a2e`, `UICorner` CornerRadius: `10px`).
4. **Header Inset:** Top title bar with TextLabel containing modal title, font `FredokaOne`, TextColor3: `#ffffff`.
5. **Content Scrolling Frame:** `ScrollingFrame` with `UIGridLayout`, automatic canvas sizing.
6. **Action / Buy Buttons:** Contrasting buttons with rounded corners and scale-in hover effect.
7. **Close Button [X]:** Top-right corner AnchorPoint `(1, 0)`, Position `(1, -8, 0, 8)`, Size `(0, 32, 0, 32)`.

---
## 3. Server-Authoritative RemoteEvent Architecture
| Remote Name | Class | Direction | Validation & Anti-Cheat Rules |
|---|---|---|---|
| `RequestClickAction` | `RemoteEvent` | Client -> Server | Rate-limit debounce (0.1s); server computes multiplier and increments balance |
| `PurchaseItem` | `RemoteFunction` | Client -> Server | Server validates player balance, deducts cost, updates inventory |
| `TriggerRebirth` | `RemoteFunction` | Client -> Server | Validates cost threshold before resetting balance and incrementing Rebirths |

---
## 4. Procedural UI Generation Script for Roblox Studio MCP
Execute directly in Studio Edit Mode via `execute_luau`:
```luau
local StarterGui = game:GetService("StarterGui")
local hud = Instance.new("ScreenGui")
hud.Name = "HUD_ScreenGui"
hud.ResetOnSpawn = false
hud.Parent = StarterGui

local topBar = Instance.new("Frame")
topBar.Name = "TopCurrencyBar"
topBar.AnchorPoint = Vector2.new(0.5, 0)
topBar.Position = UDim2.new(0.5, 0, 0, 10)
topBar.Size = UDim2.new(0, 320, 0, 48)
topBar.BackgroundColor3 = Color3.fromHex("#16213e")
topBar.Parent = hud

local corner = Instance.new("UICorner")
corner.CornerRadius = UDim.new(0, 10)
corner.Parent = topBar
```
```
