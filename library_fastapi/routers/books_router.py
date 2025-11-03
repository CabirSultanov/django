from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from starlette import status

from deps import require_roles, get_db
from models import Role, Book
from shemas import BookOut, BookCreate

router = APIRouter(prefix="/api/books", tags=["books"])

@router.post("/", response_model=BookOut, dependencies=[Depends(require_roles(Role.admin, Role.user))])
def create_book(payload: BookCreate, db: Session = Depends(get_db)):
    if db.query(Book).filter_by(title=payload.title).first() is not None:
        raise HTTPException(status_code=400, detail="Book already exists")
    book = Book(title=payload.title, author_id=payload.author_id, pages=payload.pages)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@router.get("/", response_model=dict, status_code=200)
def list_books(
    q: Optional[str] = Query(None),
    order_by: str = Query("title"),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(Book)

    if q:
        query = query.filter(Book.title.ilike(f"%{q}%"))

    if order_by.lstrip("-") not in {"title", "id"}:
        order_by = "title"

    col = getattr(Book, order_by.lstrip("-"))
    if order_by.startswith("-"):
        col = col.desc()
    query = query.order_by(col)

    total = query.count()
    books = query.offset((page - 1) * size).limit(size).all()

    return {
        "total": total,
        "page": page,
        "size": size,
        "items": [BookOut.from_orm(b) for b in books]
    }

@router.patch("/{book_id}", response_model=BookOut, dependencies=[Depends(require_roles(Role.admin))], status_code=200)
def update_book(book_id: int, payload: BookCreate, db: Session = Depends(get_db)):
    book = db.query(Book).get(book_id)
    print(book.title)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = payload.title
    db.commit()
    db.refresh(book)
    return BookOut.from_orm(book)