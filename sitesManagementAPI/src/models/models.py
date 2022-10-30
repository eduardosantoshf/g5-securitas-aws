from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from db.database import Base

# defines sqlalchemy models 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    address = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    properties = relationship("Property", back_populates="owner")


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, nullable=False)
    address = Column(String(100), primary_key=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner = relationship("User", back_populates="properties")
    alarms = relationship("Alarm", back_populates="property")


class Alarm(Base):
    __tablename__ = "alarms"

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String(100))
    property_id = Column(Integer, ForeignKey("properties.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    property = relationship("Property", back_populates="alarms")