from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from src.database import Base
from sqlalchemy.orm import relationship


# This file contains the sqlalchemy models not the pydantic ones

class VideoUsers(Base):
    __tablename__ = "videos_user"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    video_name = Column(String(100), nullable=False)
    video_path = Column(String(100), nullable=False)
    video_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))