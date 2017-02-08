# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../assets/histogram.jpg',0)
equ = cv2.equalizeHist(img)

#plt.subplot(121)
#plt.imshow(img, 'gray')
#plt.subplot(122)
#plt.imshow(equ, 'gray')
#plt.show()

res = np.hstack((img,equ)) #stacking images side-by-side
#cv2.imwrite('res.png',res)
cv2.imshow('res',res)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
