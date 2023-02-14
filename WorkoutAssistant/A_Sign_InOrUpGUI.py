from basicImportInfo import *
winXPos, winYPos = 0, 0
winLength, winHeight = 1080, 640


class Login(QWidget):
    # The pyqtSignal declarations in each class allow for specified windows to be opened
    switchToSignInWindow, switchToSignUpWindow = pyqtSignal(), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Login')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()
    
        self.signInButton = QPushButton('Sign In')
        self.signInButton.clicked.connect(self.goToSignInWindow)

        self.signUpButton = QPushButton('Sign Up')
        self.signUpButton.clicked.connect(self.goToSignUpWindow)

        self.exitButton = QPushButton('Exit Program')
        self.exitButton.clicked.connect(self.goToExit)

        # List variable that hold all of the widegts that need to be added into the current window then adds them
        self.addToLayout = [(self.signUpButton, 0, 0, 1, 1), (self.signInButton, 0, 1, 1, 1), 
                            (self.exitButton, 1, 0, 1, 2)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)

    def goToSignInWindow(self):
        self.switchToSignInWindow.emit()

    def goToSignUpWindow(self):
        self.switchToSignUpWindow.emit()

    def goToExit(self):
        exit("Thank You! \nDo Come Again")


class SignIn(QWidget):
    switchToMenuWindow, switchToLoginWindow = pyqtSignal(), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Sign In')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.userNameLabel = QLabel("Username")
        self.userNameTB = QLineEdit()
        self.passwordLabel = QLabel("Password")
        self.passwordTB = QLineEdit()


        self.backButton = QPushButton('Back To Login Page')
        self.backButton.clicked.connect(self.goToLoginWindow)

        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.goToMenuWindow)

        self.addToLayout = [(self.userNameLabel, 0, 0, 1, 1), (self.userNameTB, 0, 1, 1, 1), (self.passwordLabel, 0, 2, 1, 1), (self.passwordTB, 0, 3, 1, 1), 
                            (self.backButton, 1, 0, 1, 2), (self.submitButton, 1, 2, 1, 2)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])        
        self.setLayout(layout)

    def goToMenuWindow(self):
        uName = self.userNameTB.text()
        passW = self.passwordTB.text()
  
        #if uName in database:
        #    if database[uName] == passW:
        #        self.switchToMenuWindow.emit()
        #else:
        #    pass


    def goToLoginWindow(self):
        self.switchToLoginWindow.emit()

class SignUp(QWidget):
    switchToAccountCreationWindow, switchToLoginWindow = pyqtSignal(list), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Sign Up')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()             

        self.firstNameLabel = QLabel("First Name:*")
        self.firstNameInput = QLineEdit()
        self.lastNameLabel = QLabel("Last Name:*")
        self.lastNameInput = QLineEdit()
        
        self.fitnessLevelLabel = QLabel("Fitness Level:*")
        self.fitnessLevelInput = QLineEdit()

        self.bodyTypeLabel = QLabel("Body Type:")
        self.bodyTypeInput = QLineEdit()
        self.bodyTypeGoalLabel = QLabel("Body Type Goal:")
        self.bodyTypeGoalInput = QLineEdit()

        self.bodyWeightLabel = QLabel("Body Weight")
        self.bodyWeightInput = QLineEdit()
        self.goalWeightLabel = QLabel("Body Weight")
        self.goalWeightInput = QLineEdit()

        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.goToAccountCreationWindow)      

        self.backButton = QPushButton('Back To Login Page')
        self.backButton.clicked.connect(self.goToLoginWindow)

        self.addToLayout = [(self.firstNameLabel, 0, 0, 1, 1), (self.firstNameInput, 0, 1, 1, 1), 
                            (self.lastNameLabel, 1, 0, 1, 1), (self.lastNameInput, 1, 1, 1, 1), 
                            (self.fitnessLevelLabel, 2, 0, 1, 1), (self.fitnessLevelInput, 2, 1, 1, 1), 
                            (self.bodyTypeLabel, 3, 0, 1, 1), (self.bodyTypeInput, 3, 1, 1 ,1),
                            (self.bodyGoalLabel, 4, 0, 1, 1), (self.bodyGoalInput, 4, 1, 1 ,1),
                            (self.bodyWeightLabel, 5, 0, 1, 1), (self.bodyWeightInput, 5, 1, 1 ,1),
                            (self.goalWeightLabel, 6, 0, 1, 1), (self.goalWeightInput, 6, 1, 1 ,1),
                            (self.backButton, 7, 0, 1, 1), (self.submitButton, 7, 1, 1, 1)]

        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    
    def goToAccountCreationWindow(self):
        userInput = [self.firstNameInput, self.lastNameInput, self.fitnessLevelInput,
                     self.bodyTypeInput,
                     self.bodyGoalInput,
                     self.bodyWeightInput,
                     self.goalWeightInput
        ]


        if userInput[0] != None and userInput[1] != None and userInput[2] != None:
            self.switchToAccountCreationWindow.emit([x.text() for x in self.addToLayout])

    def goToLoginWindow(self):
        self.switchToLoginWindow.emit()


class AccountCreationWindow(QWidget):
    switchToMenuWindow, switchToSignUpWindow = pyqtSignal(), pyqtSignal()

    def __init__(self, genUserInfo):
        QWidget.__init__(self)
        self.setWindowTitle('Sign Up')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()             

        self.genUserInfo = genUserInfo
        print(self.genUserInfo)
        self.userNameLabel = QLabel("Enter A Username:")
        self.userNameInput = QLineEdit()
        self.passwordLabel = QLabel("Enter A Password:")
        self.passwordInput = QLineEdit()

        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.goToMenuWindow) 

        self.backButton = QPushButton('Back To Sign Up Page')
        self.backButton.clicked.connect(self.goToSignUpWindow)

        self.addToLayout = [(self.userNameLabel, 1, 0, 1, 1), (self.userNameInput, 1, 1, 1, 1), 
                            (self.passwordLabel, 2, 0, 1, 1), (self.passwordInput, 2, 1, 1, 1), 
                            (self.submitButton, 3, 0, 1, 1), (self.backButton, 3, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3])
        self.setLayout(layout)
    
    def goToMenuWindow(self):
        # The credentials that the User enters will be checked in this method
        # To do they will have to enter a username and password that has not been entered into the database
        userInput = [self.userNameInput, self.passwordInput] + [self.genUserInfo]

        addPersonData = {}
        num = 0
        for enum, col in enumerate(PersonData):
            if 0 < enum < 3:
                currentColInput = userInput[enum - 1]
                checkData = PersonData[col]
                check = checkDataType(checkData, currentColInput)
                if check is True:
                    addPersonData[col] = currentColInput
                else:
                    print(f"Error at {check}")
                    return


                


        try: 
            # The entered Username is compared to other Usernames in the data base
            if uName not in database: 
                self.switchToMenuWindow.emit()                
        except KeyError:
            pass
    def checkDatabase(table:str, columns: list, fromWhere: dict ):
        
        selectFromTable()
        return

    def goToSignUpWindow(self):
        self.switchToSignUpWindow.emit()