import socketio
import uvicorn

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio)



@sio.event
def connect(sid, message):
    print(f'connected')

@sio.event
def disconnect(sid, message):
    print(f'disconnected')

@sio.event
async def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    return {'result': result}

# @sio.event
# async def file(sid, data):
#     print(f'file from server invoked')
    

#     file_size = data['file_size']
#     file_name = data['file_name']
    

#     with open("./rec/" + file_name, "wb") as file:
#         c = 0

#         while c <= int(file_size):
#             print(c)
#             file_data = data['data'] 
#             print(f'File data len: {len(file_data)}')
#             if not file_data:
#                 print('finished')
#                 break
            
#             file.write(file_data)
#             c += len(file_data)

@sio.event
def message(sid, data):
    file_size = data['file_size']
    file_name = data['file_name']
    

    with open("./rec/" + file_name, "wb") as file:

        file_data = data['data'] 
        print(f'File data len: {len(file_data)}')

        file.write(file_data)




if __name__ == "__main__":
    uvicorn.run(app)

