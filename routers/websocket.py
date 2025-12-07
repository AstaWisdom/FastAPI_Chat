from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect, Query
from websocket.manager import ConnectionManager
from sqlalchemy.orm import Session
from db import get_db
from auth import get_current_user
from services.websocket import WebsocketHandler
from crud.messages import create_message

router = APIRouter()
manager = ConnectionManager()

@router.websocket('/ws/chat/{channel_id}')
async def websocket_endpoint(websocket: WebSocket, channel_id:int, db: Session = Depends(get_db)):
    token = websocket.query_params.get('token')
    print(f'{token=}')
    user = get_current_user(token, db)
    WebsocketHandler(websocket, user, manager, channel_id, db).connect()