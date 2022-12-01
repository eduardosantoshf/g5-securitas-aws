from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter

import src.db.repositories.properties_crud as crud, src.models.schemas as schemas
import src.db.repositories.users_crud as users_crud
from src.db.database import get_db


router = APIRouter(
    prefix="/sites-man-api/properties",
    tags=['Properties']
)


@router.post("/", response_model=schemas.Property, status_code=status.HTTP_201_CREATED)
def create_property(property: schemas.PropertyCreate, owner_id: int, db: Session = Depends(get_db)):
    db_owner = users_crud.get_user(db=db, user_id=owner_id)
    if db_owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {owner_id} not found')

    query = crud.create_property(property=property, owner_id=owner_id, db=db)
    
    if query is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Property already registred')

    return query


@router.get("/", response_model=list[schemas.Property])
def read_properties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_properties(skip=skip, limit=limit, db=db)


@router.get("/{property_id}", response_model=schemas.Property)
def read_property(property_id: int, db: Session = Depends(get_db)):
    db_property = crud.get_property(db=db, property_id=property_id)
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')

    return db_property


@router.put("/{property_id}", response_model=schemas.Property, status_code=status.HTTP_200_OK)
def update_property(property_id: int, new_owner_id: int | None = None, new_address: str | None = None, db: Session = Depends(get_db)):
    
    db_property = crud.update_property(db=db, property_id=property_id, new_owner_id=new_owner_id, new_address=new_address)
    
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')
    elif db_property == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user with id {new_owner_id}')
    elif db_property == -2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Property already registred at specified address')
    
    return db_property


@router.delete("/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db)):
    property_deleted = crud.delete_property(db=db, property_id=property_id)
    if property_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')

    return Response(status_code=status.HTTP_204_NO_CONTENT)