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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTextEdit,
    QWidget)
import image_rc
import image_rc

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
"background-color: rgb(48, 48, 48);\n"
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
        self.stackedWidget.setStyleSheet(u"QCheckBox::indicator {\n"
"                width: 0px;\n"
"                height: 0px;\n"
"            }\n"
"\n"
"")
        self.settings_software = QWidget()
        self.settings_software.setObjectName(u"settings_software")
        self.settings_software.setStyleSheet(u"#settings_software{\n"
"background-color: rgba(255, 255, 255, 127);\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"border: none;\n"
"padding: 0;}")
        self.checkBox = QCheckBox(self.settings_software)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(150, 20, 41, 20))
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"image: url(:/button.png);")
        self.textEdit_2 = QTextEdit(self.settings_software)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 0, 781, 391))
        self.textEdit_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"padding: 0;")
        self.textEdit_2.setReadOnly(True)
        self.stackedWidget.addWidget(self.settings_software)
        self.textEdit_2.raise_()
        self.checkBox.raise_()
        self.settings_system = QWidget()
        self.settings_system.setObjectName(u"settings_system")
        self.settings_system.setStyleSheet(u"#settings_system{\n"
"background-color: rgba(255, 255, 255, 127);\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"border: none;\n"
"padding: 0;}")
        self.stackedWidget.addWidget(self.settings_system)
        self.settings_software_button = QPushButton(self.settings_widget)
        self.settings_software_button.setObjectName(u"settings_software_button")
        self.settings_software_button.setGeometry(QRect(0, 0, 195, 100))
        sizePolicy.setHeightForWidth(self.settings_software_button.sizePolicy().hasHeightForWidth())
        self.settings_software_button.setSizePolicy(sizePolicy)
        self.settings_software_button.setMinimumSize(QSize(195, 100))
        self.settings_software_button.setMaximumSize(QSize(195, 100))
        self.settings_software_button.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border-top-left-radius: 20px;  \n"
