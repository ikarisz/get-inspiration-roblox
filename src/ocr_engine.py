import os
from PIL import Image

def extract_dominant_colors(image_path: str, num_colors: int = 4) -> list:
    """Extracts dominant hex color codes from a screenshot."""
    try:
        img = Image.open(image_path).resize((100, 100))
        result = img.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
        result.putalpha(0)
        colors = result.getcolors(10000)
        if not colors:
            return ["#1b2838", "#ffffff"]
        top_colors = sorted(colors, key=lambda c: c[0], reverse=True)[:num_colors]
        palette = img.getpalette()
        color_hexes = []
        for count, index in top_colors:
            color = palette[index*3:index*3+3]
            color_hexes.append(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
        return color_hexes
    except Exception:
        return ["#1b2838", "#ffffff"]

def run_ocr_on_images(image_paths: list) -> dict:
    """Runs OCR across all captured screenshot images."""
    results = {}
    reader = None

    try:
        import easyocr
        print("[*] Initializing EasyOCR engine (English)...")
        reader = easyocr.Reader(['en'], gpu=False, verbose=False)
    except Exception as e:
        print(f"[!] EasyOCR could not be loaded ({e}). Proceeding with visual metadata analysis.")

    for path in image_paths:
        filename = os.path.basename(path)
        extracted_text = []

        if reader:
            try:
                ocr_out = reader.readtext(path)
                for item in ocr_out:
                    text = item[1].strip()
                    conf = item[2]
                    if len(text) > 1 and conf > 0.3:
                        extracted_text.append(text)
            except Exception as e:
                extracted_text.append(f"[Error: {e}]")

        results[filename] = {
            "path": path,
            "texts": extracted_text,
            "colors": extract_dominant_colors(path)
        }
        print(f"[+] Processed '{filename}': {len(extracted_text)} text elements recognized.")

    return results
