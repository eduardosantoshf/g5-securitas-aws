from sqlalchemy.orm import Session

import src.models.models as models, src.models.schemas as schemas


def get_property(db: Session, property_id: int):
    return db.query(models.Property).filter(models.Property.id == property_id).first()

def get_properties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Property).offset(skip).limit(limit).all()

def get_properties_by_owner(db: Session, owner_id: int):
    return db.query(models.Property).filter(models.Property.owner_id == owner_id).all()

def create_property(db: Session, property: schemas.PropertyCreate, owner_id: int):
    db_property = models.Property(**property.dict(), owner_id=owner_id)
    db.add(db_property)
    db.commit()
    db.refresh(db_property)

    return db_property

def update_property(db: Session, property_id: int, updated_property: schemas.Property):
    query = db.query(models.Property).filter(models.Property.id == property_id).first()
    if query is None:
        return None

    query.update(**updated_property.dict())
    db.commit()
    return query

def delete_property(db: Session, property_id):
    query = db.query(models.Property).filter(models.Property.id == property_id).first()
    property_delete = query.first()
    if property_delete is None:
        return None
    
    query.delete()
    db.commit()
    
    return property_delete