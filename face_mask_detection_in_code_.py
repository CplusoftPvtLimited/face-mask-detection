# -*- coding: utf-8 -*-
"""Face Mask_detection in Code .ipynb

Automatically generated by Colaboratory.


# Importing the dependencies
import os
from tensorflow.keras.preprocessing import image
import cv2
import random
import numpy as np

import cv2
import tensorflow
import keras
from PIL import Image

face_cascade = 'haarcascade_frontalface_default.xml'

webcam = cv2.VideoCapture(0)

success, image_bgr = webcam.read()

while True:
    success, image_bgr = webcam.read()
    if success:
        
        image_bw = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
        
        face_classifier = cv2.CascadeClassifier(face_cascade)
        faces = face_classifier.detectMultiScale(image_bw)
        print(f'There are {len(faces)} faces found.')
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(image_bgr, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.imshow("Face Detection", image_bgr)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
webcam.release()
cv2.destroyAllWindows()





"""Wait Wait !!

This is only 10% of project Code. [Incomplete]

If you want full Project Code with full explanation. 

Please : 

# Mail me at **vatshayan007@gmail.com** 
"""



