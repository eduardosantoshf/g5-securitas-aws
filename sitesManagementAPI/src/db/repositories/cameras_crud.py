from sqlalchemy.orm import Session

from src.db.repositories import properties_crud, users_crud
import src.models.models as models, src.models.schemas as schemas



def get_camera(db: Session, camera_id: int):
    return db.query(models.Camera).filter(models.Camera.id == camera_id).first()

def get_cameras(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Camera).offset(skip).limit(limit).all()

def get_cameras_by_property(db: Session, property_id: int):
    return db.query(models.Camera).filter(models.Camera.property_id == property_id).all()

def create_camera(db: Session, camera: schemas.CameraCreate, property_id: int):
    db_camera = models.Camera(**camera.dict(), property_id=property_id)
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)

    return db_camera

def update_camera(db: Session, camera_id: int, new_property_id: int, new_description: str):
    query = db.query(models.Camera).filter(models.Camera.id == camera_id).first()
    if query is None:
        return None

    if new_property_id:
        query.property_id = new_property_id
    
    if new_description:
        query.description = new_description

    db.commit()
    return query

def delete_camera(db: Session, camera_id: int):
    camera_delete = db.query(models.Camera).filter(models.Camera.id == camera_id).first()
    
    if camera_delete is None:
        return None
    
    db.delete(camera_delete)
    db.commit()
    
    return camera_delete