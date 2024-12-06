from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import MovieCreate, MovieUpdate, MovieResponse
from crud import create_movie, update_movie, delete_movie
from database import get_db

router = APIRouter()


@router.post("/", response_model=MovieResponse)
def create_new_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return create_movie(db, movie)


@router.put("/{movie_id}", response_model=MovieResponse)
def modify_movie(movie_id: int, movie: MovieUpdate, db: Session = Depends(get_db)):
    updates = movie.dict(exclude_unset=True)
    updated_movie = update_movie(db, movie_id, updates)
    if not updated_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated_movie


@router.delete("/{movie_id}")
def remove_movie(movie_id: int, db: Session = Depends(get_db)):
    delete_movie(db, movie_id)
    return {"message": "Movie deleted"}
