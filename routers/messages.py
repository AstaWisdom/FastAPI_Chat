from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.messages import MessageCreate, MessageRead
from models.user import User
from auth import get_current_user
from crud.messages import create_message, get_messages_by_channel
from db import get_db


router = APIRouter(prefix='/message', tags=['Messages'])

@router.post('/send', response_model=MessageRead)
def send_msg(msg: MessageCreate,db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    msg = create_message(db, user.id, msg.channel_id, msg.content)
    return msg

@router.get('/get_message/{channel_id}', response_model=list[MessageRead])
def get_msg(channel_id, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    msgs = get_messages_by_channel(db, channel_id)
    if not msgs:
        raise HTTPException(status_code=404, detail='No Messages')
    return msgs