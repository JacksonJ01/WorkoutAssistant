from basicImportInfo import *


class MainMenuWindow(QWidget):
    switchToDatabaseWindow, switchToChatBotWindow, switchToWorkoutWindow, switchToLoginWindow = \
    pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal() 

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Main Window')

        layout = QGridLayout()

        self.databaseButton = QPushButton('Database Configuration')
        self.databaseButton.clicked.connect(self.goToDatabaseWindow)

        self.chatBotButton = QPushButton('Chat With Workout Assistant')
        self.chatBotButton.clicked.connect(self.goToChatBotWindow)

        self.workoutButton = QPushButton('Workout Window')
        self.workoutButton.clicked.connect(self.goToWorkoutWindow)

        self.exitButton = QPushButton('Exit Program')
        self.exitButton.clicked.connect(self.goToExit)

        self.addToLayout = [(self.databaseButton, 0, 0, 1, 1),
                           (self.chatBotButton, 1, 0, 1, 1), 
                           (self.workoutButton, 2, 0, 1, 1), 
                           (self.exitButton, 3, 0, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)

    def goToDatabaseWindow(self):
        self.switchToDatabaseWindow.emit()

    def goToChatBotWindow(self):
        self.switchToChatBotWindow.emit()

    def goToWorkoutWindow(self):
        self.switchToWorkoutWindow.emit()

    def goToExit(self):
        exit("Thank You! \nDo Come Again")
