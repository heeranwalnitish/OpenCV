import cv2
 
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
 
while True:
 
    ret, frame = cap.read()
 
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
 
    faces = faceCascade.detectMultiScale(
        frame, 
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30,30))
 
    for (x,y,w,h) in faces:
            cv2.circle(frame,(x+int(w/2),y+int(h/2)), 200, (0,0,255), 3)
 
 
    cv2.imshow('camera', frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()