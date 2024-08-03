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
import paddleocr
from pywinauto import Application
from pywinauto import findwindows,Desktop
import win32gui

def window_front(window_title):
    try:
        # 查找具有指定标题的窗口
        window = findwindows.find_window(title=window_title)
        
        # 连接到应用程序
        app = Application().connect(handle=window)
        
        # 获取窗口对象
        window_object = app.window(handle=window)
        
        # 激活窗口
        window_object.set_focus()
        window_object.minimize()
        window_object.restore()
        
        print(f"窗口'{window_title}' 被选中")
    except Exception as e:
        print(f"错误: {e}")

def find_window():
    def enum_windows_callback(hwnd, window_titles):
    # 检查窗口是否可见或存在
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            # 获取窗口标题
            window_text = win32gui.GetWindowText(hwnd)
            if window_text:  # 仅添加非空标题的窗口
                window_titles.append(window_text)

    def list_all_windows():
        window_titles = []
        # 枚举所有顶级窗口
        win32gui.EnumWindows(enum_windows_callback, window_titles)
        print(window_titles)
        return window_titles
    windows = list_all_windows()
    for window in windows:
        print(f"Title: {window}")