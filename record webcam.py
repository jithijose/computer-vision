import numpy as np
from cv2 import cv2

# Load a color image in grayscale
imgGray = cv2.imread('Learning/messi.jpg', 0)

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Learning/messiGray.png', imgGray)

# Video recording from webcam

cap = cv2.VideoCapture(0)

# Define the codec and videoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('Learning/webcam_out.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.flip(frame, 0)
        
        # write the fipped frame
        out.write(frame)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if the job is finished
cap.release()
out.release()
cv2.destroyAllWindows()