# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
# from PySide6.QtGui import QAction, QIcon
# from PySide6.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PySide6 Toolbar Example")
#         self.setGeometry(100, 100, 800, 600)

#         # 创建主布局
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         main_layout = QVBoxLayout(central_widget)

#         # 添加占位以使工具栏位于窗口的1/3处
#         spacer_top = QSpacerItem(20, int(self.height() / 3), QSizePolicy.Minimum, QSizePolicy.Expanding)
#         main_layout.addSpacerItem(spacer_top)

#         # 创建工具栏容器并设置为居中对齐
#         toolbar_container = QWidget()
#         toolbar_layout = QHBoxLayout(toolbar_container)
#         toolbar_layout.setAlignment(Qt.AlignCenter)

#         # 创建工具栏
#         toolbar = QToolBar("Main Toolbar")
#         toolbar.setMovable(False)
#         toolbar_layout.addWidget(toolbar)

#         main_layout.addWidget(toolbar_container)

#         # 添加底部占位
#         spacer_bottom = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
#         main_layout.addSpacerItem(spacer_bottom)

#         # 创建动作
#         new_action = QAction(QIcon("icons/new.png"), "New", self)
#         open_action = QAction(QIcon("icons/open.png"), "Open", self)
#         save_action = QAction(QIcon("icons/save.png"), "Save", self)
#         exit_action = QAction(QIcon("icons/exit.png"), "Exit", self)

#         # 将动作添加到工具栏
#         toolbar.addAction(new_action)
#         toolbar.addAction(open_action)
#         toolbar.addAction(save_action)
#         toolbar.addSeparator()  # 添加分隔符
#         toolbar.addAction(exit_action)

#         # 连接信号槽
#         exit_action.triggered.connect(self.close)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())





# # import psutil
# # import time
# # import ctypes
# # import sys
# # def run_as_admin():
# #     if ctypes.windll.shell32.IsUserAnAdmin() != 0:
# #         # 如果已经是管理员，直接运行
# #         print("已经以管理员权限运行。")
# #         return True
# #     else:
# #         # 如果不是管理员，使用ShellExecute以管理员权限重新运行
# #         params = ' '.join([sys.executable] + sys.argv)
# #         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
# # def close(port):
# #     for net in psutil.net_connections():
# #         if net.status == psutil.CONN_LISTEN and net.laddr.port == port:
# #             pid_s = net.pid
# #             process = psutil.Process(pid_s)
# #             name = process.name()
# #             print(name)
# #     pid = psutil.pids()#获取pid列表
# #     pids = 0#变量
# #     # try:#尝试 运行因为如果模拟器因为某些问题而提前关闭或无法启动这个代码内部的代码会报错产生错误导致这个程序的被引用的地方出现错误形成连锁反应（用途就是不报错
# #     while True:#遍历列表
# #         p = psutil.Process(pid[pids])#查看列表的第pids个pid信息
# #         if p.name() == name:#检查名称是否为模拟器进程
# #             p.kill()#结束进程
# #         pids = pids+1#如果这个变量增加到列表的上线之外就会报错而try保证了这件事不会发生
# #     # except:#如果try:内部 的程序执行失败就执行此代码内部的程序
# #     #     print(1)
# #     #     time.sleep(5)
# #     #     pass#跳过
# # run_as_admin()
# # close(8000) 

# # import psutil

# # def close(port):
# #     for proc in psutil.process_iter(['pid', 'name', 'connections']):
# #         try:
# #             # 检查进程的所有连接
# #             for conn in proc.connections(kind='inet'):
# #                 if conn.laddr.port == port:
# #                     print(f"终止 {proc.info['pid']} 使用 {port}")
# #                     proc.terminate()
# #                     proc.wait(timeout=3)
# #                     print(f"结束: {proc.info['pid']}")
# #                     return
# #         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
# #             continue
# #     print(f"找不到 {port}")

# # # 示例调用
# # close(8000)
# '''
# .button {
#     background-color: #128d09;
#     color: white;
#     width: 120px;
#     height: 45px;
#     border: 0;
#     font-size: 16px;
#     box-sizing: content-box;
#     text-align: center;
#     border-radius: 10px;
#     box-shadow: 0 5px #999;
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     transition: background-color 0.3s, transform 0.3s, box-shadow 0.3s;
#     margin: 0 25px;
# }

# .buttons {
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     margin-bottom: 20px;
# }

# .button:hover {
#     background-color: #3e8e41;
# }

# .button:active {
#     background-color: #3e8e41;
#     box-shadow: 0 5px #666;
#     transform: translateY(4px);
# }

# .button span {
#     cursor: pointer;
#     display: inline-block;
#     position: relative;
#     transition: 0.5s;
# }

# .button span:after {
#     content: '»';
#     position: absolute;
#     opacity: 0;
#     top: 0;
#     right: -20px;
#     transition: 0.5s;
# }

