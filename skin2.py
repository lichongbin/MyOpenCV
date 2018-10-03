# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:50:11 2018

@author: licb-pc
"""

import cv2
import numpy as np

img = cv2.imread('1.jpg', 1)

print('Original Dimensions : ',img.shape)
 
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

imYcc = cv2.cvtColor(resized, cv2.COLOR_BGR2YCR_CB)
yrangel = np.array([80, 0, 0])
yrangeh = np.array([255, 255, 255])

brangel = np.array([0, 0, 85])
brangeh = np.array([255, 255, 135])

rrangel = np.array([0, 135, 0])
rrangeh = np.array([255, 180, 255])

y_mask = cv2.inRange(imYcc, yrangel, yrangeh)
b_mask = cv2.inRange(imYcc, brangel, brangeh)
r_mask = cv2.inRange(imYcc, rrangel, rrangeh)

t_mask = cv2.bitwise_and(y_mask, b_mask)
mask = cv2.bitwise_and(t_mask, r_mask)

res = cv2.bitwise_and(resized, resized, mask=mask)

cv2.imshow('res', res)
cv2.waitKey (0)  
cv2.destroyAllWindows()