"\n"
"border: none;\n"
"padding: 0;\n"
"border-right: 1px solid grey;\n"
"")
        self.settings_system_button = QPushButton(self.settings_widget)
        self.settings_system_button.setObjectName(u"settings_system_button")
        self.settings_system_button.setGeometry(QRect(0, 100, 195, 100))
        sizePolicy.setHeightForWidth(self.settings_system_button.sizePolicy().hasHeightForWidth())
        self.settings_system_button.setSizePolicy(sizePolicy)
        self.settings_system_button.setMinimumSize(QSize(195, 100))
        self.settings_system_button.setMaximumSize(QSize(195, 100))
        self.settings_system_button.setStyleSheet(u"background-color: rgba(255, 255, 255, 127);\n"
"border: none;\n"
"padding: 0;\n"
"border-right: 1px solid grey;\n"
"border-top: 1px solid grey;\n"
"")
        self.widget.addWidget(self.settings_widget)
        self.settings_software_button.raise_()
        self.settings_system_button.raise_()
        self.stackedWidget.raise_()
        self.about_widget = QWidget()
        self.about_widget.setObjectName(u"about_widget")
        self.about_widget.setStyleSheet(u"#about_widget{background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;  \n"
"}")
        self.textEdit = QTextEdit(self.about_widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 975, 390))
        self.textEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"padding: 0;")
        self.textEdit.setReadOnly(True)
        self.widget.addWidget(self.about_widget)
        self.quickmenu_menu_wight = QWidget()
        self.quickmenu_menu_wight.setObjectName(u"quickmenu_menu_wight")
        self.quickmenu_menu_wight.setStyleSheet(u"#quickmenu_menu_wight{background-color: rgba(255, 255, 255, 127);\n"
"border-radius: 20px;  \n"
"}\n"
"#scrollArea_2{background-color: rgba(255, 255, 255, 0);}")
        self.scrollArea_2 = QScrollArea(self.quickmenu_menu_wight)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(-1, -1, 981, 391))
        self.scrollArea_2.setStyleSheet(u"#scrollAreaWidgetContents_2{background-color: rgba(255, 255, 255, 0);}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 962, 1000))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 1000))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"")
        self.widget1 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 23, 921, 321))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_31 = QPushButton(self.widget1)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(100, 40))
        self.pushButton_31.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_31, 2, 5, 1, 1)

        self.pushButton_24 = QPushButton(self.widget1)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(100, 40))
        self.pushButton_24.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_24, 0, 4, 1, 1)

        self.pushButton_22 = QPushButton(self.widget1)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(100, 40))
        self.pushButton_22.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_22, 0, 0, 1, 1)

        self.pushButton_29 = QPushButton(self.widget1)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(100, 40))
        self.pushButton_29.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_29, 1, 2, 1, 1)

        self.pushButton_27 = QPushButton(self.widget1)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(100, 40))
        self.pushButton_27.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_27, 3, 4, 1, 1)

        self.pushButton_26 = QPushButton(self.widget1)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(100, 40))
        self.pushButton_26.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_26, 3, 0, 1, 1)

        self.pushButton_30 = QPushButton(self.widget1)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(100, 40))
        self.pushButton_30.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_30, 1, 3, 1, 1)

        self.pushButton_32 = QPushButton(self.widget1)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(100, 40))
        self.pushButton_32.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_32, 1, 5, 1, 1)

        self.pushButton_23 = QPushButton(self.widget1)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(100, 40))
        self.pushButton_23.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_23, 1, 4, 1, 1)

        self.pushButton_28 = QPushButton(self.widget1)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(100, 40))
        self.pushButton_28.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_28, 1, 1, 1, 1)

        self.pushButton_25 = QPushButton(self.widget1)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(100, 40))
        self.pushButton_25.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_25, 0, 5, 1, 1)

        self.pushButton_33 = QPushButton(self.widget1)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(100, 40))
        self.pushButton_33.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_33, 2, 3, 1, 1)

        self.pushButton_34 = QPushButton(self.widget1)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(100, 40))
        self.pushButton_34.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_34, 3, 3, 1, 1)

        self.pushButton_35 = QPushButton(self.widget1)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(100, 40))
        self.pushButton_35.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_35, 2, 4, 1, 1)

        self.pushButton_36 = QPushButton(self.widget1)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(100, 40))
        self.pushButton_36.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_36, 3, 5, 1, 1)

        self.pushButton_37 = QPushButton(self.widget1)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(100, 40))
        self.pushButton_37.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_37, 3, 2, 1, 1)

        self.pushButton_38 = QPushButton(self.widget1)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMinimumSize(QSize(100, 40))
        self.pushButton_38.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_38, 2, 2, 1, 1)

        self.pushButton_39 = QPushButton(self.widget1)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(100, 40))
        self.pushButton_39.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_39, 3, 1, 1, 1)

        self.pushButton_40 = QPushButton(self.widget1)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMinimumSize(QSize(100, 40))
        self.pushButton_40.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_40, 2, 1, 1, 1)

        self.pushButton_41 = QPushButton(self.widget1)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMinimumSize(QSize(100, 40))
        self.pushButton_41.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_41, 2, 0, 1, 1)

        self.pushButton_42 = QPushButton(self.widget1)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(100, 40))
        self.pushButton_42.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_42, 1, 0, 1, 1)

        self.pushButton_43 = QPushButton(self.widget1)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setMinimumSize(QSize(100, 40))
        self.pushButton_43.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_43, 0, 1, 1, 1)

        self.pushButton_44 = QPushButton(self.widget1)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setMinimumSize(QSize(100, 40))
        self.pushButton_44.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_44, 0, 2, 1, 1)

        self.pushButton_45 = QPushButton(self.widget1)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMinimumSize(QSize(100, 40))
        self.pushButton_45.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border: none;\n"
"padding: 0;")

        self.gridLayout.addWidget(self.pushButton_45, 0, 3, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.widget.addWidget(self.quickmenu_menu_wight)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.widget.setCurrentIndex(3)


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

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7\u00b7", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u4f7f\u7528\u83dc\u5355\u5f0f\u5feb\u901f\u83dc\u5355</span></p></body></html>", None))
        self.settings_software_button.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u8bbe\u7f6e", None))
        self.settings_system_button.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
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
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u680f\u8bbe\u7f6e", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u" \u7f51\u7edc\u68c0\u6d4b", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u58c1\u7eb8", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"\u9f20\u6807\u8bbe\u7f6e", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"wifi\u8fde\u63a5", None))
    # retranslateUi

