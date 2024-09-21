# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'luminous.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)
from qrc import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet(u"#centralwidget{border-image: url(:/001.jpg);}")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.learn = QPushButton(self.centralwidget)
        self.learn.setObjectName(u"learn")
        self.learn.setGeometry(QRect(219, 36, 195, 100))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.learn.sizePolicy().hasHeightForWidth())
        self.learn.setSizePolicy(sizePolicy)
        self.learn.setMinimumSize(QSize(195, 100))
        self.learn.setMaximumSize(QSize(195, 100))
        self.learn.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border: none;\n"
"padding: 0;\n"
"border-right: 1px solid grey;")
        self.download = QPushButton(self.centralwidget)
        self.download.setObjectName(u"download")
        self.download.setGeometry(QRect(414, 36, 195, 100))
        sizePolicy.setHeightForWidth(self.download.sizePolicy().hasHeightForWidth())
        self.download.setSizePolicy(sizePolicy)
        self.download.setMinimumSize(QSize(195, 100))
        self.download.setMaximumSize(QSize(195, 100))
        self.download.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border: none;\n"
"padding: 0;\n"
"border-right: 1px solid grey;")
        self.quickmunu = QPushButton(self.centralwidget)
        self.quickmunu.setObjectName(u"quickmunu")
        self.quickmunu.setGeometry(QRect(24, 36, 195, 100))
        sizePolicy.setHeightForWidth(self.quickmunu.sizePolicy().hasHeightForWidth())
        self.quickmunu.setSizePolicy(sizePolicy)
        self.quickmunu.setMinimumSize(QSize(195, 100))
        self.quickmunu.setMaximumSize(QSize(195, 100))
        self.quickmunu.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border-top-left-radius: 20px;  \n"
"border-bottom-left-radius: 20px;  \n"
"border: none;\n"
"padding: 0;\n"
"border-right: 1px solid grey;\n"
"")
        self.settings = QPushButton(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(609, 36, 195, 100))
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setMinimumSize(QSize(195, 100))
        self.settings.setMaximumSize(QSize(195, 100))
        self.settings.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border: none;\n"
"padding: 0;\n"
"border-right: 1px solid grey;")
        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(804, 36, 195, 100))
        sizePolicy.setHeightForWidth(self.about.sizePolicy().hasHeightForWidth())
        self.about.setSizePolicy(sizePolicy)
        self.about.setMinimumSize(QSize(195, 100))
        self.about.setMaximumSize(QSize(195, 100))
        self.about.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"border: none;\n"
"padding: 0;\n"
"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(24, 173, 975, 390))
        self.stackedWidget.setStyleSheet(u"QTabBar { height: 0px; }")
        self.stackedWidget.setFrameShadow(QFrame.Sunken)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setStyleSheet(u"#page1{background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;  \n"
"}")
        self.lineEdit = QLineEdit(self.page1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 338, 822, 40))
        self.lineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border: none;\n"
"padding: 0;\n"
"border-radius: 10px;  ")
        self.submit = QPushButton(self.page1)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(863, 338, 95, 40))
        self.submit.setStyleSheet(u"border-radius: 10px;  \n"
"background-color: rgb(0, 0, 0);\n"
"color: white")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.page2.setStyleSheet(u"#page2{background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;  \n"
"}")
        self.frame = QFrame(self.page2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(487, -1, 1, 390))
        self.frame.setStyleSheet(u"color: gray; background-color: gray; max-width: 0.5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.page2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.currentChanged.connect(self.quickmunu.click)
        self.stackedWidget.currentChanged.connect(self.learn.click)
        self.stackedWidget.currentChanged.connect(self.download.click)
        self.stackedWidget.currentChanged.connect(self.settings.click)
        self.stackedWidget.currentChanged.connect(self.about.click)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.learn.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u4e60", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.quickmunu.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u6377\u83dc\u5355", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684\u9700\u6c42", None))
        self.submit.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
    # retranslateUi

