# main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from uis.luminous_ui import Ui_MainWindow
#from uis.luminous_ui import Ui_MainWindow   # 导入你自动生成的 UI 文件

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #self.ui = Ui_MainWindow()
        self.setupUi(self) # 调用自动生成的 UI 设置函数
        self.setup_connections()

    def setup_connections(self):
        # 设置按钮切换 QStackedWidget 的页面
        self.quickmunu.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.learn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.download.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.settings.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.about.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        # 添加更多的信号槽连接

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()  # 创建主窗口对象
    window.show()  # 显示窗口
    sys.exit(app.exec())
