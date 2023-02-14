from basicImportInfo import *
#from workoutDatabase import *
#from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QWidget
#from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread 

winXPos, winYPos = 0, 0
winLength, winHeight = 1080, 640

class ExerciseDatabaseWindow(QWidget):
    switchToExerciseTableWindow, switchToWorkoutDataTableWindow, switchToWorkoutsGivenTableWindow, switchToWorkoutFeedbackTable, switchToDatabaseWindow = \
        pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.CONTEXT = None

        self.setWindowTitle('Exercise Database Configuration')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()
        
        self.exerciseTableLabel = QPushButton("Exercise Table")
        self.exerciseTableLabel.clicked.connect(self.goToExerciseTableWindow)
        self.workoutTableLabel = QPushButton("Workout Data Table")
        self.workoutTableLabel.clicked.connect(self.goToWorkoutDataTableWindow)
        self.workoutsGvienTableLabel = QPushButton("Workouts Given Table")
        self.workoutsGvienTableLabel.clicked.connect(self.goToWorkoutsGivenTableWindow)
        self.workoutFeedbackTableLabel = QPushButton("Workout Feedback Table")
        self.workoutFeedbackTableLabel.clicked.connect(self.goToWorkoutFeedbackWindow)
        
        self.backButton = QPushButton('Back To Database Configuration')
        self.backButton.clicked.connect(self.goToDatabaseConfigurationWindow)

        self.addToLayout = [(self.exerciseTableLabel, 0, 0, 1, 1),
                            (self.workoutTableLabel, 1, 0, 1, 1),
                            (self.workoutsGvienTableLabel, 2, 0, 1, 1),
                            (self.workoutFeedbackTableLabel, 3, 0, 1, 1),
                            (self.backButton, 4, 0, 1, 1)]

        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
        
    def goToExerciseTableWindow(self):
        self.switchToExerciseTableWindow.emit()

    def goToWorkoutDataTableWindow(self):
        self.switchToWorkoutDataTableWindow.emit()

    def goToWorkoutsGivenTableWindow(self):
        self.switchToWorkoutsGivenTableWindow.emit()

    def goToWorkoutFeedbackWindow(self):
        self.switchToWorkoutFeedbackTable.emit()

    def goToDatabaseConfigurationWindow(self):
        self.switchToDatabaseWindow.emit()


