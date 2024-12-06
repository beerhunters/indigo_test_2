# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from version_2.crud import create_movie
# from version_2.schemas import MovieCreate, MovieResponse
# from version_2.database import get_db
#
# router = APIRouter()
#
#
# @router.post("/", response_model=MovieResponse)
# def create_new_movie(movie: MovieCreate, db: Session = Depends(get_db)):
#     return create_movie(db=db, movie=movie)
