from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from src.database import Base

# This file contains the sqlalchemy models not the pydantic ones

class Alarm(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)