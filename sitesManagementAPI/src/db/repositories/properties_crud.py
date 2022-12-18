from sqlalchemy.orm import Session

import src.db.repositories
import src.models.models as models, src.models.schemas as schemas


def get_property(db: Session, property_id: int):
    return db.query(models.Property).filter(models.Property.id == property_id).first()

def get_properties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Property).offset(skip).limit(limit).all()

def create_property(db: Session, property: schemas.PropertyCreate, owner_id: str):
    query = db.query(models.Property).filter(models.Property.address == property.address, models.Property.owner_id == owner_id).first()
    if query is not None:
        return None

    db_property = models.Property(**property.dict(), owner_id=owner_id)
    db.add(db_property)
    db.commit()
    db.refresh(db_property)

    return db_property

def update_property(db: Session, property_id: int, new_owner_id: str, new_address: str):
    query = db.query(models.Property).filter(models.Property.id == property_id).first()
    if query is None:
        return None

    if new_owner_id:
        query.owner_id = new_owner_id
        
    if new_address:
        query_new_address = db.query(models.Property).filter(models.Property.address == new_address).first()

        if query_new_address is None:
            query.address = new_address
        else: 
            return -1

    db.commit()
    return query

def delete_property(db: Session, property_id: int):
    property_delete = db.query(models.Property).filter(models.Property.id == property_id).first()
    
    if property_delete is None:
        return None
    
    db.delete(property_delete)
    db.commit()
    
    return property_delete


#return None if property is invalid
def get_cameras_by_property(db: Session, property_id: int):
    db_property = get_property(property_id=property_id, db=db)

    if db_property is None:
        return None

    return db_property.cameras

def get_alarms_by_property(db: Session, property_id: int):
    db_property = get_property(property_id=property_id, db=db)

    if db_property is None:
        return None

    return db_property.alarms