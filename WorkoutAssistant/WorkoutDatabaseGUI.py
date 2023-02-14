from basicImportInfo import *


###############################################
class WorkoutDataTableConfigWindow(QWidget):
    switchToEnterWorkoutDataWindow, switchToFindWorkoutDataUpdateWindow, switchToDeleteWorkoutDataWindow, switchToViewWorkoutDataWindow, switchToExerciseDatabaseWindow = \
        pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal(), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Workout Data Database')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.enterWorkout = QPushButton("Enter Workout Data")
        self.enterWorkout.clicked.connect(self.goToEnterWorkoutDataWindow)
        self.updateWorkout = QPushButton("Update Workout Data")
        self.updateWorkout.clicked.connect(self.goToFindWorkoutDataUpdateWindow)
        self.deleteWorkout = QPushButton("Delete Workout Data")
        self.deleteWorkout.clicked.connect(self.goToDeleteWorkoutDataWindow)
        self.viewWorkout = QPushButton("View Workout Data")
        self.viewWorkout.clicked.connect(self.goToViewWorkoutDataWindow)
        
        self.backButton = QPushButton('Back To Database Configuration')
        self.backButton.clicked.connect(self.goToExerciseDatabaseWindow)

        self.addToLayout = [(self.enterWorkout, 0, 0, 1, 1),
                            (self.updateWorkout, 1, 0, 1, 1),
                            (self.deleteWorkout, 2, 0, 1, 1),
                            (self.viewWorkout, 3, 0, 1, 1),
                            (self.backButton, 4, 0, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    
    def goToEnterWorkoutDataWindow(self):
        self.switchToEnterWorkoutDataWindow.emit()
    
    def goToFindWorkoutDataUpdateWindow(self):
        self.switchToFindWorkoutDataUpdateWindow.emit()
    
    def goToDeleteWorkoutDataWindow(self):
        self.switchToDeleteWorkoutDataWindow.emit()

    def goToViewWorkoutDataWindow(self):
        self.switchToViewWorkoutDataWindow.emit()

    def goToExerciseDatabaseWindow(self):
        self.switchToExerciseDatabaseWindow.emit()      


class EnterWorkoutDataWindow(QWidget):
    switchToWorkoutDataTableConfigWindow = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Enter Workout Data To Database')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()
        
        self.dateIDLabel = QLabel("Date*:")
        curDate = QDate.currentDate()
        self.dateIDInput = QDateEdit(curDate)
        self.dateIDInput.setMinimumDate(curDate.addYears(-2))
        self.dateIDInput.setMaximumDate(curDate.addYears(2))
        self.dateIDInput.setDisplayFormat("yyyy-MM-dd")

        self.exerciseIDLabel = QLabel("Exercise ID*:")
        self.exerciseIDInput = QLineEdit()
        self.exerciseIDInput.setPlaceholderText("What Was The Name Of The Exercise")

        self.repCountLabel = QLabel("Repetition Count*:")
        self.repCountInput = QLineEdit()
        self.repCountInput.setPlaceholderText("How Many Reps Did You Do")

        self.avgTimeBtwnRepsLabel = QLabel("Average Time Between Reps:")
        self.avgTimeBtwnRepsInput = QLineEdit()
        self.avgTimeBtwnRepsInput.setPlaceholderText("What Was The Average Amount Of Time Between Each Reps")
        
        self.setCountLabel = QLabel("Set Count*:")
        self.setCountInput = QLineEdit()
        self.setCountInput.setPlaceholderText("How Many Sets Were Completed")

        self.avgTimeBtwnSetsLabel = QLabel("Average Time Between Sets:")
        self.avgTimeBtwnSetsInput = QLineEdit()
        self.avgTimeBtwnSetsInput.setPlaceholderText("What Was The Average Amount Of Time Between Each Set")
        
        self.intensityLabel = QLabel("Intensity*:")
        self.intensityInput = QLineEdit()
        self.intensityInput.setPlaceholderText("What Was The Overall Intensity")
        
        self.equipmentUsedLabel = QLabel("Equipment Used:")
        self.equipmentUsedInput = QLineEdit()
        self.equipmentUsedInput.setPlaceholderText("None...")

        self.avgWeightUsedLabel = QLabel("Average Weight Used Used:")
        self.avgWeightUsedInput = QLineEdit()
        self.avgWeightUsedInput.setPlaceholderText("None...")
        
        self.submitButton = QPushButton("Submit Information")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Workout Data Database')
        self.backButton.clicked.connect(self.goToWorkoutDataTableConfigWindow)

        self.addToLayout = [(self.dateIDLabel, 1, 0, 1, 1), (self.dateIDInput, 1, 1, 1, 1),
                            (self.exerciseIDLabel, 2, 0, 1, 1), (self.exerciseIDInput, 2, 1, 1, 1),
                            (self.repCountLabel, 3, 0, 1, 1), (self.repCountInput, 3, 1, 1, 1),
                            (self.avgTimeBtwnRepsLabel, 4, 0, 1, 1), (self.avgTimeBtwnRepsInput, 4, 1, 1, 1),
                            (self.setCountLabel, 5, 0, 1, 1), (self.setCountInput, 5, 1, 1, 1),
                            (self.avgTimeBtwnSetsLabel, 6, 0, 1, 1), (self.avgTimeBtwnSetsInput, 6, 1, 1, 1),
                            (self.intensityLabel, 7, 0, 1, 1), (self.intensityInput, 7, 1, 1, 1),
                            (self.equipmentUsedLabel, 8, 0, 1, 1), (self.equipmentUsedInput, 8, 1, 1, 1),
                            (self.avgWeightUsedLabel, 9, 0, 1, 1), (self.avgWeightUsedInput, 9, 1, 1, 1),
                            (self.backButton, 10, 0, 1, 1), (self.submitButton, 10, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)


    def goToSubmitTable(self):
        userInput = [self.dateIDInput, # 0
                     self.exerciseIDInput, # 1
                     self.repCountInput, # 2
                     self.avgTimeBtwnRepsInput,
                     self.setCountInput,# 4
                     self.avgTimeBtwnSetsInput,
                     self.intensityInput, # 6
                     self.equipmentUsedInput,
                     self.avgWeightUsedInput]

        req = [0, 1, 2, 4, 6]
        totalReq = 0
        for num in req:
            if userInput[num].text() != "":
                pass
            else:
                print(f"Error at {userInput[num].text()}")
                return
        
        addWorkoutData = {}
        currentColInput = None
        for enum, col in enumerate(WorkoutData):
            if enum == 1:
                currentColInput = userInput[enum - 1].text()
            elif 3 <= enum:
                currentColInput = userInput[enum - 2].text()

            print(enum, currentColInput)

            if 1 <= enum and enum != 2 and currentColInput != "":
                checkData = WorkoutData[col]
                #print(enum, checkData, currentColInput)
                check = checkDataType(checkData, currentColInput)
                if check is True:
                    addWorkoutData[col] = currentColInput
                else:
                    print(f"Error at {check}")
                    return

        print(addWorkoutData)
        addIntoTable(dataBases[1][1][1], addWorkoutData)
                    
        
        

    def goToWorkoutDataTableConfigWindow(self):
        self.switchToWorkoutDataTableConfigWindow.emit()
        
    
class FindWorkoutDataUpdateWindow(QWidget):
    switchToUpdateWorkoutDataWindow, switchToWorkoutDataTableConfigWindow = pyqtSignal(list), pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Update Workout Data Database [FIND]')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.entryNumLabel = QLabel("Entry Num*:")
        self.entryNumInput = QLineEdit()
        self.entryNumInput.setPlaceholderText("")

        self.exerciseNameLabel = QLabel("Exercise Name*:")
        self.exerciseNameInput = QLineEdit()
        self.exerciseNameInput.setPlaceholderText("")

        self.dateIDLabel = QLabel("Date*:")
        curDate = QDate.currentDate()
        self.dateIDInput = QDateEdit(curDate)
        self.dateIDInput.setMinimumDate(curDate.addYears(-2))
        self.dateIDInput.setMaximumDate(curDate.addYears(2))
        self.dateIDInput.setDisplayFormat("yyyy-MM-dd")

        #self.repCountLabel = QLabel("Repetition Count:")
        #self.repCountInput = QLineEdit()
        #self.repCountInput.setPlaceholderText("")

        #self.setCountLabel = QLabel("Set Count:")
        #self.setCountInput = QLineEdit()
        #self.setCountInput.setPlaceholderText("Enter The Base Intensity Of The Exercise")

        #self.avgTimeBtwnRepsLabel = QLabel("Average Time Between Reps:")
        #self.avgTimeBtwnRepsInput = QLineEdit()
        #self.avgTimeBtwnRepsInput.setPlaceholderText("None")
        
        #self.intensityLabel = QLabel("Intensity:")
        #self.intensityInput = QLineEdit()
        #self.intensityInput.setPlaceholderText("Enter What Type Of Exercise This Is")
        
        #self.equipmentUsedLabel = QLabel("Equipment Used:")
        #self.equipmentUsedInput = QLineEdit()
        #self.equipmentUsedInput.setPlaceholderText("None")
        
        self.submitButton = QPushButton("Find Exercise")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Exercise Table Database')
        self.backButton.clicked.connect(self.goToExerciseDatabaseConfigurationWindow)

        self.addToLayout = [(self.entryNumLabel, 1, 0, 1, 1), (self.entryNumInput, 1, 1, 1, 1),
                            (self.exerciseNameLabel, 2, 0, 1, 1), (self.exerciseNameInput, 2, 1, 1, 1),
                            (self.dateIDLabel, 3, 0, 1, 1), (self.dateIDInput, 3, 1, 1, 1),
                            #(self.repCountLabel, 4, 0, 1, 1), (self.repCountInput, 4, 1, 1, 1),
                            #(self.setCountLabel, 5, 0, 1, 1), (self.setCountInput, 5, 1, 1, 1),
                            #(self.avgTimeBtwnRepsLabel, 6, 0, 1, 1), (self.avgTimeBtwnRepsInput, 6, 1, 1, 1),
                            #(self.intensityLabel, 7, 0, 1, 1), (self.intensityInput, 7, 1, 1, 1),
                            #(self.equipmentUsedLabel, 8, 0, 1, 1), (self.equipmentUsedInput, 8, 1, 1, 1),
                            (self.backButton, 9, 0, 1, 1), (self.submitButton, 9, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    

    def goToExerciseDatabaseConfigurationWindow(self):
        self.switchToWorkoutDataTableConfigWindow.emit()

    def goToSubmitTable(self):
        exerciseFound = True

        userInput = [self.entryNumInput,
                     self.dateIDInput, 
                     self.exerciseIDInput]
                     #self.repCountInput,
                     #self.setCountInput,
                     #self.avgTimeBtwnRepsInput,
                     #self.intensityInput,
                     #self.equipmentUsedInput]

        # Checking required inputs
        num = 0
        for currentColInput in userInput:
            if currentColInput.text() != "":
                num += 1
            else:
                return print(currentColInput.text())
        
        if self.entryNumInput.text() != "" and self.exerciseNameInput.text() != "":
            selectWorkoutData = {}
            columns = []
            currentColInput = None
            for num, col in enumerate(WorkoutData):
                if num < 2:
                    currentColInput = userInput[num].text()
                elif 2 < num:
                    currentColInput = userInput[num - 1].text()
                else:
                    continue

                if currentColInput != "":
                    checkData = PersonData[col]
                    check = checkDataType(checkData, currentColInput)
                    print(check)
                    if check is True:
                        columns.append(col)
                        selectWorkoutData[col] = currentColInput
                    else:
                        print(f"Error at {check}")
                        return
                    
                if num == 3:
                    break

            print(selectWorkoutData)
            selectFromTable(dataBases[1][1][1], columns, selectWorkoutData)

            if exerciseFound is True:
                self.switchToUpdateWorkoutDataWindow.emit(userInput)


class UpdateWorkoutDataWindow(QWidget):
    switchToFindUpdateExerciseWindow = pyqtSignal()

    def __init__(self, exerciseInfo):
        QWidget.__init__(self)

        self.setWindowTitle('Update Workout Data Database')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.currentEntryNumInput = exerciseInfo[0]
        self.currentExerciseIDInput = exerciseInfo[1]
        self.currentDateIDInput = exerciseInfo[2]
                        
        self.dateIDLabel = QLabel("Date*:")
        curDate = QDate.currentDate()
        self.dateIDInput = QDateEdit(curDate)
        self.dateIDInput.setMinimumDate(curDate.addYears(-2))
        self.dateIDInput.setMaximumDate(curDate.addYears(2))
        self.dateIDInput.setDisplayFormat("yyyy-MM-dd")

        self.exerciseIDLabel = QLabel("Exercise ID*:")
        self.exerciseIDInput = QLineEdit()
        self.exerciseIDInput.setPlaceholderText("What Was The ID Of The Exercise")

        self.repCountLabel = QLabel("Repetition Count*:")
        self.repCountInput = QLineEdit()
        self.repCountInput.setPlaceholderText("How Many Reps Did You Do")

        self.avgTimeBtwnRepsLabel = QLabel("Average Time Between Reps:")
        self.avgTimeBtwnRepsInput = QLineEdit()
        self.avgTimeBtwnRepsInput.setPlaceholderText("What Was The Average Amount Of Time Between Each Reps")
        
        self.setCountLabel = QLabel("Set Count*:")
        self.setCountInput = QLineEdit()
        self.setCountInput.setPlaceholderText("How Many Sets Were Completed")

        self.avgTimeBtwnSetsLabel = QLabel("Average Time Between Sets:")
        self.avgTimeBtwnSetsInput = QLineEdit()
        self.avgTimeBtwnSetsInput.setPlaceholderText("What Was The Average Amount Of Time Between Each Set")
        
        self.intensityLabel = QLabel("Intensity*:")
        self.intensityInput = QLineEdit()
        self.intensityInput.setPlaceholderText("What Was The Overall Intensity")
        
        self.equipmentUsedLabel = QLabel("Equipment Used:")
        self.equipmentUsedInput = QLineEdit()
        self.equipmentUsedInput.setPlaceholderText("None...")

        self.avgWeightUsedLabel = QLabel("Average Weight Used Used:")
        self.avgWeightUsedInput = QLineEdit()
        self.avgWeightUsedInput.setPlaceholderText("None...")
        
        self.submitButton = QPushButton("Update Exercise")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Exercise Configuration Database')
        self.backButton.clicked.connect(self.goToFindUpdateExercise)

        self.addToLayout = [(self.dateIDLabel, 1, 0, 1, 1), (self.dateIDInput, 1, 1, 1, 1),
                            (self.exerciseIDLabel, 2, 0, 1, 1), (self.exerciseIDInput, 2, 1, 1, 1),
                            (self.repCountLabel, 3, 0, 1, 1), (self.repCountInput, 3, 1, 1, 1),
                            (self.avgTimeBtwnRepsLabel, 4, 0, 1, 1), (self.avgTimeBtwnRepsInput, 4, 1, 1, 1),
                            (self.setCountLabel, 5, 0, 1, 1), (self.setCountInput, 5, 1, 1, 1),
                            (self.avgTimeBtwnSetsLabel, 6, 0, 1, 1), (self.avgTimeBtwnSetsInput, 6, 1, 1, 1),
                            (self.intensityLabel, 7, 0, 1, 1), (self.intensityInput, 7, 1, 1, 1),
                            (self.equipmentUsedLabel, 8, 0, 1, 1), (self.equipmentUsedInput, 8, 1, 1, 1),
                            (self.avgWeightUsedLabel, 9, 0, 1, 1), (self.avgWeightUsedInput, 9, 1, 1, 1),
                            (self.backButton, 10, 0, 1, 1), (self.submitButton, 10, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
    
    def goToFindUpdateExercise(self):
        self.switchToFindUpdateExerciseWindow.emit()

    def goToSubmitTable(self):
        userInput = [self.dateIDInput, 
                     self.exerciseNameInput, 
                     self.repCountInput,
                     self.setCountInput,
                     self.avgTimeBtwnRepsInput,
                     self.intensityInput,
                     self.equipmentUsedInput]

        updateWorkoutData = {}
        fromWhere = {}
        self.userData = None
        temp = [self.currentEntryNumInput, 
                self.currentDateIDInput,
                self.currentExerciseNameInput]
        
        num = 0
        num1 = 0
        for enum, col in enumerate(WorkoutData):
            if enum == 1 or 2 < enum: 
                currentColInput = userInput[num].text()
                if currentColInput != "":
                    updateWorkoutData[col] = currentColInput
                    num += 1
            if enum == 0 or enum == 1 or enum == 3:
                fromWhere[col] = temp[num1].text()
                num1 += 1
            elif enum == 2:
                fromWhere[col] = self.userData
                
        print(updateWorkoutData)
        modifyTable(dataBases[1][1][1], updateWorkoutData, fromWhere)


class DeleteWorkoutDataWindow(QWidget):
    switchToWorkoutDataTableConfigWindow = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Delete Exercise From Database')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.entryNumLabel = QLabel("Entry Num*:")
        self.entryNumInput = QLineEdit()
        self.entryNumInput.setPlaceholderText("What Is The Entry Num")

        self.exerciseNameLabel = QLabel("Exercise Name*:")
        self.exerciseNameInput = QLineEdit()
        self.exerciseNameInput.setPlaceholderText("What Is The Exercise Name")

        self.dateIDLabel = QLabel("Date*:")
        curDate = QDate.currentDate()
        self.dateIDInput = QDateEdit(curDate)
        self.dateIDInput.setMinimumDate(curDate.addYears(-2))
        self.dateIDInput.setMaximumDate(curDate.addYears(2))
        self.dateIDInput.setDisplayFormat("yyyy-MM-dd")
        
        self.submitButton = QPushButton("Delete Exercise")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.backButton = QPushButton('Back To Exercise Configuration Database')
        self.backButton.clicked.connect(self.goToExerciseDatabaseConfigurationWindow)

        self.addToLayout = [(self.entryNumLabel, 1, 0, 1, 1), (self.entryNumInput, 1, 1, 1, 1),
                            (self.exerciseNameLabel, 2, 0, 1, 1), (self.exerciseNameInput, 2, 1, 1, 1),
                            (self.dateIDLabel, 3, 0, 1, 1), (self.dateIDInput, 3, 1, 1, 1),
                            (self.backButton, 4, 0, 1, 1), (self.submitButton, 4, 1, 1, 1)]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)


    def goToSubmitTable(self):
        self.userData = None

        userInput = [self.entryNumInput, 
                     self.dateIDInput,
                     self.exerciseNameInput]

        # Checking required inputs
        num = 0
        for currentColInput in userInput:
            if currentColInput.text() != "":
                num += 1
            else:
                return print(currentColInput.text())

        deleteWorkoutData = {}
        num = 0
        for enum, col in enumerate(WorkoutData):
            currentColInput = userInput[num].text()
            if currentColInput != "" and enum != 2:
                deleteWorkoutData[col] = currentColInput
                num += 1
            elif currentColInput != "" and enum != 2:
                deleteWorkoutData[col] = self.userData
            if enum == 3:
                break
        print(deleteWorkoutData)
        deleteFromTable(dataBases[1][0][1], deleteWorkoutData)


    def goToExerciseDatabaseConfigurationWindow(self):
        self.switchToWorkoutDataTableConfigWindow.emit()


class ViewWorkoutDataWindow(QWidget):
    switchToWorkoutDataTableConfigWindow = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('View Workout Data Database')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()
        
        self.titleLabel = QLabel("View Workout Data Table Database")

        self.entryNumLabel = QLabel("Entry Num:")
        self.entryNumInput = QLineEdit()
        self.entryNumInput.setPlaceholderText("None...") 

        self.dateIDLabel = QLabel("Date:")
        curDate = QDate.currentDate()
        self.dateIDInput = QDateEdit()#curDate)
        self.dateIDInput.setMinimumDate(curDate.addYears(-5))
        self.dateIDInput.setMaximumDate(curDate.addYears(5))
        self.dateIDInput.setDisplayFormat("yyyy-MM-dd")

        self.exerciseIDLabel = QLabel("Exercise Name:")
        self.exerciseIDInput = QLineEdit()
        self.exerciseIDInput.setPlaceholderText("None...")

        self.repCountLabel = QLabel("Rep Count:")
        self.repCountInput = QLineEdit()
        self.repCountInput.setPlaceholderText("None...")

        self.avgTimeBtwnRepsLabel = QLabel("AvgTimeBtwnReps:")
        self.avgTimeBtwnRepsInput = QLineEdit()
        self.avgTimeBtwnRepsInput.setPlaceholderText("None...")
        
        self.setCountLabel = QLabel("Set Count:")
        self.setCountInput = QLineEdit()
        self.setCountInput.setPlaceholderText("None...")

        self.avgTimeBtwnSetsLabel = QLabel("AvgTimeBtwnSets:")
        self.avgTimeBtwnSetsInput = QLineEdit()
        self.avgTimeBtwnSetsInput.setPlaceholderText("None...")
        
        self.intensityLabel = QLabel("Intensity:")
        self.intensityInput = QLineEdit()
        self.intensityInput.setPlaceholderText("None...")
        
        self.equipmentUsedLabel = QLabel("Equipment Used:")
        self.equipmentUsedInput = QLineEdit()
        self.equipmentUsedInput.setPlaceholderText("None...")

        self.avgWeightUsedLabel = QLabel("AvgWeightUsed:")
        self.avgWeightUsedInput = QLineEdit()
        self.avgWeightUsedInput.setPlaceholderText("None...")

        self.modelViewTable = QSqlTableModel()
        self.modelViewTable.setTable("WorkoutDataTable")
        self.modelViewTable.setEditStrategy(QSqlTableModel.OnFieldChange)
        for enum, col in enumerate(WorkoutData):
            self.modelViewTable.setHeaderData(enum, Qt.Horizontal, col)
        self.modelViewTable.select()

        self.viewTable = QTableView()
        self.viewTable.setModel(self.modelViewTable)
        self.viewTable.resizeColumnsToContents()
        self.viewTable.show()
        #self.setCentralWidget(self.viewTable)

        self.prevButton = QPushButton("< Previous")
        self.prevButton.clicked.connect(self.goToPrevEntry)

        self.submitButton = QPushButton("Search Workout Data Table")
        self.submitButton.clicked.connect(self.goToSubmitTable)

        self.nextButton = QPushButton("Next >")
        self.nextButton.clicked.connect(self.goToNextEntry)
        
        self.backButton = QPushButton('Back To Exercise Configuration Database')
        self.backButton.clicked.connect(self.goToExerciseDatabaseConfigurationWindow)

        self.addToLayout = [(self.titleLabel, 0, 4, 1, 2),
                            (self.entryNumLabel, 1, 0, 1, 1), (self.dateIDLabel, 1, 1, 1, 1), (self.exerciseIDLabel, 1, 2, 1, 1), (self.repCountLabel, 1, 3, 1, 1), (self.avgTimeBtwnRepsLabel, 1, 4, 1, 1),
                            (self.setCountLabel, 1, 5, 1, 1), (self.avgTimeBtwnSetsLabel, 1, 6, 1, 1), (self.intensityLabel, 1, 7, 1, 1), (self.equipmentUsedLabel, 1, 8, 1, 1), (self.avgWeightUsedLabel, 1, 9, 1, 1),
                            
                            (self.entryNumInput, 2, 0, 1, 1), (self.dateIDInput, 2, 1, 1, 1), (self.exerciseIDInput, 2, 2, 1, 1), (self.repCountInput, 2, 3, 1, 1), (self.avgTimeBtwnRepsInput, 2, 4, 1, 1),
                            (self.setCountInput, 2, 5, 1, 1), (self.avgTimeBtwnSetsInput, 2, 6, 1, 1), (self.intensityInput, 2, 7, 1, 1), (self.equipmentUsedInput, 2, 8, 1, 1), (self.avgWeightUsedInput, 2, 9, 1, 1),

                            (self.prevButton, 3, 0, 1, 3), (self.submitButton, 3, 3, 1, 4), (self.nextButton, 3, 7, 1, 3),
                            (self.viewTable, 4, 1, 1, 8),
                            (self.backButton, 5, 0, 1, 10), 
                            ]
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)

    def goToExerciseDatabaseConfigurationWindow(self):
        self.switchToWorkoutDataTableConfigWindow.emit()
        
    def goToSubmitTable(self):
        userInput = [
            self.entryNumInput, self.dateIDInput, 
            self.exerciseIDInput, self.repCountInput, 
            self.avgTimeBtwnRepsInput, self.setCountInput, 
            self.avgTimeBtwnSetsInput, self.intensityInput, 
            self.equipmentUsedInput, self.avgWeightUsedInput
            ]

    def goToPrevEntry(self):
        pass
        entryNum = None

    def goToNextEntry(self):
        pass