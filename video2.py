# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:54:19 2018

@author: licb-pc

Command:
    q -- quit
    p -- write the current frame to a jpg file

"""

import cv2

idx = 1

cap = cv2.VideoCapture(0)
while True:
    if cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)
        # wait 50ms for command
        cmd = cv2.waitKey(50)&0xFF
        if cmd is ord('q'):
            break
        elif cmd is ord('p'):
            fn = 'cap' + str(idx) + '.jpg'
            cv2.imwrite(fn, frame)
            idx = idx + 1
# close video
cap.release()
cv2.destroyAllWindows()