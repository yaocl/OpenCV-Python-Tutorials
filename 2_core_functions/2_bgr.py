# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

#OpenCV follows BGR order, while matplotlib follows RGB order

img = cv2.imread('../assets/lena.jpg')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])

plt.subplot(121);plt.title('BGR'),plt.imshow(img) # expects distorted color (BGR)

plt.subplot(122);plt.title('RGB'),plt.imshow(img2) # expect true color (RGB)

plt.show()