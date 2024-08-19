import websocket
import websockets
import asyncio
import json
import paddlehub
from LAC import LAC
lac = LAC(mode='lac')
#                                对话式快捷菜单     修改系统设置     加载完成   传回信息
#responce_json = {"founction": "    answer   " / "   system  " / "  load  ","message":[]}
ip = "127.0.0.1"
port = "8888"

def load_complete():
    ips = ip + ":" + port
    loading = websockets.connect("ws://" + ips)
    message = {"founction" : "load","message":["load-complete!"]}
    message_json = json.dumps(message)
    while True:
        input_text = input(message_json)
        loading.send(input_text)
        responce_json = loading .recv()
        responce = json.loads(responce_json)
        if responce["founction"] == "load" and responce["message"][0] == "load-complete!":
            break


async def receive_message(websocket,path):
    responce_json = await websocket.recv()
    responce = json.loads(responce_json)
    if responce["founction"] == "answer":
        await answer(responce["message"][0])


async def answer(question):
    lac_result = lac.run(question)
    
    pass




if "main" == __name__:
    load_complete()
    server = websocket.WebSocketServer(receive_message, ip, port)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
