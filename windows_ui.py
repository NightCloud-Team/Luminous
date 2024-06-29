# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windows.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1115, 720)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1121, 721))
        self.tabWidget.setMaximumSize(QSize(1121, 16777215))
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.label = QLabel(self.tab_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 311, 41))
        self.label_2 = QLabel(self.tab_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 60, 291, 61))
        self.label_4 = QLabel(self.tab_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 150, 221, 51))
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.radioButton = QRadioButton(self.tab_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QRect(30, 10, 131, 19))
        self.radioButton.setCursor(QCursor(Qt.ArrowCursor))
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(True)
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setAutoExclusive(True)
        self.radioButton_2 = QRadioButton(self.tab_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(350, 10, 141, 19))
        self.radioButton_3 = QRadioButton(self.tab_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(700, 10, 151, 19))
        self.listWidget = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(300, 190, 256, 251))
        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 110, 101, 41))
        self.listWidget_2 = QListWidget(self.tab_3)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(660, 190, 256, 251))
        self.pushButton_2 = QPushButton(self.tab_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(740, 100, 101, 41))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_3 = QLabel(self.tab_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 30, 321, 61))
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)
        self.radioButton.clicked.connect(self.listWidget.hide)
        self.radioButton.clicked.connect(self.pushButton.hide)
        self.radioButton.clicked.connect(self.pushButton_2.hide)
        self.radioButton.clicked.connect(self.listWidget_2.hide)
        self.radioButton_2.clicked.connect(self.listWidget_2.hide)
        self.radioButton_2.clicked.connect(self.pushButton_2.hide)
        self.radioButton_2.clicked.connect(self.pushButton.show)
        self.radioButton_2.clicked.connect(self.listWidget.show)
        self.radioButton_3.clicked.connect(self.pushButton.hide)
        self.radioButton_3.clicked.connect(self.listWidget.hide)
        self.radioButton_3.clicked.connect(self.pushButton_2.show)
        self.radioButton_3.clicked.connect(self.listWidget_2.show)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"0.0.1 ui\u6d4b\u8bd5\u7b2c\u4e00\u7248", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">0.0.1  ui\u6d4b\u8bd5\u7b2c\u4e00\u7248</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt;\">1</span><span style=\" font-size:16pt; font-weight:600;\">.</span><span style=\" font-size:16pt;\">\u8fdb\u884c\u4e86ui\u7684\u8bbe\u8ba1</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u6709\u5927\u91cf\u7684bug</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Dialog", u"\u9996\u9875", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\u4f7f\u7528\u5185\u7f6e\u9ed1\u540d\u5355", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"\u4f7f\u7528\u81ea\u5b9a\u4e49\u9ed1\u540d\u5355", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"\u4f7f\u7528\u81ea\u5b9a\u4e49\u767d\u540d\u5355", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u9879\u76ee", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"\u7f51\u9875\u5c4f\u853d\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Dialog", u"\u8f6f\u4ef6\u5c4f\u853d\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u7eff\u539f\u2014\u2014ui\u8bbe\u8ba1/\u6280\u672f\u652f\u6301</span></p><p><br/></p><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"\u9e23\u8c22\u6e05\u5355", None))
    # retranslateUi

