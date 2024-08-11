# from openai import OpenAI
# client = OpenAI(
# 				# 控制台获取key和secret拼接，假使APIKey是key123456，APISecret是secret123456
#         api_key="a486bc27629c79308e2b06975ef46d41:Y2I0YjMxNzc2MjUwYTFkMTM1OWM5NGQ4", 
#         base_url = 'https://spark-api-open.xf-yun.com/v1' # 指向讯飞星火的请求地址
#     )
# completion = client.chat.completions.create(
#     model='general', # 指定请求的版本
#     messages=[
#         {
#             "role": "user",
#             "content": '你是谁'
#         }
#     ]
# )
# print(completion.choices[0].message)



import _thread as thread
import base64
import datetime
import hashlib
import hmac
import json
import time
from urllib.parse import urlparse
import ssl
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time
import json
import requests



# import json
# import http.client
# import requests

# obj = {
#         "text": 高兴,
#         "lang": "zh",
#         "relation": "synonym_of",
#         "k": 10
# }
# r = requests.post(url="https://texsmart.qq.com/api/text_graph", json= obj)
# print(r.text)

def text(texts):#分词
    obj = {"str": texts}
    req_str = json.dumps(obj).encode()
    url = "https://texsmart.qq.com/api"
    r = requests.post(url, data=req_str)
    r.encoding = "utf-8"
    result = json.loads(r.text)
    print(result)
    return result
    #print(json.loads(r.text))

def text_graph(text):#返回同义词
    # "text": 高兴,
    #     "lang": "zh",
    #     "relation": "synonym_of",
    #     "k": 10返回数量

    obj ={
        "text": text,
        "lang": "zh",
        "relation": "synonym_of",
        "k": 100
    }
    r = requests.post(url="https://texsmart.qq.com/api/text_graph", json= obj)
    r.encoding = "utf-8"
    result = json.loads(r.text)
    print(result)
    return result

def text_process(texts):
    VV_word = []
    NN_word = []
    result = text(texts)
    process = result["phrase_list"]
    print(process)
    for process_1 in process:
        if process_1["tag"] == "VV":
            VV_word.append(process_1["str"])
        elif process_1["tag"] == "NN":
            NN_word.append(process_1["str"])
    result_VV = " ".join(VV_word)
    result_NN = " ".join(NN_word)
    print("主意图:" + result_VV + result_NN)

