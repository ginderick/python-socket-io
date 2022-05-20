import os
import socketio

sio = socketio.Client()

SEPARATOR = "<SEPARATOR>"

@sio.event
def connect():
    print('connected')

    filename = "doge.jpg"
    file_size = os.path.getsize(filename)

    #  Determine chunks by file_size/1024
    total_chunk =  file_size/1024

    with open(filename, "rb") as file:
        
        chunk = 0

        # read the bytes from the file
        bytes_read  = file.read(1024)

        while bytes_read:
            
            file_name = "chunk" + str(chunk) + ".txt"
            sio.emit('receive_file', {"total_chunk": total_chunk, "current_chunk": chunk, "file_name": filename, 'bytes_read': bytes_read})
            bytes_read = file.read(1024)
            chunk += 1
            
@sio.event
def disconnect():
    print('disconnected')






sio.connect('http://localhost:5000')


