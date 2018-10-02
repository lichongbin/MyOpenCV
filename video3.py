# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:08:10 2018

@author: licb-pc

Command:
        q -- quit
        s -- start recording
        e -- end recording
"""

import cv2
import time

fc = 0 # the number of frames recorded

Writing = False

cap = cv2.VideoCapture(0)

fps = 0
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)

CC = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

if cap.isOpened():
    t = cv2.getTickCount()
    tf = 0
    while True:
        ret, frame = cap.read()
        tf = tf + 1
        
        if Writing:
            cv2.putText(frame, 
                        str(fc),
                        (30,30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2, 
                        (100, 255, 10))
        else:
            cv2.putText(frame, 
                        str(tf),
                        (30,30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2, 
                        (100, 255, 10))
        ts = time.strftime('%H-%M-%S',time.localtime(time.time()))
        cv2.putText(frame,
                    ts,
                    (30,60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2,
                    (100, 255, 10))  

        # wait 1ms for command
        cmd = cv2.waitKey(1)&0xFF
        if cmd is ord('q'):
            break
        elif cmd is ord('s'):
            videoWriter = cv2.VideoWriter('temp.avi', CC, fps, size)
            Writing = True
            fc = 0
        elif cmd is ord('e'):
            videoWriter.release()
            Writing = False
        elif Writing:
            videoWriter.write(frame)
            fc = fc + 1
        
        cv2.imshow('Camera', frame)
        
        if tf % 20 == 0:
            sec = (cv2.getTickCount() - t) / cv2.getTickFrequency()
            fps = tf / sec
            print(fps)

    # close video
    cap.release()
    cv2.destroyAllWindows()