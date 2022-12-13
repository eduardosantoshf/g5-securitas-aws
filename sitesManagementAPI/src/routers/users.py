from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter
from fastapi.responses import RedirectResponse
from fastapi_keycloak import OIDCUser, KeycloakUser

import src.db.repositories.users_crud as crud, src.models.schemas as schemas
from src.db.repositories import properties_crud
from src.db.database import get_db
from idp.idp import idp


router = APIRouter(
    prefix="/sites-man-api/users",
    tags=['Users']
)


@router.get("/", response_model=list[KeycloakUser])
def read_users(user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):
    return idp.get_all_users()


@router.get("/{user_id}", response_model=KeycloakUser)
def read_user(user_id: str = None, query: str = "", user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):
    
    return idp.get_user(user_id=user_id, query=query)


@router.get("/{user_id}/cameras", response_model=list[schemas.Camera], status_code=status.HTTP_200_OK)
def read_user_cameras(user_id: str, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))): 
    
    idp.get_user(user_id=user_id, query=None)
    
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
def read_user_alarms(user_id: str, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    
    idp.get_user(user_id=user_id, query=None)
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
def read_user_properties(user_id: str, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    
    idp.get_user(user_id=user_id, query=None)
    db_properties = crud.get_properties_by_owner(db=db, owner_id=user_id)
    if db_properties is None:
        return []

    return db_properties