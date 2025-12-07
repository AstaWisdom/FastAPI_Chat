from sqlalchemy.orm import Session
from models.channels import Channel


def get_channel(db: Session, channel_id: int):
    return db.query(Channel).filter(Channel.id == channel_id).first()


def get_channels(db:Session):
    return db.query(Channel).all()



def create_channel(db: Session, name: str, description: str = None):
    channel = Channel(
        name = name,
        description = description
    )
    db.add(channel)
    db.commit()
    db.refresh(channel)
    return channel