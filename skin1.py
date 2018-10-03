# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:29:24 2018

@author: licb-pc
"""

import cv2

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
y, cr, cb = cv2.split(imYcc)

for r in range(height):
    for c in range(width):
        yv = y.item(r, c)
        cbv= cb.item(r, c)
        crv= cr.item(r, c)
        if yv < 80 or cbv < 85 or cbv > 135 or crv < 135 or crv > 180:
            resized.itemset(r, c, 0, 0)
            resized.itemset(r, c, 1, 0)
            resized.itemset(r, c, 2, 0)
        
cv2.imshow('Resized Image', resized)

cv2.waitKey (0)  
cv2.destroyAllWindows()