from sqlalchemy.orm import Session
from models import User, Movie, Favorite
from schemas import UserCreate, MovieCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, updates: dict):
    user = db.query(User).filter(User.id == user_id).first()  # type: ignore
    if not user:
        return None
    for key, value in updates.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()  # type: ignore
    if user:
        db.delete(user)
        db.commit()


def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(title=movie.title, description=movie.description)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def update_movie(db: Session, movie_id: int, updates: dict):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()  # type: ignore
    if not movie:
        return None
    for key, value in updates.items():
        setattr(movie, key, value)
    db.commit()
    db.refresh(movie)
    return movie


def delete_movie(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()  # type: ignore
    if movie:
        db.delete(movie)
        db.commit()


def add_favorite(db: Session, user_id: int, movie_id: int):
    favorite = db.query(Favorite).filter(Favorite.user_id == user_id, Favorite.movie_id == movie_id).first()  # type: ignore
    if favorite:
        return favorite  # Уже добавлено в избранное
    new_favorite = Favorite(user_id=user_id, movie_id=movie_id)
    db.add(new_favorite)
    db.commit()
    db.refresh(new_favorite)
    return new_favorite


def remove_favorite(db: Session, user_id: int, movie_id: int):
    favorite = db.query(Favorite).filter(Favorite.user_id == user_id, Favorite.movie_id == movie_id).first()  # type: ignore
    if favorite:
        db.delete(favorite)
        db.commit()
        return favorite
    return None


def get_favorites_by_user(db: Session, user_id: int):
    return db.query(Movie).join(Favorite).filter(Favorite.user_id == user_id).all()  # type: ignore
