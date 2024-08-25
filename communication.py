import ctypes

import websocket
import websockets
import asyncio
import json
import paddlehub
from function import SparkApi
from function.SparkApi import *
#from LAC import LAC
import ctypes
from function.system import *
import os

#lac = LAC(mode='lac')
#                                对话式快捷菜单     修改系统设置     加载完成   传回信息
#response_json = {"function": "    chat   " / "   system  " / "  load  ","message":[]}
#{"function" : "system","message" : ["",""]}

#from LAC import LAC
#lac = LAC(mode='lac')
#                                对话式快捷菜单     修改系统设置     加载完成   传回信息
#response_json = {"function": "    chat   " / "   system  " / "  load  ","message":[]}
ip = "127.0.0.1"
port = "8888"

appid = "91f141e6"
api_secret = "Y2I0YjMxNzc2MjUwYTFkMTM1OWM5NGQ4"
api_key ="a486bc27629c79308e2b06975ef46d41"
domain = "general"
Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"
text = []

# def load_complete():
#     ips = ip + ":" + port
#     loading = websockets.connect("ws://" + ips)
#     message = {"function" : "load","message":["load-complete!"]}
#     message_json = json.dumps(message)
#     while True:
#         input_text = input(message_json)
#         loading.send(input_text)
#         response_json = loading .recv()
#         response = json.loads(response_json)
#         if response["function"] == "load" and response["message"][0] == "load-complete!":
#             break


async def receive_message(websocket,path):
    try:
        print("connect...")
        response_json = await websocket.recv()
        response = json.loads(response_json)
        if response["function"] == "chat":
            spark_answer = await answer(response["message"][0])
            websocket.send({"function" : "answer","message":[spark_answer]})
        elif response["function"] == "system":
            pass
        response_json = await websocket.recv()
        response = json.loads(response_json)
        if response["function"] == "chat":
            spark_answer = await answer(response["message"][0])
            websocket.send({"function" : "chatr","message":[spark_answer]})
        elif response["function"] == "system":
            response_system = await system(response["message"])
            websocket.send({"function" : "function","message":[response_system]})
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")
    except Exception as e:
        print(f"An error occurred: {e}")



async def answer(question):
    question_out = checklen(getText("user",question))
    SparkApi.answer =""
    SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question_out)
    text.append(question_out[0])
    text.append({"role": "assistant", "content": SparkApi.answer})
    return SparkApi.answer


async def system(function):
    if function[0] == "wallpaper":
        try:
            image_path = open_file()
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
            return True
        except:
            return False
    elif function[0] == "taskbar":
        try:
            if function[1] == True:
                os.path.abspath("./Turn_ON_auto-hide_taskbar.bat")
            elif function[1] == False:
                os.path.abspath("./Turn_OFF_auto-hide_taskbar.bat")
            else:
                return False
            return True
        except:
            return False


async def main():
    async with websockets.serve(receive_message, "localhost", 8888):
        print("loading...")
        await asyncio.Future()

asyncio.run(main())