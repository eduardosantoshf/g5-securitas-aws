from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter
from fastapi_keycloak import OIDCUser

import src.db.repositories.alarms_crud as crud, src.models.schemas as schemas
import src.db.repositories.properties_crud as properties_crud
from src.db.database import get_db
from src.idp.idp import idp

router = APIRouter(
    prefix="/sites-man-api/alarms",
    tags=['Alarms']
)


@router.post("/", response_model=schemas.Alarm, status_code=status.HTTP_201_CREATED)
def create_alarm(alarm: schemas.AlarmCreate, property_id: int, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    
    #check if it is a valid property id
    db_property = properties_crud.get_property(db, property_id)
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Property with id {property_id} not found")
    
    return crud.create_alarm(alarm=alarm, property_id=property_id, db=db)


@router.get("/", response_model=list[schemas.Alarm])
def read_alarms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):
    return crud.get_alarms(db=db, skip=skip, limit=limit)


@router.get("/{alarm_id}", response_model=schemas.Alarm)
def read_alarm(alarm_id: int, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):
    
    db_alarm = crud.get_alarm(db=db, alarm_id=alarm_id)
    if db_alarm is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Alarm with id {alarm_id} not found")
    
    return db_alarm


@router.put("/{alarm_id}", response_model=schemas.Alarm, status_code=status.HTTP_200_OK)
def update_alarm(alarm_id: int, new_description: str | None = None, new_property_id: int | None = None, db: Session = Depends(get_db), \
                user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):

    if new_property_id:
        query = properties_crud.get_property(db=db, property_id=new_property_id)
        
        if query is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Property with id {new_property_id} not found")

    db_alarm = crud.update_alarm(db=db, alarm_id=alarm_id, new_property_id=new_property_id, new_description=new_description)
    if db_alarm is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Alarm with id {alarm_id} not found")

    return db_alarm


@router.delete("/{alarm_id}")
def delete_alarm(alarm_id: int, db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-admin']))):
    alarm_deleted = crud.delete_alarm(db=db, alarm_id=alarm_id)
    if alarm_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Alarm with id {alarm_id} not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)