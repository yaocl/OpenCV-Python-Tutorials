# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('../assets2/simple.jpg')
surf = cv2.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img,None)

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
cv2.imwrite('surf_keypoints.jpg',img2)