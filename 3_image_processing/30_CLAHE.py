# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../assets/status.png',0)
equ = cv2.equalizeHist(img)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

plt.subplot(131)
plt.imshow(img, 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

plt.subplot(132)
plt.imshow(equ, 'gray')
plt.title('Equal Equlization'), plt.xticks([]), plt.yticks([])

plt.subplot(133)
plt.imshow(cl1, 'gray')
plt.title('CLAHE'), plt.xticks([]), plt.yticks([])
plt.show()
