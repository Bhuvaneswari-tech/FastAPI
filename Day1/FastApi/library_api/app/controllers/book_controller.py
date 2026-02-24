from fastapi import APIRouter, Depends
from app.dependencies.book_dependency import get_book_service
from app.services.book_service import BookService

router = APIRouter()

@router.get("/books")
def get_books(book_service: BookService = Depends(get_book_service)):
    return book_service.get_all_books() 

