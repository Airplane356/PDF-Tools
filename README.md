# PDF Tools 🛠️

Some simple tools that I use for quick handling of PDFs and images

---

## Merging multiple PDFs together (merge_pdfs.py)

1. Requires: 
   ```
   pip install pypdf

2. ```
   python merge_pdfs.py output.pdf input1.pdf input2.pdf ...
  where output.pdf is the merged PDF, and input1.pdf, input2.pdf, etc are the respective individual files to be merged. 

---

## Convert Image (PNG, JPG, HEIC*, etc.) to PDF (image_to_pdf.py)

1. Requires:
   ```
   pip install pillow
   pip install pillow-heif
   
2. ```
   python images_to_pdf.py output.pdf img1.jpg
  where output.pdf is the converted PDF, and img1.jpg is the image to be converted. 

3. If converting multiple images and merging into one pdf:
   ```
   python images_to_pdf.py output.pdf img1.jpg img2.png img3.tiff
