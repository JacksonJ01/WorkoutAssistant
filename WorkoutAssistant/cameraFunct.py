from pickle import FALSE
from cv2 import resize, imshow, error, putText, COLOR_BGR2RGB, flip, FILLED, \
    destroyAllWindows, FONT_HERSHEY_PLAIN, cvtColor, circle, waitKey, VideoCapture as VC
import mediapipe as mp
from time import time

from math import atan2, pi


def readImg(video, pose, drawLM, exName, showInterest=False, showDots=False,
            showLines=False, showText=False, known=False):
    returned, img = video.read()
    
    #try:
    #    img = resize(img, (900, 500))
    #except error:
    #        pass
    #if not returned:
    #    pass

    img, results = findLandmarks(img, pose)
    img, locationsOfInterest, allLocations = getLandmarkLocations(img, drawLM, results, showInterest, showDots,
                                                                  showLines)
    detected = None
    repC = False
    try:
        img, leftAngles, rightAngles = calculateAngle(img, locationsOfInterest, showText)
        
        if known is True:
            repC = detectRepetitions(leftAngles, rightAngles, exName)
            #print(repC)
        else:
            detected, exName = detectExercise(leftAngles, rightAngles, locationsOfInterest)
    except TypeError:
        pass

    return returned, img, detected, exName, repC, allLocations


# _____________________________________________________________________________
def findLandmarks(img, pose):
    """Hello"""

    imgRGB = cvtColor(img, COLOR_BGR2RGB)
    results = pose.process(imgRGB).pose_landmarks
    return img, results


# _____________________________________________________________________________
def getLandmarkLocations(img, drawLM, results, showInterest=False, showDots=False, showLines=False):
    """

    """

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
            xcor, ycor, zcor, vis = int(info.x * w), int(info.y * h), (info.z * c), info.visibility
            allLocations.append((num, xcor, ycor, zcor, vis))

            if num in [0, 11, 12, 13, 14, 15, 16,
                       23, 24, 25, 26, 27, 28]:
                locationsOfInterests.append((num, xcor, ycor, zcor, vis))

                if showDots is True or showInterest is True and num != 0:
                    circle(img, (xcor, ycor), 5, (0, 0, 0), FILLED)
                    #displayText(img, str(num), (xcor, ycor), 2, (255, 0, 0))

    return img, locationsOfInterests, allLocations


