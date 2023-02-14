#from dataBase import database
from basicImportInfo import *
from A_Sign_InOrUpGUI import Login, SignIn, SignUp, AccountCreationWindow
from PersonDatabaseGUI import PersonDatabaseWindow, PersonTableWindow  #, MorningTableWindow
from ExerciseDatabaseGUI import ExerciseDatabaseWindow, ExerciseTableConfigurationWindow, AddExerciseWindow, FindUpdateExerciseWindow, UpdateExerciseWindow, DeleteExerciseWindow, ViewExerciseWindow
from WorkoutDatabaseGUI import WorkoutDataTableConfigWindow, EnterWorkoutDataWindow, FindWorkoutDataUpdateWindow, UpdateWorkoutDataWindow, DeleteWorkoutDataWindow, ViewWorkoutDataWindow
from ChatBotGUI import ChatBotWindow
from LiveWorkoutGUI import WorkoutWindow

from sys import argv, exit as Exit
  

class MainMenuWindow(QWidget):
    switchToDatabaseWindow, switchToChatBotWindow, switchToWorkoutWindow, switchToLoginWindow = \
    pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal() 

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Main Window')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

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


class DatabaseWindow(QWidget):
    switchToPersonDatabseWindow, switchToExerciseDatabaseWindow, switchToMenuWindow = pyqtSignal(), pyqtSignal(), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.CONTEXT = None

        self.setWindowTitle('Database Configuration')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.personDatabaseConfig = QPushButton("Person Database Configuration")
        self.personDatabaseConfig.clicked.connect(self.goToPersonDatabaseWindow)
        self.exerciseDatabaseConfig = QPushButton("Exercise Database Configuation")
        self.exerciseDatabaseConfig.clicked.connect(self.goToExerciseDatabaseWindow)

        self.backButton = QPushButton('Back To Menu')
        self.backButton.clicked.connect(self.goToMenuWindow)

        self.addToLayout = [(self.personDatabaseConfig, 0, 0, 1, 1),
                            (self.exerciseDatabaseConfig, 1, 0, 1, 1),
                            (self.backButton, 2, 0, 1, 1)]

        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
        
        self.setLayout(layout)
    
    def goToMenuWindow(self):
        self.switchToMenuWindow.emit()

    def goToPersonDatabaseWindow(self):
        self.switchToPersonDatabseWindow.emit()

    def goToExerciseDatabaseWindow(self):
        self.switchToExerciseDatabaseWindow.emit()

        
