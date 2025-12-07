from typing import Dict, List
from fastapi import WebSocket
import asyncio


class ConnectionManager:
    def __init__(self):
        # int is the channel id and their websockets
        self.active_connections: Dict[int, List[dict]] = {}


    async def connect(self, websocket: WebSocket, channel_id: int, user_id: int):
        await websocket.accept()
        conns = self.active_connections.setdefault(channel_id, [])
        conns.append({
            'websocket': websocket,
            'user_id': user_id
            })

    async def disconnect(self, websocket: WebSocket, channel_id: int, user_id: int):
        conns = self.active_connections.get(channel_id)
        if not conns:
            return
        
        self.active_connections[channel_id] = [
        u for u in conns if u.get('user_id') != user_id
        ]

        if not self.active_connections[channel_id]:
            self.active_connections.pop(channel_id)

        if len(conns) == 0:
            self.active_connections.pop(channel_id, None)


    async def broadcast(self, channel_id: int, message: dict, user_id):
        conns =  self.active_connections.get(channel_id, [])
        if not conns:
            return
        
        send_tasks = []
        for ws in list(conns):
            send_tasks.append(self._safe_send(ws, message, channel_id, user_id))
        
        await asyncio.gather(*send_tasks)

    
    async def _safe_send(self, websocket: WebSocket, message: dict, channel_id: int, user_id):
        try:
            await websocket.send_json(message)
        except Exception:
            await self.disconnect(websocket, channel_id, user_id)