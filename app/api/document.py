from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService
from typing import List

from app.schemas.document import DocumentResponse

router = APIRouter(
    prefix="/document",
    tags=["Document"]
)


@router.post("/upload", response_model=DocumentResponse)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return DocumentService.upload_document(
        db=db,
        file=file,
        user_id=current_user.id
    )

@router.get("/", response_model=List[DocumentResponse])
def get_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return DocumentService.get_documents(
        db=db,
        user_id=current_user.id
    )


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return DocumentService.delete_document(
        db=db,
        document_id=document_id,
        user_id=current_user.id
    )