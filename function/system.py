
import ctypes
import sys
from ctypes import wintypes

ABM_GETSTATE = 0x00000004  # 获取任务栏状态的消息
ABS_AUTOHIDE = 0x1         # 自动隐藏状态

# 定义APPBARDATA结构体
class APPBARDATA(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.DWORD),
        ("hWnd", wintypes.HWND),
        ("uCallbackMessage", wintypes.UINT),
        ("uEdge", wintypes.UINT),
        ("rc", wintypes.RECT),
        ("lParam", wintypes.LPARAM)
    ]

# 检查任务栏是否自动隐藏
def is_taskbar_auto_hide_enabled():
    app_bar_data = APPBARDATA()
    app_bar_data.cbSize = ctypes.sizeof(APPBARDATA)

    # 调用SHAppBarMessage获取任务栏状态
    result = ctypes.windll.shell32.SHAppBarMessage(ABM_GETSTATE, ctypes.byref(app_bar_data))
    if result & ABS_AUTOHIDE:
        print("任务栏在桌面模式下自动隐藏已启用。")
        return True
    else:
        print("任务栏在桌面模式下自动隐藏已禁用。")
        return False


def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin() != 0:
        # 如果已经是管理员，直接运行
        print("已经以管理员权限运行。")
        return True
    else:
        # 如果不是管理员，使用ShellExecute以管理员权限重新运行
        params = ' '.join([sys.executable] + sys.argv)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        return False