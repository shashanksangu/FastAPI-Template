from typing import Dict, Optional, Any, List
from fastapi import FastAPI, Request, Depends, WebSocket, WebSocketDisconnect, Query, APIRouter
from datetime import datetime

app = FastAPI()

@app.get("/metadata")
async def metadata():
    return {}

class WebSocketConnectionModel:
    user_id: str
    connection_date_time_utc: datetime
    socket: WebSocket


class SocketManager:
    def __init__(self):
        self.connections: List[WebSocketConnectionModel] = []

    def len(self):
        return len(self.connections)

    def connect(self, user_id: int, websocket: WebSocket):
        connection = WebSocketConnectionModel()
        connection.user_id = user_id
        connection.socket = websocket
        connection.connection_date_time_utc = datetime.utcnow()
        self.connections.append(connection)
        return connection

    def disconnect(self, item: WebSocketConnectionModel):
        self.connections.remove(item)

manager = SocketManager()

@app.websocket("/websocket/1")
async def websocket_test(websocket: WebSocket, user_id: str, activity_id: str, reps: bool = True, hold: bool = False, format: str = "json"):
    await websocket.accept()
    connection = manager.connect(user_id, websocket)
    try:
        out = {
            "sample": bool(True)
        }
        await websocket.send_text(f"{str(out)}")
    except WebSocketDisconnect:
        manager.disconnect(connection)

