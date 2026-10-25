#!/usr/bin/env python3
"""
get-inspiration-roblox
CLI & Desktop Assistant for capturing Roblox game references and synthesizing implementation prompts.
"""

import os
import sys
import time
import argparse
import ctypes
from datetime import datetime
import glob

from src.window_capture import WindowCapture
from src.ui_detector import calculate_image_diff
from src.ocr_engine import run_ocr_on_images
from src.prompt_synthesizer import build_super_prompt

VK_F9 = 0x78   # F9: Manual Capture
VK_F10 = 0x79  # F10: Finish & Synthesize

def is_key_pressed(vk_code):
    return (ctypes.windll.user32.GetAsyncKeyState(vk_code) & 0x0001) != 0

def record_session(game_name: str, auto_mode: bool, diff_threshold: float, out_dir: str):
    capturer = WindowCapture()
    hwnd = capturer.find_roblox_window()
    
    if hwnd:
        print(f"[+] Attached to Roblox Player window (HWND: {hwnd})")
    else:
        print("[*] Roblox Player window not detected; recording full desktop display.")

    print(f"[+] Output folder: {out_dir}")
    print("\n" + "=" * 60)
    print("  RECORDING ACTIVE:")
    print("  - [F9]  : Snap current screen / menu manually")
    print("  - [F10] : Finish recording and Generate Super Prompt")
    if auto_mode:
        print(f"  - Auto  : Enabled (snaps on UI diff > {diff_threshold})")
    print("=" * 60 + "\n")
    print("Play the game normally. Open Shop, Upgrades, Quests, or Rebirth menus...\n")

    captured_count = 0
    last_img = None
    last_capture_time = 0

    try:
        while True:
            current_hwnd = capturer.find_roblox_window()
            now = time.time()

            f9 = is_key_pressed(VK_F9)
            f10 = is_key_pressed(VK_F10)

            if f10:
                print("\n[+] Finish trigger [F10] detected!")
                break

            should_snap = False
            reason = ""

            if f9:
                should_snap = True
                reason = "Manual [F9]"
            elif auto_mode and (now - last_capture_time > 1.5):
                frame = capturer.capture_frame(current_hwnd)
                diff = calculate_image_diff(last_img, frame)
                if diff > diff_threshold:
                    should_snap = True
                    reason = f"Auto UI change detected (diff: {diff:.2f})"
                    img_to_save = frame

            if should_snap:
                if not auto_mode or f9:
                    img_to_save = capturer.capture_frame(current_hwnd)

                captured_count += 1
                filename = f"ref_{captured_count:02d}.png"
                filepath = os.path.join(out_dir, filename)
                img_to_save.save(filepath, "PNG")

                print(f"[{datetime.now().strftime('%H:%M:%S')}] Saved #{captured_count:02d}: {filename} ({reason})")
                last_img = img_to_save
                last_capture_time = now
                time.sleep(0.4)

            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\n[*] Stopped by user.")

    return captured_count

def process_analysis(out_dir: str, game_name: str):
    image_paths = sorted(glob.glob(os.path.join(out_dir, "*.png")))
    if not image_paths:
        print(f"[!] No screenshots found in {out_dir}")
        return

    print(f"\n[+] Running visual analysis & OCR on {len(image_paths)} images...")
    ocr_data = run_ocr_on_images(image_paths)

    print("[+] Synthesizing Master Clone Implementation Prompt...")
    super_prompt = build_super_prompt(game_name, out_dir, ocr_data)

    out_file = os.path.join(out_dir, "CLONE_SUPER_PROMPT.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(super_prompt)

    # Save root shortcut
    with open("LATEST_GAME_CLONE_PROMPT.md", "w", encoding="utf-8") as f:
        f.write(super_prompt)

    print("\n" + "=" * 65)
    print("  [SUCCESS] Super Prompt generated successfully!")
    print(f"  - Document: {out_file}")
    print("  - Quick Link: LATEST_GAME_CLONE_PROMPT.md")
    print("=" * 65)

def main():
    parser = argparse.ArgumentParser(description="Roblox UI Reference Recorder & Prompt Synthesizer")
    parser.add_argument("--name", type=str, default="", help="Name of the game being referenced")
    parser.add_argument("--auto", action="store_true", default=True, help="Enable automatic screenshot on UI change")
    parser.add_argument("--diff", type=float, default=0.12, help="Visual change threshold (0.05 to 0.30)")
    parser.add_argument("--analyze", type=str, default="", help="Analyze existing folder of screenshots instead of recording")

    args = parser.parse_args()

    if args.analyze:
        game_name = args.name or os.path.basename(args.analyze)
        process_analysis(args.analyze, game_name)
        return

    game_name = args.name
    if not game_name:
        try:
            game_name = input("Enter Game Name (or press Enter for 'RobloxGame'): ").strip()
        except EOFError:
            game_name = "RobloxGame"
        if not game_name:
            game_name = "RobloxGame"

    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = os.path.join("references", "captured_ui", f"{game_name}_{timestamp_str}")
    os.makedirs(out_dir, exist_ok=True)

    count = record_session(game_name, args.auto, args.diff, out_dir)
    if count > 0:
        process_analysis(out_dir, game_name)
    else:
        print("[!] No images captured during session.")

if __name__ == "__main__":
    main()
