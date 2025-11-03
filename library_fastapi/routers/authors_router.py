from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from deps import require_roles, get_db
from models import Author, Role
from shemas import AuthorOut, AuthorCreate

router = APIRouter(prefix="/api/authors", tags=["authors"])


@router.post("/", response_model=AuthorOut, dependencies=[Depends(require_roles(Role.admin))])
def create_author(payload: AuthorCreate, db: Session = Depends(get_db)):
    if db.query(Author).filter_by(name=payload.name).first() is not None:
        raise HTTPException(status_code=400, detail="Author already exists")
    author = Author(name=payload.name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


@router.get("/", response_model=dict, status_code=200)
def list_authors(
    q: Optional[str] = Query(None),
    order_by: str = Query("name"),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(Author)

    if q:
        query = query.filter(Author.name.ilike(f"%{q}%"))

    if order_by.lstrip("-") not in {"name", "id"}:
        order_by = "name"

    col = getattr(Author, order_by.lstrip("-"))
    if order_by.startswith("-"):
        col = col.desc()
    query = query.order_by(col)

    total = query.count()
    authors = query.offset((page - 1) * size).limit(size).all()

    return {
        "total": total,
        "page": page,
        "size": size,
        "items": [AuthorOut.from_orm(a) for a in authors]
    }


@router.patch("/{author_id}", response_model=AuthorOut,dependencies=[Depends(require_roles(Role.admin))], status_code=200)
def update_author(author_id: int, author: AuthorOut, db: Session = Depends(get_db)):
    author = db.query(Author).get(author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    author.name = author.name
    db.commit()
    db.refresh(author)
    return AuthorOut.from_orm(author)

@router.delete("/{author_id}", response_model=AuthorOut, dependencies=[Depends(require_roles(Role.admin))],status_code=200)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).get(author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(author)
    db.commit()
    return None
