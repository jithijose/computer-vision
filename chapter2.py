#####################################################################
#                       BASIC FUNCTIONS                             #
#####################################################################
from cv2 import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')

# Convert to gray scale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) 

# Edge Detection
imgCanny = cv2.Canny(img, 100, 100)

# Edge Dilation
kernal = np.ones((5, 5), np.uint8)
imgDilation  = cv2.dilate(imgCanny, kernal, iterations=1)

# Erode
imgEroded = cv2.erode(imgDilation, kernal, iterations=1)

cv2.imshow('Original Image', img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilate Image', imgDilation)
cv2.imshow('Erode Image', imgEroded)

cv2.waitKey(0)
