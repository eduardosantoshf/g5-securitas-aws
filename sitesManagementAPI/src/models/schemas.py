from pydantic import BaseModel

# defines the pydantic models 

class AlarmBase(BaseModel):
    description: str | None = None

class AlarmCreate(AlarmBase):
    pass

class Alarm(AlarmBase):
    id: int
    property_id: int
    is_alive: bool
    is_active: bool

    class Config:
        orm_mode = True


class CameraBase(BaseModel):
    description: str | None = None

class CameraCreate(CameraBase):
    pass

class Camera(CameraBase):
    id: int
    property_id: int 
    is_alive: bool
    is_streaming: bool

    class Config:
        orm_mode = True


class PropertyBase(BaseModel):
    address: str

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: int
    owner_id: str
    alarms: list[Alarm] = []
    cameras: list[Camera] = []

    class Config:
        orm_mode = True


class IntrusionBase(BaseModel):
    description: str | None = None
    datetime: str

class IntrusionCreate(IntrusionBase):
    pass

class Intrusion(IntrusionBase):
    id: int
    user_id: str
    property_id: int | None = None

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    address: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

class User(UserBase):
    id: str
    properties: list[Property] = []
    intrusions: list[Intrusion] = []
    
    class Config:
        orm_mode = True