# .button:hover span {
#     padding-right: 25px;
# }

# .button:hover span:after {
#     opacity: 1;
#     right: 0;
# }


# .center {
#     text-align: center;
# }
# '''

#result = text_process("帮我更改鼠标灵敏度")
#设置检测
#from function.system import *
# #from function.AI import *
# import threading
# import paddlehub as hub
# import jieba.analyse
#embedding = hub.Module(name='w2v_baidu_encyclopedia_target_word-ngram_1-2_dim300')
#jieba = hub.Module(name="jieba_paddle")
#result_1 = jieba.textrank("请帮我更改鼠标灵敏度", topK=20, withWeight=False, allowPOS=('vn'))
#print(result_1)

# result = text_process("请帮我更改鼠标灵敏度")




# print(embedding.cosine_sim("设置", "滚"))
# print(embedding.dot("设置", "帮"))

# def load():
#     global compare_set
#     compare_set = hub.Module(name='w2v_baidu_encyclopedia_target_word-ngram_1-2_dim300')

# thread = threading.Thread(target=load)
# thread.start()
# thread.join()
# result_word = compare_set.cosine_sim("设置", "我")
# print(result_word)


# from LAC import LAC
# import paddlehub as hub
# compare_set = hub.Module(name='w2v_baidu_encyclopedia_target_word-ngram_1-2_dim300')
# lac = LAC(mode='lac')
# lac_result = lac.run("请帮我更改鼠标灵敏度为1")
# v_word = []
# n_word = []
# m_word = []
# for i in range(len(lac_result[1])):
#     result_set = compare_set.cosine_sim("设置", lac_result[0][i])
#     result_switch = compare_set.cosine_sim("关闭", lac_result[0][i])
#     if result_set >= 0.1:
#         pass
#     else:
#         pass
    # if lac_result[1][i] == "v":
    #     v_word.append(lac_result[0][i])
    #     # result_word = compare_set.cosine_sim("设置", lac_result[0][i])
    #     # if result_word >= 0.1:
    #     #     pass
    #     # else:
    #     #     pass
    # elif lac_result[1][i] == "n":
    #     n_word.append(lac_result[0][i])
    # elif lac_result[1][i] == "m":
    #     m_word.append(lac_result[0][i])
# import pygame
# import sys

# def create_spotlight():
#     pygame.init()
#     screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#     clock = pygame.time.Clock()
#     radius = 100

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()

#         # 获取鼠标位置
#         mouse_x, mouse_y = pygame.mouse.get_pos()

#         # 创建半透明黑色遮罩
#         overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
#         overlay.fill((0, 0, 0, 180))  # 半透明黑色

#         # 创建聚光灯效果
#         pygame.draw.circle(overlay, (0, 0, 0, 0), (mouse_x, mouse_y), radius)

#         # 绘制到屏幕
#         screen.fill((0, 0, 0))
#         screen.blit(overlay, (0, 0))
#         pygame.display.update()
#         clock.tick(60)

# create_spotlight()
# coding:utf-8
 
import pywifi
from pywifi import const
import time
# ssid = []
# wifi = pywifi.PyWiFi()
# iface = wifi.interfaces()[0]
# iface.disconnect()
# time.sleep(1)
# assert iface.status() in\
#     [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
 
# print("^_^ 开始扫描附近wifi...")
# iface.scan()
 
# scanres = iface.scan_results()
# nums = len(scanres)
# print("数量: %s"%(nums))
# print ("| %s |  %s |  %s | %s"%("WIFIID","SSID","BSSID","signal"))
# for index,wifi_info in enumerate(scanres):
#     print("| %s | %s | %s | %s \n"%(index, wifi_info.ssid, wifi_info.bssid, wifi_info.signal))
#     ssid.append(wifi_info.ssid)
# saved_profiles = iface.network_profiles()
# for profile in saved_profiles:
#     if profile.ssid in ssid:
#         iface.connect(profile)
#         time.sleep(5)
#         if iface.status() == const.IFACE_CONNECTED:
#             print("1")
def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    # 断开连接
    iface.disconnect()
    time.sleep(1)
    
    # 确保设备处于断开或空闲状态
    while iface.status() not in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        time.sleep(1)
    
    print("^_^ 开始扫描附近的 Wi-Fi...")
    
    # 触发 Wi-Fi 扫描
    iface.scan()
    time.sleep(5)  # 扫描时间
    
    # 获取扫描结果
    scan_results = iface.scan_results()
    print("发现的 Wi-Fi 数量: %s" % len(scan_results))
    
    for wifi_info in scan_results:
        print("SSID: %s, 信号强度: %s" % (wifi_info.ssid, wifi_info.signal))
for attempt in range(3):
    print(f"第 {attempt + 1} 次扫描...")
    scan_wifi()