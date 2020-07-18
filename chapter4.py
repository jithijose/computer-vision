#####################################################################
#                       SHAPES AND TEXTS                            #
#####################################################################
from cv2 import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

img[:] = 255, 0, 0
cv2.imshow('Image', img)

img[100:200, 100:200] = 0, 255, 0
cv2.imshow('Image', img)

img = np.zeros((512, 512, 3), np.uint8)

# Draw a line in an image
cv2.line(img, (0, 0), (400, 400), (0, 255, 0), 1)
cv2.line(img, (50, 150), (img.shape[0], img.shape[1]), (0, 0, 255), 1)

# Draw a rectangle in an image
cv2.rectangle(img, (10, 10), (200, 400), (255, 0, 0), 2)
cv2.rectangle(img, (210, 10), (400, 200), (255, 200, 0), cv2.FILLED)

# Draw a circle in an image
cv2.circle(img, (300, 400), 30, (86, 132, 178), 2)
cv2.circle(img, (300, 105), 30, (86, 132, 240), 1)

# Put text in an image
cv2.putText(img, 'SAMPLE TEXT', (100, 500), cv2.FONT_HERSHEY_COMPLEX, 1, (100, 220, 147), 1)

cv2.imshow('Image', img)


cv2.waitKey(0)
