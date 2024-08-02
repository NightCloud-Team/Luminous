import flask
import os
import ctypes
from flask import Flask, redirect, url_for,request
from ctypes import wintypes
import winreg
import subprocess
from function.system import *
from flask_caching import Cache

app = flask.Flask(__name__)

app.config['CACHE_TYPE'] = 'filesystem'
app.config['CACHE_DIR'] = './tmp/flask_cache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # 设置默认超时时间为300秒

# 初始化缓存
cache = Cache(app)

@app.route('/')
def index():
    return flask.render_template('quickmenu.html')#




@app.route('/shortcut_menu')
@cache.cached(timeout=60)
def shortcut_menu():
    return flask.render_template('quickmenu.html')#




@app.route('/shortcut_menu/select_personalization')
@cache.cached(timeout=60)
def select_personalization():
    return flask.render_template('quickmenu_personalization.html')#




@app.route('/shortcut_menu/select_personalization/wallpaper')
@cache.cached(timeout=60)
def wallpaper():
    return flask.render_template('wallpaper.html')#




@app.route('/shortcut_menu/select_personalization/wallpaper_upload',methods=['POST'])
def wallpaper_upload():
    if 'file' not in request.files:
        return redirect(url_for('error',error='没有上传文件'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('error',error='没有上传文件'))
    file.save('./picture/wallpaper.jpg')
    image_path = os.path.abspath("./picture/wallpaper.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    return flask.render_template('success.html')#




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



@app.route('/clean')
def clean():
    cache.clear()
    return "关闭"




#app.run(host='127.0.0.1', port=8000,debug=True)
app.run(host='127.0.0.1', port=8000)