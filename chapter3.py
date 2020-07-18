#####################################################################
#                     RESIZING AND CROPPING                         #
#####################################################################
from cv2 import cv2

img = cv2.imread('Resources/lambo.png')
print(img.shape)

# Resize an image
imgResize = cv2.resize(img, (300, 200))

# Crop an image
imgCropped = img[0:200, 200:500]

cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', imgResize)
cv2.imshow('Cropped Image', imgCropped)

cv2.waitKey(0)