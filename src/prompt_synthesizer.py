import os
from typing import Dict, Any, List

def classify_ui_screen(texts: List[str]) -> Dict[str, str]:
    """Classifies a screenshot into a semantic Roblox UI component based on OCR words."""
    corpus = " ".join([t.lower() for t in texts])
    
    if any(k in corpus for k in ["hatch", "egg", "pet", "rarity", "odds"]):
        return {
            "type": "Pet Hatching & Gacha System",
            "container": "StarterGui.HatchGui.HatchModal",
            "role": "Displays pet egg drop rates, auto-hatch toggles, and animated egg opening card."
        }
    elif any(k in corpus for k in ["shop", "buy", "purchase", "store", "product"]):
        return {
            "type": "Shop / Upgrade Modal",
            "container": "StarterGui.ShopGui.MainFrame",
            "role": "Item purchasing grid with ScrollingFrame, price cards, and purchase CTA buttons."
        }
    elif any(k in corpus for k in ["rebirth", "prestige", "rank up", "tier"]):
        return {
            "type": "Rebirth & Progression Modal",
            "container": "StarterGui.RebirthGui.RebirthFrame",
            "role": "Shows current milestone, next rebirth cost requirement, and multiplier rewards."
        }
    elif any(k in corpus for k in ["inventory", "backpack", "storage", "equip", "delete"]):
        return {
            "type": "Inventory / Storage Modal",
            "container": "StarterGui.InventoryGui.InventoryFrame",
            "role": "Grid layout showing player items, equip best button, and item stat tooltips."
        }
    elif any(k in corpus for k in ["quest", "task", "mission", "reward", "claim"]):
        return {
            "type": "Quests & Achievements Screen",
            "container": "StarterGui.QuestGui.QuestFrame",
            "role": "List of active tasks, progress bars, and reward claim buttons."
        }
    elif any(k in corpus for k in ["setting", "music", "sfx", "code", "redeem", "mute"]):
        return {
            "type": "Settings & Promo Code Modal",
            "container": "StarterGui.SettingsGui.SettingsFrame",
            "role": "Toggles for audio, particle quality, and a text input field for promo codes."
        }
    elif any(k in corpus for k in ["coins", "gems", "cash", "level", "strength", "leaderstats"]):
        return {
            "type": "Main HUD & Currency Bar",
            "container": "StarterGui.HUD_ScreenGui",
            "role": "Always-visible top status bar displaying player currencies, level, and sidebar action buttons."
        }
    return {
        "type": "Gameplay Screen / Dialogue",
        "container": "StarterGui.GeneralGui.Frame",
        "role": "Gameplay interface or notification popup."
    }

def infer_game_genre(detected_words: set) -> str:
    corpus = " ".join([w.lower() for w in detected_words])
    
    if any(k in corpus for k in ["pet", "egg", "rebirth", "click", "multiplier", "hatch", "coins", "strength", "tap"]):
        return "Simulator (Clicker / Pet Hatching / Progression)"
    elif any(k in corpus for k in ["dropper", "collector", "conveyor", "tycoon", "factory", "deposit"]):
        return "Tycoon (Base Building & Automated Economy)"
    elif any(k in corpus for k in ["stage", "checkpoint", "timer", "obby", "jump", "speedrun"]):
        return "Obby (Obstacle Course)"
    elif any(k in corpus for k in ["quest", "inventory", "level", "xp", "sword", "stats", "dungeon"]):
        return "RPG / Adventure (Combat & Leveling)"
    elif any(k in corpus for k in ["monster", "door", "dark", "survive", "escape", "jumpscare"]):
        return "Horror (Survival & Escape)"
    elif any(k in corpus for k in ["storm", "loot", "elimination", "royale", "arena", "pvp"]):
        return "Battle Royale / PvP Arena"
    return "Custom Roblox Experience"

