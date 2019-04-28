from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from widgets import getBlock_uis as ui
import os
import blockchain

class RegClass(QDialog, ui.Ui_reg):
	def __init__(self, patern):
		super(RegClass, self).__init__(patern)
		self.setupUi(self)
		#connect
		self.foto_btn.clicked.connect(self.showMessage)
		self.send_btn.clicked.connect(self.reg_block)
		self.close_btn.clicked.connect(self.close)
		self.setStyleSheet(open('style.css').read())


	def showMessage(self):
		_filter='*.jpg;;*.png;;*.jpeg'
		path=QFileDialog.getOpenFileName(self, 'Фотография', os.curdir, _filter)
		foto_l=self.foto.setText(str(path[0]))
		return foto_l


	def reg_block(self):
		files=os.listdir(blockchain.server_directory)
		login = self.login.text()
		if login in files:
			msgBox=QMessageBox()
			msgBox.setWindowIcon(QIcon('icons/passport.png'))
			msgBox.setStyleSheet(open('style.css').read())
			msgBox.setText('Логин уже существует')
			ret=msgBox.exec_()
		elif login not in files:
			password = self.password.text()
			two_pass = self.rep_password.text()
			foto_path = self.foto.text()
			name = self.name.text()
			surname = self.surname.text()
			patronymic = self.patronymic.text()
			registration = self.registration.text()
			residence = self.residence.text()
			data_borh = self.dateEdit.text()
			if password==two_pass:
				self.record_new_block=blockchain.reg_auto(
					login=login, 
					password=password, 
					path=foto_path,
					name=name, 
					surname=surname, 
					patronymic=patronymic, 
					registration=registration, 
					residence=residence, 
					data_borth=data_borh
					)
				msgBox=QMessageBox()
				msgBox.setWindowIcon(QIcon('icons/passport.png'))
				msgBox.setStyleSheet(open('style.css').read())
				msgBox.setText('Данные внесены в новый блок.')
				ret=msgBox.exec_()
				self.close()
			else:
				msgBox=QMessageBox()
				msgBox.setWindowIcon(QIcon('icons/passport.png'))
				msgBox.setStyleSheet(open('style.css').read())
				msgBox.setText('Пароли не совпадают. Попробуйте еще раз.')
				ret=msgBox.exec_()
		else:
			print('ERROR')
