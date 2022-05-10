import cv2
from PIL import Image
import numpy as np

#thug life meme mask image path
maskPath = "mask.png"
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open mask as PIL image
mask = Image.open(maskPath)

def thug_mask(img):

    #convert input image to greyscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detect faces in grayscale image
    faces = facedetect.detectMultiScale(gray, 1.15)

    # convert cv2 image to PIL image
    background = Image.fromarray(img)

    for (x,y,w,h) in faces:
        # resize mask
        resized_mask = mask.resize((w,h), Image.ANTIALIAS)
        # define offset for mask
        offset = (x,y)
        # paste mask on background
        background.paste(resized_mask, offset, mask = resized_mask)

    # return backgroun as cv2 image
    return np.asarray(background)

# VideoCapture Object
cap = cv2.VideoCapture(cv2.CAP_ANY)

while True:
    # read return value and frame
    ret, frame = cap.read()

    if ret == True:
        # show frame with thug life mask
        cv2.imshow("Live", thug_mask(frame))

        k = cv2.waitKey(1)
        if k == ord('q'):
            break


# release cam
cap.release()
cv2.destroyAllWindows()
