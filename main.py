from fastapi import FastAPI
from database import Base, engine
from routes import users_router, movies_router, favorites_router

app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Подключение маршрутов
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(movies_router, prefix="/movies", tags=["Movies"])
app.include_router(favorites_router, prefix="/favorites", tags=["Favorites"])


@app.get("/")
def root():
    return {"message": "Welcome to the Movie Library API"}
