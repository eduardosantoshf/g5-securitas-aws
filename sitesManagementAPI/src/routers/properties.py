from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter
from fastapi_keycloak import OIDCUser
from jose import ExpiredSignatureError

import src.db.repositories.properties_crud as crud, src.models.schemas as schemas
import src.db.repositories.users_crud as users_crud
from src.db.database import get_db
from src.idp.idp import idp


router = APIRouter(
    prefix="/sites-man-api/properties",
    tags=['Properties']
)


@router.post("/", response_model=schemas.Property, status_code=status.HTTP_201_CREATED)
def create_property(property: schemas.PropertyCreate, owner_id: str, db: Session = Depends(get_db), \
                        user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    try:
        idp.get_user(user_id=owner_id, query=None)
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Signature expired")
    except: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {owner_id} not found")

    query = crud.create_property(property=property, owner_id=owner_id, db=db)
    
    if query is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Property already registred')

    return query


@router.get("/", response_model=list[schemas.Property])
def read_properties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), \
                        user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):
    try: 
        return crud.get_properties(skip=skip, limit=limit, db=db)
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Signature expired")


@router.get("/{property_id}", response_model=schemas.Property)
def read_property(property_id: int, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    db_property = crud.get_property(db=db, property_id=property_id)
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')

    return db_property


@router.put("/{property_id}", response_model=schemas.Property, status_code=status.HTTP_200_OK)
def update_property(property_id: int, new_owner_id: str | None = None, new_address: str | None = None, \
                        db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    try:
        idp.get_user(user_id=new_owner_id, query=None)
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Signature expired")
    except: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {new_owner_id} not found")

    db_property = crud.update_property(db=db, property_id=property_id, new_owner_id=new_owner_id, new_address=new_address)
    
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')
    elif db_property == -1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Property already registred at specified address')
    
    return db_property


@router.delete("/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    property_deleted = crud.delete_property(db=db, property_id=property_id)
    if property_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')

    return Response(status_code=status.HTTP_204_NO_CONTENT)