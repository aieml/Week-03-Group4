import cv2          #importing opencv library
import dlib
import imutils     #image utilities libray
from imutils import face_utils

face_detector=dlib.get_frontal_face_detector()
#a pretrained face detecting classifier
landmark_detector=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#a pretrained classifier for etecting 68 landmarks in face

camera=cv2.VideoCapture(0)
#camera object has the access to the default camera of your pc

while(True):

    ret,img=camera.read()
    #img is a single frame (RGB) captured by the camera
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img will be converted into a gray image

    rect=face_detector(gray)

    try:

        points=landmark_detector(gray,rect[0])
        #getting the 68 points of the face
        points=face_utils.shape_to_np(points)
        #converting the points into a numpy array

        for p in points:

            cen=(p[0],p[1])
            cv2.circle(img,cen,2,(0,255,0),-1)
            cv2.imshow('LIVE',img)
            cv2.waitKey(100)
        #p=points[0]
        #cen=(p[0],p[1])
        #cv2.circle(img,cen,5,(0,0,255),-1)        
        
    except Exception as e:

       print(e)

    
    cv2.waitKey(1)



