"""
Author: Eric Chen
Date: August 12 2025
Description: Convert one or more images (PNG, JPG, HEIC*, etc.) into a PDF.

How to use:
    # Single image -> single-page PDF
    python images_to_pdf.py output.pdf image.png

    # Multiple images -> multi-page PDF (order matters)
    python3 images_to_pdf.py output.pdf img1.jpg img2.png img3.tiff

Requires:
    pip install pillow
    # For HEIC/HEIF support you may also need:
    #   pip install pillow-heif
"""

import sys
from pathlib import Path
from PIL import Image

def load_image(path: Path) -> Image.Image:
    img = Image.open(path)
    # Convert modes that PDF doesn't support directly (e.g., RGBA, P, LA) to RGB/L
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        img = img.convert("RGB")
    elif img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    return img

def main():
    if len(sys.argv) < 3:
        print("Usage: python images_to_pdf.py output.pdf input1 [input2 ...]")
        sys.exit(1)

    output_pdf = Path(sys.argv[1])
    input_paths = [Path(p) for p in sys.argv[2:]]

    first = load_image(input_paths[0])

    if len(input_paths) == 1:
        first.save(output_pdf, "PDF", resolution=100.0)
        print(f"[done] Wrote: {output_pdf}")
        return

    rest = [load_image(p) for p in input_paths[1:]]
    first.save(output_pdf, "PDF", resolution=100.0, save_all=True, append_images=rest)
    print(f"[done] Wrote: {output_pdf} ({len(input_paths)} pages)")

main() 