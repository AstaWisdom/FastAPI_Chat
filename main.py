from db import engine, Base
from models import user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, channels, messages, websocket

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(engine)

app.include_router(users.router)
app.include_router(channels.router)
app.include_router(messages.router)
app.include_router(websocket.router)

@app.get('/')
def root():
    return {'msg' : 'Hello'}
