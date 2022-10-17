from pydantic import BaseModel

# This file has the pydantic models 

class UserBase(BaseModel):
    email: str
    address: str

class User(UserBase):
    id: int 
    is_active: bool
    
    class Config:
        orm_mode = True