# _____________________________________________________________________________
def calculateAngle(img, locationsOfInterest, showText=False):

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
                # The node point number, angle, visibilityw
                rightAngles.append((sub, angle, locationsOfInterest[sub - 2][4]))
            else:
                leftAngles.append((sub, angle, locationsOfInterest[sub - 2][4]))

            # Display the angles on screen
            if showText is True:
                displayText(img, str(angle), (x2, y2), 2, (255, 0, 0))
                pass

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
        #print(leftAngles, rightAngles)

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
    
    
def trackLocation(specifcPositioning, loc: list):
    """
    Loc:
    # 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
    # 0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28

    Nose 0, 
    0
    leftShoulder 11, leftElbow 13, leftWrist 15,
    1, 3, 5
    rightShoulder 12, rightElbow 14, rightWrist 16,
    2, 4, 6
    leftHip 23, leftKnee 25, leftAnkle 27,
    7, 9, 11
    rightHip 24, rightKnee 26, rightAnkle 28
    8, 10, 12

    (num, xcor, ycor, zcor, vis)

    """
    checking = False
        
    if specifcPositioning == 0:
        legOut = [True, True]
        for pos in loc:
            if pos[0] != 27 or pos[0] != 28:
                leftAnkleX = loc[11][1]
                rightAnkleX = loc[12][1]
                # If the LEFT or RIGHT leg is not the furthest out, then the loop will return False
                if pos[0] % 2 != 0 and pos[0] != 27:
                    if pos[1] < leftAnkleX:
                        pass
                    else:
                        legOut[0] = False
                elif pos[0] % 2 == 0 and pos[0] != 28:
                    if rightAnkleX < pos[1]:
                        pass
                    else:
                        legOut[1] = False

        # If the loop makes it to this point without leaving, this exercise is returned as True
        # print(legOut)
        if True in legOut:
            #print("Left Ankle Is Out") if legOut[0] is True else print("Right Ankle Is Out") 
            checking = True

    elif specifcPositioning == 1:
        noseHeight = int(loc[0][2])
        avgShoulderHeight = (int(loc[1][2]) + int(loc[2][2])) // 2
        avgWristHeight = (int(loc[5][2]) + int(loc[6][2])) // 2
        avgElbowHeight = (int(loc[3][2]) + int(loc[4][2])) // 2

        if noseHeight < avgShoulderHeight < avgElbowHeight and \
            noseHeight < avgWristHeight < avgElbowHeight:
            checking = True

    elif specifcPositioning == 2:
        noseHeight = int(loc[0][2])
        LeftWristHeight = int(loc[5][2])
        RightWristHeight = int(loc[6][2])
        avgElbowHeight = (int(loc[3][2]) + int(loc[4][2])) // 2

        if noseHeight < LeftWristHeight < avgElbowHeight and \
            noseHeight < RightWristHeight < avgElbowHeight:
            checking = True

        checking = True
    elif specifcPositioning == 3:
        noseHeight = int(loc[0][2])
        avgShoulderHeight = (int(loc[1][2]) + int(loc[2][2])) // 2
        leftWristHeight = int(loc[5][2])
        rightWristHeight = int(loc[6][2])
        avgElbowHeight = (int(loc[3][2]) + int(loc[4][2])) // 2

        if ((avgShoulderHeight < avgElbowHeight < leftWristHeight) and (noseHeight < rightWristHeight < avgElbowHeight)) \
            or ((avgShoulderHeight < avgElbowHeight < rightWristHeight) and (noseHeight < leftWristHeight < avgElbowHeight)):
            checking = True

    elif specifcPositioning == 4:
        noseHeight = int(loc[0][2])

        leftWristX = int(loc[5][1])
        rightWristX = int(loc[6][1])
        avgWristHeight = (int(loc[5][2]) + int(loc[6][2])) // 2

        leftShoulderX = int(loc[1][1])
        rightShoulderX = int(loc[2][1])
        avgHipShoulderMidHeight = ((int(loc[1][2]) + int(loc[2][2])) + (int(loc[7][2]) + int(loc[8][2]))) // 4

        leftElbowX = int(loc[3][1])
        rightElbowX = int(loc[4][1])
        avgElbowHeight = (int(loc[3][2]) + int(loc[4][2])) // 2
        
        if rightWristX < rightElbowX < rightShoulderX and \
            leftShoulderX < leftElbowX < leftWristX and \
            noseHeight < avgWristHeight < avgHipShoulderMidHeight and \
            noseHeight < avgElbowHeight < avgHipShoulderMidHeight:
            checking = True

    elif specifcPositioning == 5:
        noseHeight = int(loc[0][2])

        leftWristX = int(loc[5][1])
        rightWristX = int(loc[6][1])
        leftWristHeight = int(loc[5][2])
        rightWristHeight = int(loc[6][2])

        leftShoulderX = int(loc[1][1])
        rightShoulderX = int(loc[2][1])
        avgHipShoulderMidHeight = ((int(loc[1][2]) + int(loc[2][2])) + (int(loc[7][2]) + int(loc[8][2]))) // 4

        leftElbowX = int(loc[3][1])
        rightElbowX = int(loc[4][1])
        avgElbowHeight = (int(loc[3][2]) + int(loc[4][2])) // 2
        
        if (rightWristX < rightElbowX < rightShoulderX or \
            leftShoulderX < leftElbowX < leftWristX) and \
            (noseHeight < leftWristHeight < avgHipShoulderMidHeight or \
            noseHeight < rightWristHeight < avgHipShoulderMidHeight):
            checking = True

    elif specifcPositioning == 6:
        noseHeight = int(loc[0][2])

        leftWristX = int(loc[5][2])
        rightWristX = int(loc[6][2])
        avgWristHeight = (int(loc[5][2]) + int(loc[6][2])) // 2

        leftShoulderX = int(loc[1][1])
        rightShoulderX = int(loc[2][1])
        avgHipShoulderMidHeight = ((int(loc[1][2]) + int(loc[2][2])) + (int(loc[7][2]) + int(loc[8][2]))) // 4

        leftElbowX = int(loc[3][1])
        rightElbowX = int(loc[4][1])
        avgElbowHeight = (int(loc[3][2]) + int(loc[4][2])) // 2
        
        if noseHeight < avgWristHeight < avgHipShoulderMidHeight and \
            noseHeight < avgElbowHeight < avgHipShoulderMidHeight:
            checking = True

    elif specifcPositioning == 7:
        noseHeight = int(loc[0][2])

        leftWristX = int(loc[5][2])
        rightWristX = int(loc[6][2])
        avgWristHeight = (int(loc[5][2]) + int(loc[6][2])) // 2

        leftShoulderX = int(loc[1][1])
        rightShoulderX = int(loc[2][1])
        avgHipShoulderMidHeight = ((int(loc[1][2]) + int(loc[2][2])) + (int(loc[7][2]) + int(loc[8][2]))) // 4

        leftElbowX = int(loc[3][1])
        rightElbowX = int(loc[4][1])
        avgElbowHeight = (int(loc[3][2]) + int(loc[4][2])) // 2
        
        if noseHeight < avgWristHeight < avgHipShoulderMidHeight or \
            noseHeight < avgElbowHeight < avgHipShoulderMidHeight:
            checking = True

    elif specifcPositioning == 8:
        noseHeight = int(loc[0][2])

        leftWristX = int(loc[5][2])
        rightWristX = int(loc[6][2])
        avgWristHeight = (int(loc[5][2]) + int(loc[6][2])) // 2

        leftShoulderX = int(loc[1][1])
        rightShoulderX = int(loc[2][1])
        #avgHipShoulderMidHeight = ((int(loc[1][2]) + int(loc[2][2])) + (int(loc[7][2]) + int(loc[8][2]))) // 4

        avgElbowHeight = (int(loc[3][2]) + int(loc[4][2])) // 2
        
        if rightShoulderX < rightWristX < leftWristX < leftShoulderX:
            if noseHeight < avgWristHeight < avgElbowHeight:
               checking = True

    elif specifcPositioning == 9:
        noseHeight = int(loc[0][2])
        avgWristHeight = (int(loc[5][2]) + int(loc[6][2])) // 2
        avgElbowHeight = (int(loc[3][2]) + int(loc[4][2])) // 2
        
        if avgWristHeight < noseHeight < avgElbowHeight:
            checking = True

    elif specifcPositioning == 10:
        noseHeight = int(loc[0][2])
        leftWristHeight = int(loc[5][2]) 
        rightWristHeight = int(loc[6][2])
        leftElbowHeight = int(loc[3][2]) 
        rightElbowHeight = int(loc[4][2])

        if leftWristHeight < noseHeight < leftElbowHeight or \
            rightWristHeight < noseHeight < rightElbowHeight:
            checking = True

    return checking


