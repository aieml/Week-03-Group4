import cv2          #importing opencv library
import dlib

face_detector=dlib.get_frontal_face_detector()

#a pretrained face detecting classifier

camera=cv2.VideoCapture(0)
#camera object has the access to the default camera of your pc

while(True):

    ret,img=camera.read()
    #img is a single frame (RGB) captured by the camera
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img will be converted into a gray image

    rect=face_detector(gray)

    try:

        x1=rect[0].left()
        y1=rect[0].top()
        x2=rect[0].right()
        y2=rect[0].bottom()

        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

    except Exception as e:

       print(e)

    cv2.imshow('LIVE',img)
    cv2.waitKey(1)
