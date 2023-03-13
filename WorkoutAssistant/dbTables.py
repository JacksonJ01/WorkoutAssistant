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
    
  PRIMARY KEY (userID, userName)
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
  userID           INTEGER,
  dateID           DATE,
  exID             INTEGER NOT NULL,
  setCount         INTEGER NOT NULL,
  repCount         INTEGER NOT NULL,
);
"""


dataBases = [
    [personTable, "PersonTable"],
    [exerciseTable, "ExerciseTable"],
    [workoutData, "WorkoutDataTable"],
] 


