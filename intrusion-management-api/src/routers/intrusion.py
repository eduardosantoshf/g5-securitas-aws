from fastapi import Depends, Response, status, APIRouter, UploadFile
from sqlalchemy.orm import Session
from src.database import get_db
from src.service import intrusion_service

router = APIRouter(
    prefix="/intrusion-management-api/intrusion",
    tags=['Intrusion']
)

@router.get("/events-triggered/{user_id}", status_code=status.HTTP_200_OK)
def get_events_triggered(user_id: int, db: Session = Depends(get_db)):
    res = intrusion_service.get_events_triggered(db=db, user_id=user_id)
    if res is None or len(res) == 0:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return res
