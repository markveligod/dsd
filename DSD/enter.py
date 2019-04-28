from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from widgets import passport_uis as ui
import os
import blockchain
import pickle
import datetime
import check_Block

class PassportClass(QWidget, ui.Ui_passport):
	def __init__(self):
		super(PassportClass, self).__init__()
		self.setupUi(self)
		# ui
		self.setWindowIcon(QIcon('icons/passport.png'))
		# start
		self.start_func()
		#connect's
		self.check_btn.clicked.connect(self.start_check)
		self.close_btn.clicked.connect(self.close)
		self.setStyleSheet(open('style.css').read())

	def start_check(self):
		self.dial=check_Block.checkClass(self)
		if self.dial.exec_():
			print('CHECK')


	def anytime(self):
		data_time=str(datetime.date.today().strftime("%d/%m/%Y"))
		return data_time

	def status_dif(self, born):
		today = datetime.date.today().strftime("%d.%m.%Y")
		year_result=int(today[-4:])-int(born[-4:])
		res={}
		if year_result <= 21:
			res['Status']='Действующий'
		elif year_result >= 21:
			res['Status']='Не действующий'
		return 'Статус: {}'.format(res['Status'])

	def start_func(self):
		data_passport=blockchain.decryption()
		blockchain.save_image(data_passport['foto'])
		pix=QPixmap('log.jpg').scaled(200, 130, Qt.KeepAspectRatio, Qt.SmoothTransformation)
		self.image.setPixmap(pix)
		self.name.setText(data_passport['name'])
		self.surname.setText(data_passport['surname'])
		self.patronymic.setText(data_passport['patronymic'])
		self.registration.setText(data_passport['registration'])
		self.residence.setText(data_passport['residence'])
		self.data_borh.setText(data_passport['data_borth'])
		with open('logs', 'rb') as f:
			log=pickle.load(f)
			self.welcome.setText('Добро пожаловать, {}'.format(log['login']))
		self.time_now.setText(self.anytime())
		self.by_author.setText('Author by Mark Veligod')
		self.Status.setText(self.status_dif(data_passport['data_borth']))
		os.remove('logs')
		os.remove('log.jpg')