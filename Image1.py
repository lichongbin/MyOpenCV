# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 19:20:51 2018

@author: licb-pc

Demo for Image.convert and
         numpy.asarray

"""

from PIL import Image
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
cwd = os.getcwd()
image_path = "logo.jpg"

img1 = Image.open(os.path.join(cwd, image_path))

# color image -> gray image
img2 = img1.convert('L')

# image -> array
image_array = np.asarray(img2, dtype=float)

# array -> image
img3 = Image.fromarray(image_array)