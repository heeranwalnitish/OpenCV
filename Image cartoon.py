import cv2

img = cv2.imread('nick.jpg',)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_grar = cv2.medianBlur(img_gray, 5)
edges = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9,9)

color = cv2.bilateralFilter(img, 9, 300,300)
cartoon = cv2.bitwise_and(color, color, mask = edges)

cv2.imshow("Original Image", img)
cv2.imshow("Cartoon ", cartoon)


cv2.waitKey(0)
cv2.destroyAllWindows()