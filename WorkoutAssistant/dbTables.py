# This variable holds the Person Table
# Everything that is labeled "NOT NULL" will be filled out by the user
#  However the user can fill out the extra information if they wish
personTable = """
CREATE TABLE IF NOT EXISTS 
  PersonTable (
  userID       INTEGER NOT NULL,
  userName     TEXT    NOT NULL,
  password     TEXT    NOT NULL,
  firstName    TEXT    NOT NULL,
  lastName     TEXT    NOT NULL,
  fitnessLevel INTEGER NOT NULL,
  bodyType     INTEGER,
  bodyGoal     INTEGER,
  bodyWeight   INTEGER,
  goalWeight   INTEGER,
  
  PRIMARY KEY (userID, userName)
);
"""

morningTable = """
CREATE TABLE IF NOT EXISTS
  MorningTable (
  mID         INTEGER PRIMARY KEY AUTOINCREMENT,
  userID      INTEGER NOT NULL,
  dateID      DATE    NOT NULL,
  awakeAt     TIME    NOT NULL,
  energyLevel INTEGER NOT NULL,
  feeling     INTEGER NOT NULL,
  food        TEXT    NOT NULL,
  drink       TEXT    NOT NULL,
  
  FOREIGN KEY (userID)
  REFERENCES  PersonTable (userID)
);
"""

nightTable = """
CREATE TABLE IF NOT EXISTS
  NightTable (
  nID         INTEGER PRIMARY KEY AUTOINCREMENT,
  userID      INTEGER NOT NULL,
  dateID      DATE    NOT NULL,
  asleepAt    TIME    NOT NULL,
  energyLevel INTEGER NOT NULL,
  feeling     INTEGER NOT NULL,
  food        TEXT    NOT NULL,
  drink       TEXT    NOT NULL,
  
  FOREIGN KEY (userID)
  REFERENCES  PersonTable (userID)
);
"""

dayLog = """
CREATE TABLE IF NOT EXISTS
  DayLogTable(
  dayLogEntryNum INTEGER PRIMARY KEY AUTOINCREMENT,
  dateID         DATE    NOT NULL,
  userID         INTEGER NOT NULL,
  mID            INTEGER,
  nID            INTEGER,

  FOREIGN KEY (userID)
  REFERENCES  PersonTable (userID),
  
  FOREIGN KEY (mID)
  REFERENCES  MorningTable (mID),
  
  FOREIGN KEY (nID)
  REFERENCES  NightTable (nID)
);
"""

# This variable holds the Exercise Table
# The user has the ability to Add/Update/Delete Exercises 
# Each exercise has a Base Intensity that can be Edited
#  but the overall intensity can be increased through reps and sets
exerciseTable = """
CREATE TABLE IF NOT EXISTS
  ExerciseTable (
  exID            INTEGER,
  exName          TEXT,
  muscleGroups    TEXT    NOT NULL,
  baseIntensity   INTEGER NOT NULL,
  exTypes         TEXT    NOT NULL,
  equipmentNeeded INTEGER NOT NULL, # 0 for No
  
 PRIMARY KEY (exID, exName)
);
"""

# This variable holds the Workout Data Table
# Including the rep/set Counts will be helpful for determining how workouts can be progressed
# I could include a rating in this able as well
workoutData = """
CREATE TABLE IF NOT EXISTS
  WorkoutDataTable (
  workoutEntryNum  INTEGER PRIMARY KEY AUTOINCREMENT,
  dateID           DATE,
  userID           INTEGER,
  exID             INTEGER NOT NULL,
  repCount         INTEGER NOT NULL,
  avgTimeBtwnReps  INTEGER,
  setCount         INTEGER NOT NULL,
  avgTimeBtwnSets  INTEGER,
  overallIntensity INTEGER NOT NULL,
  equipmentUsed    TEXT,
  avgWeightUsed    INTEGER
);
"""

# This variable holds the WorkoutsGiven Table
# Any workouts given to the user will be logged in this table
workoutsGiven = """
CREATE TABLE IF NOT EXISTS
  WorkoutsGivenTable (
  workoutGivenEntryNum INTEGER PRIMARY KEY AUTOINCREMENT,
  dateID               DATE    NOT NULL,
  userID               INTEGER NOT NULL,
  exID                 INTEGER NOT NULL,
  repCount             INTEGER NOT NULL,
  avgTimeBtwnReps      INTEGER,
  setCount             INTEGER NOT NULL,
  avgTimeBtwnSets      INTEGER,
  predictedIntensity   INTEGER NOT NULL,
  avgWeightToUse       INTEGER
);
"""

# This variable holds the Workout Data Table
# After the user completes the exercise given to them,
#  the hope is that they rate the quality of said exercise,
#   and the program will adapt future workouts
workoutFeedBack = """
CREATE TABLE IF NOT EXISTS
  WorkoutFeedbackTable (
  feedbackEntryNum     INTEGER NOT NULL,
  workoutGivenEntryNum INTEGER NOT NULL,
  userID               INTEGER NOT NULL,
  actualIntensity      INTEGER NOT NULL,
  rating               INTEGER NOT NULL,
    
  FOREIGN KEY (workoutGivenEntryNum)
  REFERENCES WorkoutsGivenTable (workoutGivenEntryNum),

  PRIMARY KEY (feedbackEntryNum, workoutGivenEntryNum)
);
"""


personDataBase = [
    [personTable, "PersonTable"],
    [morningTable, "MorningTable"],
    [nightTable, "NightTable"],
    [dayLog, "DayLogTable"]
]

workoutDataBase = [
    [exerciseTable, "ExerciseTable"],
    [workoutData, "WorkoutDataTable"],
    [workoutsGiven, "WorkoutsGivenTable"],
    [workoutFeedBack, "WorkoutFeedbackTable"]
]

dataBases = [
    personDataBase,
    workoutDataBase
]



