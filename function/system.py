
import ctypes
import sys
from ctypes import wintypes
import psutil#引用库
import subprocess
import win32gui
import win32con

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
def close(port):
    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        try:
            # 检查进程的所有连接
            for conn in proc.connections(kind='inet'):
                if conn.laddr.port == port:
                    print(f"终止 {proc.info['pid']} 使用 {port}")
                    proc.terminate()
                    proc.wait(timeout=3)
                    print(f"结束: {proc.info['pid']}")
                    return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    print(f"找不到 {port}")

def windows_fix_web():
    subprocess.run(["msdt", "/id", "NetworkDiagnosticsNetworkAdapter"], check=True)

def open_file():
    flags = win32con.OFN_FILEMUSTEXIST | win32con.OFN_HIDEREADONLY
    file_dialog = win32gui.GetOpenFileNameW(InitialDir='C:\\', Flags=flags)
    return file_dialog[0]

def install():
    if ctypes.windll.shell32.IsUserAnAdmin() != 0:
        result = subprocess.run(["powershell Install-Module -Name PSReadLine -Force -SkipPublisherCheck"])
        print(result.stdout)
        # 如果已经是管理员，直接运行
    else:
        # 如果不是管理员，使用ShellExecute以管理员权限重新运行
        params = ' '.join([sys.executable] + sys.argv)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    #subprocess.run(["runas" , "/user:Administrator" , "'powershell Install-Module -Name PSReadLine -Force -SkipPublisherCheck'"])demo.sln