# Real-Time Chat Backend (FastAPI)

A real-time chat backend built with FastAPI, WebSockets, JWT authentication, and PostgreSQL.  
Designed for multi-room communication and persistent messaging with async architecture.

---

## ✨ Features

- Real-time WebSocket communication
- Room-based chat system
- JWT authentication
- PostgreSQL database
- Message persistence
- User presence logic
- Async architecture
- Clean project structure
- Scalable for future modules

---

## 🛠 Tech Stack

- FastAPI
- WebSockets
- SQLAlchemy
- PostgreSQL
- JWT Auth
- Docker
- Python 3.11+

---

## 📂 Project Structure



/app
/routers
/models
/schemas
/database
main.py


---

## 🚀 Running Locally

### Install dependencies
```bash
pip install -r requirements.txt

Start the server
uvicorn main:app --reload
```
App runs on:
http://127.0.0.1:8000

🔐 Authentication Flow

Login with JWT

Pass token in WebSocket connection

Validate users per channel

Store messages in DB

🔌 WebSocket Endpoint Example

ws://localhost:8000/ws/chat/{channel_id}?token=YOUR_JWT_TOKEN

Example payload:
```
{
  "action": "send_message",
  "content": "hello world"
}
```
🗄 Environment Variables

Create .env based on
DATABASE_URL=postgresql://user:password@localhost:5432/chatdb
SECRET_KEY=changeme

🧪 Tests (coming soon)

Planned:

unit tests

WebSocket connect tests

message persistence tests

🔧 Future Enhancements

Docker & Docker Compose

User typing state

Delivery/read receipts

Presence logic

Message pagination

Notification service

🧪 Status

This project is ready to be used as a real-time backend or extended into a full messaging platform.
Architected for scalability and production deployment.

📌 Notes

This repository focuses on backend logic.

Frontend implementation can be React, Next.js, or any WebSocket client.

Example WebSocket JS client can be added later

🔗 Author

Developed as part of backend portfolio demonstrating:

real-time communication

async patterns

authentication

database integration

---
How to run using env:
Create a `.env` file based on `.env.example`

Then run:

uvicorn app.main:app --reload
