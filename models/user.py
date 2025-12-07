from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base

class User(Base):

    __tablename__ = 'Users'

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    username = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    phone_number = Column(String, nullable=True, unique=True)
    email = Column(String, index=True, nullable=True, unique=True)