from pydantic import BaseModel

class Frame(BaseModel):
    camera_id: int
    timestamp_intrusion: float
    
    class Config:
        orm_mode = True

class VideoUsers(BaseModel):
    id: int

    class Config:
        orm_mode = True