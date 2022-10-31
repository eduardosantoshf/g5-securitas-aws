from sqlalchemy.orm import Session

import src.models.models as models, src.models.schemas as schemas


def get_alarm(db: Session, alarm_id: int):
    return db.query(models.Alarm).filter(models.Alarm.id == alarm_id).first()

def get_alarms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Alarm).offset(skip).limit(limit).all()

def get_alarms_by_property(db: Session, property_id: int):
    return db.query(models.Alarm).filter(models.Alarm.property_id == property_id).all()

def create_alarm(db: Session, alarm: schemas.AlarmCreate, property_id: int):
    db_alarm = models.Alarm(**alarm.dict(), property_id=property_id)
    db.add(db_alarm)
    db.commit()
    db.refresh(db_alarm)

    return db_alarm

def update_alarm(db: Session, alarm_id: int, updated_alarm: schemas.Alarm):
    query = db.query(models.Alarm).filter(models.Alarm.id == alarm_id).first()
    if query is None:
        return None

    query.property_id = updated_alarm.property_id

    db.commit()
    return query

def delete_alarm(db: Session, alarm_id):
    alarm_delete = db.query(models.Alarm).filter(models.Alarm.id == alarm_id).first()
    
    if alarm_delete is None:
        return None
    
    db.delete(alarm_delete)
    db.commit()
    
    return alarm_delete