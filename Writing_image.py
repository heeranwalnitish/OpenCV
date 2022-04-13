import cv2

img = cv2.imread('nick.jpg')

cv2.imshow('Original Image', img)

cv2.imwrite('Output.jpg', img)

cv2.imwrite('Output.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()