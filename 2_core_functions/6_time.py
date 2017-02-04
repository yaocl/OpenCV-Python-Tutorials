# -*- coding: utf-8 -*-
import cv2
import numpy as np

img1 = cv2.imread('../assets/lena.jpg')

e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()

t = (e2 - e1)/cv2.getTickFrequency()
print "cv2.useOptimized()=",cv2.useOptimized(),", time=",t

cv2.setUseOptimized(False)

e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()

t = (e2 - e1)/cv2.getTickFrequency()
print "cv2.useOptimized()=",cv2.useOptimized(),", time=",t
