#####################################################################
#                      FACE DETECTION                               #
#####################################################################
from cv2 import cv2

faceCascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread('Resources/group-of-people.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 2)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Original Image', img)

cv2.waitKey(0)