import cv2

img = cv2.imread('nick.jpg')

print(img.shape)
print("Height pixel value : ", img.shape[0])
print("Width pixel value : ", img.shape[1])
print("No. of layers : ",img.shape[2])
cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()