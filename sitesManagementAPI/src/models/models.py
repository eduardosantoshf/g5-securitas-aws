from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from src.db.database import Base

# defines sqlalchemy models 

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    address = Column(String(100), nullable=False)
    owner_id = Column(String(150), nullable=False, index=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    alarms = relationship("Alarm", back_populates="property", cascade="delete, delete-orphan")
    cameras = relationship("Camera", back_populates="property", cascade="delete, delete-orphan")


class Alarm(Base):
    __tablename__ = "alarms"

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String(100))
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"))
    is_alive = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    property = relationship("Property", back_populates="alarms")


class Camera(Base):
    __tablename__ = "cameras"

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String(100))
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"))
    is_alive = Column(Boolean, nullable=False, default=False)
    is_streaming = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    property = relationship("Property", back_populates="cameras")


class Intrusion(Base):
    __tablename__ = "intrusions"

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String(100))
    user_id = Column(String(150), index=True)
    property_id = Column(Integer, nullable=False)
    datetime = Column(String(100))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
