# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from database import get_db
# from crud import add_to_favorites
#
# router = APIRouter()
#
#
# @router.post("/")
# def add_favorite(user_id: int, movie_id: int, db: Session = Depends(get_db)):
#     return add_to_favorites(db=db, user_id=user_id, movie_id=movie_id)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import add_favorite, remove_favorite, get_favorites_by_user
from schemas import MovieResponse
from database import get_db

router = APIRouter(prefix="/favorites", tags=["favorites"])


@router.post("/{user_id}/{movie_id}")
def add_movie_to_favorites(user_id: int, movie_id: int, db: Session = Depends(get_db)):
    favorite = add_favorite(db, user_id, movie_id)
    if not favorite:
        raise HTTPException(status_code=400, detail="Favorite already exists")
    return {"message": "Movie added to favorites"}


@router.delete("/{user_id}/{movie_id}")
def remove_movie_from_favorites(user_id: int, movie_id: int, db: Session = Depends(get_db)):
    favorite = remove_favorite(db, user_id, movie_id)
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return {"message": "Movie removed from favorites"}


@router.get("/{user_id}", response_model=list[MovieResponse])
def get_user_favorites(user_id: int, db: Session = Depends(get_db)):
    favorites = get_favorites_by_user(db, user_id)
    if not favorites:
        raise HTTPException(status_code=404, detail="No favorites found for user")
    return favorites
