# pdf-image-docx-hadith-pipeline

Description This project automatically processes a PDF file and converts it into structured data: PDF pages are converted into images Images are inserted into a Word document Word file is processed to extract: Chapters Sections Hadith Final output is saved in Excel files
Requirements

Before running this project, install Python dependencies:

pip install -r requirements.txt
📁 Folder Setup (IMPORTANT)

Make sure your project structure looks like this:

project/
│
├── input_pdf/
│ └── book.pdf 👈 (your PDF file)
│
├── images/ 👈 (auto created)
│
├── pdf_to_img.py
├── img_to_docx.py
├── hadith_data_extractor.py
├── requirements.txt
└── README.md
▶️ How to Run (STEP BY STEP)
Step 1: Convert PDF to Images
python pdf_to_img.py

👉 This will create images in /images folder

Step 2: Convert Images to Word File
python img_to_docx.py

👉 This will create:

output_images.docx
Step 3: Extract Hadith Data to Excel
python hadith_data_extractor.py

👉 This will generate:

chapter.xlsx
section.xlsx
hadith.xlsx

Final Output

After running all steps, you will get:

🖼️ Images from PDF
📄 Word document with images
📊 Excel files with structured data
