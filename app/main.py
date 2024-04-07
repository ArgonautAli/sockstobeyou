from fastapi import FastAPI
from websocket import WebSocket

app = FastAPI()

@app.get("/")
async def get():
    return {"socks to be": "you" }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket
    data = await websocket.receive_text()
    await websocket.send_text(f"Message text: {data}")

