import cv2
import numpy as np

img = cv2.imread('nick.jpg')

height, width = img.shape[:2]


# Let's get the starting pixel coordinates(top left of the cropping rectangle)
start_row, start_col = int(height *.25),int(width*.25)

# Let's get the ending pixel coordinates(bottom right)
end_row, end_col = int(height*.75),int(width*.75)

#Simply use the indexing to crop the image
cropped = img[start_row:end_row, start_col:end_col]

cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()