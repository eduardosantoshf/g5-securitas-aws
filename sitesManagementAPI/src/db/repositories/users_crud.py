from sqlalchemy.orm import Session
import src.models.models as models, src.models.schemas as schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_address(db: Session, address: str):
    return db.query(models.User).filter(models.User.address == address).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

def update_user(db: Session, user_id: int, updated_user: schemas.User):
    query = db.query(models.User).filter(models.User.id == user_id).first()
    if query is None:
        return None
    
    query.name = updated_user.name
    query.email = updated_user.email
    query.address = updated_user.address
    
    db.commit()
    return query

def delete_user(db: Session, user_id: int):
    query = db.query(models.User).filter(models.User.id == user_id)
    user_delete = query.first()
    if user_delete is None:
        return None
    
    query.delete()
    db.commit()
    
    return user_delete