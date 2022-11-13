from sqlalchemy.orm import Session
from fastapi import Depends, Response, HTTPException, status, APIRouter

import src.db.repositories.cameras_crud as crud, src.models.schemas as schemas
import src.db.repositories.properties_crud as properties_crud
import src.db.repositories.alarms_crud as alarms_crud
from src.db.database import get_db

router = APIRouter(
    prefix="/sites-man-api/cameras",
    tags=['Cameras']
)


@router.post("/", response_model=schemas.Camera, status_code=status.HTTP_201_CREATED)
def create_(camera: schemas.CameraCreate, property_id: int, db: Session = Depends(get_db)):
    db_property = properties_crud.get_property(db, property_id)
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Property with id {property_id} not found")
    
    return crud.create_camera(camera=camera, property_id=property_id, db=db)


@router.get("/", response_model=list[schemas.Camera])
def read_cameras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_cameras(db=db, skip=skip, limit=limit)


@router.get("/{camera_id}", response_model=schemas.Camera)
def read_camera(camera_id: int, db: Session = Depends(get_db)):
    
    db_camera = crud.get_camera(db=db, camera_id=camera_id)
    if db_camera is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Camera with id {camera_id} not found")
    
    return db_camera


@router.put("/{camera_id}", response_model=schemas.Camera, status_code=status.HTTP_200_OK)
def update_camera(camera_id: int, new_description: str | None = None, new_property_id: int | None = None, db: Session = Depends(get_db)):

    if new_property_id:
        query = properties_crud.get_property(db=db, property_id=new_property_id)
        
        if query is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Property with id {new_property_id} not found")

    db_camera = crud.update_camera(db=db, camera_id=camera_id, new_property_id=new_property_id, new_description=new_description)
    if db_camera is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Camera with id {camera_id} not found")

    return db_camera


@router.delete("/{camera_id}")
def delete_camera(camera_id: int, db: Session = Depends(get_db)):
    camera_deleted = crud.delete_camera(db=db, camera_id=camera_id)
    if camera_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Camera with id {camera_id} not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)