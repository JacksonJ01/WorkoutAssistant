from cv2 import resize, imshow, error, putText, COLOR_BGR2RGB, FILLED, \
    destroyAllWindows, FONT_HERSHEY_PLAIN, cvtColor, circle, waitKey, VideoCapture
import mediapipe as mp
from math import atan2, pi
from time import time


def readImg(video, pose, drawLM, exName, showInterest=False, showDots=False,
            showLines=False, showText=False, known=False, confirmedExercise=None):
    returned, img = video.read()

    try:
        img = resize(img, (900, 500))
    except error:
            pass

    if not returned:
        return

    img, results = findLandmarks(img, pose)
    img, locationsOfInterest, allLocations = getLandmarkLocations(img, drawLM, results, showInterest, showDots,
                                                                  showLines)
    assumption = None
    try:
        img, leftAngles, rightAngles = calculateAngle(img, locationsOfInterest, showText)
        if known is True:
            return returned, img, assumption, exName, detectRepetitions(confirmedExercise, leftAngles, rightAngles, allLocations, exName), trackAngles(leftAngles, rightAngles), allLocations
        else:
            assumption, exName = detectExercise(leftAngles, rightAngles, locationsOfInterest)

    except TypeError:
        pass

    return returned, img, assumption, exName, [False, None], None, allLocations


# _____________________________________________________________________________
def findLandmarks(img, pose):
    """Hello"""

    imgRGB = cvtColor(img, COLOR_BGR2RGB)
    results = pose.process(imgRGB).pose_landmarks
    return img, results


# _____________________________________________________________________________
def getLandmarkLocations(img, drawLM, results, showInterest=False, showDots=False, showLines=False):
    """"""

    locationsOfInterests = []
    allLocations = []
    if results:
        if showLines is True:
            connDots = mp.solutions.pose.POSE_CONNECTIONS
            drawLM.draw_landmarks(img, results, connDots)

        elif showDots is True:
            drawLM.draw_landmarks(img, results)

        for num, info in enumerate(results.landmark):
            

            h, w, c = img.shape
            xcor, ycor, zcor, vis = int(info.x * w), int(info.y * h), info.z, info.visibility
            allLocations.append((num, xcor, ycor, zcor, vis))

            if num in [0, 11, 12, 13, 14, 15, 16,
                       23, 24, 25, 26, 27, 28]:
                locationsOfInterests.append((num, xcor, ycor, zcor, vis))

                if showDots is True or showInterest is True and num != 0:
                    circle(img, (xcor, ycor), 5, (0, 0, 0), FILLED)

    return img, locationsOfInterests, allLocations


# _____________________________________________________________________________
def calculateAngle(img, locationsOfInterest, showText=False):
    """"""
    # 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
    # 0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28
    
    # Nose 0,
    # leftShoulder 11, leftElbow 13, leftWrist 15,
    # rightShoulder 12, rightElbow 14, rightWrist 16,
    # leftHip 23, leftKnee 25, leftAnkle 27,
    # rightHip 24, rightKnee 26, rightAnkle 28

    leftAngles = []
    rightAngles = []
    for sub, _ in enumerate(locationsOfInterest):
        try:
            x1, y1 = None, None
            x2, y2 = None, None
            x3, y3 = None, None

            if sub in [1, 2, 7, 8]:
                _, x1, y1, _, _ = locationsOfInterest[sub]
                _, x2, y2, _, _ = locationsOfInterest[sub + 2]
                _, x3, y3, _, _ = locationsOfInterest[sub + 4]

            elif sub in [3, 4]:
                _, x1, y1, _, _ = locationsOfInterest[sub]
                _, x2, y2, _, _ = locationsOfInterest[sub - 2]
                _, x3, y3, _, _ = locationsOfInterest[sub + 4]

            elif sub in [9, 10]:
                _, x1, y1, _, _ = locationsOfInterest[sub]
                _, x2, y2, _, _ = locationsOfInterest[sub - 2]
                _, x3, y3, _, _ = locationsOfInterest[sub - 8]

            #
            angle = abs(atan2(y3 - y2, x3 - x2) - atan2(y1 - y2, x1 - x2))
            angle = int(angle * 180 / pi)

            if angle > 180:
                # The joints will never bend the opposite way,
                # so this prevents the program from giving you an angle greater than 180
                angle = 180 - (angle - 180)

            if sub % 2 == 0:
                #formatting the data to be saved in a list as a tuple element
                rightAngles.append((sub, angle, locationsOfInterest[sub - 2][3]))
            else:
                leftAngles.append((sub, angle, locationsOfInterest[sub - 2][3]))

            # Display the angles on screen
            if showText is True:
                img = displayText(img, str(angle), (x2, y2), 2, (255, 0, 0))

        except TypeError:
            pass

    #Elbow angles     | 1, 2
    #Shoulder angles  | 3, 4
    #Knee angles      | 7, 8
    #Hip angles#      | 9, 10
    
    try:
        leftAngles[0], leftAngles[1] = leftAngles[1], leftAngles[0]
        leftAngles[2], leftAngles[3] = leftAngles[3], leftAngles[2]

        rightAngles[0], rightAngles[1] = rightAngles[1], rightAngles[0]
        rightAngles[2], rightAngles[3] = rightAngles[3], rightAngles[2]
        
        # Reformatted
        #Shoulder angles  | 3, 4
        #Elbow angles     | 1, 2
        #Hip angles#      | 9, 10
        #Knee angles      | 7, 8
        print(leftAngles, rightAngles)


        return img, leftAngles, rightAngles

    except IndexError:
        pass


