from pydantic import BaseModel

# defines the pydantic models 

class AlarmBase(BaseModel):
    description: str | None = None

class AlarmCreate(AlarmBase):
    pass

class Alarm(AlarmBase):
    id: int
    property_id: int

    class Config:
        orm_mode = True


class PropertyBase(BaseModel):
    address: str

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: int
    owner_id: int
    alarms: list[Alarm] = []

    class Config:
        orm_mode = True


class IntrusionBase(BaseModel):
    description: str | None = None
    datetime: str

class IntrusionCreate(IntrusionBase):
    pass

class Intrusion(IntrusionBase):
    id: int
    user_id: int
    property_id: int | None = None

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    address: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    properties: list[Property] = []
    intrusions: list[Intrusion] = []
    
    class Config:
        orm_mode = True