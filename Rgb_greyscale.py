# Converting the RGB inmage to graay Scale
import cv2

img = cv2.imread('nick.jpg')


cv2.imshow("Original Image", img)
cv2.waitKey(0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2. imshow("Gray Scale Image",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()