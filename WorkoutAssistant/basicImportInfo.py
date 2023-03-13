from workoutDatabase import *

from cameraFunct import *

from sys import argv, exit as Exit

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QDate, QPropertyAnimation, QSize, Qt, QThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDateEdit, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTableView, QTimeEdit, QTableWidget, QWidget

#winXPos, winYPos = 0, 0
#screenRes = QApplication([])
#screenRes = screenRes.desktop().screenGeometry()
#winLength, winHeight = screenRes.width(), screenRes.height()

#input(f'{winLength, winHeight}')

defaultCam = 12

#from PySide import QtGui

#app = QtGui.QApplication([])
#screen_resolution = app.desktop().screenGeometry()
#width, height = screen_resolution.width(), screen_resolution.height()