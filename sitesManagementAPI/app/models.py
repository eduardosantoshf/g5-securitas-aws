from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

# This file contains the sqlalchemy models not the pydantic ones

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    address = Column(String(100), nullable=False)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)