###############################################
class ExerciseTableConfigurationWindow(QWidget):
    switchToAddNewExerciseWindow, switchToFindUpdateExerciseWindow, switchToFindDeleteExerciseWindow, switchToViewExerciseWindow, switchToExerciseDatabaseWindow = \
        pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Exercise Table Configuration')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.addNewExercise = QPushButton("Add New Exercise")
        self.addNewExercise.clicked.connect(self.goToAddNewExerciseWindow)
        self.updateExercise = QPushButton("Update Exercise")
        self.updateExercise.clicked.connect(self.goToUpdateExerciseWindow)
        self.deleteExercise = QPushButton("Delete Exercise")
        self.deleteExercise.clicked.connect(self.goToDeleteExerciseWindow)
        self.viewExercise = QPushButton("View Exercise")
        self.viewExercise.clicked.connect(self.goToViewExerciseWindow)
        
        self.backButton = QPushButton('Back To Database Configuration')
        self.backButton.clicked.connect(self.goToExerciseDatabaseWindow)

        self.addToLayout = [(self.addNewExercise, 0, 0, 1, 1),
                            (self.updateExercise, 1, 0, 1, 1),
                            (self.deleteExercise, 2, 0, 1, 1),
                            (self.viewExercise, 3, 0, 1, 1),
                            (self.backButton, 4, 0, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    
    def goToAddNewExerciseWindow(self):
        self.switchToAddNewExerciseWindow.emit()
    
    def goToUpdateExerciseWindow(self):
        self.switchToFindUpdateExerciseWindow.emit()
    
    def goToDeleteExerciseWindow(self):
        self.switchToFindDeleteExerciseWindow.emit()

    def goToViewExerciseWindow(self):
        self.switchToViewExerciseWindow.emit()

    def goToExerciseDatabaseWindow(self):
        self.switchToExerciseDatabaseWindow.emit()      


class AddExerciseWindow(QWidget):
    switchToExerciseTableConfigurationWindow = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Add Exercise To Database')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.exerciseNameLabel = QLabel("Exercise Name*:")
        self.exerciseNameInput = QLineEdit()
        self.exerciseNameInput.setPlaceholderText("Enter The Name Of This Exercise")

        self.muscleGroupLabel = QLabel("Muscle Group*:")
        self.muscleGroupInput = QLineEdit()
        self.muscleGroupInput.setPlaceholderText("Enter Muscle Group The Exercise Belongs To")

        self.baseIntensityLabel = QLabel("Base Intensity*:")
        self.baseIntensityInput = QLineEdit()
        self.baseIntensityInput.setPlaceholderText("Enter The Base Intensity Of The Exercise")

        self.exerciseTypeLabel = QLabel("Exercise Type*:")
        self.exerciseTypeInput = QLineEdit()
        self.exerciseTypeInput.setPlaceholderText("Enter What Type Of Exercise This Is")
        
        self.submitButton = QPushButton("Submit Information")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Exercise Configuration Database')
        self.backButton.clicked.connect(self.goToExerciseTAbleConfigurationWindow)

        self.addToLayout = [(self.exerciseNameLabel, 1, 0, 1, 1), (self.exerciseNameInput, 1, 1, 1, 1),
                            (self.muscleGroupLabel, 2, 0, 1, 1), (self.muscleGroupInput, 2, 1, 1, 1),
                            (self.baseIntensityLabel, 3, 0, 1, 1), (self.baseIntensityInput, 3, 1, 1, 1),
                            (self.exerciseTypeLabel, 4, 0, 1, 1), (self.exerciseTypeInput, 4, 1, 1, 1),
                            (self.backButton, 5, 0, 1, 1), (self.submitButton, 5, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)


    def goToSubmitTable(self):
        userInput = [self.exerciseNameInput, 
                     self.muscleGroupInput,
                     self.baseIntensityInput,
                     self.exerciseTypeInput]
        
        addExerciseData = {}
        for num, col in enumerate(ExerciseData):
            if 0 < num:
                addExerciseData[col] = userInput[num - 1].text()
        
        print(addExerciseData)

    def goToExerciseTableConfigurationWindow(self):
        self.switchToExerciseTableConfigurationWindow.emit()
        
    
class FindUpdateExerciseWindow(QWidget):
    switchToUpdateExerciseWindow, switchToExerciseTableConfigurationWindow = pyqtSignal(list), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Update Exercise [Find]')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.exerciseIDLabel = QLabel("Exercise ID*:")
        self.exerciseIDInput = QLineEdit()
        self.exerciseIDInput.setPlaceholderText("Enter The ID Of This Exercise")

        self.exerciseNameLabel = QLabel("Exercise Name*:")
        self.exerciseNameInput = QLineEdit()
        self.exerciseNameInput.setPlaceholderText("Enter The Name Of This Exercise")

        self.muscleGroupLabel = QLabel("Muscle Group:")
        self.muscleGroupInput = QLineEdit()
        self.muscleGroupInput.setPlaceholderText("Enter Muscle Group The Exercise Belongs To")

        self.baseIntensityLabel = QLabel("Base Intensity:")
        self.baseIntensityInput = QLineEdit()
        self.baseIntensityInput.setPlaceholderText("Enter The Base Intensity Of The Exercise")

        self.exerciseTypeLabel = QLabel("Exercise Type:")
        self.exerciseTypeInput = QLineEdit()
        self.exerciseTypeInput.setPlaceholderText("Enter What Type Of Exercise This Is")
        
        self.submitButton = QPushButton("Find Exercise")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Exercise Configuration Database')
        self.backButton.clicked.connect(self.goToExerciseDatabaseConfigurationWindow)

        self.addToLayout = [(self.exerciseIDLabel, 1, 0, 1, 1), (self.exerciseIDInput, 1, 1, 1, 1),
                            (self.exerciseNameLabel, 2, 0, 1, 1), (self.exerciseNameInput, 2, 1, 1, 1),
                            (self.muscleGroupLabel, 3, 0, 1, 1), (self.muscleGroupInput, 3, 1, 1, 1),
                            (self.baseIntensityLabel, 4, 0, 1, 1), (self.baseIntensityInput, 4, 1, 1, 1),
                            (self.exerciseTypeLabel, 5, 0, 1, 1), (self.exerciseTypeInput, 5, 1, 1, 1),
                            (self.backButton, 6, 0, 1, 1), (self.submitButton, 6, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    

    def goToExerciseDatabaseConfigurationWindow(self):
        self.switchToExerciseTableConfigurationWindow.emit()

    def goToSubmitTable(self):
        exerciseFound = True

        userInput = [self.exerciseIDInput,
                     self.exerciseNameInput, 
                     self.muscleGroupInput,
                     self.baseIntensityInput,
                     self.exerciseTypeInput]
        
        selectExerciseData = ExerciseData

        for num, col in enumerate(ExerciseData):
            currentColInput = userInput[num].text()
            if currentColInput is not None:
                selectExerciseData[col] = currentColInput
        
        print(selectExerciseData)

        # selectFromTable(dataBases[1][0][1], ExerciseData)

        if exerciseFound is True:
            self.switchToUpdateExerciseWindow.emit(userInput)


class UpdateExerciseWindow(QWidget):
    switchToFindUpdateExerciseWindow = pyqtSignal()

    def __init__(self, exerciseInfo):
        QWidget.__init__(self)

        self.setWindowTitle('Update Exercise')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        currentExerciseName = exerciseInfo[1]
        currentMuscleGroup = exerciseInfo[2]
        currentBaseIntensity = exerciseInfo[3]
        currentExerciseType = exerciseInfo[4]
                        
        self.exerciseNameLabel = QLabel("Exercise Name:")
        self.exerciseNameInput = QLineEdit()
        self.exerciseNameInput.setPlaceholderText("Enter The Updated Name Of This Exercise")

        self.muscleGroupLabel = QLabel("Muscle Group:")
        self.muscleGroupInput = QLineEdit()
        self.muscleGroupInput.setPlaceholderText("Enter The Updated Muscle Group This Exercise Belongs To")

        self.baseIntensityLabel = QLabel("Base Intensity:")
        self.baseIntensityInput = QLineEdit()
        self.baseIntensityInput.setPlaceholderText("Enter The Updated Base Intensity Of The Exercise")

        self.exerciseTypeLabel = QLabel("Exercise Type:")
        self.exerciseTypeInput = QLineEdit()
        self.exerciseTypeInput.setPlaceholderText("Update What Type Of Exercise This Is")
        
        self.submitButton = QPushButton("Find Exercise")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Exercise Configuration Database')
        self.backButton.clicked.connect(self.goToFindUpdateExercise)

        self.addToLayout = [(self.exerciseNameLabel, 2, 0, 1, 1), (self.exerciseNameInput, 2, 1, 1, 1),
                            (self.muscleGroupLabel, 3, 0, 1, 1), (self.muscleGroupInput, 3, 1, 1, 1),
                            (self.baseIntensityLabel, 4, 0, 1, 1), (self.baseIntensityInput, 4, 1, 1, 1),
                            (self.exerciseTypeLabel, 5, 0, 1, 1), (self.exerciseTypeInput, 5, 1, 1, 1),
                            (self.backButton, 6, 0, 1, 1), (self.submitButton, 6, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    
    def goToFindUpdateExercise(self):
        self.switchToFindUpdateExerciseWindow.emit()

    def goToSubmitTable(self):
        userInput = [self.exerciseNameInput, 
                     self.muscleGroupInput,
                     self.baseIntensityInput,
                     self.exerciseTypeInput]

        updateExerciseData = ExerciseData
        for num, col in enumerate(ExerciseData):
            if 0 < num: 
                currentColInput = userInput[num].text()
                updateExerciseData[col] = currentColInput
        
        print(updateExerciseData)


class DeleteExerciseWindow(QWidget):
    switchToExerciseTableConfigurationWindow = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Delete Exercise [Find]')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.exerciseIDLabel = QLabel("Exercise ID*:")
        self.exerciseIDInput = QLineEdit()
        self.exerciseIDInput.setPlaceholderText("Enter The ID Of This Exercise")

        self.exerciseNameLabel = QLabel("Exercise Name*:")
        self.exerciseNameInput = QLineEdit()
        self.exerciseNameInput.setPlaceholderText("Enter The Name Of This Exercise")

        
        self.submitButton = QPushButton("Delete Exercise")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Exercise Configuration Database')
        self.backButton.clicked.connect(self.goToExerciseDatabaseConfigurationWindow)

        self.addToLayout = [(self.exerciseIDLabel, 1, 0, 1, 1), (self.exerciseIDInput, 1, 1, 1, 1),
                            (self.exerciseNameLabel, 2, 0, 1, 1), (self.exerciseNameInput, 2, 1, 1, 1),
                            (self.backButton, 3, 0, 1, 1), (self.submitButton, 3, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)

        def goToSubmitTable(self):
            userInput = [self.exerciseIDInput, 
                         self.exercisNameInput]



        def goToExerciseDatabaseConfigurationWindow(self):
            self.switchToExerciseTableConfigurationWindow.emit()


class ViewExerciseWindow(QWidget):
    _ = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()


###############################################
class WorkoutDataTableConfigurationWindow(QWidget):
    _ = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()