import asyncio
import os
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connected')

    file_name = "yt.txt"
    file_size = os.path.getsize(file_name)

    with open(file_name, 'rb') as file:
        
        data = file.read(1024)
        await sio.send({'data': data, 'file_name': file_name, 'file_size': file_size})


    

@sio.event
async def disconnect():
    print('disconnected')


async def main():
    await sio.connect('http://localhost:8000')
    await sio.wait()


asyncio.run(main())

