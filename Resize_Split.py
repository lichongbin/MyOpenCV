# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:50:03 2018

@author: licb-pc

演示按原图像比例尺缩小图片的方法和分离彩色图像各个通道的方法
Demonstrate how to resize an image preserving aspect ratio and 
how to split the color by channel

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
y, cb, cr = cv2.split(imYcc)
cv2.imshow('Resized Image', resized)
cv2.imshow('Y Channel', y)
cv2.imshow('Cb Channel', cb)
cv2.imshow('Cr Channel', cr)

cv2.waitKey (0)  
cv2.destroyAllWindows()