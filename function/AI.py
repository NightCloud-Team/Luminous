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

def create_url(url,APISecret):
        host = urlparse(url).netloc
        path = urlparse(url).path
        # 生成RFC1123格式的时间戳
        now = datetime.now(url)
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + path + " HTTP/1.1"

        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'

        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # 拼接鉴权参数，生成url
        url = self.Spark_url + '?' + urlencode(v)
        # print(url)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        return url
