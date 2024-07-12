# import psutil
# import time
# import ctypes
# import sys
# def run_as_admin():
#     if ctypes.windll.shell32.IsUserAnAdmin() != 0:
#         # 如果已经是管理员，直接运行
#         print("已经以管理员权限运行。")
#         return True
#     else:
#         # 如果不是管理员，使用ShellExecute以管理员权限重新运行
#         params = ' '.join([sys.executable] + sys.argv)
#         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
# def close(port):
#     for net in psutil.net_connections():
#         if net.status == psutil.CONN_LISTEN and net.laddr.port == port:
#             pid_s = net.pid
#             process = psutil.Process(pid_s)
#             name = process.name()
#             print(name)
#     pid = psutil.pids()#获取pid列表
#     pids = 0#变量
#     # try:#尝试 运行因为如果模拟器因为某些问题而提前关闭或无法启动这个代码内部的代码会报错产生错误导致这个程序的被引用的地方出现错误形成连锁反应（用途就是不报错
#     while True:#遍历列表
#         p = psutil.Process(pid[pids])#查看列表的第pids个pid信息
#         if p.name() == name:#检查名称是否为模拟器进程
#             p.kill()#结束进程
#         pids = pids+1#如果这个变量增加到列表的上线之外就会报错而try保证了这件事不会发生
#     # except:#如果try:内部 的程序执行失败就执行此代码内部的程序
#     #     print(1)
#     #     time.sleep(5)
#     #     pass#跳过
# run_as_admin()
# close(8000) 

import psutil

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

# 示例调用
close(8000)

