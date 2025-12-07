from fastapi import WebSocket, WebSocketDisconnect
from models.user import User
from sqlalchemy.orm import Session
from websocket.manager import ConnectionManager
import json
from crud.messages import create_message

class WebsocketHandler:
    def __init__(self, websocket: WebSocket, user: User, manager: ConnectionManager, channel_id: int, db: Session):
        self.ws = websocket
        self.user = user
        self.manager = manager
        self.channel_id = channel_id
        self.db = db
        self.actions = {
            'send_message': self.send_msg,
            'user_joined': self.user_joined,
            'typing': self.user_typing,
            'user_left': self.user_left,
            #'delivered': self.msg_delivered,
        }


    async def connect(self):
        await self.manager.connect(self.websocket, self.user.id)
        await self.run()
        
    async def get_action(self, action: str, payload):
        if not self.actions.get(action):
            return {'error': 'invalid action'}

        await self.actions[action](payload)

    async def user_joined(self, payload):
        msg = {
            'type': 'user_joined',
            'data': {
                'username': self.user.username,
                'id' : self.user.id
            }
        }
        await self.manager.broadcast(self.channel_id, msg, self.user.id)

    async def user_left(self, payload):
        msg = {
            'type': 'user_left',
            'data':{
                'username': self.user.username,
                'id': self.user.id
            }
        }
        await self.manager.broadcast(self.channel_id, msg, self.user.id)

    async def user_typing(self, payload):
        msg = {
            'type': 'user_typing',
            'data': {
                'username' : self.user.username,
                'id': self.user.id
            }
        }
        await self.manager.broadcast(self.channel_id, msg, self.user.id)

    async def send_msg(self, payload):

        content = payload.get('content')
        if not content:
            await self.websocket.send_json({'error': 'Content required'})
            return
        # save to db
        msg = create_message(self.db, self.user.id, self.channel_id, content)
        message = {
            'action': "new_message",
            'channel_id': self.channel_id,
            'content': msg.content,
            'user': self.user.id,
            'username': self.user.username,
            'timestamp': msg.timestamp.isoformat()
        }
        print(f'{message=}')
        await self.manager.broadcast(self.channel_id, message, self.user.id)

    async def run(self):
        try:
            while True:
                data = await self.websocket.receive_text()

                try:
                    payload = json.loads(data)

                except Exception:
                    await self.websocket.send_json({'error': "Invalid json"})
                    continue
                    
                action = payload.get('action')
                await self.get_action(action, payload)
                
        except WebSocketDisconnect:
            await self.manager.disconnect(self.websocket, self.channel_id, self.user.id)