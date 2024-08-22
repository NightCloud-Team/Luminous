import websocket
import websockets
import asyncio
import json
import paddlehub
from function import SparkApi
from function.SparkApi import *
from LAC import LAC
lac = LAC(mode='lac')
#                                对话式快捷菜单     修改系统设置     加载完成   传回信息
#responce_json = {"founction": "    chat   " / "   system  " / "  load  ","message":[]}
ip = "127.0.0.1"
port = "8888"

appid = "91f141e6"
api_secret = "Y2I0YjMxNzc2MjUwYTFkMTM1OWM5NGQ4"
api_key ="a486bc27629c79308e2b06975ef46d41"
domain = "general"
Spark_url = "wss://spark-api.xf-yun.com/v1.1/chat"
text = []

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
    if responce["founction"] == "chat":
        spark_answer = await answer(responce["message"][0])
        websocket.send({"founction" : "answer","message":[spark_answer]})
    elif responce["founction"] == "system":
        pass


async def answer(question):
    question_out = checklen(getText("user",question))
    SparkApi.answer =""
    SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question_out)
    text.append(question_out[0])
    text.append({"role": "assistant", "content": SparkApi.answer})
    return SparkApi.answer

async def systen():
    pass


if "main" == __name__:
    load_complete()
    server = websocket.WebSocketServer(receive_message, ip, port)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
