from sqlalchemy.orm import Session
import src.models.models as models
from sqlalchemy.sql import text



def get_events_triggered(db: Session, user_id: str) -> list:
    #return db.query(models.VideoUsers).filter(models.VideoUsers.user_id == user_id)
    return db.execute(text("SELECT id, building_id, camera_id, video_date FROM videos_user WHERE user_id = :user_id"), {'user_id': user_id}).fetchall()
