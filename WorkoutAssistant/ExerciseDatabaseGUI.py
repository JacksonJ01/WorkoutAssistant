from basicImportInfo import *

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
    switchToAddNewExerciseWindow, switchToFindUpdateExerciseWindow, switchToDeleteExerciseWindow, switchToViewExerciseWindow, switchToExerciseDatabaseWindow = \
        pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Exercise Table Database')
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
        self.switchToDeleteExerciseWindow.emit()

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

        """
        combobox1 = QComboBox()
        combobox1.addItem('One')
        combobox1.addItem('Two')
        combobox1.addItem('Three')
        combobox1.addItem('Four')

        combobox2 = QComboBox()
        combobox2.addItems(['One', 'Two', 'Three', 'Four'])

        """


        self.muscleGroupLabel = QLabel("Muscle Groups*:")
        self.muscleGroupInput = QLineEdit()
        self.muscleGroupInput.setPlaceholderText("Enter The Muscle Group(s) The Exercise Belongs To")

        self.baseIntensityLabel = QLabel("Base Intensity*:")
        self.baseIntensityInput = QLineEdit()
        self.baseIntensityInput.setPlaceholderText("Enter The Base Intensity Of The Exercise")

        self.exerciseTypeLabel = QLabel("Exercise Types*:")
        self.exerciseTypeInput = QLineEdit()
        self.exerciseTypeInput.setPlaceholderText("Enter What Type(s) Of Exercise This Is")
        
        self.equipmentNeededLabel = QLabel("Equipment Needed*:")
        self.equipmentNeededInput = QLineEdit()
        self.equipmentNeededInput.setPlaceholderText("No:0 | Yes:1 | Both:2")
        
        self.submitButton = QPushButton("Submit Information")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Exercise Table Database')
        self.backButton.clicked.connect(self.goToExerciseTableConfigurationWindow)

        self.addToLayout = [(self.exerciseNameLabel, 1, 0, 1, 1), (self.exerciseNameInput, 1, 1, 1, 1),
                            (self.muscleGroupLabel, 2, 0, 1, 1), (self.muscleGroupInput, 2, 1, 1, 1),
                            (self.baseIntensityLabel, 3, 0, 1, 1), (self.baseIntensityInput, 3, 1, 1, 1),
                            (self.exerciseTypeLabel, 4, 0, 1, 1), (self.exerciseTypeInput, 4, 1, 1, 1),
                            (self.equipmentNeededLabel, 5, 0, 1, 1), (self.equipmentNeededInput, 5, 1, 1, 1),
                            (self.backButton, 6, 0, 1, 1), (self.submitButton, 6, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)


    def goToSubmitTable(self):
        userInput = [self.exerciseNameInput, 
                     self.muscleGroupInput,
                     self.baseIntensityInput,
                     self.exerciseTypeInput,
                     self.equipmentNeededInput]
        
        #print(userInput, type(userInput))
        #reqFilled, errNum = checkReq(userInput)
        #if reqFilled is False:
        #    print(userInput[errNum])
        #checkReq_ = checkReq()

        # Checking required inputs
        num = 0
        for currentColInput in userInput:
            if currentColInput.text() != "":
                num += 1
            else:
                return print(currentColInput.text())

        addExerciseData = {}
        check = None
        for num, col in enumerate(ExerciseData):
            if 0 < num:
                currentColInput = userInput[num - 1].text()
                if currentColInput != "":
                    checkData = ExerciseData[col]
                    check = checkDataType(checkData, currentColInput)
                    print(check)
                    if check is True:
                        addExerciseData[col] = currentColInput
                    else:
                        print(f"Error at {check}")
                        return
        
        print(addExerciseData)
        addIntoTable(dataBases[1][0][1], addExerciseData)
                    
        
    def goToExerciseTableConfigurationWindow(self):
        self.switchToExerciseTableConfigurationWindow.emit()
        
    
class FindUpdateExerciseWindow(QWidget):
    switchToUpdateExerciseWindow, switchToExerciseTableConfigurationWindow = pyqtSignal(list), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Update Exercise Database [Find]')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.exerciseIDLabel = QLabel("Exercise ID*:")
        self.exerciseIDInput = QLineEdit()
        self.exerciseIDInput.setPlaceholderText("Enter The ID Of This Exercise")

        self.exerciseNameLabel = QLabel("Exercise Name*:")
        self.exerciseNameInput = QLineEdit()
        self.exerciseNameInput.setPlaceholderText("Enter The Name Of This Exercise")

        #self.muscleGroupLabel = QLabel("Muscle Group:")
        #self.muscleGroupInput = QLineEdit()
        #self.muscleGroupInput.setPlaceholderText("Enter Muscle Group The Exercise Belongs To")

        #self.baseIntensityLabel = QLabel("Base Intensity:")
        #self.baseIntensityInput = QLineEdit()
        #self.baseIntensityInput.setPlaceholderText("Enter The Base Intensity Of The Exercise")

        #self.exerciseTypeLabel = QLabel("Exercise Type:")
        #self.exerciseTypeInput = QLineEdit()
        #self.exerciseTypeInput.setPlaceholderText("Enter What Type Of Exercise This Is")
        

        self.submitButton = QPushButton("Find Exercise")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Exercise Table Database')
        self.backButton.clicked.connect(self.goToExerciseDatabaseConfigurationWindow)

        self.addToLayout = [(self.exerciseIDLabel, 1, 0, 1, 1), (self.exerciseIDInput, 1, 1, 1, 1),
                            (self.exerciseNameLabel, 2, 0, 1, 1), (self.exerciseNameInput, 2, 1, 1, 1),
                            #(self.muscleGroupLabel, 3, 0, 1, 1), (self.muscleGroupInput, 3, 1, 1, 1),
                            #(self.baseIntensityLabel, 4, 0, 1, 1), (self.baseIntensityInput, 4, 1, 1, 1),
                            #(self.exerciseTypeLabel, 5, 0, 1, 1), (self.exerciseTypeInput, 5, 1, 1, 1),
                            (self.backButton, 6, 0, 1, 1), (self.submitButton, 6, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    

    def goToExerciseDatabaseConfigurationWindow(self):
        self.switchToExerciseTableConfigurationWindow.emit()

    def goToSubmitTable(self):
        exerciseFound = True

        userInput = [self.exerciseIDInput,
                     self.exerciseNameInput#, 
                     #self.muscleGroupInput,
                     #self.baseIntensityInput,
                     #self.exerciseTypeInput
                     ]

        # Checking required inputs
        num = 0
        for currentColInput in userInput:
            if currentColInput.text() != "":
                num += 1
            else:
                return print(currentColInput.text())

        if self.exerciseIDInput.text() != "" and self.exerciseNameInput != "":
            selectExerciseData = {}
            columns = []
            for num, col in enumerate(ExerciseData):
                currentColInput = userInput[num].text()
                if currentColInput != "":
                    columns.append(col)
                    checkData = ExerciseData[col]
                    check = checkDataType(checkData, currentColInput)
                    if check is True:
                        selectExerciseData[col] = currentColInput
                    else:
                        print(f"Error at {check}")
                        return

                if num == 1:
                    break
        
            print(selectExerciseData)
            selectFromTable(dataBases[1][0][1], columns, selectExerciseData)

            if exerciseFound is True:
                self.switchToUpdateExerciseWindow.emit(userInput)


class UpdateExerciseWindow(QWidget):
    switchToFindUpdateExerciseWindow = pyqtSignal()

    def __init__(self, exerciseInfo: list):
        QWidget.__init__(self)

        self.setWindowTitle('Update Exercise Database')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.currentExerciseID = exerciseInfo[0]
        self.currentExerciseName = exerciseInfo[1]
        #self.currentMuscleGroup = exerciseInfo[2]
        #self.currentBaseIntensity = exerciseInfo[3]
        #self.currentExerciseType = exerciseInfo[4]

                        
        self.exerciseNameLabel = QLabel("Exercise Name:")
        self.exerciseNameInput = QLineEdit()
        self.exerciseNameInput.setPlaceholderText("Enter The Updated Name Of This Exercise")

        """
        combobox1 = QComboBox()
        combobox1.addItem('One')
        combobox1.addItem('Two')
        combobox1.addItem('Three')
        combobox1.addItem('Four')

        combobox2 = QComboBox()
        combobox2.addItems(['One', 'Two', 'Three', 'Four'])

        """

        self.muscleGroupLabel = QLabel("Muscle Group:")
        self.muscleGroupInput = QLineEdit()
        self.muscleGroupInput.setPlaceholderText("Enter The Updated Muscle Group This Exercise Belongs To")
        
        """
        combobox1 = QComboBox()
        combobox1.addItem('One')
        combobox1.addItem('Two')
        combobox1.addItem('Three')
        combobox1.addItem('Four')

        combobox2 = QComboBox()
        combobox2.addItems(['One', 'Two', 'Three', 'Four'])

        """

        self.baseIntensityLabel = QLabel("Base Intensity:")
        self.baseIntensityInput = QLineEdit()
        self.baseIntensityInput.setPlaceholderText("Enter The Updated Base Intensity Of The Exercise")

        """
        combobox1 = QComboBox()
        combobox1.addItem('One')
        combobox1.addItem('Two')
        combobox1.addItem('Three')
        combobox1.addItem('Four')

        combobox2 = QComboBox()
        combobox2.addItems(['One', 'Two', 'Three', 'Four'])

        """

        self.exerciseTypeLabel = QLabel("Exercise Type:")
        self.exerciseTypeInput = QLineEdit()
        self.exerciseTypeInput.setPlaceholderText("Update What Type Of Exercise This Is")
        
        self.equipmentNeededLabel = QLabel("Equipment Needed:")
        self.equipmentNeededInput = QLineEdit()
        self.equipmentNeededInput.setPlaceholderText("No:0 | Yes:1 | Both:2")

        self.submitButton = QPushButton("Update Exercise")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Find Update Exercise')
        self.backButton.clicked.connect(self.goToFindUpdateExercise)

        self.addToLayout = [(self.exerciseNameLabel, 2, 0, 1, 1), (self.exerciseNameInput, 2, 1, 1, 1),
                            (self.muscleGroupLabel, 3, 0, 1, 1), (self.muscleGroupInput, 3, 1, 1, 1),
                            (self.baseIntensityLabel, 4, 0, 1, 1), (self.baseIntensityInput, 4, 1, 1, 1),
                            (self.exerciseTypeLabel, 5, 0, 1, 1), (self.exerciseTypeInput, 5, 1, 1, 1),
                            (self.equipmentNeededLabel, 6, 0, 1, 1), (self.equipmentNeededInput, 6, 1, 1, 1),
                            (self.backButton, 7, 0, 1, 1), (self.submitButton, 7, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    
    def goToFindUpdateExercise(self):
        self.switchToFindUpdateExerciseWindow.emit()

    def goToSubmitTable(self):
        userInput = [self.exerciseNameInput, 
                     self.muscleGroupInput,
                     self.baseIntensityInput,
                     self.exerciseTypeInput,
                     self.equipmentNeededInput]

        updateExerciseData = {}
        fromWhere = {}
        temp = [self.currentExerciseID, self.currentExerciseName]
        
        for num, col in enumerate(ExerciseData):
            if 0 < num: 
                currentColInput = userInput[num - 1].text()
                if currentColInput != "":
                    checkData = ExerciseData[col]
                    check = checkDataType(checkData, currentColInput)
                    if check is True:
                        updateExerciseData[col] = currentColInput
                    else:
                        print(f"Error at {check}")
                        return
            if num <= 1:
                fromWhere[col] = temp[num].text()

        print(updateExerciseData)
        modifyTable(dataBases[1][0][1], updateExerciseData, fromWhere)


class DeleteExerciseWindow(QWidget):
    switchToExerciseTableConfigurationWindow = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Delete Exercise From Database')
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
                        self.exerciseNameInput]

        # Checking required inputs
        num = 0
        for currentColInput in userInput:
            if currentColInput.text() != "":
                num += 1
            else:
                return print(currentColInput.text())

        deleteExerciseData = {}
        for num, col in enumerate(ExerciseData):
            currentColInput = userInput[num].text()
            if currentColInput != "":
                checkData = ExerciseData[col]
                check = checkDataType(checkData, currentColInput)
                if check is True:
                    deleteExerciseData[col] = currentColInput
                else:
                    print(f"Error at {check}")
                    return
            if num == 1:
                break
        print(deleteExerciseData)
        deleteFromTable(dataBases[1][0][1], deleteExerciseData)
        # deploy message box

    def goToExerciseDatabaseConfigurationWindow(self):
        self.switchToExerciseTableConfigurationWindow.emit()


class ViewExerciseWindow(QWidget):
    switchToWorkoutDataTableConfigWindow = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('View Exercise Database')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.submitButton = QPushButton("View Exercise Data")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Exercise Configuration Database')
        self.backButton.clicked.connect(self.goToExerciseDatabaseConfigurationWindow)

        self.addToLayout = [
                            (self.backButton, 3, 0, 1, 1), (self.submitButton, 3, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)

    def goToExerciseDatabaseConfigurationWindow(self):
        self.switchToWorkoutDataTableConfigWindow.emit()

    def goToSubmitTable(self):
        pass

