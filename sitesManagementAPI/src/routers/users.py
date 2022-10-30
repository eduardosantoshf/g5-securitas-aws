from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter

import db.repositories.users_crud as crud, models.schemas as schemas
from db.database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    
    return db_user

@router.put("/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, updated_user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud.update_user(db=db, user_id=user_id, updated_user=updated_user)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")

    return db_user  

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_deleted = crud.delete_user(db=db, user_id=user_id)
    if user_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

