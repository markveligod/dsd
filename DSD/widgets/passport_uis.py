# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\markveligod\Desktop\DSD\widgets\passport.ui',
# licensing of 'C:\Users\markveligod\Desktop\DSD\widgets\passport.ui' applies.
#
# Created: Sun Apr 28 17:55:04 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_passport(object):
    def setupUi(self, passport):
        passport.setObjectName("passport")
        passport.resize(557, 314)
        self.passport_box = QtWidgets.QGroupBox(passport)
        self.passport_box.setGeometry(QtCore.QRect(190, 30, 351, 241))
        self.passport_box.setObjectName("passport_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.passport_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.passport_box)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name = QtWidgets.QLabel(self.passport_box)
        self.name.setText("")
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.passport_box)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.surname = QtWidgets.QLabel(self.passport_box)
        self.surname.setText("")
        self.surname.setObjectName("surname")
        self.horizontalLayout_2.addWidget(self.surname)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.passport_box)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.patronymic = QtWidgets.QLabel(self.passport_box)
        self.patronymic.setText("")
        self.patronymic.setObjectName("patronymic")
        self.horizontalLayout_3.addWidget(self.patronymic)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.passport_box)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.registration = QtWidgets.QLabel(self.passport_box)
        self.registration.setText("")
        self.registration.setObjectName("registration")
        self.horizontalLayout_4.addWidget(self.registration)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.passport_box)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.residence = QtWidgets.QLabel(self.passport_box)
        self.residence.setText("")
        self.residence.setObjectName("residence")
        self.horizontalLayout_5.addWidget(self.residence)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.passport_box)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.data_borh = QtWidgets.QLabel(self.passport_box)
        self.data_borh.setText("")
        self.data_borh.setObjectName("data_borh")
        self.horizontalLayout_6.addWidget(self.data_borh)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.check_btn = QtWidgets.QPushButton(self.passport_box)
        self.check_btn.setObjectName("check_btn")
        self.horizontalLayout_7.addWidget(self.check_btn)
        self.close_btn = QtWidgets.QPushButton(self.passport_box)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_7.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.by_author = QtWidgets.QLabel(passport)
        self.by_author.setGeometry(QtCore.QRect(290, 280, 239, 13))
        self.by_author.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.by_author.setObjectName("by_author")
        self.welcome = QtWidgets.QLabel(passport)
        self.welcome.setGeometry(QtCore.QRect(20, 10, 239, 13))
        self.welcome.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.welcome.setObjectName("welcome")
        self.time_now = QtWidgets.QLabel(passport)
        self.time_now.setGeometry(QtCore.QRect(290, 10, 239, 13))
        self.time_now.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time_now.setObjectName("time_now")
        self.widget = QtWidgets.QWidget(passport)
        self.widget.setGeometry(QtCore.QRect(30, 30, 151, 191))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.photo_box = QtWidgets.QGroupBox(self.widget)
        self.photo_box.setObjectName("photo_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.photo_box)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.image = QtWidgets.QLabel(self.photo_box)
        self.image.setObjectName("image")
        self.verticalLayout_2.addWidget(self.image)
        self.verticalLayout_3.addWidget(self.photo_box)
        self.Status = QtWidgets.QLabel(self.widget)
        self.Status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Status.setObjectName("Status")
        self.verticalLayout_3.addWidget(self.Status)
        self.verticalLayout_3.setStretch(0, 1)

        self.retranslateUi(passport)
        QtCore.QMetaObject.connectSlotsByName(passport)

    def retranslateUi(self, passport):
        passport.setWindowTitle(QtWidgets.QApplication.translate("passport", "Blockchain DSD", None, -1))
        self.passport_box.setTitle(QtWidgets.QApplication.translate("passport", "Паспорт", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("passport", "Имя:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("passport", "Фамилия:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("passport", "Отчество:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("passport", "Место регистрации:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("passport", "Место жительства:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("passport", "Дата рождения:", None, -1))
        self.check_btn.setText(QtWidgets.QApplication.translate("passport", "Проверка блоков", None, -1))
        self.close_btn.setText(QtWidgets.QApplication.translate("passport", "Закрыть", None, -1))
        self.by_author.setText(QtWidgets.QApplication.translate("passport", "author", None, -1))
        self.welcome.setText(QtWidgets.QApplication.translate("passport", "welcome", None, -1))
        self.time_now.setText(QtWidgets.QApplication.translate("passport", "time", None, -1))
        self.photo_box.setTitle(QtWidgets.QApplication.translate("passport", "Фото", None, -1))
        self.image.setText(QtWidgets.QApplication.translate("passport", "изображение", None, -1))
        self.Status.setText(QtWidgets.QApplication.translate("passport", "Статус", None, -1))

