import cv2
import numpy as np

cam = cv2.VideoCapture(0)


while True:
    ret, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_range = np.array([110, 50, 50])
    upper_range = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow("Show", mask)
    cv2.imshow("show1",frame)


    if cv2.waitKey(1) == 13:
        break


cam.release()
cv2.destroyAllWindows()
