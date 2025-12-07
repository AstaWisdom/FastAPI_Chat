from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from db import Base
from datetime import datetime

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('Users.id'))
    channel_id = Column(Integer, ForeignKey('channels.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)