from asyncore import write
from genericpath import isfile
import socketio
import eventlet
import os

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
    print('Emit from client')
    write_file(data)
    

def write_file(data):

    file_name = data['file_name']
    bytes_read = data['bytes_read']

    #  write the binary from client
    with open(file_name, "wb") as file:
        file.write(bytes_read)


@sio.event
def merge_file(sid, data):

    total_chunk = data['total_chunk']
    

    chunk = 0

    with open("ytCopy.jpg", "wb") as fileM:
        while chunk <= total_chunk:
            fileName = "chunk" + str(chunk) + ".txt"
            print(f' File is {isfile(fileName)}')

            with open(fileName, "rb") as fileTemp:
                byte = fileTemp.read(1024)
                fileM.write(byte)

                chunk += 1
    

        



if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

