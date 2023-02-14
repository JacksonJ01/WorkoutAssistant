from dbTables import dataBases
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlQuery


# creates the database###############################################################################3
def workoutDatabase():
    #connect = None
    #try:
    connect = QSqlDatabase.addDatabase("QSQLITE")
    connect.setDatabaseName("workoutDB.sqlite")
    print('connection successful'.upper())
    #except Error as oops:
    #    print('there has been an error:', oops)
    
    try:
        if connect.isOpen():  
            return connect
    except:
        print("Error")


def addIntoTable(table: str, data: dict):
    global dbConnection

    columnName = [col for col in data]
    valueName = []

    for val in data:
        valueName.append(data[val])

    colFormat = ""
    for col in columnName:
        colFormat += f"{col}, "
    valFormat = ""
    for val in valueName:
        valFormat += f"'{val}', "
    colFormat, valFormat = colFormat[:-2], valFormat[:-2]
 
    addToTable = f"""
    INSERT INTO
        {table} 
        ({colFormat})
    VALUES
        ({valFormat})"""

    #try: 
    #    if dbConnection.isOpen():
    #        return QSqlQuery().exec(addToTable)
    #except: 
    #    print("Could Not")

    print(addToTable)
    


def clearTable(clearPersonTable=False, clearMorningTable=False, 
               clearNightTable=False, clearDayLogTable=False,
               clearExerciseTable=False, clearWorkoutDataTable=False, 
               clearWorkoutsGivenTable=False, clearWorkoutFeedbackTable=False,
               clearAll=False, clearAllPassword=None):
    
    global dbConnection

    tablesToClear = [
        [clearPersonTable, clearMorningTable, 
         clearNightTable, clearDayLogTable],
        [clearExerciseTable, clearWorkoutDataTable, 
         clearWorkoutsGivenTable, clearWorkoutFeedbackTable]
         ]

    if True in tablesToClear or (clearAll is True and clearAllPassword is None):
        for database, clearTable in enumerate(tablesToClear):
            for table, clear in enumerate(clearTable):
                if clear is True or (clearAll is True and clearAllPassword is None):
#                    print(dataBases[database][table][1])
                    dropTable = f"""
                    drop table if exists
                      {dataBases[database][table][1]}
                    """

                    try: 
                        if dbConnection.isOpen():
                            QSqlQuery().exec(dropTable)
                    except: 
                        print("Could Not")


def createTable( table: str):
    global dbConnection

    try: 
        if dbConnection.isOpen():
            QSqlQuery().exec(table)
    except:
        print("Could Not")
    print(table)

def deleteFromTable(table: str, fromWhere: dict):
    global dbConnection

    fromFormat = ""
    for col in fromWhere:
        fromFormat += f"{col} = '{fromWhere[col]}' AND "
    fromFormat = fromFormat[:-5]
    
    delFromTable = f"""
    DELETE FROM 
        {table}
    WHERE
        {fromFormat}
    """

    #try: 
    #    if dbConnection.isOpen():
    #        QSqlQuery().exec(delFromTable)
    #except: 
    #    print("Could Not")
    
    print(delFromTable)
        

def modifyTable(table: str, toSet: dict, fromWhere: dict):
    global dbConnection

    setFormat = ""
    for setCol in toSet:
        setFormat += f"{setCol} = '{toSet[setCol]}', "
    setFormat = setFormat[:-2]

    fromFormat = ""
    for col in fromWhere:
        fromFormat += f"{col} = '{fromWhere[col]}' AND "
    fromFormat = fromFormat[:-5]

    modTable = f"""
    UPDATE
        {table}
    SET
        {setFormat}
    WHERE
        {fromFormat}
    """

    #try: 
    #    if dbConnection.isOpen():
    #        QSqlQuery().exec(modTable)
    #except: 
    #    print("Could Not")
    
    print(modTable)


def selectFromTable(table: str, columns: list, fromWhere: dict):

    global dbConnection
    colFormat = ""
    for col in columns:
        colFormat += f"{col}, "
    colFormat = colFormat[:-2]

    fromFormat = ""
    for col in fromWhere:
        fromFormat += f"{col} = '{fromWhere[col]}' AND "
    fromFormat = fromFormat[:-5]

    selFromTable = f"""
    SELECT
        {colFormat}
    FROM
        {table}
    WHERE  
            {fromFormat}
    """

    #try: 
    #    if dbConnection.isOpen():
    #        QSqlQuery().exec(selFromTable)
    #except: 
    #    print("Could Not")

    print(selFromTable)


dbConnection = None # workoutDatabase()
#print(dbConnection.isOpen())



#clearTable(dbConnection, clearAll=True)

#for database in dataBases:
#   for table in database:
#       print(table[0])
#       createTable(dbConnection, table[0])


def checkReq(userInput:list, req: list = None):
    if req is None:
        num = 0
        for currentColInput in userInput:
            if currentColInput.text() != "":
                num += 1
            else:
                return False, num
    else:
        for num in req:
            if userInput[num].text() != "":
                pass
            else:
                return False, num


def checkDataType(dataType: int, data):
    try:
        if dataType == 1:
            data = int(data)
        elif 2 <= dataType <= 3:
            pass

        return True

    except ValueError:
        return data
    except TypeError:
        return data


# TEXT: 0
# INTEGER: 1
# DATE: 2
# TIME: 3
PersonData = {
    "userID": 1,
    "userName": 0,
    "password": 0,
    "firstName": 0,
    "lastName": 0,
    "fitnessLevel": 1,
    "bodyType": 1,
    "bodyGoal": 1,
    "bodyWeight": 1,
    "goalWeight": 1
        }

MorningData = {
    "mID": 1,
    "userID": 1,
    "dateID": 2,
    "awakeAt": 3,
    "energyLevel": 1,
    "feeling": 1,
    "food": 0,
    "drink": 0,
   }

NightData = {
    "nID": 1,
    "userID": 1,
    "dateID": 2,
    "asleepAt": 3,
    "energyLevel": 1,
    "feeling": 1,
    "food": 0,
    "drink": 0
        }

DayLogData = {
    "dayLogEntryNum": 1,
    "dateID": 2,
    "userID": 1,
    "mID": 1,
    "nID": 1,
   }

# TEXT: 0
# INTEGER: 1
# DATE: 2
# TIME: 3
ExerciseData = {
    "exID": 1,
    "exName": 0,
    "muscleGroups": 0,
    "baseIntensity": 1,
    "exTypes": 0,
    "equipmentNeeded": 1
    }

WorkoutData = {
    "workoutEntryNum": 1,
    "dateID": 2,
    "userID": 1,
    "exID": 0,
    "repCount": 1,
    "avgTimeBtwnReps": 1,
    "setCount": 1,
    "avgTimeBtwnSets": 1,
    "overallIntensity": 1,
    "equipmentUsed": 0,
    "avgWeightUsed": 1
   }

WorkoutGivenData = {
    "workoutGivenEntryNum": 1,
    "dateID": 2,
    "userID": 1,
    "exName": 0,
    "repCount": 1,
    "avgTimeBtwnReps": 1,
    "setCount": 1,
    "predictedIntensity": 1,
    "avgWeightToUse": 1
   }

WorkoutFeedBackData = {
    "feedbackEntryNum": 1,
    "workoutGivenEntryNum": 1,
    "userID": 1,
    "actualIntensity": 1,
    "rating": 1
   }