from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from schemas.channels import ChannelCreate, ChannelRead
from crud.channels import get_channel, create_channel, get_channels
from auth import get_current_user
from models.user import User

router = APIRouter(prefix='/channel', tags=['/channels'])


@router.post('/create_channel', response_model=ChannelRead)
def create_new_channel(data: ChannelCreate, user : User = Depends(get_current_user), db: Session = Depends(get_db)):
    channel = create_channel(db, data.name, data.description)
    return channel


@router.get('/all_channels', response_model=list[ChannelRead])
def get_all_channels(db: Session = Depends(get_db), user : User = Depends(get_current_user)):
    return get_channels(db)


@router.get("/{channel_id}", response_model=ChannelRead)
def get_single_channel(channel_id: int, db: Session = Depends(get_db), 
                       user: User = Depends(get_current_user)):
    channel = get_channel(db, channel_id)
    if not channel:
        raise HTTPException(status_code=404, detail='Channel not Found')
    
    return channel
