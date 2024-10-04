
import ctypes
import sys
from ctypes import wintypes
import psutil#引用库
import subprocess
import win32gui
import win32con
import time
import pywifi
from pywifi import const

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
    for proc in psutil.process_iter(['pid', 'name']):  # 删除 'connections'
        try:
            # 通过 proc.connections() 获取连接信息
            for conn in proc.connections(kind='inet'):
                if conn.laddr.port == port:
                    print(f"终止进程 {proc.info['name']} (PID: {proc.info['pid']}) 占用端口 {port}")
                    proc.terminate()
                    try:
                        proc.wait(timeout=3)
                        print(f"成功结束进程 {proc.info['name']} (PID: {proc.info['pid']})")
                    except psutil.TimeoutExpired:
                        print(f"进程 {proc.info['name']} (PID: {proc.info['pid']}) 未能在超时时间内结束")
                    return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"无法处理进程 (PID: {proc.info.get('pid')}), 错误: {e}")
            continue
    print(f"找不到占用端口 {port} 的进程")

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

def memory():
    if ctypes.windll.shell32.IsUserAnAdmin() != 0:
        memory_s = psutil.virtual_memory()
        print(memory_s.available / (1024**3))
        pids = psutil.pids()
        for pid in pids:
            try:
                process = ctypes.windll.kernel32.OpenProcess(0x001F0FFF, False, pid)
                if process:
                        # Empty the working set of the process
                        ctypes.windll.psapi.EmptyWorkingSet(process)
                        ctypes.windll.kernel32.CloseHandle(process)
            except Exception as e:
                    print(f"Could not clear memory for process {pid}: {e}")
        memory_s = psutil.virtual_memory()
        print(memory_s.available / (1024**3))
        # 如果已经是管理员，直接运行
    else:
        # 如果不是管理员，使用ShellExecute以管理员权限重新运行
        params = ' '.join([sys.executable] + sys.argv)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
   
def connect_wifi(name,password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    # 断开当前连接
    iface.disconnect()
    time.sleep(1)  # 等待断开
    
    # 检查是否成功断开
    if iface.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = name  # 设置Wi-Fi名称
        profile.key = password  # 设置Wi-Fi密码
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        
        iface.remove_all_network_profiles()  # 删除所有配置
        tmp_profile = iface.add_network_profile(profile)  # 加载配置
        
        iface.connect(tmp_profile)  # 连接
        time.sleep(10)  # 等待连接
        
        if iface.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        return False
    
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

def mouse():
    subprocess.run(['control.exe', 'main.cpl,,4'])