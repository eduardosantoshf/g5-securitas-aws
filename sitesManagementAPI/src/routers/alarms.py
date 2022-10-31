from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter

import src.db.repositories.alarms_crud as crud, src.models.schemas as schemas
import src.db.repositories.properties_crud as properties_crud
from src.db.database import get_db

router = APIRouter(
    prefix="/alarms",
    tags=['Alarms']
)


@router.post("/", response_model=schemas.Alarm, status_code=status.HTTP_201_CREATED)
def create_alarm(alarm: schemas.AlarmCreate, property_id: int, db: Session = Depends(get_db)):
    db_property = properties_crud.get_property(db, property_id)
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Property with id {property_id} not found')
    
    return crud.create_alarm(alarm=alarm, property_id=property_id, db=db)


@router.get("/", response_model=list[schemas.Alarm])
def read_alarms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_alarms(db=db, skip=skip, limit=limit)


@router.get("/{alarm_id}", response_model=schemas.Alarm)
def read_alarm(alarm_id: int, db: Session = Depends(get_db)):
    db_alarm = crud.get_alarm(db=db, alarm_id=alarm_id)
    if db_alarm is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Alarm with id {alarm_id} not found')
    
    return db_alarm


@router.put("/{alarm_id}", status_code=status.HTTP_200_OK)
def update_alarm(alarm_id: int, updated_alarm: schemas.AlarmBase, db: Session = Depends(get_db)):
    db_alarm = crud.update_alarm(db=db, alarm_id=alarm_id, updated_alarm=updated_alarm)
    if db_alarm is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Alarm with id {alarm_id} not found')

    return db_alarm


@router.delete("/{alarm_id}")
def delete_alarm(alarm_id: int, db: Session = Depends(get_db)):
    alarm_deleted = crud.delete_alarm(db=db, alarm_id=alarm_id)
    if alarm_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Alarm with id {alarm_id} not found')

    return Response(status_code=status.HTTP_204_NO_CONTENT)