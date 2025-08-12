"""
Author: Eric Chen
Date: August 12 2025
Description: This is a script that merges multiple PDFs together. 

Usage:
    python merge_pdfs.py output.pdf input1.pdf input2.pdf ...

Requires:
    pip install pypdf
"""
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 merge_pdfs.py output.pdf input1.pdf input2.pdf ...")
        sys.exit(1)

    output = Path(sys.argv[1])
    inputs = [Path(p) for p in sys.argv[2:]]

    writer = PdfWriter()
    for pdf_path in inputs:
        reader = PdfReader(str(pdf_path))
        for page in reader.pages:
            writer.add_page(page)

    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "wb") as f:
        writer.write(f)

main()