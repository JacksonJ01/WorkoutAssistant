from workoutDatabase import *
from PyQt5.QtWidgets import QApplication, QDateEdit, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTableView, QTimeEdit, QTableWidget, QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QDate, Qt, QThread
 
winXPos, winYPos = 0, 0
winLength, winHeight = 1080, 640
defaultCam = 0

#from PySide import QtGui

#app = QtGui.QApplication([])
#screen_resolution = app.desktop().screenGeometry()
#width, height = screen_resolution.width(), screen_resolution.height()