# _____________________________________________________________________________
class Exercise:
    """
    This is the Exercise Class:
    The Attributes in the 8 Locations of interest are represented as tuples here
    (minimum expected angle, maximum EA, target EA)

    Bicep Curls and Single Arm Bicep Curls both use the same base angles, 
     so that distinction is made with the Boolean mirrored variable
    
    The Specific Positioning is how I will check these exercises in the trackLocation function 
     """

    def __init__(self, name,
                 pit, elbow, hip, knee,
                 mirrored=True,
                 specificPositioning: int=None,
                 skipFull: list=None):
        """
        Each exercise will have its own set of angles, and other attributes
        """
        self.name = name
        self.angles = [pit, elbow, hip, knee]
        self.mirrored = mirrored
        self.specific = specificPositioning
        self.sFull = skipFull

    def exerciseAngles(self):
        return self.angles


abductorLegRaises = Exercise("Abductor Leg Raises",
                             (0, 135), (0, 150), (130, 155), (170, 180),
                             False, 0)

barbellSquats = Exercise("Barbell Squats",
                         (30, 90), (75, 150), (0, 135), (0, 135),
                         True, 1, [0, 1])

bicepCurls = Exercise("Bicep Curls",
                      (0, 30), (0, 90), (160, 180), (160, 180),
                      True, 2)
singleArmBicepCurls = Exercise("Single Arm Bicep Curls",
                               (0, 30), (0, 90), (160, 180), (160, 180),
                               False, 3)

deltoidArmRaises = Exercise("Deltoid Arm Raises",
                            (75, 135), (160, 180), (160, 180), (160, 180),
                            True, 4)
singleArmDeltoidRaises = Exercise("Single Arm Deltoid Raises",
                                  (75, 135), (160, 180), (160, 180), (160, 180),
                                  False, 5)

