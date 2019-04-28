# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\markveligod\Desktop\DSD\widgets\authorization.ui',
# licensing of 'C:\Users\markveligod\Desktop\DSD\widgets\authorization.ui' applies.
#
# Created: Sun Apr 28 13:25:08 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_authorization_form(object):
    def setupUi(self, authorization_form):
        authorization_form.setObjectName("authorization_form")
        authorization_form.resize(277, 170)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(authorization_form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(authorization_form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QtWidgets.QLabel(self.groupBox)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.login_line = QtWidgets.QLineEdit(self.groupBox)
        self.login_line.setObjectName("login_line")
        self.horizontalLayout.addWidget(self.login_line)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(56, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pass_line = QtWidgets.QLineEdit(self.groupBox)
        self.pass_line.setObjectName("pass_line")
        self.horizontalLayout_2.addWidget(self.pass_line)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.enter_btn = QtWidgets.QPushButton(self.groupBox)
        self.enter_btn.setObjectName("enter_btn")
        self.horizontalLayout_3.addWidget(self.enter_btn)
        self.reg_btn = QtWidgets.QPushButton(self.groupBox)
        self.reg_btn.setObjectName("reg_btn")
        self.horizontalLayout_3.addWidget(self.reg_btn)
        self.close_btn = QtWidgets.QPushButton(self.groupBox)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_3.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.by_author = QtWidgets.QLabel(self.groupBox)
        self.by_author.setAlignment(QtCore.Qt.AlignCenter)
        self.by_author.setObjectName("by_author")
        self.verticalLayout.addWidget(self.by_author)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(authorization_form)
        QtCore.QMetaObject.connectSlotsByName(authorization_form)

    def retranslateUi(self, authorization_form):
        authorization_form.setWindowTitle(QtWidgets.QApplication.translate("authorization_form", "Blockchain DSD", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("authorization_form", "Авторизация", None, -1))
        self.image.setText(QtWidgets.QApplication.translate("authorization_form", "icon", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("authorization_form", "Имя пользователя:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("authorization_form", "Пароль:", None, -1))
        self.enter_btn.setText(QtWidgets.QApplication.translate("authorization_form", "Войти", None, -1))
        self.reg_btn.setText(QtWidgets.QApplication.translate("authorization_form", "Регистрация", None, -1))
        self.close_btn.setText(QtWidgets.QApplication.translate("authorization_form", "Закрыть", None, -1))
        self.by_author.setText(QtWidgets.QApplication.translate("authorization_form", "author", None, -1))

