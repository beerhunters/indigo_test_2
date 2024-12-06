from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


class MovieBase(BaseModel):
    title: str
    description: str


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class MovieResponse(MovieBase):
    id: int

    class Config:
        from_attributes = True


class FavoriteResponse(BaseModel):
    id: int
    user_id: int
    movie_id: int

    class Config:
        from_attributes = True
