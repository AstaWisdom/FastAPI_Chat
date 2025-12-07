from pydantic import BaseModel
from datetime import datetime
from schemas.users import UserCreate


class MessageRead(BaseModel):
    id : int
    content : str 
    channel_id : int
    user_id : int
    timestamp : datetime

    class Config:
        orm_mode = True


class MessageCreate(BaseModel):
    content : str
    channel_id : int