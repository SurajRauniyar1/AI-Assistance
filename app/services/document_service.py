import os
import shutil
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.repositories.document_repository import DocumentRepository
from app.ai.pdf_reader import extract_text_from_pdf
from app.ai.text_chunker import chunk_text
from app.ai.embeddings import create_embeddings
from app.ai.vector_store import add_chunks

UPLOAD_DIR = "uploads/documents"


class DocumentService:

    @staticmethod
    def upload_document(
        db: Session,
        file: UploadFile,
        user_id: int
    ):
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        document = DocumentRepository.create_document(
            db=db,
            filename=file.filename,
            filepath=file_path,
            user_id=user_id
        )

    # Extract text
        text = extract_text_from_pdf(file_path)

        print("=" * 50)
        print("Text Length:", len(text))
        print("First 500 characters:")
        print(text[:500])

        chunks = chunk_text(text)

        print("Chunks:", len(chunks))

        if not chunks:
            raise ValueError("No text extracted from the PDF.")

        embeddings = create_embeddings(chunks)

        print("Embeddings:", len(embeddings))

        add_chunks(
            chunks=chunks,
            embeddings=embeddings,
            document_id=document.id
            )
        return document

    @staticmethod
    def get_documents(db, user_id):
        return DocumentRepository.get_user_documents(db, user_id)


    @staticmethod
    def delete_document(db, document_id, user_id):
        document = DocumentRepository.get_document_by_id(db, document_id)

        if not document:
            raise HTTPException(
                status_code=404,
                detail="Document not found"
        )

        if document.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="Not authorized"
                )

        if os.path.exists(document.filepath):
            os.remove(document.filepath)

        DocumentRepository.delete_document(db, document)

        return {"message": "Document deleted successfully"}