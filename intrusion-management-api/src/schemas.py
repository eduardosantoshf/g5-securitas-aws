from pydantic import BaseModel

class Frame(BaseModel):
    frame_number: int
    
    class Config:
        orm_mode = True