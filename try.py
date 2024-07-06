import ctypes
from ctypes import wintypes

# 定义常量
ABM_GETSTATE = 0x00000004  # 获取任务栏状态的消息
ABS_AUTOHIDE = 0x1         # 自动隐藏状态

# 定义APPBARDATA结构体
APPBARDATA = ctypes.Structure
APPBARDATA._fields_ = [
    ("cbSize", wintypes.DWORD),
    ("hWnd", wintypes.HWND),
    ("uCallbackMessage", wintypes.UINT),
    ("uEdge", wintypes.UINT),
    ("rc", wintypes.RECT),
    ("lParam", wintypes.LPARAM)
]

# 创建APPBARDATA实例
app_bar_data = APPBARDATA()
app_bar_data.cbSize = ctypes.sizeof(APPBARDATA)

# 调用SHAppBarMessage获取任务栏状态
result = ctypes.windll.shell32.SHAppBarMessage(ABM_GETSTATE, ctypes.byref(app_bar_data))
if result & ABS_AUTOHIDE:
    print("任务栏在桌面模式下自动隐藏已启用。")
else:
    print("任务栏在桌面模式下自动隐藏已禁用。")
