from speechFunct import analyzeResponse
from basicImportInfo import *


CurrentRepCount = None  
CurrentExercise = None
CurrentAngles = None
ShowTargetAngles = True


class WorkoutWindow(QWidget):
    switchToMenuWindow = pyqtSignal()

    def __init__(self):
        global CurrentExercise
        global CurrentRepCount
        global CurrentAngles

        QWidget.__init__(self)
        self.setWindowTitle('Workout Window')
        #self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.title = QLabel("Live Exercise View")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
        QLabel {
            font-size: 45px;
            font: bold italic "Times New Roman";

            min-height: 50px;
            max-height: 75px;
            min-width: 1080px;
            
            border: 3px solid;
            border-radius: 25%;

            margin-top: 1px;
            
            background-color: lightgray;
        }
        """)

        CurrentExercise = QLabel("Exercise: ____")
        CurrentExercise.setAlignment(Qt.AlignCenter)
        CurrentExercise.setStyleSheet("""
        QLabel {
            font-size: 25px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 30px;
            max-height: 50px;
            
            border: 3px solid;
            border-radius: 20%;

            background-color: lightgray;
            float:left;
        }
        """)
            #min-width: 400px;
            #max-width: 400px;
        
            #margin-top: 1px;
        CurrentRepCount = QLabel("Rep Count: ____")
        CurrentRepCount.setAlignment(Qt.AlignCenter)
        CurrentRepCount.setStyleSheet("""
        QLabel {
            font-size: 25px;
            font: bold italic "Times New Roman";

            min-height: 30px;
            max-height: 50px;
            min-width: 280px;
            
            border: 3px solid;
            border-radius: 20%;

            background-color: lightgray;
            text-align: center;
        }
        """)
        CurrentAngles = QLabel("Within Range: ____")
        CurrentAngles.setAlignment(Qt.AlignCenter)
        CurrentAngles.setStyleSheet("""
        QLabel {
            font-size: 25px;
            font: bold italic "Times New Roman";
            text-align: center;

            min-height: 30px;
            max-height: 50px;
            border: 3px solid;
            border-radius: 20%;

            background-color: lightgray;

            float: right;
        }
        """)
            #min-width: 400px;
            #max-width: 400px;
            
        
        self.videoLabel = QLabel(self)
        #self.videoLabel.move(280, 120)
        #self.videoLabel.resize(640, 480)
        th = Thread()
        th.changePixmap.connect(self.captureImage)
        th.start()
        #self.show()
        self.videoLabel.setAlignment(Qt.AlignCenter)
        self.videoLabel.setStyleSheet("""
        QLabel {
            height: 480px;
            text-align: center; 
            border: 3px solid;
            background-color: lightgray;

            margin-top: 0px:
            margin-bottom: 0px:
            border-radius: 25%;
        }
        """)
            #margin-left: 200px;
            #margin-right: 200px;

        #self.videoLabel.setFixedWidth(720)
            #float: left;
            #min-width: 1080px;
            #max-width: 1080px;

        self.backButton = QPushButton('Back To Menu')
        self.backButton.clicked.connect(self.goToMenuWindow)
        self.backButton.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;

            border: 1px solid;
            border-radius: 15%;
         
            background-color: lightgray;
        }
        QPushButton:hover {
            font-size: 25px;
            font: bold italic "Times New Roman";

            background-color: white;
        }
        """)
            #has to match width for each cell
            #min-width: 300px;
            #max-width: 300px;

        self.finishWorkout = QPushButton("Finish Workout")
        self.finishWorkout.clicked.connect(self.goToFinishWorkout)
        self.finishWorkout.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;

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
            #min-width: 400px;
            #max-width: 400px;

        showingLines = QPushButton("Show Target Angles")
        showingLines.clicked.connect(self.goToShowLines)
        showingLines.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-family: "Times New Roman";

            min-height: 30px;
            max-height: 50px;

            border: 1px solid;
            border-radius: 15%;
         
            background-color: lightgray;
        }
        QPushButton:hover {
            font-size: 25px;
            font: bold italic "Times New Roman";

            background-color: white;
        }
        """)
            #min-width: 380px;
            #max-width: 380px;
        
        self.addToLayout = [(self.title, 0, 0, 1, 3), 
                            (CurrentRepCount, 1, 0, 1, 1), (CurrentExercise, 1, 1, 1, 1), (CurrentAngles, 1, 2, 1, 1), 
                            (self.videoLabel, 2, 0, 1, 3),
                            (self.backButton, 3, 0, 1, 1), (showingLines, 3, 1, 1, 1), (self.finishWorkout, 3, 2, 1, 1)]
        
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)

        self.setLayout(layout)
    
    def captureImage(self, image):
        self.videoLabel.setPixmap(QPixmap.fromImage(image))        

    def goToMenuWindow(self):
        terminateWindows(video)
        self.switchToMenuWindow.emit()

    def goToFinishWorkout(self):
        pass

    def goToShowLines(self):
        global ShowTargetAngles
        if ShowTargetAngles is True:
            ShowTargetAngles = False
        else:
            ShowTargetAngles = True


repCount = 0
video = None
class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        
        def saveWorkout():
            try:
                if 2 <= self.repCount and exName.mirrored is False:
                    self.repCount //= 2

                if self.repCount > minimumRepCount:
                    # key = [setCount, repCount]
                    if exName.name not in exerciseDict:
                        exerciseDict[exName.name] = [1, self.repCount]

                    else:
                        setCount, repCount = exerciseDict[exName.name]
                        exerciseDict[exName.name] = [setCount + 1, (repCount + self.repCount) // 2]
                            
                print(exerciseDict)

            finally:
                input("ENTER To Quit")
                quit()

        def pauseWorkout():
            ent = input("ENTER 2 Resume")
            if ent == "q":
                quit()


        global defaultCam
        global video
        self.defaultCam = defaultCam
        global repCount
        self.repCount = repCount

        mPose = mp.solutions.pose
        pose = mPose.Pose()
        drawLM = mp.solutions.drawing_utils

        pTime = 0

        # Thinking of tracking the positioning of
        # tracked = {"nose": [],
        #            "leftShoulder|leftWrist": [], "rightShoulder|rightWrist": [],
        #            "leftHip|LeftAnkle": [], "rightHip|rightAnkle": []}

        exerciseDict = {}
        verificationTime = 1  # The program will take 2x seconds to verify the workout
        startingPreparations = time()
        beginVerification = None

        detected = False
        assumption = None
        assumptionMade = False
        known = False

        exercisesCompletedList = []
        exerciseCount = 0
        nOrLatch = False
        self.repCount = -1

        endWorkout = False
        exName = None

        downTime = 4
        currentDownTime = time()
        # firstTimeCheckBool = True
        minimumRepCount = 1
    
        xLength = 720
        yHeight = 480

        #abductorLegRaises,
        #barbellSquats,
        #bicepCurls,                                    
        #singleArmBicepCurls,
        #deltoidArmRaises,
        #singleArmDeltoidRaises,
        #frontLatRaises,          
        #singleArmFrontLatRaises,
        #gobletSquats,
        #shoulderPress,
        #singleArmShoulderPress

        if self.defaultCam == 0:
            video = VC(0)
        elif self.defaultCam == (0, 1):
            print("Okay")
            video = VC(1)
        elif self.defaultCam == 1:
            video = VC("C:\\Users\\Big Boi J\\Downloads\\test1.gif")  # Single Arm Bicep Curl
        elif self.defaultCam == 2:
            video = VC("C:\\Users\\Big Boi J\\Downloads\\test2.mp4")  # Bicep Curl 2
        elif self.defaultCam == 3:
            video = VC("C:\\Users\\Big Boi J\\Downloads\\test3.gif")  # Bicep Curls  need new
        elif self.defaultCam == 4:
            video = VC("C:\\Users\\Big Boi J\\Downloads\\test4.gif")  # Squat
        elif self.defaultCam == 5:
            video = VC("C:\\Users\\Big Boi J\\Downloads\\test5.gif")  # Back Squat 2
        elif self.defaultCam == 6:
            video = VC("C:\\Users\\Big Boi J\\Downloads\\test6.gif")  # Squat 3  need new
        elif self.defaultCam == 7:
            video = VC("C:\\Users\\Big Boi J\\Downloads\\test7.gif")  # Front Squats
        elif self.defaultCam == 8:
            video = VC("C:\\Users\\Big Boi J\\Downloads\\test8.gif")  # Front Squats
        elif self.defaultCam == 9:
            video = VC("C:\\Users\\Big Boi J\\Downloads\\test9.gif")
        elif self.defaultCam == 11:
            video = VC("C:\\Users\\Big Boi J\\source\\repos\\WorkoutAssistant\\WorkoutAssistant\\workoutTrainingVideos\\bicepCurls\\bicep0.mp4")
        elif self.defaultCam ==12:
            video = VC("C:\\Users\\Big Boi J\\source\\repos\\WorkoutAssistant\\WorkoutAssistant\\workoutTrainingVideos\\allExercisesVideo\\allEx.mp4")
            

        video.set(3, xLength)
        video.set(4, yHeight)

        global CurrentExercise
        global CurrentRepCount
        global CurrentAngles
        global ShowTargetAngles

        #input('Start')
        #while True: 
        while True:
            #input("Next")
            try:
                returned, img, detected, \
                exName, repCompleted, \
                allLocations = readImg(video, pose, drawLM, exName,
                                       showInterest=ShowTargetAngles, showDots=ShowTargetAngles,
                                       showLines=ShowTargetAngles, showText=ShowTargetAngles, known=known)

                #print(repCompleted)
                # print(allLocations)
                #convertedLoc = []
                # Loop to adjust the Y cords of the location
                #for cor in allLocations:
                #    new = cor[1], yHeight - cor[2], cor[3]
                    #convertedLoc.append(new)

                # server.sendto(str.encode(str(convertedLoc)), serverAddressPort)
                # print(convertedLoc)

            except TypeError as T:
                print('Error:', T)
                continue
            except RuntimeError as R:
                print('Error:', R)
                saveWorkout()
            except error:
                saveWorkout()


            #pTime = fps(img, pTime)
            elapsedTime = time()
            if known is True:
                #input("Waiting")
                # if firstTimeCheckBool is True:
                #     firstTimeCheckBool = False
                    # currentDownTime = time()

                try:
                    CurrentExercise.setText(f"Exercise: {exName.name}") 
                    CurrentRepCount.setText(f"Rep Count: {self.repCount}")
                    CurrentAngles.setText(f"Within Range: {repCompleted}")
                except AttributeError as a:
                    print("Error:", a)
                    pass

                print("\nWithin Repetition Target Range:", repCompleted, nOrLatch)
                print('\nDownTime', int(time()) - currentDownTime)
                if repCompleted is True and nOrLatch is False:
                    self.repCount += 1
                    nOrLatch = True

                elif repCompleted is not True and nOrLatch is True:
                    if nOrLatch is True:
                        currentDownTime = int(time())
                        nOrLatch = False

                if repCompleted is False:
                    # Prevents the DownTime from entering; norLatch is True when the rep is completed, but downTime 
                    if int(time()) - currentDownTime >= downTime and nOrLatch is not True:
                        try:
                            CurrentExercise.setText(f"Exercise: ____") 
                            CurrentRepCount.setText(f"Rep Count: ____")
                            CurrentAngles.setText(f"Within Range: ____")
                        except AttributeError as a:
                            print("Error:", a)
                            pass


                        known = False
                        assumptionMade = False
                        startingPreparations, currentDownTime = time(), time()

                        if 2 <= self.repCount and exName.mirrored is False:
                            self.repCount //= 2

                        if self.repCount > minimumRepCount:
                            # key = [setCount, repCount]
                            if exName.name not in exerciseDict:
                                exerciseDict[exName.name] = [1, self.repCount]

                            else:
                                setCount, repCount = exerciseDict[exName.name]
                                exerciseDict[exName.name] = [setCount + 1, (repCount + self.repCount) // 2]
                            self.repCount = -1

                        # reset the values
                print(exerciseDict)
                #print("Repetition Tracker:", self.repCount)

            else:
                # This allows the program to get an initial idea on what the exercise might be
                # Once it makes this assumption, the computer will wait x amount of time before checking again
                print(elapsedTime, '-', startingPreparations, '>', verificationTime)
                if (elapsedTime - startingPreparations) > verificationTime and assumptionMade is False:
                    try:
                        if assumptionMade is False:
                            assumption = exName
                            print("First assumption:", [x.name for x in assumption])
                            assumptionMade = True
                            beginVerification = time()
                    except IndexError as I:
                        assumptionMade = False
                        print('Error:', I)
                    except TypeError as T:
                        print('Error:', T)
                        assumptionMade = False

                    # Once x amount of time passes, the computer will make it's second check
                    # If current assumption matches the prior assumption, then the exercise will be seen as known

                if assumptionMade is True:
                    print(elapsedTime, '-', beginVerification, '>', verificationTime)
                    if (elapsedTime - beginVerification) > verificationTime:
                        print("\nTime Elapsed Between Detection:", float(elapsedTime - beginVerification))
                        print("assumption1:", [x.name for x in assumption], " | assumption2:", [x.name for x in exName])
                        try:
                            if detected is False:
                                assumptionMade = False
                            else:
                                try:
                                    print(assumption, exName)
                                    if exName == assumption or exName in assumption:
                                        exName = exName[0]
                                        print("\nExercise Confirmed:", exName.name, "\n")
                                        known = True
                                    # If the assumed workout doesn't match, then the process will start over
                                    else:
                                        assumption = exName
                                        startingPreparations = time()
                                        assumptionMade = False
                                except TypeError:
                                    assumption = exName
                                    startingPreparations = time()
                                    assumptionMade = False

                        except IndexError or TypeError:
                            assumption = exName 
                            startingPreparations = time()
                            assumptionMade = False

            try:
                #img = flip(img, 1)
                #imshow("Picture", img)
                pass
            except error:
                pass

            if waitKey(1) & 0xFF == ord('q'):
                pauseWorkout()
                #saveWorkout()

            
            #if waitKey(1) & 0xFF == ord('p'):
            #    pauseWorkout()

            if returned:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cvtColor(img, COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(720, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
