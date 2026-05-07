import fitz
import os

# =========================
# PDF SETTINGS
# =========================

pdf_path = "input_pdf/book.pdf"

# Page range
start_page = 27
end_page = 47

# Output folder
output_folder = "images"



os.makedirs(output_folder, exist_ok=True)

pdf = fitz.open(pdf_path)

# =========================
# PDF TO IMAGE
# =========================

for page_num in range(start_page - 1, end_page):

    page = pdf.load_page(page_num)

    pix = page.get_pixmap()

    image_path = f"{output_folder}/page_{page_num + 1}.png"

    pix.save(image_path)

    print(f"Saved: {image_path}")

print("\nConversion Completed Successfully!")