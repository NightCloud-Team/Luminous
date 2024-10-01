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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QTextEdit, QWidget)

from qrc import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet(u"#centralwidget{border-image: url(:/001.jpg);}\n"
"")
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
        self.quickmenu = QPushButton(self.centralwidget)
        self.quickmenu.setObjectName(u"quickmenu")
        self.quickmenu.setGeometry(QRect(24, 36, 195, 100))
        sizePolicy.setHeightForWidth(self.quickmenu.sizePolicy().hasHeightForWidth())
        self.quickmenu.setSizePolicy(sizePolicy)
        self.quickmenu.setMinimumSize(QSize(195, 100))
        self.quickmenu.setMaximumSize(QSize(195, 100))
        self.quickmenu.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
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
        self.widget = QStackedWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(24, 173, 975, 390))
        self.widget.setStyleSheet(u"#settings_widget{background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;  \n"
"}")
        self.widget.setFrameShadow(QFrame.Sunken)
        self.quickmenu_widget = QWidget()
        self.quickmenu_widget.setObjectName(u"quickmenu_widget")
        self.quickmenu_widget.setStyleSheet(u"#quickmenu_widget{background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;  \n"
"}")
        self.lineEdit = QLineEdit(self.quickmenu_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 338, 822, 40))
        self.lineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border: none;\n"
"padding: 0;\n"
"border-radius: 10px;  ")
        self.submit = QPushButton(self.quickmenu_widget)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(863, 338, 95, 40))
        self.submit.setStyleSheet(u"border-radius: 10px;  \n"
"background-color: rgb(0, 0, 0);\n"
"color: white")
        self.widget.addWidget(self.quickmenu_widget)
        self.learn_widget = QWidget()
        self.learn_widget.setObjectName(u"learn_widget")
        self.learn_widget.setStyleSheet(u"#learn_widget{background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;  \n"
"}")
        self.frame = QFrame(self.learn_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(487, -1, 1, 390))
        self.frame.setStyleSheet(u"color: gray; background-color: gray; max-width: 0.5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.normal = QPushButton(self.learn_widget)
        self.normal.setObjectName(u"normal")
        self.normal.setGeometry(QRect(180, 46, 140, 40))
        self.normal.setStyleSheet(u"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"background-color: rgb(22, 155, 213);\n"
"border: none;\n"
"padding: 0;\n"
"")
        self.normal_2 = QPushButton(self.learn_widget)
        self.normal_2.setObjectName(u"normal_2")
        self.normal_2.setGeometry(QRect(180, 155, 140, 40))
        self.normal_2.setStyleSheet(u"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"background-color: rgb(22, 155, 213);\n"
"border: none;\n"
"padding: 0;\n"
"")
        self.comboBox = QComboBox(self.learn_widget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 210, 140, 42))
        self.comboBox.setStyleSheet(u"")
        self.normal_3 = QPushButton(self.learn_widget)
        self.normal_3.setObjectName(u"normal_3")
        self.normal_3.setGeometry(QRect(700, 46, 140, 40))
        self.normal_3.setStyleSheet(u"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"background-color: rgb(22, 155, 213);\n"
"border: none;\n"
"padding: 0;\n"
"")
        self.normal_4 = QPushButton(self.learn_widget)
        self.normal_4.setObjectName(u"normal_4")
        self.normal_4.setGeometry(QRect(700, 155, 140, 40))
        self.normal_4.setStyleSheet(u"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"background-color: rgb(22, 155, 213);\n"
"border: none;\n"
"padding: 0;\n"
"")
        self.comboBox_2 = QComboBox(self.learn_widget)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(700, 210, 140, 42))
        self.comboBox_2.setStyleSheet(u"")
        self.widget.addWidget(self.learn_widget)
        self.download_widget = QWidget()
        self.download_widget.setObjectName(u"download_widget")
        self.download_widget.setStyleSheet(u"#download_widget{background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;  \n"
"}\n"
"#scrollArea{background-color: rgba(255, 255, 255, 0);}")
        self.scrollArea = QScrollArea(self.download_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 975, 390))
        self.scrollArea.setSizeIncrement(QSize(0, 0))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 956, 100000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 100000))
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents{background-color: rgba(255, 255, 255, 0);}")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget.addWidget(self.download_widget)
        self.settings_widget = QWidget()
        self.settings_widget.setObjectName(u"settings_widget")
        self.settings_widget.setStyleSheet(u"#settings_widget{background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;  \n"
"}")
        self.stackedWidget = QStackedWidget(self.settings_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(195, 0, 780, 390))
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"#page{\n"
"background-color: rgba(255, 255, 255, 127);\n"
"border: none;\n"
"padding: 0;}")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"#page_2{\n"
"	background-color: rgba(255, 255, 255, 0);}")
        self.stackedWidget.addWidget(self.page_2)
        self.quickmenu_2 = QPushButton(self.settings_widget)
        self.quickmenu_2.setObjectName(u"quickmenu_2")
        self.quickmenu_2.setGeometry(QRect(0, 0, 195, 100))
        sizePolicy.setHeightForWidth(self.quickmenu_2.sizePolicy().hasHeightForWidth())
        self.quickmenu_2.setSizePolicy(sizePolicy)
        self.quickmenu_2.setMinimumSize(QSize(195, 100))
        self.quickmenu_2.setMaximumSize(QSize(195, 100))
        self.quickmenu_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border-top-left-radius: 20px;  \n"
