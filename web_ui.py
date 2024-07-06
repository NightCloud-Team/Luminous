import flask
from flask import Flask, redirect, url_for

app = flask.Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('shortcut_menu'))

@app.route('/shortcut_menu')
def shortcut_menu():
    return flask.render_template('index.html')

@app.route('/shortcut_menu/select_personalization')
def select_personalization():
    return flask.render_template('index_personalization.html')

@app.route('/shortcut_menu/select_system')
def select_system():
    return flask.render_template('index_system.html')

@app.route('/shortcut_menu/internet')
def internet():
    #功能待实现-显示\检测当前网络连接情况
    return flask.render_template('index_internet.html')

@app.route('/software')
def software():
    return flask.render_template('software.html')

@app.route('/SpecialThanks')
def SpecialThanks():
    return flask.render_template('SpecialThanks.html')


@app.route('/website')
def website():
    return flask.render_template('website.html')


app.run(host='127.0.0.1', port=8000,debug=True)
