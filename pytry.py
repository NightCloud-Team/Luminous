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