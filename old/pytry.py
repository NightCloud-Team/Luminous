"""
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader

class LoginGui(object):

    def __init__(self):
        self.ui = QUiLoader().load('windows.ui')


if __name__ == '__main__':
    app = QApplication([])
    gui = LoginGui()
    gui.ui.show()
    app.exec_()
"""
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader

from windows import Ui_Dialog

# class LoginGui(object):
#     def __init__(self):
#         self.ui = QUiLoader().load('./demo/demo.ui')


class LoginGui(QMainWindow,Ui_Dialog):
    def __init__(self):
        super(LoginGui, self).__init__()   # 调用父类的初始化方法
        self.setupUi(self)                 #  调用Ui_MainWindow的setupUi方法布置界面



if __name__ == '__main__':
    app = QApplication([])
    gui = LoginGui()
    gui.show()
    app.exec_()