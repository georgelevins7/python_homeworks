import websockets, asyncio

async def receive_message(websocket):
    async for message in websocket:
        print(f"\n{message}")

async def send_message(websocket):
    username = input("Enter your username: ")
    await websocket.send(username)
    while True:
        message = await asyncio.to_thread(input, "Enter message: ")

        if message == "exit":
            break

        await websocket.send(message)

async def main():
    async with websockets.connect("ws://localhost:8000") as websocket:
        receive_task = asyncio.create_task(receive_message(websocket))

        await send_message(websocket)

        receive_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())