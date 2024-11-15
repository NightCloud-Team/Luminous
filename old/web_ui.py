###########################################
#                                         #
#                                         #
#        ***已废弃请勿编写!!!***           #
#                                         #
#                                         #
###########################################









import flask
import os
import ctypes
from flask import Flask, redirect, url_for,request,jsonify
from ctypes import wintypes
import winreg
import subprocess
from function.system import *
from flask_caching import Cache
import threading
from function.SparkApi import *
from function import SparkApi
from function.AI import text_process
import importlib
import paddlehub as hub

compare_set = hub.Module(name='w2v_baidu_encyclopedia_target_word-ngram_1-2_dim300')
app = flask.Flask(__name__)

app.config['CACHE_TYPE'] = 'filesystem'
app.config['CACHE_DIR'] = './tmp/flask_cache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # 设置默认超时时间为300秒

# 初始化缓存
cache = Cache(app)


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(
#         app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon'
#     )

@app.route('/')
def index():
    #thread = threading.Thread(target=load)
    #thread.start()
    return flask.render_template('load_AI.html')#




@app.route('/shortcut_menu')
@cache.cached(timeout=60)
def shortcut_menu():
    return flask.render_template('quickmenu_AI.html')#




@app.route('/shortcut_menu/select_personalization')
@cache.cached(timeout=60)
def select_personalization():
    return flask.render_template('quickmenu_personalization.html')#




@app.route('/shortcut_menu/select_personalization/wallpaper')
@cache.cached(timeout=60)
def wallpaper():
    return flask.render_template('wallpaper.html')#









@app.route('/shortcut_menu/select_personalization/color')
@cache.cached(timeout=60)
def color():
    return flask.render_template('quickmenu_color.html')#




@app.route('/shortcut_menu/select_personalization/taskbar')
@cache.cached(timeout=60)
def taskbar():
    return flask.render_template('quickmenu_taskbar.html',toggle_checked_1=is_taskbar_auto_hide_enabled())#




@app.route('/shortcut_menu/select_personalization/taskbar_set',methods=['POST'])
@cache.cached(timeout=60)
def taskbar_set():
    option1 = request.form.get('option1')
    path_1 = os.path.abspath("./Turn_ON_auto-hide_taskbar.bat")
    path_2 = os.path.abspath("./Turn_OFF_auto-hide_taskbar.bat")
    print(path_1)
    print(path_2)
    if option1 == 'on':
        os.system(path_1)
    else:
        os.system(path_2)
    #print(value)
    return flask.render_template('success.html')#




@app.route('/shortcut_menu/select_system')
@cache.cached(timeout=60)
def select_system():
    return flask.render_template('quickmenu_system.html')#




@app.route('/shortcut_menu/internet')
@cache.cached(timeout=60)
def internet():
    #功能待实现-显示\检测当前网络连接情况
    return flask.render_template('quickmenu_internet.html')#




@app.route('/softwaresetting')
@cache.cached(timeout=60)
def softwaresetting():
    return flask.render_template('softwaresetting.html')#




@app.route('/SpecialThanks')
@cache.cached(timeout=60)
def SpecialThanks():
    return flask.render_template('SpecialThanks.html')#




@app.route('/learn')
@cache.cached(timeout=60)
def learn():
    return flask.render_template('learn.html')#




@app.route('/systemsetting')
@cache.cached(timeout=60)
def systemsetting():
    return flask.render_template('systemsetting.html')#




@app.route('/error/<error>')
def error(error):
    return flask.render_template('error.html',error=error)








######################################################
#====================================================#
#                      功 能 区                       #
#====================================================#
######################################################

@app.route('/fix_web')
def fix_web():
    thread = threading.Thread(target=windows_fix_web)
    thread.start()
    return flask.render_template('custom.html',custom = "按照提示完成检测")#



    # web_error = []


    # result = subprocess.run(['netsh', 'interface', 'show', 'interface'], capture_output=True, text=True)
    # adapters = []
    # for line in result.stdout.splitlines():
    #     if "已连接" in line or "已断开" in line:
    #         parts = line.split()
    #         adapter_status = parts[-1]
    #         adapter_name = " ".join(parts[3:-1])
    #         adapters.append((adapter_name, adapter_status))
        
    #     else:
    #         web_error.append
    # yield jsonify({"status": "task1_completed"}), '\n'

    # pass
    # yield jsonify({"status": "task1_completed"}), '\n'
 
    # pass
    # yield jsonify({"status": "task1_completed"}), '\n'

    # pass
    # yield jsonify({"status": "task1_completed"}), '\n'

    # pass
    # yield jsonify({"status": "task1_completed"}), '\n'

    # pass
    # yield jsonify({"status": "task1_completed"}), '\n'

    # pass
    # yield jsonify({"status": "task1_completed"}), '\n'

    # pass
    # yield jsonify({"status": "task1_completed"}), '\n'

@app.route("/select_file",methods = ['post'])
def select_file():
    file = open_file()
    return file




@app.route('/shortcut_menu/select_personalization/wallpaper_upload',methods=['POST'])
def wallpaper_upload():
    # if 'file' not in request.files:
    #     return redirect(url_for('error',error='没有上传文件'))
    # file = request.files['file']
    # if file.filename == '':
    #     return redirect(url_for('error',error='没有上传文件'))
    # file.save('./picture/wallpaper.jpg')
    # image_path = os.path.abspath("./picture/wallpaper.jpg")
    image_path = open_file()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    return flask.render_template('success.html')#




@app.route("/chat", methods=["POST"])
def AI():
    # appid = "91f141e6"
    # api_secret = "Y2I0YjMxNzc2MjUwYTFkMTM1OWM5NGQ4"
    # api_key ="a486bc27629c79308e2b06975ef46d41"
    # domain = "general"
    # Spark_url = "wss://spark-api.xf-yun.com/v1.1/chat"
    # question = request.get_json()
    # print(question)
    # user_message = question.get('message')
    # text = [{"role": "system", "content": "你现在需要"}]
    # question = checklen(getText(text,"user",user_message))

    # SparkApi.answer =""
    # SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
    question = request.get_json()
    print(question)
    user_message = question.get('message')
    result = text_process(user_message)
    result_1 = "".join(result[1])
    print(result_1 + "1")
    for traverse in result[0]:
        print(traverse)
        if word_compare("设置",traverse):
            print(result_1)
            if result_1=="鼠标灵敏度":
                answer = result_1
                print(jsonify({'response': answer}))
                break





    #word_compare_NN = {}

    
    #answer = text_process(user_message)
    





    return jsonify({'response': answer})
        

@app.route('/clean')
def clean():
    cache.clear()
    return "关闭"




def word_compare(text_1,text_2):
    result_word = compare_set.cosine_sim(text_1, text_2)
    if result_word >= 0.1:
        return True
    else:
        return False

# def load():
#     global compare_set
#     hub = importlib.import_module('paddlehub')
#     compare_set = hub.Module(name='w2v_baidu_encyclopedia_target_word-ngram_1-2_dim300')



#app.run(host='127.0.0.1', port=8000,debug=True)
app.run(host='127.0.0.1', port=8000)