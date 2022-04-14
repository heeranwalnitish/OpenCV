import cv2


img = cv2 .imread('nick.jpg', 0)

cv2.imshow("Gray scale image", img)
cv2.waitKey(0)




#thersholding technique
ret, bw = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
cv2.imshow("Binary",bw)
cv2.waitKey(0)




cv2.destroyAllWindows()