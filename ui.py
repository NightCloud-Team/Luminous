# main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from uis.luminous_ui import Ui_MainWindow
from uis.wifi_ui_ui import Ui_Form
from function.system import *
from function.functions import *
from pywifi import PyWiFi, const, Profile
import json

#from uis.luminous_ui import Ui_MainWindow   # 导入你自动生成的 UI 文件

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #self.ui = Ui_MainWindow()
        self.setupUi(self) # 调用自动生成的 UI 设置函数
        self.setup_connections()
        self.button_function()
        self.checkBox.stateChanged.connect(self.change_image)
        with open("./settings/software_settings.json","r") as self.pages:
            self.data = json.load(self.pages)
            if self.data["menu_quick_menu"]:
                self.page = 5
                self.checkBox.setStyleSheet(u"image: url(:/button_1.png);")
                self.widget.setCurrentIndex(5)
            else:
                self.page = 0
                self.checkBox.setStyleSheet(u"image: url(:/button.png);")
                self.widget.setCurrentIndex(0)

    def setup_connections(self):
        # 设置按钮切换 QStackedWidget 的页面
        self.quickmenu.clicked.connect(lambda: self.widget.setCurrentIndex(self.page))
        self.learn.clicked.connect(lambda: self.widget.setCurrentIndex(1))
        self.download.clicked.connect(lambda: self.widget.setCurrentIndex(2))
        self.settings.clicked.connect(lambda: self.widget.setCurrentIndex(3))
        self.about.clicked.connect(lambda: self.widget.setCurrentIndex(4))
        self.settings_software_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.settings_system_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        # 添加更多的信号槽连接
    def change_image(self):
        if self.checkBox.isChecked():
            self.checkBox.setStyleSheet(u"image: url(:/button_1.png);")
            self.page = 5  # 选中时的图片
            self.data["menu_quick_menu"] = True
            with open("./settings/software_settings.json","w") as self.pages:
                json.dump(self.data, self.pages, indent=4)
        else:
            self.checkBox.setStyleSheet(u"image: url(:/button.png);")
            self.page = 0
            self.data["menu_quick_menu"] = False
            with open("./settings/software_settings.json","w") as self.pages:
                json.dump(self.data, self.pages, indent=4)
    def button_function(self):
        self.pushButton_43.clicked.connect(wallpaper_upload)#更改壁纸
        self.pushButton_44.clicked.connect(mouse)#鼠标设置
        self.pushButton_22.clicked.connect(windows_fix_web)
        self.pushButton_45.clicked.connect(self.wifi_window)
    def wifi_window(self):
        # app_1 = QApplication(sys.argv)
        self.windows = wifi_window()
        #windows.setupUi(self)
        self.windows.show()
        # sys.exit(app_1.exec())
class wifi_window(QWidget,Ui_Form):
    def __init__(self):
        super(wifi_window,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("wifi")
        self.button_function()
        #self.wifi()
        self.ui.progressBar.setValue(0)
    def wifi(self):
        times = 5
        wifi_names = []
        #self.button_function()
        for i in range(times):
            wifi_networks = get_wifi_list()
            for names in wifi_networks:
                wifi_names.append(names)
            self.ui.progressBar.setValue((i+1)*(100/times))
        lists = remove_duplicates_but_keep_specific(wifi_names,"")
        print(lists)
        lists = [item for item in lists if item != ""]
        print(lists)
        for wifi in lists:
            #name = ''.join(f'\\u{ord(c):04x}' for c in wifi)
            self.ui.comboBox.addItem(wifi)
    # def refresh(self):
    #     wifi_networks = get_wifi_list()
    #     for wifi in wifi_networks:
    #         #name = ''.join(f'\\u{ord(c):04x}' for c in wifi)
    #         self.ui.comboBox.addItem(wifi)
    def button_function(self):
        self.ui.pushButton.clicked.connect(self.wifi)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()  # 创建主窗口对象
    window.show()  # 显示窗口
    sys.exit(app.exec())
