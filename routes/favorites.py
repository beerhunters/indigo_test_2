# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from version_2.database import get_db
# from version_2.crud import add_to_favorites
#
# router = APIRouter()
#
#
# @router.post("/")
# def add_favorite(user_id: int, movie_id: int, db: Session = Depends(get_db)):
#     return add_to_favorites(db=db, user_id=user_id, movie_id=movie_id)