def build_super_prompt(game_title: str, target_dir: str, ocr_data: Dict[str, Any]) -> str:
    all_words = set()
    for item in ocr_data.values():
        for t in item.get("texts", []):
            all_words.add(t)

    genre = infer_game_genre(all_words)
    abs_dir = os.path.abspath(target_dir).replace("\\", "/")

    lines = []
    lines.append(f"# MASTER CLONE IMPLEMENTATION SPECIFICATION (SUPER PROMPT)")
    lines.append(f"<!-- Synthesized by get-inspiration-roblox | Ready for roblox-game & roblox-studs-ui skills -->\n")
    lines.append(f"> **Reference Game:** {game_title}")
    lines.append(f"> **Detected Genre:** {genre}")
    lines.append(f"> **Captured Reference Screens:** {len(ocr_data)}")
    lines.append(f"> **Reference Folder (Absolute):** `file:///{abs_dir}`\n")
    
    lines.append("> [!IMPORTANT]")
    lines.append("> **Instructions for AI Coding Agent:**")
    lines.append("> You are building a clean-room Roblox game inspired by the reference screens captured below.")
    lines.append("> Use the **`roblox-game`** skill for system architecture & networking, and the **`roblox-studs-ui`** design system for UI construction.")
    lines.append("> Inspect each linked reference image carefully to match its layout, color palette, button styling, and screen hierarchy.\n")

    lines.append("---")
    lines.append("## 1. Visual Reference & Screen Mapping Table\n")
    lines.append("Inspect each image before building its corresponding `StarterGui` element:\n")
    lines.append("| Screen | Visual Preview | Classification | Target Instance in Studio | Dominant Colors | Key Extracted Texts |")
    lines.append("|---|:---:|---|---|---|---|")

    for filename, info in sorted(ocr_data.items()):
        img_rel_path = f"{abs_dir}/{filename}"
        classification = classify_ui_screen(info.get("texts", []))
        colors = " ".join([f"`{c}`" for c in info.get("colors", [])[:3]])
        sample_texts = ", ".join([f'"{t}"' for t in info.get("texts", [])[:4]]) or "*HUD / 3D Scene*"
        
        lines.append(
            f"| `{filename}` | [{filename}](file:///{img_rel_path}) | **{classification['type']}** | `{classification['container']}` | {colors} | {sample_texts} |"
        )

    lines.append("\n---")
    lines.append("## 2. Screen-by-Screen UI Reconstruction Specifications\n")

    for filename, info in sorted(ocr_data.items()):
        img_rel_path = f"{abs_dir}/{filename}"
        classification = classify_ui_screen(info.get("texts", []))
        palette = info.get("colors", ["#1b2838", "#ffffff"])
        primary_bg = palette[0] if palette else "#1b2838"
        accent_color = palette[1] if len(palette) > 1 else "#ffaa00"

        lines.append(f"### Visual Reference: [{filename}](file:///{img_rel_path}) — {classification['type']}")
        lines.append(f"- **Studio Placement:** `{classification['container']}`")
        lines.append(f"- **Role:** {classification['role']}")
        lines.append(f"- **Color Palette:** Primary BG: `{primary_bg}`, Accent: `{accent_color}`")
        
        texts = info.get("texts", [])
        if texts:
            lines.append("- **OCR Detected Labels & Controls:**")
            for t in texts[:10]:
                lines.append(f"  - `{t}`")
                
        lines.append("\n**UI Construction Layer Stack (Texture-First / Studs Style):**")
        lines.append(f"1. **Container / Shadow:** Outer canvas frame with anchor `(0.5, 0.5)`, position `(0.5, 0, 0.5, 0)`, size scale (e.g. `{0.65}, 0, {0.75}, 0`).")
        lines.append(f"2. **Outer Rim & Border:** `UIStroke` (Color: `{accent_color}`, Thickness: `2.5px`, ApplyStrokeMode: `Border`).")
        lines.append(f"3. **Base Plate:** `Frame` (BackgroundColor3: `{primary_bg}`, `UICorner` CornerRadius: `10px`).")
        lines.append(f"4. **Header Inset:** Top title bar with TextLabel containing modal title, font `FredokaOne` or `GothamBold`, TextColor3: `#ffffff`.")
        lines.append(f"5. **Content Scrolling Frame:** `ScrollingFrame` with `UIGridLayout` or `UIListLayout` (CellSize: `UDim2.new(0.28, 0, 0.35, 0)`), automatic canvas sizing.")
        lines.append(f"6. **Action / Buy Buttons:** Contrasting buttons with rounded corners and scale-in hover effect.")
        lines.append(f"7. **Close Button [X]:** Top-right corner AnchorPoint `(1, 0)`, Position `(1, -8, 0, 8)`, Size `(0, 32, 0, 32)`.\n")

    lines.append("---")
    lines.append("## 3. Reverse-Engineered Game Loop & Mechanics\n")
    lines.append(f"**Identified Genre:** {genre}\n")
    lines.append("### Core Mechanics:")
    lines.append("1. **First-Time User Experience (FTUE):**")
    lines.append("   - Spawns player at designated hub with default starting stats (e.g. Coins = 0, Gems = 0, Multiplier = 1).")
    lines.append("   - Loads `HUD_ScreenGui` with Top Currency Bar and sidebar action icons.")
    lines.append("2. **Active Progression Loop:**")
    lines.append("   - Player actions increment primary currency with floating pop-up text.")
    lines.append("   - Purchasing items/upgrades validates balance on server and grants persistent ownership.")
    lines.append("3. **Prestige / Rebirth Mechanic:**")
    lines.append("   - Reaching threshold allows Rebirth, resetting basic currency in exchange for permanent global multipliers.\n")

    lines.append("---")
    lines.append("## 4. Server-Authoritative RemoteEvent Architecture\n")
    lines.append("Place all definitions in `ReplicatedStorage.Remotes`:\n")
    lines.append("| Remote Name | Class | Direction | Validation & Anti-Cheat Rules |")
    lines.append("|---|---|---|---|")
    lines.append("| `RequestClickAction` | `RemoteEvent` | Client -> Server | Rate-limit debounce (0.1s); server computes multiplier and increments balance |")
    lines.append("| `PurchaseItem` | `RemoteFunction` | Client -> Server | Server validates player balance, deducts cost, updates inventory |")
    lines.append("| `TriggerRebirth` | `RemoteFunction` | Client -> Server | Validates cost threshold before resetting balance and incrementing Rebirths |")
    lines.append("| `EquipItem` | `RemoteEvent` | Client -> Server | Validates player actually owns the item in DataStore profile |")
    lines.append("| `RedeemPromoCode` | `RemoteFunction` | Client -> Server | Validates code string against active code table; verifies one-time use |")

    lines.append("\n---")
    lines.append("## 5. DataStore Schema (`ProfileService` Template)\n")
    lines.append("Implement in `ServerScriptService.DataManager`:\n")
    lines.append("```luau")
    lines.append("local ProfileTemplate = {")
    lines.append("    Coins = 0,")
    lines.append("    Gems = 0,")
    lines.append("    Rebirths = 0,")
    lines.append("    Inventory = {},")
    lines.append("    Equipped = {},")
    lines.append("    ClaimedCodes = {},")
    lines.append("    Settings = { Music = true, SFX = true },")
    lines.append("    UnlockedZones = { 1 }")
    lines.append("}")
    lines.append("```\n")

    lines.append("---")
    lines.append("## 6. Procedural UI Generation Script for Roblox Studio MCP\n")
    lines.append("You can execute this Luau script directly via `execute_luau` in Studio Edit Mode to generate the initial UI foundation:\n")
    lines.append("```luau")
    lines.append("-- Run via execute_luau in Studio Edit Mode")
    lines.append("local StarterGui = game:GetService(\"StarterGui\")")
    lines.append("local ChangeHistoryService = game:GetService(\"ChangeHistoryService\")")
    lines.append("ChangeHistoryService:SetWaypoint(\"Before Creating Inspired UI\")\n")
    lines.append("local hud = Instance.new(\"ScreenGui\")")
    lines.append("hud.Name = \"HUD_ScreenGui\"")
    lines.append("hud.ResetOnSpawn = false")
    lines.append("hud.Parent = StarterGui\n")
    lines.append("-- Top Currency Bar")
    lines.append("local topBar = Instance.new(\"Frame\")")
    lines.append("topBar.Name = \"TopCurrencyBar\"")
    lines.append("topBar.AnchorPoint = Vector2.new(0.5, 0)")
    lines.append("topBar.Position = UDim2.new(0.5, 0, 0, 10)")
    lines.append("topBar.Size = UDim2.new(0, 320, 0, 48)")
    lines.append("topBar.BackgroundColor3 = Color3.fromHex(\"#16213e\")")
    lines.append("topBar.Parent = hud\n")
    lines.append("local corner = Instance.new(\"UICorner\")")
    lines.append("corner.CornerRadius = UDim.new(0, 10)")
    lines.append("corner.Parent = topBar\n")
    lines.append("local stroke = Instance.new(\"UIStroke\")")
    lines.append("stroke.Color = Color3.fromHex(\"#e94560\")")
    lines.append("stroke.Thickness = 2")
    lines.append("stroke.Parent = topBar\n")
    lines.append("local coinLabel = Instance.new(\"TextLabel\")")
    lines.append("coinLabel.Name = \"CoinsLabel\"")
    lines.append("coinLabel.Size = UDim2.new(1, 0, 1, 0)")
    lines.append("coinLabel.BackgroundTransparency = 1")
    lines.append("coinLabel.Text = \"Coins: 0\"")
    lines.append("coinLabel.TextColor3 = Color3.fromRGB(255, 255, 255)")
    lines.append("coinLabel.TextSize = 20")
    lines.append("coinLabel.Font = Enum.Font.FredokaOne")
    lines.append("coinLabel.Parent = topBar\n")
    lines.append("print(\"[Inspiration Generator] Base HUD created successfully in StarterGui.\")")
    lines.append("```\n")

    lines.append("---")
    lines.append("## 7. Execution Checklist for Coding Agent\n")
    lines.append("- [ ] **Step 1:** Read each reference image and verify layout and colors.")
    lines.append("- [ ] **Step 2:** Scaffold `ReplicatedStorage.Remotes` with all RemoteEvents.")
    lines.append("- [ ] **Step 3:** Implement `ServerScriptService.DataManager` using ProfileService with `:BindToClose()`.")
    lines.append("- [ ] **Step 4:** Build `StarterGui` ScreenGuis matching the screen breakdown table.")
    lines.append("- [ ] **Step 5:** Wire client controllers in `StarterPlayerScripts` to trigger remotes and animations.")
    lines.append("- [ ] **Step 6:** Launch Studio Play Mode via MCP and verify all buttons open their intended modals.")

    return "\n".join(lines)
