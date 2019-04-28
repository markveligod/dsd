from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from widgets import check_uis as ui
import os
import blockchain

class checkClass(QDialog, ui.Ui_check_form):
	def __init__(self, parent):
		super(checkClass, self).__init__(parent)
		self.setupUi(self)
		# connect's
		self.check_btn.clicked.connect(self.checker)
		self.close_btn.clicked.connect(self.close)
		self.setStyleSheet(open('style.css').read())

	def checker(self):
		self.list_status.clear()
		res=blockchain.check_block()
		for i in res:
			self.list_status.addItem('Блок: {} Статус: {}'.format(i['Block'], i['Status']))