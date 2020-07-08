import numpy as np
import cv2
import turn_screen_on_off as ts
from cv2 import CascadeClassifier
from cv2 import VideoCapture

face_cascade = CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = CascadeClassifier('haarcascade_eye.xml')

vc = VideoCapture(0)

while True:
  ret, img = vc.read() #Reads image
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Sets background gray?
  faces = face_cascade.detectMultiScale(gray,1.3,5) #Retrieves faces in image

  for (x,y,w,h) in faces:
    #Make a red rectangle the size of your face on your face to track
    cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0),2) 
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = img[y:y+h, x:x+w]

    eyes = eyes_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
      cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,0,255),2)
  
  if(len(faces) >= 1):
    ts.screen_off()
  else:
    ts.screen_on()

  
  cv2.imshow('img',img) #Show image in window
  k = cv2.waitKey(30) & 0xff
  if k == 27:
    break

cap.release()
cv2.destroyAllWindows()
