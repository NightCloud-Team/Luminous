def download (lines):
    import webbrowser
    #用户点击某软件的下载按钮后，由ui返回一个值，值的大小对应着Download_list.Download_list里的第多少行，返回的值应储存在message.message的第一行
    download_list = ["https://www.microsoft.com/zh-cn/edge/download?form=MA13FJ",
                     "https://www.google.cn/chrome/",
                     "http://www.firefox.com.cn/",
                     "https://pc.weixin.qq.com/",
                     "https://page.dingtalk.com/wow/z/dingtalk/simple/ddhomedownlaod#/"]
    url = download_list[int(lines)]
    webbrowser.open(url, new=0, autoraise=True)
def set (cpls,number):
    import subprocess
    cpl_list = ["desk.cpl",
                "main.cpl",
                "appwiz.cpl",
                "bthprops.cpl",
                "firewall.cpl",
                "hdwwiz.cpl",
                "mmsys.cpl",]
    if number == "none":
        cpl = cpl_list[int(cpls)]
    else:
        number = str(number)
        cpl = cpl_list[int(cpls)] + ",," + number
    subprocess.run(['control.exe',cpl])
    #subprocess.run(['control.exe', 'desk.cpl,,0'])
    #1为屏幕保护程序，2为个性化,3为系统，4不明（系统，5为桌面图标设置，67不明（桌面图标设置
    #subprocess.run(['control.exe', 'main.cpl,,4'])
    #这是关于鼠标的设置
    #subprocess.run(['control.exe', 'appwiz.cpl,,5'])
    #程序和功能（卸载,1不需要，2是windows程序和功能管理（可能会出现警告提示optionalfeatures.exe缺失但是点是之后正常查看，3为设置里的应用里的默认应用#
    #4及之后应该就没了
    #subprocess.run(['control.exe', 'bthprops.cpl'])
    #设置里的设备,1为蓝牙设置
    #subprocess.run(['control.exe', 'firewall.cpl'])
    #防火墙
    #subprocess.run(['control.exe', 'hdwwiz.cpl'])
    #设备管理器
    #subprocess.run(['control.exe', 'inetcpl.cpl'])
    #internet属性，用不着可以扔高级设置里
    #subprocess.run(['control.exe', 'intl.cpl'])
    #时间和区域格式，用不着可以扔高级设置
    #subprocess.run(['control.exe', 'irprops.cpl'])
    #经查阅资料为无线链接（相关方面设置可能），实际运行无效果，不排除机型原因
    #subprocess.run(['control.exe', 'joy.cpl'])
    #游戏控制器，卵用没有
    #subprocess.run(['control.exe', 'mmsys.cpl'])
    #声音设置,可能有用
    #subprocess.run(['control.exe', 'ncpa.cpl'])
    #网络连接，可能有用吧
    #subprocess.run(['control.exe', 'powercfg.cpl'])
    #电池/(电源？)设置,呃，可能有用
    #subprocess.run(['control.exe', 'sapi.cpl'])
    #居然没有这个东西的资料，怀疑是戴尔自己加进去的，不知道干啥用的，需要更多机型进行实验，感觉这玩意在骂我
    #subprocess.run(['control.exe', 'sysdm.cpl'])
    #系统属性，呃，不知道能干啥，可能有用吧
    #subprocess.run(['control.exe', 'TabletPC.cpl'])
    #笔和触控？？但是似乎我这台电脑运行会出错,好像需要识别电脑是否支持笔和触控，应该有用，但是不知道界面长啥样
    #subprocess.run(['control.exe', 'telephon.cpl'])
    #md拨号上网，这年头谁还拨号上网啊，暂且留着万一有人用呢
    #subprocess.run(['control.exe', 'timedate.cpl'])
    #日期和时间设置，可不能瞎改
    #subprocess.run(['control.exe', 'wscui.cpl'])
    #安全和维护？，不知道能干啥，先留着，可能有用
def tcp ():
    import socket
    TCPclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = '127.0.0.1'
    port = 65520
    ip_and_port = (ip, port)
    TCPclient.connect(ip_and_port)
    message = TCPclient.recv(1024)
    TCPclient.close()
    return message.decode('utf-8')