frontLatRaises = Exercise("Front Lat Raises",
                          (75, 135), (160, 180), (160, 180), (160, 180),
                          True, 6)
singleArmFrontLatRaises = Exercise("Single Arm Front Lat Raises",
                                   (75, 135), (160, 180), (160, 180), (160, 180),
                                   False, 7)

gobletSquats = Exercise("Goblet Squats",
                        (0, 20), (0, 45), (0, 135), (0, 135),
                        True, 8)

shoulderPress = Exercise("Shoulder Press",
                         (80, 180), (80, 180), (160, 180), (160, 180),
                         True, 9)
singleArmShoulderPress = Exercise("Single Arm Shoulder Press",
                                  (80, 180), (80, 180), (160, 180), (160, 180),
                                  False, 10)


exercises = [abductorLegRaises,
             #barbellSquats,
             bicepCurls,                                    
             singleArmBicepCurls,
             deltoidArmRaises,
             singleArmDeltoidRaises,
             #frontLatRaises,          
             #singleArmFrontLatRaises,
             gobletSquats,
             shoulderPress,
             singleArmShoulderPress]


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
    """
 
    pE = []
    mirrored = {}
    angles = leftAngles, rightAngles
    for exercise in exercises:
        #print('\n\n', exercise.name)
        try:
            mirrored[exercise.name] = [True, True]
            for sub in range(2):
                # The name of the exercise is stored in the mirrored dictionary
                #  As the loop iterates twice
                #   If the currentAngle is between that of the exercise being checked, 
                #    the left or right print False will stay True
                #   That tells me if the exercise being done is, well, mirrored 
                for point in range(4):
                    # point loops though the shoulder, elbow, hip, and knee angles
                    if exercise.angles[point][0] <= angles[sub][point][1] <= exercise.angles[point][1]:
                        #print('\nTrue', sub, point, 
                        #        exercise.angles[point][0], "<=", angles[sub][point][1], "<=", exercise.angles[point][1])
                        pass
                    else:
                        #print('\nFalse', sub, point, 
                        #        exercise.angles[point][0], "<=", angles[sub][point][1], "<=", exercise.angles[point][1])
                        mirrored[exercise.name][sub] = False
                        
            if True in mirrored[exercise.name]:
                pE.append(exercise)
                #print(exercise.name,mirrored[exercise.name])

        except IndexError:
            pass

    #print('\n1', [x.name for x in pE],
    #      '\n', angles)
    
    _pE = [x for x in pE]
    pE = []
    for sub, exer in enumerate(_pE):
        a, b = mirrored[exer.name]
        if (a is True and b is True) and exer.mirrored is True:
            pE.append(exer)
        elif (a is False or b is False) and exer.mirrored is False: 
            pE.append(exer)
        else:
            pass

    _pE = []
    #print('\nLoc:', loc, '\n')
    for exer in pE:
        if trackLocation(exer.specific, loc) is True:
            #print(exer.name, 'has potential')
            _pE.append(exer)
        else:
            pass

    try:
        #print("\nExercise Check")
        #print('\n4', [x.name for x in _pE])
        #input("Press Enter For Next Check")
        # If there is more than one exercise in the list, then it will pass and check against a new list
        if len(_pE) == 1:
            #print(_pE[0].name)
            return True, _pE
        elif 1 < len(_pE):
            #print(x.name for x in _pE)
            return False, _pE
    except IndexError:
        pass

    return False, []


# _____________________________________________________________________________
def detectRepetitions(leftAngles, rightAngles, exName: Exercise=None):
    # print(f"\nDetecting Reps For: {exName.name}\n")
    #input("Wait Here1")
    try:
        currentAngle = leftAngles, rightAngles
        reps = [True, True]

        for sub in range(2):
            for point in range(4):
                # point loops though the shoulder, elbow, hip, and knee angles
                #print(exName.angles[point][0], '<=', currentAngle[sub][point][1], '<=', exName.angles[point][1])
                if exName.angles[point][0] <= currentAngle[sub][point][1] <= exName.angles[point][1]:
                    pass
                else:
                    reps[sub] = False
                

        if reps[0] is True and reps[1] is True and exName.mirrored is True:
            return True
        elif reps[0] is True or reps[1] is True and exName.mirrored is False:
            return True
        else:
           return False

    except IndexError:
        return False

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
