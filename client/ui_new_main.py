# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_mainQjsfOE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.11
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 300, 360))
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 291, 71))
        self.widget = QWidget(self.home)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 100, 231, 201))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEditLogin = QLineEdit(self.widget)
        self.lineEditLogin.setObjectName(u"lineEditLogin")

        self.verticalLayout.addWidget(self.lineEditLogin)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lineEditPass = QLineEdit(self.widget)
        self.lineEditPass.setObjectName(u"lineEditPass")
        self.lineEditPass.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.lineEditPass)

        self.pushButtonCheck = QPushButton(self.widget)
        self.pushButtonCheck.setObjectName(u"pushButtonCheck")

        self.verticalLayout.addWidget(self.pushButtonCheck)

        self.stackedWidget.addWidget(self.home)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(6, 6, 281, 141))
        self.widget1 = QWidget(self.page_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 200, 281, 121))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.widget1)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget1)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.widget2 = QWidget(self.page_3)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(40, 290, 219, 36))
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1, 1, 291, 171))
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d \u0438 \u043f\u0430\u0440\u043e\u043b\u044c</p><p align=\"center\">\u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0432 \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.pushButtonCheck.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c (25%)</p><p align=\"center\">\u043d\u0435 \u043c\u043e\u0436\u0435\u0442 \u0434\u0430\u0442\u044c \u043e\u0442\u0432\u0435\u0442\u0430.</p><p align=\"center\">\u0423\u0432\u0435\u043b\u0438\u0447\u0438\u0442\u044c \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c?</p><p align=\"center\">(\u041c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0435\u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e)</p></body></html>", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0441\u043d\u043e\u0432\u0430", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0441\u043d\u043e\u0432\u0430", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c (50%)</p><p align=\"center\">\u043d\u0435 \u043c\u043e\u0436\u0435\u0442 \u0434\u0430\u0442\u044c \u043e\u0442\u0432\u0435\u0442\u0430.</p><p align=\"center\">\u0423\u0432\u0435\u043b\u0438\u0447\u0438\u0442\u044c \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c \u0434\u043e 100%?</p><p align=\"center\">(\u041c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0435\u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e)</p></body></html>", None))
    # retranslateUi

