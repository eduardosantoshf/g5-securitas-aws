from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter
from fastapi_keycloak import OIDCUser

import src.db.repositories.intrusions_crud as crud, src.models.schemas as schemas
import src.db.repositories.properties_crud as properties_crud
import src.db.repositories.users_crud as users_crud
from src.db.database import get_db
from idp.idp import idp

router = APIRouter(
    prefix="/sites-man-api/intrusions",
    tags=['Intrusions']
)


@router.post("/", response_model=schemas.Intrusion, status_code=status.HTTP_201_CREATED)
def create_intrusion(intrusion: schemas.IntrusionCreate, user_id: int, property_id: int | None = None, db: Session = Depends(get_db), \
                    user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    
    db_user = users_crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {user_id} not found')

    if property_id:
        db_property = properties_crud.get_property(db, property_id)
        if db_property is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')

    return crud.create_intrusion(intrusion=intrusion, user_id=user_id, property_id=property_id, db=db)


@router.get("/{intrusion_id}", response_model=schemas.Intrusion, status_code=status.HTTP_200_OK)
def read_intrusion(intrusion_id: int, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    db_intrusion = crud.get_intrusion(db, intrusion_id)

    if db_intrusion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Intrusion with id {intrusion_id} not found')

    return db_intrusion


@router.get("/", response_model=list[schemas.Intrusion], status_code=status.HTTP_200_OK)
def read_intrusions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):
    return crud.get_intrusions(db=db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=list[schemas.Intrusion], status_code=status.HTTP_200_OK)
def read_intrusions_by_user(user_id: int, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    db_user = users_crud.get_user(user_id=user_id, db=db)

    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {user_id} not found')
    
    return crud.get_intrusions_by_user(user_id=user_id, db=db)  


@router.put("/{intrusion_id}", response_model=schemas.Intrusion, status_code=status.HTTP_200_OK)
def update_intrusion(intrusion_id: int, updated_intrusion: schemas.IntrusionBase, new_property_id: int | None = None, new_user_id: int | None = None, db: Session = Depends(get_db), \
                    user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):
    
    db_intrusion = crud.update_intrusion(db=db, intrusion_id=intrusion_id, new_property_id=new_property_id, new_user_id=new_user_id, updated_intrusion=updated_intrusion)
  
    if db_intrusion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Intrusion with id {intrusion_id} not found")
    elif db_intrusion == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {new_user_id} not found")
    elif db_intrusion == -2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Property with id {new_property_id} not found")

    return db_intrusion 


@router.delete("/{intrusion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_intrusion(intrusion_id: int, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):
    intrusion_deleted = crud.delete_intrusion(intrusion_id=intrusion_id, db=db)

    if intrusion_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Intrusion with id {intrusion_id} not found")