# _____________________________________________________________________________
def checkVisibility(leftVisibility: list, rightVisibility: list):
    """"""

    leftShoulder = leftVisibility[0][2]
    leftElbow = leftVisibility[1][2]
    # leftWrist = leftVisibility
    leftHip = leftVisibility[2][2]
    leftKnee = leftVisibility[3][2]
    # leftAnkle = leftVisibility
    leftVisibility = [leftShoulder, leftElbow, leftHip, leftKnee]

    rightShoulder = rightVisibility[0][2]
    rightElbow = rightVisibility[1][2]
    # rightWrist = rightVisibility
    rightHip = rightVisibility[2][2]
    rightKnee = rightVisibility[3][2]
    # rightAnkle = rightVisibility
    rightVisibility = [rightShoulder, rightElbow, rightHip, rightKnee]

    visibility = [[], []]
    for left in leftVisibility:
        if left > .85:
            visibility[0].append(True)
        else:
            visibility[0].append(False)

    for right in rightVisibility:
        if right > .85:
            visibility[1].append(True)
        else:
            visibility[1].append(False)

    # print(visibility)
    return visibility


# _____________________________________________________________________________
class Exercise:
    """"""

    def __init__(self, name,
                 lpit, lelbow, lhip, lknee,
                 rpit, relbow, rhip, rknee,
                 mirrored=True,
                 specificPositioning=None):
        """
        Each exercise will have its own set of angles, and other attributes
        """
        self.name = name
        self.leftAngles = [lpit, lelbow, lhip, lknee]
        self.rightAngles = [rpit, relbow, rhip, rknee]
        self.mirrored = mirrored
        self.specific = specificPositioning

    def exerciseLeftAngles(self):
        return self.leftAngles

    def exerciseRightAngles(self):
        return self.rightAngles

"""
# 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
# 0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28

Elbow Angle, Shoulder Angle, Hip Angle, Knee Angle

Nose 0, 
0
leftShoulder 11, leftElbow 13, leftWrist 15,
1, 2, 3
rightShoulder 12, rightElbow 14, rightWrist 16,
4, 5, 6
leftHip 23, leftKnee 25, leftAnkle 27,
7, 8, 9
rightHip 24, rightKnee 26, rightAnkle 28
10, 11, 12

(num, xcor, ycor, zcor, vis)

"""
def trackLocation(exerciseName, loc: list):
    for exercise in exercises:
        #
    pass

abductorLegRaises = Exercise("Abductor Leg Raises",
                             (0, 180, 180), (0, 180, 180), (90, 180, 150), (160, 180, 180),
                             (0, 180, 180), (0, 180, 180), (90, 180, 135), (160, 180, 180),
                             False
                             1)