class Controller:

    def __init__(self):
        pass

    def showLogin(self):
        try:
           self.signIn.close()
        except:
            pass
        try:
           self.signUp.close()
        except:
            pass
        
        self.login = Login()
        self.login.switchToSignInWindow.connect(self.showSignIn)
        self.login.switchToSignUpWindow.connect(self.showSignUp)
        self.login.show()

    def showSignIn(self):
        try:
           self.login.close()
        except:
            pass

        self.signIn = SignIn()
        self.signIn.switchToMenuWindow.connect(self.showMainMenu)
        self.signIn.switchToLoginWindow.connect(self.showLogin)
        self.signIn.show()

    def showSignUp(self):
        try:
           self.login.close()
        except:
            pass
        try:
           self.accountCreation.close()
        except:
            pass

        self.signUp = SignUp()
        self.signUp.switchToAccountCreationWindow.connect(self.showAccountCreation)
        self.signUp.switchToLoginWindow.connect(self.showLogin)
        self.signUp.show()

    def showAccountCreation(self, genUserInfo):
        try:
           self.signUp.close()
        except:
            pass

        self.accountCreation = AccountCreationWindow(genUserInfo)
        self.accountCreation.switchToMenuWindow.connect(self.showMainMenu)
        self.accountCreation.switchToSignUpWindow.connect(self.showSignUp)
        self.accountCreation.show()


    def showMainMenu(self):
        
        # This doesn't work??
        #windowsToClose = [self.signIn, self.signUp, self.chatBot, self.workOut]

        #for window in windowsToClose:
        #    try:
        #        window.close()
        #    except AttributeError:
        #        pass

        try:
           self.signIn.close()
        except:
            pass
        try:
           self.accountCreation.close()
        except:
            pass
        try:
            self.database.close()
        except:
            pass
        try:
           self.chatBot.close()
        except:
            pass
        try:
           self.workOut.close()
        except:
            pass
        
        self.mainMenuWindow = MainMenuWindow()
        self.mainMenuWindow.switchToDatabaseWindow.connect(self.showDatabaseWindow)
        self.mainMenuWindow.switchToChatBotWindow.connect(self.showChatBot)
        self.mainMenuWindow.switchToWorkoutWindow.connect(self.showWorkout)
        
        self.mainMenuWindow.show()


    #################################################
    def showDatabaseWindow(self):
        try:
            self.mainMenuWindow.close()
        except AttributeError:
            pass
        try:
            self.personDatabase.close()
        except AttributeError:
            pass
        try:
            self.exerciseDatabase.close()
        except AttributeError:
            pass

        self.database = DatabaseWindow()
        self.database.switchToPersonDatabseWindow.connect(self.showPersonDatabaseWindow)
        self.database.switchToExerciseDatabaseWindow.connect(self.showExerciseDatabaseWindow)
        self.database.switchToMenuWindow.connect(self.showMainMenu)
        self.database.show()
    

    #################################################
    def showPersonDatabaseWindow(self):
        try:
            self.database.close()
        except AttributeError:
            pass
        try:
            self.personTable.close()
        except AttributeError:
            pass
        
        self.personDatabase = PersonDatabaseWindow()
        self.personDatabase.switchToPersonTableWindow.connect(self.showPersonTableWindow)
        self.personDatabase.switchToMorningTableWindow.connect(self.showMorningTableWindow)
        self.personDatabase.switchToNightTableWindow.connect(self.showNightTableWindow)
        self.personDatabase.switchToDayLogTableWindow.connect(self.showDayLogTableWindow)
        self.personDatabase.switchToDatabaseWindow.connect(self.showDatabaseWindow)
        self.personDatabase.show()

    def showPersonTableWindow(self):
        try:
            self.personDatabase.close()
        except:
            pass
        #try:
        #    self..close()
        #except:
        #    pass
        #try:
        #    self..close()
        #except:
        #    pass
        #try:
        #    self..close()
        #except:
        #    pass
        #try:
        #    self..close()
        #except:
        #    pass


        self.personTable = PersonTableWindow()
        self.personTable.switchToPersonDatabaseWindow.connect(self.showPersonDatabaseWindow)
        self.personTable.show()
        
    def showMorningTableWindow(self):
        try:
            self.personDatabase.close()
        except:
            pass

        #self.morningTable = None
        #self.morning..connect(self.)
        #self...connect(self.)
        #self..show()

    def showNightTableWindow(self):
        try:
            self.personDatabase.close()
        except:
            pass

    #    self. = 
    #    self...connect(self.)
    #    self...connect(self.)
    #    self..show()
    
    def showDayLogTableWindow(self):
        try:
            self.persondatabase.close()
        except:
            pass

    #    self. = 
    #    self...connect(self.)
    #    self...connect(self.)
    #    self..show()


    #################################################
    def showExerciseDatabaseWindow(self):
        try:
            self.database.close()
        except AttributeError:
            pass
        try:
            self.exerciseTable.close()
        except:
            pass
        try:
            self.workoutDataTable.close()
        except:
            pass
        self.exerciseDatabase = ExerciseDatabaseWindow()
        self.exerciseDatabase.switchToExerciseTableWindow.connect(self.showExerciseTableConfigurationWindow)
        self.exerciseDatabase.switchToWorkoutDataTableWindow.connect(self.showWorkoutDataTableConfigurationWindow)
        self.exerciseDatabase.switchToWorkoutsGivenTableWindow.connect(self.showWorkoutsGivenConfigurationTableWindow)
        self.exerciseDatabase.switchToWorkoutFeedbackTable.connect(self.showWorkoutFeedbackConfigurationTableWindow)
        self.exerciseDatabase.switchToDatabaseWindow.connect(self.showDatabaseWindow)
        self.exerciseDatabase.show()

    #################################################
    def showExerciseTableConfigurationWindow(self):
        try:
            self.exerciseDatabase.close()
        except:
            pass
        try:
            self.addExerciseTable.close()
        except:
            pass
        try:
            self.findUpdateExercise.close()
        except:
            pass
        try:
            self.deleteExercise.close()
        except:
            pass
        try:
            self.viewExercise.close()
        except:
            pass

        self.exerciseTable = ExerciseTableConfigurationWindow()
        self.exerciseTable.switchToAddNewExerciseWindow.connect(self.showAddExerciseTableWindow)
        self.exerciseTable.switchToFindUpdateExerciseWindow.connect(self.showFindUpdateExerciseWindow)
        self.exerciseTable.switchToDeleteExerciseWindow.connect(self.showDeleteExerciseWindow)
        self.exerciseTable.switchToViewExerciseWindow.connect(self.showViewExerciseWindow)
        self.exerciseTable.switchToExerciseDatabaseWindow.connect(self.showExerciseDatabaseWindow)
        self.exerciseTable.show()

    def showAddExerciseTableWindow(self):
        try:
            self.exerciseTable.close()
        except:
            pass

        self.addExerciseTable = AddExerciseWindow()
        self.addExerciseTable.switchToExerciseTableConfigurationWindow.connect(self.showExerciseTableConfigurationWindow)
        self.addExerciseTable.show()

    def showFindUpdateExerciseWindow(self):
        try:
            self.exerciseTable.close()
        except:
            pass
        try:
            self.updateExercise.close()
        except:
            pass

        self.findUpdateExercise = FindUpdateExerciseWindow()
        self.findUpdateExercise.switchToExerciseTableConfigurationWindow.connect(self.showExerciseTableConfigurationWindow)
        self.findUpdateExercise.switchToUpdateExerciseWindow.connect(self.showUpdateExerciseWindow)
        self.findUpdateExercise.show()

    def showUpdateExerciseWindow(self, exerciseInfo):
        try:
            self.findUpdateExercise.close()
        except:
            pass

        self.updateExercise = UpdateExerciseWindow(exerciseInfo)
        self.updateExercise.switchToFindUpdateExerciseWindow.connect(self.showFindUpdateExerciseWindow)
        self.updateExercise.show()

    def showDeleteExerciseWindow(self):
        try:
            self.exerciseTable.close()
        except:
            pass

        self.deleteExercise = DeleteExerciseWindow()
        self.deleteExercise.switchToExerciseTableConfigurationWindow.connect(self.showExerciseTableConfigurationWindow)
        self.deleteExercise.show()

    def showViewExerciseWindow(self):
        try:
            self.exerciseTable.close()
        except:
            pass

        self.viewExercise = ViewExerciseWindow()
        self.viewExercise.switchToWorkoutDataTableConfigWindow.connect(self.showExerciseTableConfigurationWindow)
        self.viewExercise.show()
    
    #################################################
    def showWorkoutDataTableConfigurationWindow(self):
        try:
            self.exerciseDatabase.close()
        except:
            pass
        try:
            self.enterWorkoutData.close()
        except:
            pass
        try:
            self.findWorkoutData.close()
        except:
            pass
        try:
            self.deleteWorkoutData.close()
        except:
            pass
        try:
            self.viewWorkoutData.close()
        except:
            pass

        self.workoutDataTable = WorkoutDataTableConfigWindow()
        self.workoutDataTable.switchToEnterWorkoutDataWindow.connect(self.showEnterWorkoutDataWindow)
        self.workoutDataTable.switchToFindWorkoutDataUpdateWindow.connect(self.showFindWorkoutDataUpdateWindow)
        self.workoutDataTable.switchToDeleteWorkoutDataWindow.connect(self.showDeleteWorkoutDataWindow)
        self.workoutDataTable.switchToViewWorkoutDataWindow.connect(self.showViewWorkoutDataWindow)
        self.workoutDataTable.switchToExerciseDatabaseWindow.connect(self.showExerciseDatabaseWindow)
        self.workoutDataTable.show()

    def showEnterWorkoutDataWindow(self):
        try:
            self.workoutDataTable.close()
        except:
            pass

        self.enterWorkoutData = EnterWorkoutDataWindow()
        self.enterWorkoutData.switchToWorkoutDataTableConfigWindow.connect(self.showWorkoutDataTableConfigurationWindow)
        self.enterWorkoutData.show()

    def showFindWorkoutDataUpdateWindow(self):
        try:
            self.workoutDataTable.close()
        except:
            pass
        try:
            self.updateWorkoutData.close()
        except:
            pass

        self.findWorkoutData = FindWorkoutDataUpdateWindow()
        self.findWorkoutData.switchToUpdateWorkoutDataWindow.connect(self.showUpdateWorkoutDataWindow)
        self.findWorkoutData.switchToWorkoutDataTableConfigWindow.connect(self.showWorkoutDataTableConfigurationWindow)
        self.findWorkoutData.show()

    def showUpdateWorkoutDataWindow(self, exerciseInfo):
        try:
            self.findWorkoutData.close()
        except:
            pass

        self.updateWorkoutData = UpdateWorkoutDataWindow(exerciseInfo)
        self.updateWorkoutData.switchToFindUpdateExerciseWindow.connect(self.showFindWorkoutDataUpdateWindow)
        self.updateWorkoutData.show()


    def showDeleteWorkoutDataWindow(self):
        try:
            self.workoutDataTable.close()
        except:
            pass

        self.deleteWorkoutData = DeleteWorkoutDataWindow()
        self.deleteWorkoutData.switchToWorkoutDataTableConfigWindow.connect(self.showWorkoutDataTableConfigurationWindow)
        self.deleteWorkoutData.show()


    def showViewWorkoutDataWindow(self):
        try:
            self.workoutDataTable.close()
        except:
            pass

        self.viewWorkoutData = ViewWorkoutDataWindow()
        self.viewWorkoutData.switchToWorkoutDataTableConfigWindow.connect(self.showWorkoutDataTableConfigurationWindow)
        self.viewWorkoutData.show()

    def showWorkoutsGivenConfigurationTableWindow(self):
        # Play around with update window button back past the find update
        try:
            self.exerciseDatabase.close()
        except:
            pass

    #    self. = 
    #    self...connect(self.)
    #    self...connect(self.)
    #    self..show()

    def showWorkoutFeedbackConfigurationTableWindow(self):
        try:
            self.exerciseDatabase.close()
        except:
            pass

    #    self. = 
    #    self...connect(self.)
    #    self...connect(self.)
    #    self..show()

    def showChatBot(self):
        try:
            self.mainMenuWindow.close()
        except AttributeError:
            pass

        self.chatBot = ChatBotWindow()
        self.chatBot.switchToMenuWindow.connect(self.showMainMenu)
        self.chatBot.show()

    def showWorkout(self):
        try:
            self.mainMenuWindow.close()
        except AttributeError:
            pass

        self.workOut = WorkoutWindow()
        self.workOut.switchToMenuWindow.connect(self.showMainMenu)
        self.workOut.show()


def main():
    app = QApplication(argv)
    controller = Controller()
    
    #controller.showLogin()
    #controller.showSignIn()
    #controller.showSignUp()
    #controller.showAccountCreation()
    #controller.showMainMenu()
    #controller.showDatabaseWindow()
    #controller.showExerciseDatabaseWindow()
    #controller.showExerciseTableConfigurationWindow()
    #controller.showWorkoutDataTableConfigurationWindow()
    #controller.showAddExerciseTableWindow()
    #controller.showChatBot()
    controller.showWorkout()
    Exit(app.exec_())