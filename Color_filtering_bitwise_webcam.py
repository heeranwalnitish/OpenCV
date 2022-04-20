from platform import release
from unittest import result
import cv2
import numpy as np
from sympy import re 

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_range = np.array([110, 50, 50])
    upper_range = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_range, upper_range)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('show', mask)
    cv2.imshow('result', result)

    if cv2.waitKey(1) == 13:
        break

cam.release()
cv2.destroyAllWindows()
