from speechFunct import analyzeResponse
from cameraFunct import cvtColor, COLOR_BGR2RGB, error, fps, imshow, mp, readImg, terminateWindows, time, VideoCapture as VC, waitKey
from basicImportInfo import *
from PyQt5.QtGui import QImage, QPixmap

workoutAngles = None
currentWorkout = None


class WorkoutWindow(QWidget):
    switchToMenuWindow = pyqtSignal()

    def __init__(self):
        global workoutAngles
        global currentWorkout
        self.CONTEXT = None
        QWidget.__init__(self)
        self.setWindowTitle('Workout Window')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.videoLabel = QLabel(self)
        #self.videoLabel.move(280, 120)
        #self.videoLabel.resize(640, 480)
        th = Thread()
        th.changePixmap.connect(self.captureImage)
        th.start()
        #self.show()

        workoutAngles = QLabel("____")
        currentWorkout = QLabel("____")

        self.backButton = QPushButton('Back To Menu')
        self.backButton.clicked.connect(self.goToMenuWindow)
        self.userInput = QLineEdit()
        self.userInput.returnPressed.connect(self.goToAskChatBot)

        self.chatBotMessageHistory5 = QLabel("____")
        self.chatBotMessageHistory4 = QLabel("____")
        self.chatBotMessageHistory3 = QLabel("____")
        self.chatBotMessageHistory2 = QLabel("____")
        self.chatBotMessageHistory1 = QLabel("____")

        self.addToLayout = [(self.videoLabel, 0, 0, 3, 4), (self.chatBotMessageHistory5, 0, 4, 1, 1),
                            (self.chatBotMessageHistory4, 1, 4, 1, 1),
                            (self.chatBotMessageHistory3, 2, 4, 1, 1),
                            (workoutAngles, 3, 0, 1, 2), (currentWorkout, 3, 2, 1, 2), (self.chatBotMessageHistory2, 3, 4, 1, 1),
                            (self.backButton, 4, 0, 1, 1), (self.userInput, 4, 1, 1, 2), (self.chatBotMessageHistory1, 4, 4, 1, 1)]
        
        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)

        self.setLayout(layout)
    
    def captureImage(self, image):
        self.videoLabel.setPixmap(QPixmap.fromImage(image))        

    def goToMenuWindow(self):
        terminateWindows(video)
        self.switchToMenuWindow.emit()

    def goToAskChatBot(self):
        self.chatBotMessageHistory5.setText(self.chatBotMessageHistory4.text())
        self.chatBotMessageHistory4.setText(self.chatBotMessageHistory3.text())
        self.chatBotMessageHistory3.setText(self.chatBotMessageHistory2.text())
        self.chatBotMessageHistory2.setText(self.chatBotMessageHistory1.text())

        response, self.CONTEXT = analyzeResponse(self.userInput.text(), self.CONTEXT)
        self.chatBotMessageHistory1.setText(response)

        self.userInput.clear()

repCount = 0
video = None
class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
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
        verificationTime = 2  # The program will take 2x seconds to verify the workout
        startingPreparations = time()
        beginVerification = None

        assumption = None
        assumptionMade = False
        known = False
        confirmedExercise = ""  # "bicep curl"

        exercisesCompletedList = []
        exerciseCount = 0
        nOrLatch = False
        self.repCount = 0

        endWorkout = False
        exName = None

        downTime = 5
        currentDownTime = time()
        # firstTimeCheckBool = True
        minimumRepCount = 1
    
        xLength = 720
        yHeight = 480
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


        video.set(3, xLength)
        video.set(4, yHeight)

        global workoutAngles
        global currentWorkout

        while True: 
            try:
                returned, img, assumption2, exName, \
                repCompleted, trackedAngles, \
                allLocations = readImg(video, pose, drawLM, exName,
                                       showInterest=True, showDots=False,
                                       showLines=True, showText=True, known=known,
                                       confirmedExercise=confirmedExercise)
                
                workoutAngles.setText(repCompleted[1])
                currentWorkout.setText(f"{confirmedExercise}: {self.repCount}")
                
                # print(allLocations)
                convertedLoc = []
                # Loop to adjust the Y cords of the location
                for cor in allLocations:
                    new = cor[1], yHeight - cor[2], cor[3]
                    convertedLoc.append(new)

                # server.sendto(str.encode(str(convertedLoc)), serverAddressPort)
                # print(convertedLoc)

            except TypeError:
                continue
            except RuntimeError:
                break

            pTime = fps(img, pTime)
            elapsedTime = time()

            if known is True:
                # if firstTimeCheckBool is True:
                #     firstTimeCheckBool = False
                    # currentDownTime = time()

                # Here 09/17/22
                print("\nWithin Repetition Target Range:", repCompleted)

                if repCompleted[0] is True and nOrLatch is False:
                    self.repCount += 1
                    nOrLatch = True
                    currentDownTime = int(time())

                elif repCompleted[0] is False and nOrLatch is True:
                    nOrLatch = False

                if repCompleted[0] is False:
                    if int(time()) - currentDownTime >= downTime:
                        known = False
                        assumptionMade = False
                        startingPreparations, currentDownTime = time(), time()

                        if exName.mirrored is False:
                            self.repCount /= 2

                        if self.repCount > minimumRepCount:
                            if confirmedExercise not in exerciseDict:
                                exerciseDict[confirmedExercise] = self.repCount
                            else:
                                exerciseDict[str(confirmedExercise) + "*"] = self.repCount
                            self.repCount = 0

                        # reset the values
                print(exerciseDict)
                print("Repetition Tracker:", self.repCount)

            else:
                # This allows the program to get an initial idea on what the exercise might be
                # Once it makes this assumption, the computer will wait x amount of time before checking again
                if (elapsedTime - startingPreparations) > verificationTime and assumptionMade is False:

                    try:
                        if assumptionMade is False:
                            assumption = assumption2
                            print("First assumption:", assumption)
                            assumptionMade = True
                            beginVerification = time()
                    except IndexError or TypeError:
                        assumptionMade = False

                    # Once x amount of time passes, the computer will make it's second check
                    # If current assumption matches the prior assumption, then the exercise will be seen as known

                if assumptionMade is True:
                    if (elapsedTime - beginVerification) > verificationTime:
                        print("\nTime Elapsed:", float(elapsedTime - beginVerification))
                        print("assumption1:", assumption, " | assumption2:", assumption2)
                        try:
                            if assumption == assumption2 and assumption2 is not None:
                                confirmedExercise = assumption
                                print("\nExercise Confirmed:", confirmedExercise, "\n")
                                known = True

                        except IndexError or TypeError:
                            assumptionMade = False

                        # If the assumed workout doesn't match, then the process will start over
                        else:
                            assumption = assumption2
                            startingPreparations = time()
                            assumptionMade = False

            try:
                #imshow("Picture", img)
                pass
            except error:
                pass

            if waitKey(1) & 0xFF == ord('q'):
                if self.repCount > minimumRepCount:
                    if confirmedExercise not in exerciseDict:
                        exerciseDict[confirmedExercise] = self.repCount
                    else:
                        exerciseDict[str(confirmedExercise) + "*"] = self.repCount
                    self.repCount = 0

                print(exerciseDict)
                quit()

            if returned:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cvtColor(img, COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(winLength - 150, winHeight - 150, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
