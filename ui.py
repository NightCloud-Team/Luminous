import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,high,width):
        super().__init__()

        self.setWindowTitle("微光")
        self.setFixedSize(high, width)
        self.setWindowIcon(QIcon("luminous_logo.png"))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(1280,720)
    window.show()
    sys.exit(app.exec())
