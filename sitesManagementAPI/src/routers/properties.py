from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter

import db.repositories as crud, models.schemas as schemas
from db.database import get_db

router = APIRouter(
    prefix="/properties",
    tags=['Properties']
)


@router.post("/", response_model=schemas.Property, status_code=status.HTTP_201_CREATED)
def create_property(property: schemas.PropertyCreate, owner_id: int, db: Session = Depends(get_db)):
    db_owner = crud.users_crud.get_user(db=db, user_id=owner_id)
    if db_owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')
    
    return crud.properties_crud.create_property(property=property, owner_id=owner_id, db=db)


@router.get("/", response_model=list[schemas.Property])
def read_properties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.properties_crud.get_properties(skip=skip, limit=limit, db=db)


@router.get("/{property_id}", response_model=schemas.Property)
def read_property(property_id: int, db: Session = Depends(get_db)):
    db_property = crud.properties_crud.get_property(db=db, property_id=property_id)
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')

    return db_property

@router.put("/{property_id}", status_code=status.HTTP_200_OK)
def update_property(property_id: int, updated_property: schemas.PropertyBase, db: Session = Depends(get_db)):
    db_property = crud.properties_crud.update_property(db=db, property_id=property_id, updated_property=updated_property)
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')
    
    return db_property

@router.delete("/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db)):
    property_deleted = crud.properties_crud.delete_property(db=db, property_id=property_id)
    if property_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')

    return Response(status_code=status.HTTP_204_NO_CONTENT)