"\n"
"border: none;\n"
"padding: 0;\n"
"border-right: 1px solid grey;\n"
"")
        self.quickmenu_3 = QPushButton(self.settings_widget)
        self.quickmenu_3.setObjectName(u"quickmenu_3")
        self.quickmenu_3.setGeometry(QRect(0, 100, 195, 100))
        sizePolicy.setHeightForWidth(self.quickmenu_3.sizePolicy().hasHeightForWidth())
        self.quickmenu_3.setSizePolicy(sizePolicy)
        self.quickmenu_3.setMinimumSize(QSize(195, 100))
        self.quickmenu_3.setMaximumSize(QSize(195, 100))
        self.quickmenu_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border: none;\n"
"padding: 0;\n"
"border-right: 1px solid grey;\n"
"border-top: 1px solid grey;\n"
"")
        self.widget.addWidget(self.settings_widget)
        self.about_widget = QWidget()
        self.about_widget.setObjectName(u"about_widget")
        self.about_widget.setStyleSheet(u"#about_widget{background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;  \n"
"}")
        self.textEdit = QTextEdit(self.about_widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 975, 390))
        self.textEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.widget.addWidget(self.about_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.learn.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u4e60", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.quickmenu.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u6377\u83dc\u5355", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684\u9700\u6c42", None))
        self.submit.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.normal.setText(QCoreApplication.translate("MainWindow", u"\u666e\u901a\u6a21\u5f0f", None))
        self.normal_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u7ae0", None))

        self.normal_3.setText(QCoreApplication.translate("MainWindow", u"\u5267\u60c5\u6a21\u5f0f", None))
        self.normal_4.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u7ae0", None))

        self.quickmenu_2.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u6377\u83dc\u5355", None))
        self.quickmenu_3.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u6377\u83dc\u5355", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">ui\u5236\u4f5c\uff1asudoxue\uff0c\u96f7\u77f3\u4e1c</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u56fe\u6807\u8bbe\u8ba1\uff1a</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">ui\u8bbe\u8ba1\uff1a\u96f7\u77f3\u4e1c\uff0csudoxue</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u529f\u80fd\u5b9e\u73b0\uff1a\u96f7\u77f3\u4e1c</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u4ee3\u7801\u6d4b\u8bd5\uff1asudoxue\uff0c\u96f7\u77f3\u4e1c</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u6280\u672f\u652f\u6301\uff1a\u96f7\u77f3\u4e1c\uff0csudoxue</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u529f\u80fd\u8bbe\u8ba1\uff1a\u96f7\u77f3\u4e1c</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u5fae\u5149\u5b98\u7f51</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u5fae\u5149\u5ba3\u4f20\u7247</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u5fae\u5149\u4e3b\u9875\uff08\u5fae\u535a\uff09</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u5fae\u5149\u4e3b\u9875\uff08b\u7ad9\uff09</span></p>\n"
"<p align=\"ce"
                        "nter\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>", None))
    # retranslateUi

