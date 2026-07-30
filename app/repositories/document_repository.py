from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    @staticmethod
    def create_document(
        db: Session,
        filename: str,
        filepath: str,
        user_id: int,
    ):
        document = Document(
            filename=filename,
            filepath=filepath,
            user_id=user_id,
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def get_user_documents(db: Session, user_id: int):
        return (
            db.query(Document)
            .filter(Document.user_id == user_id)
            .order_by(Document.created_at.desc())
            .all()
        )

    @staticmethod
    def get_document_by_id(db: Session, document_id: int):
        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    @staticmethod
    def delete_document(db: Session, document: Document):
        db.delete(document)
        db.commit()