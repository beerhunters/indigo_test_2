from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import create_user, update_user, delete_user
from database import get_db
from schemas import UserCreate, UserResponse, UserUpdate

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.put("/{user_id}", response_model=UserResponse)
def modify_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updates = user.dict(exclude_unset=True)
    updated_user = update_user(db, user_id, updates)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return {"message": "User deleted"}
