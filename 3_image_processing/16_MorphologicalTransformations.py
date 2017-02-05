# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../assets/j.png',0)
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)

dilation = cv2.dilate(img,kernel,iterations = 1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Rectangular Kernel
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#array([[1, 1, 1, 1, 1],
#       [1, 1, 1, 1, 1],
#       [1, 1, 1, 1, 1],
#       [1, 1, 1, 1, 1],
#       [1, 1, 1, 1, 1]], dtype=uint8)

# Elliptical Kernel
ellip_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#array([[0, 0, 1, 0, 0],
#       [1, 1, 1, 1, 1],
#       [1, 1, 1, 1, 1],
#       [1, 1, 1, 1, 1],
#       [0, 0, 1, 0, 0]], dtype=uint8)

# Cross-shaped Kernel
cross_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
#array([[0, 0, 1, 0, 0],
#       [0, 0, 1, 0, 0],
#       [1, 1, 1, 1, 1],
#       [0, 0, 1, 0, 0],
#       [0, 0, 1, 0, 0]], dtype=uint8)

dst1 = cv2.erode(img,rect_kernel,iterations = 1)
dst2 = cv2.erode(img,ellip_kernel,iterations = 1)
dst3 = cv2.erode(img,cross_kernel,iterations = 1)

plt.subplot(3,4,1),plt.imshow(img)
plt.title("original")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,2),plt.imshow(erosion)
plt.title("erosion")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,3),plt.imshow(dilation)
plt.title("dilation")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,4),plt.imshow(opening)
plt.title("opening")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,5),plt.imshow(closing)
plt.title("closing")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,6),plt.imshow(gradient)
plt.title("gradient")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,7),plt.imshow(tophat)
plt.title("tophat")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,8),plt.imshow(blackhat)
plt.title("blackhat")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,9),plt.imshow(img)
plt.title("original")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,10),plt.imshow(dst1)
plt.title("Rectangular")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,11),plt.imshow(dst2)
plt.title("Elliptical")
plt.xticks([]),plt.yticks([])

plt.subplot(3,4,12),plt.imshow(dst3)
plt.title("Cross-shaped")
plt.xticks([]),plt.yticks([])

plt.show()
