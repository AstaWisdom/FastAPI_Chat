from sqlalchemy.orm import Session
from models.messages import Message
from datetime import datetime


def create_message(db: Session, user_id : int, channel_id: int,content: str, timestamp: datetime= None):
    message = Message(
        user_id = user_id,
        channel_id = channel_id,
        content = content,
        timestamp = timestamp or datetime.utcnow()
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_messages_by_channel(db: Session, channel_id: int):
    return db.query(Message).filter(Message.channel_id == channel_id).all()