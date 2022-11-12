from sqlalchemy.orm import Session

import src.models.models as models, src.models.schemas as schemas


def get_intrusion(db: Session, intrusion_id: int):
    return db.query(models.Intrusion).filter(models.Intrusion.id == intrusion_id).first()


def get_intrusions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Intrusion).offset(skip).limit(limit).all()


def get_intrusion_by_user(db: Session, user_id: int):
    return db.query(models.Intrusion).filter(models.Intrusion.user_id == user_id).all()


def create_intrusion(db: Session, intrusion: schemas.IntrusionCreate, user_id: int, property_id: int | None = None):
    db_intrusion = models.Intrusion(**intrusion.dict(), user_id=user_id, property_id=property_id)
    db.add(db_intrusion)
    db.commit()
    db.refresh(db_intrusion)

    return db_intrusion


def update_intrusion(db: Session, intrusion_id: int, updated_intrusion: schemas.IntrusionBase, new_user_id: int | None = None, new_property_id: int | None = None):
    query = db.query(models.Intrusion).filter(models.Intrusion.id == intrusion_id).first()
    if query is None:
        return None

    if new_user_id:
        query_user = db.query(models.User).filter(models.User.id == new_user_id).first()
        if query_user is None:
            return -1
        query.user_id = new_user_id

    if new_property_id:
        query_property = db.query(models.Property).filter(models.Property.id == new_property_id).first()
        if query_property is None:
            return -2
        query.property_id = new_property_id
    
    query.description = updated_intrusion.description
    query.datetime = updated_intrusion.datetime

    db.commit()
    return query


def delete_intrusion(db: Session, intrusion_id: int):
    intrusion_delete = db.query(models.Intrusion).filter(models.Intrusion.id == intrusion_id).first()
    
    if intrusion_delete is None:
        return None
    
    db.delete(intrusion_delete)
    db.commit()
    
    return intrusion_delete