from pydantic import BaseModel
import datetime

class Frame(BaseModel):
    camera_id: int
    timestamp_intrusion: datetime.time
    
    class Config:
        orm_mode = True

class VideoUsers(BaseModel):
    id: int

    class Config:
        orm_mode = True