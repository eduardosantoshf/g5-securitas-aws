from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter
from fastapi.responses import RedirectResponse
from fastapi_keycloak import OIDCUser, KeycloakUser, KeycloakError
from jose import  ExpiredSignatureError

import src.db.repositories.users_crud as crud, src.models.schemas as schemas
import src.db.repositories.cameras_crud as cameras_crud
import src.db.repositories.properties_crud as properties_crud
from src.db.repositories import properties_crud
from src.db.database import get_db
from src.idp.idp import idp
import json


router = APIRouter(
    prefix="/sites-man-api/users",
    tags=['Users']
)


@router.get("/", response_model=list[KeycloakUser])
def read_users(user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):
    try:
        return idp.get_all_users()
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Signature expired")
    except KeycloakError: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")

    


@router.get("/{user_id}", response_model=KeycloakUser)
def read_user(user_id: str = None, query: str = "", user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):
    try:
        user = idp.get_user(user_id=user_id, query=query)
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Signature expired")
    except KeycloakError: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")

    return user


@router.get("/{user_id}/cameras", response_model=list[schemas.Camera], status_code=status.HTTP_200_OK)
def read_user_cameras(user_id: str, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))): 
    
    try:
        idp.get_user(user_id=user_id, query="")
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Signature expired")
    except KeycloakError: 
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
def read_user_alarms(user_id: str, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    
    try:
        idp.get_user(user_id=user_id, query="")
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Signature expired")
    except KeycloakError: 
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
def read_user_properties(user_id: str, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    
    try:
        idp.get_user(user_id=user_id, query="")
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Signature expired")
    except KeycloakError: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    
    prpty = schemas.PropertyCreate(address=f"{user.sub}'s address")

    query = properties_crud.create_property(property=prpty, owner_id=user.sub, db=db)
    
    db_properties = crud.get_properties_by_owner(db=db, owner_id=user_id)
    if db_properties is None:
        return []

    return db_properties


@router.get("/{camera_id}/user", status_code=status.HTTP_200_OK)
def get_user_by_camera(camera_id: int, db: Session = Depends(get_db)):

    db_camera = cameras_crud.get_camera(db=db, camera_id=camera_id)

    if db_camera is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Camera not found")

    db_property =  properties_crud.get_property(db=db, property_id=db_camera.property_id)

    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No cameras for such property")

    data = {
        "user_id": str(db_property.owner_id),
        "property": str(db_property.id),
    }

    return json.dumps(data)
