# coding: utf-8
import SparkApi
import time
#以下密钥信息从控制台获取   https://console.xfyun.cn/services/bm35
appid = "91f141e6"
api_secret = "Y2I0YjMxNzc2MjUwYTFkMTM1OWM5NGQ4"
api_key ="a486bc27629c79308e2b06975ef46d41"
domain = "general"
Spark_url = "wss://spark-api.xf-yun.com/v1.1/chat"   # Max服务地址
#Spark_url = "wss://spark-api.xf-yun.com/v3.1/chat"  # Pro服务地址
#Spark_url = "wss://spark-api.xf-yun.com/v1.1/chat"  # Lite服务地址

#初始上下文内容，当前可传system、user、assistant 等角色
text =[
    # {"role": "system", "content": "你现在扮演李白，你豪情万丈，狂放不羁；接下来请用李白的口吻和用户对话。"} , # 设置对话背景或者模型角色
    # {"role": "user", "content": "你是谁"},  # 用户的历史问题
    # {"role": "assistant", "content": "....."} , # AI的历史回答结果
    # # ....... 省略的历史对话
    # {"role": "user", "content": "你会做什么"}  # 最新的一条问题，如无需上下文，可只传最新一条问题
]


def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text
    


if __name__ == '__main__':

    while(1):
        Input = input("\n" +"我:")
        question = checklen(getText("user",Input))
        SparkApi.answer =""
        print("星火:",end ="")
        SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
        print(SparkApi.answer)
        getText("assistant",SparkApi.answer)




