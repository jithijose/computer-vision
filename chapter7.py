#####################################################################
#                         COLOR DETECTION                           #
#####################################################################
from cv2 import cv2
import numpy as np

# Define a function for trackbars
def empty_fn(a):
    pass

# Function to stack images
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


# Define Trackbars
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)

cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty_fn)
cv2.createTrackbar('Hue Max', 'TrackBars', 19, 179, empty_fn)
cv2.createTrackbar('Sat Min', 'TrackBars', 110, 255, empty_fn)
cv2.createTrackbar('Sat Max', 'TrackBars', 240, 255, empty_fn)
cv2.createTrackbar('Val Min', 'TrackBars', 153, 255, empty_fn)
cv2.createTrackbar('Val Max', 'TrackBars', 255, 255, empty_fn)

while True:
    # Read image file from path
    path = 'Resources/lambo.png'
    img = cv2.imread(path)

    # convert image to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the value from the trackbar
    hue_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    hue_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    sat_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    sat_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    val_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
    val_max = cv2.getTrackbarPos('Val Max', 'TrackBars')
    
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    mask = cv2.inRange(imgHSV, lower, upper)

    imgResult = cv2.bitwise_and(img, img, mask=mask)

    #cv2.imshow('Original Image', img)
    #cv2.imshow('HSV Image', imgHSV)
    #cv2.imshow('Mask Image', mask)
    #cv2.imshow('Result Image', imgResult)

    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow('Stacked Image', imgStack)

    cv2.waitKey(1)