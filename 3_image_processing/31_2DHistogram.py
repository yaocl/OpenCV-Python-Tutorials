# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../assets/lena.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

print hsv.shape
hue = hsv[:, :, 0]
sat = hsv[:, :, 1]
hist2, xbins, ybins = np.histogram2d(hue.ravel(),sat.ravel(),[180,256],[[0,180],[0,256]])

plt.subplot(131)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('original'), plt.xticks([]), plt.yticks([])

plt.subplot(132)
plt.imshow(hist,interpolation = 'nearest')
plt.title('OpenCV')

plt.subplot(133)
plt.imshow(hist2,interpolation = 'nearest')
plt.title('numpy')
plt.show()
