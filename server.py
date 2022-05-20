from asyncore import write
from genericpath import isfile
import socketio
import eventlet
import os
import math

sio = socketio.Server()
app = socketio.WSGIApp(sio)



@sio.event
def connect(sid, message):
    print(f'connected')

@sio.event
def disconnect(sid, message):
    print(f'disconnected')

@sio.event
def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    return {'result': result}

@sio.event
def receive_file(sid, data):
    chunk = data['current_chunk']
    total_chunk = data['total_chunk']
    print(f"Progress {round(chunk/total_chunk*100, 2)}")
    sio.start_background_task(write_file, data)
    
    

def write_file(data):

    file_name = data['file_name']
    bytes_read = data['bytes_read']

    #  write the binary from client
    with open("copy"+ file_name, "ab") as file:
        file.write(bytes_read)


if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

