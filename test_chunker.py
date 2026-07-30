from app.ai.pdf_reader import extract_text_from_pdf
from app.ai.text_chunker import chunk_text

text = extract_text_from_pdf(
    "uploads/documents/Suraj_Rauniyar_Resume.pdf"
)

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])