# main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from uis.luminous_ui import Ui_MainWindow
from function.system import *
#from uis.luminous_ui import Ui_MainWindow   # 导入你自动生成的 UI 文件

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #self.ui = Ui_MainWindow()
        self.setupUi(self) # 调用自动生成的 UI 设置函数
        self.setup_connections()
        self.button_function()
        self.checkBox.stateChanged.connect(self.change_image)
        self.page = 0

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
        else:
            self.checkBox.setStyleSheet(u"image: url(:/button.png);")
            self.page = 0
    def button_function(self):
        self.pushButton_43.clicked.connect(wallpaper_upload)#更改壁纸
        self.pushButton_44.clicked.connect(mouse)#鼠标设置
        self.pushButton_22.clicked.connect(windows_fix_web)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()  # 创建主窗口对象
    window.show()  # 显示窗口
    sys.exit(app.exec())
