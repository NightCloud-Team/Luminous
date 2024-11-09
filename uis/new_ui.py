# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget = QStackedWidget(MainWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 1024, 600))
        self.stackedWidget.setStyleSheet(u"#settings_widget{\n"
"background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.quickmenu = QPushButton(self.page)
        self.quickmenu.setObjectName(u"quickmenu")
        self.quickmenu.setGeometry(QRect(0, 0, 250, 120))
        self.quickmenu.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 20px;")
        self.learn = QPushButton(self.page)
        self.learn.setObjectName(u"learn")
        self.learn.setGeometry(QRect(0, 120, 250, 120))
        self.learn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.about = QPushButton(self.page)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(0, 480, 250, 120))
        self.about.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 20px;")
        self.settings = QPushButton(self.page)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(0, 360, 250, 120))
        self.settings.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.download = QPushButton(self.page)
        self.download.setObjectName(u"download")
        self.download.setGeometry(QRect(0, 240, 250, 120))
        self.download.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.quickmenu.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u6377\u83dc\u5355", None))
        self.learn.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u4e60", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
    # retranslateUi

