# Tutorial 9 : Image translation
from hashlib import sha1
from turtle import heading
import cv2
import numpy as np 

img = cv2.imread('nick.jpg')
#cv2.waitKey(0)

hight, width = img.shape[:2] 
print(hight)
print(width)

quater_height, quater_width = hight/4, width/4
print(quater_height)
print(quater_width)

# T is Our translation Matrix

T = np.float32([[1,0,quater_width],
[0,1, quater_height]])
print(T)


# We use warpAffine Transformation to shift the image
img_translation = cv2.warpAffine(img, T, (width, hight))

cv2.imshow("Original Image", img)
cv2.imshow('Translation', img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()