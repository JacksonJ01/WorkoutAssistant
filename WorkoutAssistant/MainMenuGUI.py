from basicImportInfo import *


class MainMenuWindow(QWidget):
    switchToDatabaseWindow, switchToChatBotWindow, switchToWorkoutWindow, switchToLoginWindow = \
    pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal() 

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Sign Up Window')
        self.setStyleSheet("background-color: gray")

        layout = QGridLayout()

        self.title = QLabel("Main Menu")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
        QLabel {
            font-size: 45px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 1100px;
            
            border: 3px solid;
            border-radius: 25%;

            margin: 1px 0px 0px 10px;
            
            background-color: lightgray;
        }
        
        """)

        self.databaseButton = QPushButton('Database Configuration')
        self.databaseButton.clicked.connect(self.goToDatabaseWindow)
        self.databaseButton.setStyleSheet("""
        QPushButton {
            font-size: 28px;
            font-family: "Times New Roman";

            min-height: 150px;
            max-height: 150px;

            border: 2px solid;
            border-radius: 25%;
         
            background-color: lightgray;
        }
        QPushButton:hover {
            font-size: 38px;
            font: bold italic "Times New Roman";

            border-style: solid double solid solid;
            border-width: 4px;
            border-radius: 40%;
            
            background-color: white;
        }
        """)


        self.workoutButton = QPushButton('AI Workout Assistant')
        self.workoutButton.clicked.connect(self.goToWorkoutWindow)
        self.workoutButton.setStyleSheet("""
        QPushButton {
            font-size: 28px;
            font-family: "Times New Roman";

            min-height: 150px;
            max-height: 150px;

            border: 3px solid;
            border-radius: 25%;
         
            background-color: lightgray;
        }
        QPushButton:hover {
            font-size: 38px;
            font: bold italic "Times New Roman";
            
            border-style: solid double solid double;
            border-width: 4px;
            border-radius: 40%;

            background-color: white;

        }
        """)


        self.chatBotButton = QPushButton('Chat With Assistant')
        self.chatBotButton.clicked.connect(self.goToChatBotWindow)
        self.chatBotButton.setStyleSheet("""
        QPushButton {
            font-size: 28px;
            font-family: "Times New Roman";

            min-height: 150px;
            max-height: 150px;

            border: 2px solid;
            border-radius: 25%;
         
            background-color: lightgray;
        }
        QPushButton:hover {
            font-size: 38px;
            font: bold italic "Times New Roman";
            
            border-width: 4px;
            border-style: solid solid solid double;
            border-radius: 40%;

            background-color: white;
        }
        """)

        self.exitButton = QPushButton('Exit Program')
        self.exitButton.clicked.connect(self.goToExit)
        self.exitButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 1100px;

            border: 1px solid;
            border-radius: 8%;
         
            background-color: lightgray;
        }
        QPushButton:hover {
            font-size: 25px;
            font: bold italic "Times New Roman";

            background-color: white;
        }
        """)


        self.bufferZone1 = QLabel()
        self.bufferZone1.setStyleSheet("""
        QLabel {
            min-height: 200px;
            max-height: 200px;
        }
        """)

        self.bufferZone2 = QLabel()
        self.bufferZone2.setAlignment(Qt.AlignCenter)
        self.bufferZone2.setStyleSheet("""
        QLabel {
            min-height: 150px;
            max-height: 150px;
        }
        """)

        #self.addToLayout = [(self.title, 0, 0, 1, 1),
        #                    (self.databaseButton, 1, 0, 1, 1),
        #                   (self.chatBotButton, 2, 0, 1, 1), 
        #                   (self.workoutButton, 3, 0, 1, 1), 
        #                   (self.exitButton, 4, 0, 1, 1)]
        
        self.addToLayout = [(self.title, 0, 0, 1, 3),
                            (self.bufferZone1, 1, 0, 1, 3),
                            (self.databaseButton, 2, 0, 1, 1), (self.workoutButton, 2, 1, 1, 1), (self.chatBotButton, 2, 2, 1, 1), 
                            (self.bufferZone2, 3, 0, 1, 3),
                           (self.exitButton, 4, 0, 1, 3)]
        
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
