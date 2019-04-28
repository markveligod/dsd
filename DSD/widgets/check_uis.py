# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\markveligod\Desktop\DSD\widgets\check.ui',
# licensing of 'C:\Users\markveligod\Desktop\DSD\widgets\check.ui' applies.
#
# Created: Sun Apr 28 13:25:05 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_check_form(object):
    def setupUi(self, check_form):
        check_form.setObjectName("check_form")
        check_form.resize(306, 198)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(check_form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(check_form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check_btn = QtWidgets.QPushButton(self.groupBox)
        self.check_btn.setObjectName("check_btn")
        self.horizontalLayout.addWidget(self.check_btn)
        self.close_btn = QtWidgets.QPushButton(self.groupBox)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.list_status = QtWidgets.QListWidget(self.groupBox)
        self.list_status.setObjectName("list_status")
        self.verticalLayout.addWidget(self.list_status)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(check_form)
        QtCore.QMetaObject.connectSlotsByName(check_form)

    def retranslateUi(self, check_form):
        check_form.setWindowTitle(QtWidgets.QApplication.translate("check_form", "Blockchain DSD", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("check_form", "Состояние блоков", None, -1))
        self.check_btn.setText(QtWidgets.QApplication.translate("check_form", "Проверить", None, -1))
        self.close_btn.setText(QtWidgets.QApplication.translate("check_form", "Закрыть", None, -1))

