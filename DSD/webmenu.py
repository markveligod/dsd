from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from widgets import authorization_uis as ui
import os
import reg
import enter
import blockchain



class AutoClass(QWidget, ui.Ui_authorization_form):
	def __init__(self):
		super(AutoClass, self).__init__()
		self.setupUi(self)
		# ui
		pix=QPixmap('icons/auto.png').scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
		self.image.setPixmap(pix)
		self.setWindowIcon(QIcon('icons/passport.png'))
		self.by_author.setText('Author by Mark Veligod')
		# connect's
		self.enter_btn.clicked.connect(self.enter)
		self.reg_btn.clicked.connect(self.registr)
		self.close_btn.clicked.connect(self.close)
		self.setStyleSheet(open('style.css').read())


	def registr(self):
		self.dial=reg.RegClass(self)
		if self.dial.exec_():
			print('REG')

	def start(self):
		self.dial=enter.PassportClass()
		self.dial.show()

	def enter(self):
		login=self.login_line.text()
		password=self.pass_line.text()
		files=os.listdir(blockchain.server_directory)
		if login in files:
			try:
				data_log=blockchain.decryption_log(login, password)
				os.remove(blockchain.server_directory + login + '.txt')
				msgBox=QMessageBox()
				msgBox.setWindowIcon(QIcon('icons/passport.png'))
				msgBox.setStyleSheet(open('style.css').read())
				msgBox.setText('Добро пожаловать, {}'.format(login))
				ret=msgBox.exec_()
				self.close()
				self.start()
			except Exception as info:
				print(info)
				os.remove(blockchain.server_directory + login + '.txt')
				msgBox=QMessageBox()
				msgBox.setWindowIcon(QIcon('icons/passport.png'))
				msgBox.setStyleSheet(open('style.css').read())
				msgBox.setText('Пароль неверный. Введите корректный пароль.')
				ret=msgBox.exec_()
		elif login not in files: 
			msgBox=QMessageBox()
			msgBox.setText('Логин не зарегистрирован')
			ret=msgBox.exec_()

if __name__ == '__main__':
	app=QApplication([])
	w=AutoClass()
	w.show()
	app.exec_()