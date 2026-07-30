from app.ai.pdf_reader import extract_text_from_pdf

text = extract_text_from_pdf(
    "uploads/documents/Suraj_Rauniyar_Resume.pdf"
)

print(text[:1000])