barbellSquats = Exercise("Barbell Squats",
                         (75, 110, 110), (15, 110, 110), (0, 150, 150), (0, 150, 150),
                         (15, 110, 110), (15, 110, 110), (0, 150, 150), (0, 150, 150),
                         True,
                         ["", "", "", ""]
                         2)

bicepCurls = Exercise("Bicep Curls",
                      (0, 110, 75), (0, 45, 45), (120, 180, 180), (120, 180, 180),
                      (0, 110, 75), (0, 45, 45), (120, 180, 180), (120, 180, 180),
                      True)

deltoidArmRaises = Exercise("Deltoid Arm Raises",
                        (45, 110, 90), (150, 180, 180), (150, 180, 180), (120, 180, 180),
                        (45, 110, 90), (150, 180, 180), (150, 180, 180), (120, 180, 180),
                        True,
                        ["", "", "", ""]
                        )

"""
# 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
# 0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28

Elbow Angle, Shoulder Angle, Hip Angle, Knee Angle

Nose 0, 
0
leftShoulder 11, leftElbow 13, leftWrist 15,
1, 2, 3
rightShoulder 12, rightElbow 14, rightWrist 16,
4, 5, 6
leftHip 23, leftKnee 25, leftAnkle 27,
7, 8, 9
rightHip 24, rightKnee 26, rightAnkle 28
10, 11, 12

(num, xcor, ycor, zcor, vis)

"""


frontLatRaises = Exercise("Front Lat Raises",
                        (0, 110, 90), (120, 180, 180), (120, 180, 180), (120, 180, 180),
                        (0, 110, 90), (120, 180, 180), (120, 180, 180), (120, 180, 180),
                        True
                        )

gobletSquats = Exercise("Goblet Squats",
                        (0, 30, 30), (0, 50, 50), (0, 150, 150), (0, 150, 150),
                        (0, 30, 30), (0, 50, 50), (0, 150, 150), (0, 150, 150),
                        True
                        )

shoulderPress = Exercise("Shoulder Press",
                        (30, 180, 110), (60, 110, 90), (120, 180, 180), (120, 180, 180),
                        (30, 180, 110), (60, 110, 90), (120, 180, 180), (120, 180, 180),
                        True
                        )

"""
# 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
# 0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28

Elbow Angle, Shoulder Angle, Hip Angle, Knee Angle

Nose 0, 
0
leftShoulder 11, leftElbow 13, leftWrist 15,
1, 2, 3
rightShoulder 12, rightElbow 14, rightWrist 16,
4, 5, 6
leftHip 23, leftKnee 25, leftAnkle 27,
7, 8, 9
rightHip 24, rightKnee 26, rightAnkle 28
10, 11, 12

(num, xcor, ycor, zcor, vis)

"""



singleArmBicepCurls = Exercise("Single Arm Bicep Curls",
                               (0, 110, 75), (0, 45, 45), (120, 180, 180), (120, 180, 180),
                               (0, 110, 75), (0, 45, 45), (120, 180, 180), (120, 180, 180)
                               )

singleArmFrontLatRaises = Exercise("Single Arm Front Lat Raises",
                        (0, 110, 90), (120, 180, 180), (120, 180, 180), (120, 180, 180),
                        (0, 110, 90), (120, 180, 180), (120, 180, 180), (120, 180, 180),
                        False
                        )


singleDeltoidArmRaises = Exercise("Single Arm Deltoid Raises",
                        (45, 110, 90), (150, 180, 180), (150, 180, 180), (120, 180, 180),
                        (45, 110, 90), (150, 180, 180), (150, 180, 180), (120, 180, 180),
                        False
                        )

singleArmShoulderPress = Exercise("Single Arm Shoulder Press",
                        (30, 180, 110), (60, 180, 90), (120, 180, 180), (120, 180, 180),
                        (30, 180, 110), (60, 180, 90), (120, 180, 180), (120, 180, 180),
                        True
                        )


