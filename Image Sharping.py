import cv2
import numpy as np
 

img = cv2.imread('nick.jpg')
cv2.imshow('Original Image', img)
cv2.waitKey()


#Create our sharpening krnel, we don't normalize since the values in the matrix sum to 1.
kernel_sharpening = np.array([[-1,-1,-1,-1,-1],
                               [-1,-1,-1,-1,-1],
                               [-1,-1,25,-1,-1],
                               [-1,-1,-1,-1,-1],
                               [-1,-1,-1,-1,-1]])

# applying different kernel to the different iage
sharpened = cv2.filter2D(img, -1, kernel_sharpening)

cv2.imshow('Image sharpening', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()