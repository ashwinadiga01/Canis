import asyncio
import websockets
import time

async def hello():
    uri = "ws://localhost:8765"
    while True:
        async with websockets.connect(uri) as websocket:
            # print(f"helloooooooo")
            greeting = await websocket.recv()
            res = list(eval(greeting))
            print("!!!!!!!!!!!",res)
        time.sleep(1)


# if __name__ == "__main__":
#     asyncio.run(hello())

def connect():
    asyncio.run(hello())