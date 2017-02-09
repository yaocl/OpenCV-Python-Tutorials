# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../assets/mario.jpg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('../assets/mario_template.jpg',0)
w, h = template.shape[::-1]

img_res = img_rgb.copy()
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_res, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)

plt.subplot(2,2,1),plt.imshow(img_rgb)
plt.title("original"), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(img_res)
plt.title("result"), plt.xticks([]), plt.yticks([])


img = cv2.imread('../assets/mario2.jpg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('../assets/mario2_template.jpg',0)
w, h = template.shape[::-1]

img_res = img_rgb.copy()
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_res, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)

plt.subplot(2,2,3),plt.imshow(img_rgb)
plt.title("original"), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.imshow(img_res)
plt.title("result"), plt.xticks([]), plt.yticks([])

plt.show()
#cv2.imwrite('res.png',img_rgb)