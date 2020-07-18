#####################################################################
#             READ IMAGE VIDEO AND WEBCAM                           #
#####################################################################
# import cv2 package(cv2 - computer vision)
from cv2 import cv2


# Read an image file and show
img = cv2.imread('Resources/lena.png')

cv2.imshow('Output Image', img) 

cv2.waitKey(0)

# Read a video file and play
cap = cv2.VideoCapture('Resources/test_video.mp4')

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Read Web Camera
cap = cv2.VideoCapture(0)
cap.set(3, 640) # set width of image - property value:3
cap.set(4, 480) # set height of image - property value:4
cap.set(10, 200) # set brightness of image - property value:10

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break