exercises = {abductorLegRaises: [abductorLegRaises.exerciseLeftAngles(),
                                 abductorLegRaises.exerciseRightAngles()],

             barbellSquats: [barbellSquats.exerciseLeftAngles(),
                             barbellSquats.exerciseRightAngles()],
             
             bicepCurls: [bicepCurls.exerciseLeftAngles(),
                          bicepCurls.exerciseRightAngles()],

             deltoidArmRaises: [deltoidArmRaises.exerciseLeftAngles(),
                               deltoidArmRaises.exerciseRightAngles()],

             frontLatRaises: [frontLatRaises.exerciseLeftAngles(),
                              frontLatRaises.exerciseRightAngles()],

             gobletSquats: [gobletSquats.exerciseLeftAngles(),
                            gobletSquats.exerciseRightAngles()],
             
             shoulderPress: [shoulderPress.exerciseLeftAngles(),
                             shoulderPress.exerciseRightAngles()],

             singleArmBicepCurls: [singleArmBicepCurls.exerciseLeftAngles(),
                                   singleArmBicepCurls.exerciseRightAngles()],
             
             singleArmFrontLatRaises: [singleArmFrontLatRaises.exerciseLeftAngles(),
                                       singleArmFrontLatRaises.exerciseRightAngles()],

             singleDeltoidArmRaises: [singleDeltoidArmRaises.exerciseLeftAngles(),
                                      singleDeltoidArmRaises.exerciseRightAngles()],

             singleArmShoulderPress: [singleArmShoulderPress.exerciseLeftAngles(),
                                      singleArmShoulderPress.exerciseRightAngles()]
             }


# _____________________________________________________________________________
def detectExercise(leftAngles, rightAngles, loc):
    """
    Exercises listed below have 2 lists. These lists correlate to the major and minor angles list;
    When the computer checks for the exercises, it will loop through the list and append that to another loop#

    The first [] takes you to either the:
    exerciseLeftAngles list: [0] or
    exerciseRightAngles list [1]

    The second [] takes you to the specific angle range for each exercise:
    Shoulder Angle Range: [0]
    Elbow Angle Range: [1]
    Knee Angle Range: [2]
    Hip Angle Range: [3]

    The third [] takes you to the:
    Minimum range: [0]
    Maximum range: [1]

    
    _________


    # 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
    # 0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28

    Elbow Angle, Shoulder Angle, Hip Angle, Knee Angle

    Nose 0, 
    0
    leftShoulder 11, leftElbow 13, leftWrist 15,
    1, 2, 3
    rightShoulder 12, rightElbow 14, rightWrist 16,
    4, 5, 6
    leftHip 23, leftKnee 25, leftAnkle 27,
    7, 8, 9
    rightHip 24, rightKnee 26, rightAnkle 28
    10, 11, 12

    (num, xcor, ycor, zcor, vis)

    """



    potentialExercises = []
    mirrored = {}
    angles = leftAngles, rightAngles
    for exercise in exercises:

        try:
            mirrored[exercise.name] = [False, False]
            for sub in range(2):
                if (exercises[exercise][sub][0][0] <= angles[sub][0][1] <= exercises[exercise][sub][0][1] and
                        exercises[exercise][sub][1][0] <= angles[sub][1][1] <= exercises[exercise][sub][1][1] and
                        exercises[exercise][sub][2][0] <= angles[sub][2][1] <= exercises[exercise][sub][2][1] and
                        exercises[exercise][sub][3][0] <= angles[sub][3][1] <= exercises[exercise][sub][3][1]):
                    mirrored[exercise.name][sub] = True
                    if exercise not in potentialExercises:
                        potentialExercises.append(exercise)
        except IndexError:
            pass

    for exer in potentialExercises:

        # check if exer returns True in the trackLocation section


        a, b = mirrored[exer.name]
        if exer.mirrored is True:
            if a == b:
                pass
            else:
                potentialExercises.remove(exer)

        else:
            if a == b:
                potentialExercises.remove(exer)
            else:
                pass

    try:
        exName = potentialExercises[0]
        return exName.name, exName
    except IndexError:
        pass


# _____________________________________________________________________________
def detectRepetitions(confirmedExercise, leftAngles, rightAngles, loc=None, exName=None):
    # print(f"\nDetecting Reps For: {confirmedExercise}\n")
    try:
        currentAngle = leftAngles, rightAngles
        _exName = [exName.exerciseLeftAngles(), exName.exerciseRightAngles()]

        reps = [False, False]
        # Display for a visual of the angles at work
