from time import time

import websockets, asyncio

client_list = {}

async def broadcast(message):
    for client in client_list.keys():
        await client.send(message)

async def handler(websocket):
    username = await websocket.recv()
    client_list[websocket] = username

    try:
        async for message in websocket:
            print(f"{client_list[websocket]}: {message}")

            await broadcast(f"{client_list[websocket]}: {message}")

    finally:
        client_list.pop(websocket, None)

async def main():
    async with websockets.serve(handler, "localhost", 8000):
        print("Server started...")
        await asyncio.Future()

        

if __name__ == "__main__":
    asyncio.run(main())