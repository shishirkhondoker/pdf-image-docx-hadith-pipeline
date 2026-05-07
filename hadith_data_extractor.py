from docx import Document
import pandas as pd
import re

# Load docx
doc = Document("marge.docx")

# Read paragraphs
paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

# Data storage
chapters = []
sections = []
hadiths = []

# IDs
chapter_id = 1
section_id = 1
hadith_id = 1

# Regex
hadith_pattern = r'^\[[০-৯0-9]+\]'

for text in paragraphs:

    # ======================
    # CHAPTER
    # ======================
    if text.startswith("অধ্যায়"):

        chapter_name = text.replace("অধ্যায়:", "").strip()

        chapters.append({
            "id": chapter_id,
            "name": chapter_name
        })

        chapter_id += 1

    # ======================
    # HADITH
    # ======================
    elif re.match(hadith_pattern, text):

        hadiths.append({
            "id": hadith_id,
            "hadith": text
        })

        hadith_id += 1

    # ======================
    # SECTION
    # ======================
    else:

        # Section usually:
        # short
        # no full stop at end
        # not too many words

        if (
            len(text.split()) <= 8
            and not text.endswith("।")
            and not text.endswith(".")
        ):

            sections.append({
                "id": section_id,
                "name": text
            })

            section_id += 1

# Create DataFrames
chapter_df = pd.DataFrame(chapters)
section_df = pd.DataFrame(sections)
hadith_df = pd.DataFrame(hadiths)

# Save Excel
chapter_df.to_excel("chapter.xlsx", index=False)
section_df.to_excel("section.xlsx", index=False)
hadith_df.to_excel("hadith.xlsx", index=False)

print("Done Successfully!")