#        paddedPrint = f"""
#                |      Left Side      |      Right Side
#Shoulder Angle  |  {padding(f'{_exName[0][0][0]} <= {currentAngle[0][1][1]} <= {_exName[0][0][2]}')}|  {padding(f'{_exName[1][0][0]} <= {currentAngle[1][1][1]} <= {_exName[1][0][2]}')}|
#Elbow Angle     |  {padding(f'{_exName[0][1][0]} <= {currentAngle[0][0][1]} <= {_exName[0][1][2]}')}|  {padding(f'{_exName[1][1][0]} <= {currentAngle[1][0][1]} <= {_exName[1][1][2]}')}|
#Hip Angle       |  {padding(f'{_exName[0][2][0]} <= {currentAngle[0][2][1]} <= {_exName[0][2][2]}')}|  {padding(f'{_exName[1][2][0]} <= {currentAngle[1][2][1]} <= {_exName[1][2][2]}')}|
#Knee Angle      |  {padding(f'{_exName[0][3][0]} <= {currentAngle[0][3][1]} <= {_exName[0][3][2]}')}|  {padding(f'{_exName[1][3][0]} <= {currentAngle[1][3][1]} <= {_exName[1][3][2]}')}|"""

        # print(paddedPrint)
        majorPoints = [{"Shoulder": [currentAngle[0][1][1], currentAngle[1][1][1]]}, 
                       {"Elbow": [currentAngle[0][0][1], currentAngle[1][0][1]]}, 
                       {"Hip": [currentAngle[0][2][1], currentAngle[1][2][1]]}, 
                       {"Knee": [currentAngle[0][3][1], currentAngle[0][1][1]]}]

        print(confirmedExercise, majorPoints)

        for sub in range(2):
            if _exName[sub][0][0] <= currentAngle[sub][0][1] <= _exName[sub][0][2] and \
                    _exName[sub][1][0] <= currentAngle[sub][1][1] <= _exName[sub][1][2] and \
                    _exName[sub][2][0] <= currentAngle[sub][2][1] <= _exName[sub][2][2] and \
                    _exName[sub][3][0] <= currentAngle[sub][3][1] <= _exName[sub][3][2]:
                reps[sub] = True
            else:
                reps[sub] = False

        # print(reps)
        if reps[0] is True or reps[1] is True:
            return [True, majorPoints]
        else:
            return [False, majorPoints]
    except IndexError:
        pass


# _____________________________________________________________________________
def trackMovement(num, xcor, ycor):
    # Nose, leftShoulder, leftElbow, leftWrist, rightShoulder, rightElbow, rightWrist,
    # leftHip, leftKnee, leftAnkle, rightHip, rightKnee, rightAnkle
    # if num == 0:
    #     pass
    return


# _____________________________________________________________________________
def trackAngles(leftAngles, rightAngles):
    return


# _____________________________________________________________________________
def displayText(img, txt, location: tuple, size=1, color=(255, 0, 0), thickness=3):
    putText(img, txt, location, FONT_HERSHEY_PLAIN, size, color, thickness)
    return img


# _____________________________________________________________________________
def fps(img, pTime):
    try:
        cTime = time()
        frames = 1 / (cTime - pTime)
        pTime = cTime

        putText(img, str(int(frames)), (30, 30), FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
    except ZeroDivisionError:
        pass
    return pTime


# _____________________________________________________________________________
def terminateWindows(video):
    video.release()
    destroyAllWindows()


def padding(pad):
    padless = len(pad)
    if padless < 19:
        pad += " " * (19 - padless)
    return pad


def findDur(imgObj):
    imgObj.seek(0)
    total = 0
    while True:
        try:
            # print(total)
            frame_duration = imgObj.info['duration']  # returns current frame duration in milli sec.
            total += frame_duration
            # now move to the next frame of the gif
            imgObj.seek(imgObj.tell() + 1)  # image.tell() = current frame

        except EOFError:
            return total / 1000

#
# gif = Image.open("C:\\Users\\Big Boi J\\Downloads\\test1.gif")
# length = findDur(gif)
# print(length / 1000)



# _____________________________________________________________________________
# _____________________________________________________________________________
def objetDetection():
    return
