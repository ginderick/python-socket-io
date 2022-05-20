import asyncio
import os
import socketio

sio = socketio.Client()

SEPARATOR = "<SEPARATOR>"

@sio.event
def connect():
    print('connected')

    file_name = "doge.jpg"
    file_size = os.path.getsize(file_name)

    #  Determine chunks by file_size/1024
    chunks =  file_size/1024

    with open(file_name, "rb") as file:
        
        chunk = 0

        # read the bytes from the file
        bytes_read  = file.read(1024)

        while bytes_read:
            if chunk == 0: print(bytes_read)
            file_name = "chunk" + str(chunk) + ".txt"
            sio.emit('receive_file', {"total_chunk": chunks, "current_chunk": chunk, "file_name": file_name, 'bytes_read': bytes_read})
            
            bytes_read = file.read(1024)
            chunk += 1
        

            
@sio.event
def disconnect():
    print('disconnected')






sio.connect('http://localhost:5000')


