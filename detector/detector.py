import cv2 as cv
import sys

face_cascade = cv.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(1)
while(True):
    ret,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        print('Here\'s one.')

        face = gray[y:y+h, x:x+w]
        # cv.imwrite('face.png', face)

        _,png = cv.imencode('.png', face)
        msg = png.tobytes()

print('Done.')
