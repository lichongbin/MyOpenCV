# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:30:29 2018

@author: licb-pc

打开和关系摄像头的方法

demonstration of opening and closing of video capture
"""

import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    if cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)
        # wait 50ms for quit
        if cv2.waitKey(50)&0xFF is ord('q'):
            break
# close video
cap.release()
cv2.destroyAllWindows()