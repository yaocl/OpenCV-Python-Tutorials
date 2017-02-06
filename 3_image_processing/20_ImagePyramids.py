# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

higher_reso = cv2.imread('../assets/lena.jpg')

lower_reso = cv2.pyrDown(higher_reso)

lower_reso2 = cv2.pyrDown(lower_reso)

plt.subplot(231),plt.imshow(higher_reso)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(232),plt.imshow(lower_reso)
plt.title('lower_reso'), plt.xticks([]), plt.yticks([])

plt.subplot(233),plt.imshow(lower_reso2)
plt.title('lower_reso2'), plt.xticks([]), plt.yticks([])

higher_reso2 = cv2.pyrUp(lower_reso2)

higher_reso3 = cv2.pyrUp(higher_reso2)

plt.subplot(234),plt.imshow(lower_reso2)
plt.title('lower_reso2'), plt.xticks([]), plt.yticks([])

plt.subplot(235),plt.imshow(higher_reso2)
plt.title('higher_reso2'), plt.xticks([]), plt.yticks([])

plt.subplot(236),plt.imshow(higher_reso3)
plt.title('higher_reso3'), plt.xticks([]), plt.yticks([])

plt.show()
