from basicImportInfo import *


class PersonDatabaseWindow(QWidget):
    switchToPersonTableWindow, switchToMorningTableWindow, switchToNightTableWindow, switchToDayLogTableWindow, switchToDatabaseWindow = \
        pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Person Database Configuration')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.personTableLabel = QPushButton("Person Configuration Table")
        self.personTableLabel.clicked.connect(self.goToPersonTableWindow)
        self.morningTableLabel = QPushButton("Morning Configuration Table")
        self.morningTableLabel.clicked.connect(self.goToMorningTableWindow)
        self.nightTableLabel = QPushButton("Night Configuration Table")
        self.nightTableLabel.clicked.connect(self.goToNightTableWindow)
        self.dayLogTableLabel = QPushButton("Day Log Configuration Table")
        self.dayLogTableLabel.clicked.connect(self.goToDayLogTableWindow)
        
        self.backButton = QPushButton('Back To Database Configuartion')
        self.backButton.clicked.connect(self.goToDatabaseConfigurationWindow)

        self.addToLayout = [(self.personTableLabel, 0, 0, 1, 1),
                            (self.morningTableLabel, 1, 0, 1, 1),
                            (self.nightTableLabel, 2, 0, 1, 1),
                            (self.dayLogTableLabel, 3, 0, 1, 1),
                            (self.backButton, 4, 0, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    
    def goToPersonTableWindow(self):
        self.switchToPersonTableWindow.emit()
    
    def goToMorningTableWindow(self):
        self.switchToMorningTableWindow.emit()
    
    def goToNightTableWindow(self):
        self.switchToNightTableWindow.emit()

    def goToDayLogTableWindow(self):
        self.switchToDayLogTable.emit()

    def goToDatabaseConfigurationWindow(self):
        self.switchToDatabaseWindow.emit()

     
class PersonTableWindow(QWidget):
    switchToPersonDatabaseWindow = \
        pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Person Table Configuration')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        currentPassword = None
        currentFirstName = None
        currentLastName = None
        currentFitnessLevel = None
        currentBodyType = None
        currentBodyGoal = None
        currentBodyWeight = None
        currentGoalWeight = None

        self.passwordLabel = QLabel(f"Current Password: {currentPassword}")
        self.passwordInput = QLineEdit()
        self.passwordInput.setPlaceholderText("Type New Password")

        self.firstNameLabel = QLabel(f"Current First Name: {currentFirstName}")
        self.firstNameInput = QLineEdit()
        self.firstNameInput.setPlaceholderText("Type New First Name")

        self.lastNameLabel = QLabel(f"Current Last Name: {currentLastName}")
        self.lastNameInput = QLineEdit()
        self.lastNameInput.setPlaceholderText("Type New Last Name")

        self.fitnessLevelLabel = QLabel(f"Current Fitness Level: {currentFitnessLevel}")
        self.fitnessLevelInput = QLineEdit()
        self.fitnessLevelInput.setPlaceholderText("Type New Fitness Level")

        self.bodyTypeLabel = QLabel(f"Current Body Type: {currentBodyType}")
        self.bodyTypeInput = QLineEdit()
        self.bodyTypeInput.setPlaceholderText("Type New Body Type")

        self.bodyGoalLabel = QLabel(f"Current Body Goal: {currentBodyGoal}")
        self.bodyGoalInput = QLineEdit()
        self.bodyGoalInput.setPlaceholderText("Type New Body Goal")

        self.bodyWeightLabel = QLabel(f"Current Body Weight: {currentBodyWeight}")
        self.bodyWeightInput = QLineEdit()
        self.bodyWeightInput.setPlaceholderText("Type New Body Weight")

        self.goalWeightLabel = QLabel(f"Currrent Weight Goal: {currentGoalWeight}")
        self.goalWeightInput = QLineEdit()
        self.goalWeightInput.setPlaceholderText("Type New Weight Goal")

        self.submitButton = QPushButton("Submit Information")
        self.submitButton.clicked.connect(self.goToSubmitTable)
        
        self.backButton = QPushButton('Back To Person Database Configuartion')
        self.backButton.clicked.connect(self.goToPersonDatabaseConfigurationWindow)

        self.addToLayout = [(self.passwordLabel, 1, 0, 1, 1), (self.passwordInput, 1, 1, 1, 1),
                            (self.firstNameLabel, 2, 0, 1, 1), (self.firstNameInput, 2, 1, 1, 1),
                            (self.lastNameLabel, 3, 0, 1, 1), (self.lastNameInput, 3, 1, 1, 1),
                            (self.fitnessLevelLabel, 4, 0, 1, 1), (self.fitnessLevelInput, 4, 1, 1, 1),
                            (self.bodyTypeLabel, 5, 0, 1, 1), (self.bodyTypeInput, 5, 1, 1, 1),
                            (self.bodyGoalLabel, 6, 0, 1, 1), (self.bodyGoalInput, 6, 1, 1, 1),
                            (self.bodyWeightLabel, 7, 0, 1, 1), (self.bodyWeightInput, 7, 1, 1, 1),
                            (self.goalWeightLabel, 8, 0, 1, 1), (self.goalWeightInput, 8, 1, 1, 1),
                             
                            (self.backButton, 9, 0, 1, 1), (self.submitButton, 9, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    
    def goToSubmitTable(self):
        userInput = [self.passwordInput,
                     self.firstNameInput,
                     self.lastNameInput,
                     self.fitnessLevelInput,
                     self.bodyTypeInput,
                     self.bodyGoalInput,
                     self.bodyWeightInput,
                     self.goalWeightInput]

        addPersonData = {}
        num = 0
        for enum, col in enumerate(PersonData):
            if 1 < enum:
                currentColInput = userInput[num].text()
                num += 1
                if currentColInput != "":
                    checkData = PersonData[col]
                    check = checkDataType(checkData, currentColInput)
                    print(check)
                    if check is True:
                        addPersonData[col] = currentColInput[col] = currentColInput
                    else:
                        print(f"Error at {check}")
                        return
                    

        print(addPersonData)
        addIntoTable(dataBases[0][0][1], addPersonData)
        #clear input
            

    def goToPersonDatabaseConfigurationWindow(self):
        self.switchToPersonDatabaseWindow.emit()
    
        
#class MorningTableWindow(QWidget):
#     = \
#        pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal()

#    def __init__(self):
#        QWidget.__init__(self)

#        self.setWindowTitle('Person Database Configuration')
#        self.setGeometry(winXPos, winYPos, winLength, winHeight)

#        layout = QGridLayout()

#        self.personTableLabel = QPushButton("Person Configuration Table")
#        self.personTableLabel.clicked.connect(self.goToPersonTableWindow)
#        self.morningTableLabel = QPushButton("Morning Configuration Table")
#        self.morningTableLabel.clicked.connect(self.goToMorningTableWindow)
#        self.nightTableLabel = QPushButton("Night Configuration Table")
#        self.nightTableLabel.clicked.connect(self.goToNightTableWindow)
#        self.dayLogTableLabel = QPushButton("Day Log Configuration Table")
#        self.dayLogTableLabel.clicked.connect(self.goToDayLogTableWindow)
        
#        self.backButton = QPushButton('Back To Database Configuartion')
#        self.backButton.clicked.connect(self.goToDatabaseConfigurationWindow)

#        self.addToLayout = [(self.personTableLabel, 0, 0, 1, 1),
#                            (self.morningTableLabel, 1, 0, 1, 1),
#                            (self.nightTableLabel, 2, 0, 1, 1),
#                            (self.dayLogTableLabel, 3, 0, 1, 1),
#                            (self.backButton, 4, 0, 1, 1)]
#        for x in self.addToLayout:
#            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
#        self.setLayout(layout)
    
#    def goToPersonTableWindow(self):
#        self.switchToPersonTableWindow.emit()
    
#    def goToMorningTableWindow(self):
#        self.switchToMorningTableWindow.emit()
    
#    def goToNightTableWindow(self):
#        self.switchToNightTableWindow.emit()

#    def goToDayLogTableWindow(self):
#        self.switchToDayLogTable.emit()

#    def goToDatabaseConfigurationWindow(self):
#        self.switchToDatabaseWindow.emit()
        