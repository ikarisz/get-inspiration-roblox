# get-inspiration-roblox

> **Automated Roblox UI reference capture & clean-room implementation prompt synthesizer.**
> Capture game UI inspiration hands-free while playing in Roblox Player, extract OCR metadata, and auto-generate an exhaustive **"Super Prompt"** for AI coding agents (Antigravity, Claude, ChatGPT) to build the game in Roblox Studio.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

---

## Why get-inspiration-roblox?

When designing a new Roblox game inspired by existing titles, developers usually have to:
1. Play the game and manually press PrintScreen dozens of times.
2. Crop and organize images into folders.
3. Manually write lengthy prompt descriptions explaining each menu, button, and currency system to AI.

**`get-inspiration-roblox` automates this entire pipeline:**
- **Zero-touch capture**: Automatically detects when a new UI modal / popup opens on screen and snaps a clean screenshot.
- **Hotkeys**: Press `[F9]` anytime you see a cool menu or HUD design; press `[F10]` when done.
- **Built-in OCR & Color Palette extraction**: Reads all button titles, prices, upgrades, and dominant hex colors.
- **Super Prompt Synthesis**: Generates an exhaustive GDD and Implementation Specification ready for AI agents.
- **Safe & Non-Invasive**: Operates purely at the OS desktop level. Does **not** modify game memory, inject DLLs, or interact with Roblox networking.

---

## Architecture

```
get-inspiration-roblox/
├── start_capture.bat          # 1-Click launcher for Windows
├── main.py                    # CLI entrypoint & recorder controller
├── requirements.txt           # Lightweight dependencies (mss, Pillow, easyocr)
├── src/
│   ├── window_capture.py      # Auto-locates Roblox Player & captures high-res frames
│   ├── ui_detector.py         # Visual frame-diff engine to detect modal openings
│   ├── ocr_engine.py          # Optical Character Recognition & color palette extraction
│   └── prompt_synthesizer.py  # Generates the Master Clone / GDD Super Prompt
└── skills/                    # Antigravity Skill integration
    └── roblox-inspiration/
        └── SKILL.md
```

---

## Quick Start

### 1. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/ikarisz/get-inspiration-roblox.git
cd get-inspiration-roblox
pip install -r requirements.txt
```

### 2. Run the Recorder

1. Open your target game in **Roblox Player**.
2. Run the recorder (or double-click `start_capture.bat`):

```bash
python main.py
```

### 3. Controls While Playing

- **Auto-Capture**: Enabled by default. Whenever you open a Shop, Inventory, Rebirth, or Quest menu, the tool detects the visual change and snaps the frame automatically.
- **`[F9]`**: Manually snap the current screen at any time.
- **`[F10]`**: Finish recording and automatically generate the **Super Prompt**.

---

## Output

After pressing `[F10]`, the tool produces:
1. **`references/captured_ui/<GameName>_<Timestamp>/`**: All cropped reference screenshots.
2. **`CLONE_SUPER_PROMPT.md`**: An exhaustive Markdown implementation specification containing:
   - Screen breakdown with dominant colors and button labels
   - Inferred Core Gameplay Loop
   - UI/UX layout hierarchy for `StarterGui`
   - Server-authoritative `RemoteEvent` contracts
   - Step-by-step implementation plan for AI coding agents

---

## Using with Antigravity

Pass the generated `CLONE_SUPER_PROMPT.md` directly to Antigravity along with the `roblox-game` skill:

> *"Build a complete Roblox game in Roblox Studio based on the specification in `CLONE_SUPER_PROMPT.md`."*

The agent will read the layout, colors, and game mechanics to construct the game directly in Roblox Studio!

---

## License

This project is licensed under the [MIT License](LICENSE).
