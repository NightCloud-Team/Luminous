import sys
import subprocess
import pathlib
import threading
import os
import signal
import atexit
from function.system import *
import urllib.request
import flask
import ctypes
from ctypes import wintypes
import winreg

print("开始快捷教程创建")
name = input("输入教程名称:")

while True: