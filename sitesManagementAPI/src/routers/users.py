from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter
from fastapi.responses import RedirectResponse
from fastapi_keycloak import OIDCUser

from src.db.repositories import properties_crud
import src.db.repositories.users_crud as crud, src.models.schemas as schemas
from src.db.database import get_db
from idp.idp import idp

router = APIRouter(
    prefix="/sites-man-api/users",
    tags=['Users']
)


# @router.post("/callback")
# def callback(session_state: str, code: str):
#     if idp == None:
#         return
#     return idp.exchange_authorization_code(session_state=session_state, code=code)

# @router.post("/login")
# def login():
#     if idp == None:
#         return
#     return RedirectResponse(idp.login_uri)



@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=list[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    
    return users

@router.get("/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    
    return db_user

@router.put("/{user_id}", response_model=schemas.User, status_code=status.HTTP_200_OK)
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


@router.get("/{user_id}/cameras", response_model=list[schemas.Camera], status_code=status.HTTP_200_OK)
def read_user_cameras(user_id: int, db: Session = Depends(get_db), user = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    valid_id = crud.verify_user_id(db=db, user_id=user_id)
    if not valid_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    
    db_properties = crud.get_properties_by_owner(db=db, owner_id=user_id)
    if db_properties is None:
        return []
    
    cameras = []
    tmp = []
    for i in db_properties:
        tmp = properties_crud.get_cameras_by_property(db=db, property_id=i.id)
        cameras.extend(tmp)

    return cameras


@router.get("/{user_id}/alarms", response_model=list[schemas.Alarm], status_code=status.HTTP_200_OK)
def read_user_alarms(user_id: int, db: Session = Depends(get_db), user = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    valid_id = crud.verify_user_id(db=db, user_id=user_id)
    if not valid_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    
    db_properties = crud.get_properties_by_owner(db=db, owner_id=user_id)
    if db_properties is None:
        return []
    
    alarms = []
    tmp = []
    for i in db_properties:
        tmp = properties_crud.get_alarms_by_property(db=db, property_id=i.id)
        alarms.extend(tmp)

    return alarms

@router.get("/{user_id}/properties", response_model=list[schemas.Property], status_code=status.HTTP_200_OK)
def read_user_properties(user_id: int, db: Session = Depends(get_db), user = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    valid_id = crud.verify_user_id(db=db, user_id=user_id)
    if not valid_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    
    db_properties = crud.get_properties_by_owner(db=db, owner_id=user_id)
    if db_properties is None:
        return []

    return db_properties
