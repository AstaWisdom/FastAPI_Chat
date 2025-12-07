from sqlalchemy import Column, Integer, String
from db import Base


class Channel(Base):
    __tablename__ = 'channels'

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)