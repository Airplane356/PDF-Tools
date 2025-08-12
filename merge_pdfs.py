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
        try: 
            reader = PdfReader(str(pdf_path))
            
            # check if pdf needs password
            if reader.is_encrypted:
                print(f"[info] '{pdf_path}' is password-protected.")
                password = input("Enter password: ")
                if not reader.decrypt(password):
                    print(f"[error] Incorrect password for '{pdf_path}'. Skipping.")
                    continue
                
            for page in reader.pages:
                writer.add_page(page)
                print(f"[ok] Added: {pdf_path}")
                
        except Exception as e:
            print(f"[error] Could not read '{pdf_path}': {e}")

    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "wb") as f:
        writer.write(f)
        
    print(f"[done] Wrote merged PDF: {output}")

main()