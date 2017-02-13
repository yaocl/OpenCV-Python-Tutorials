# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../assets2/simple.jpg',0)
# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()
# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, color=(255,0,0),outImage=img)
# Print all default params
#print "Threshold: ", fast.getInt('threshold')
#print "nonmaxSuppression: ", fast.getBool('nonmaxSuppression')
#print "neighborhood: ", fast.getInt('type')
#print "Total Keypoints with nonmaxSuppression: ", len(kp)
cv2.imwrite('fast_with_nonmaxSuppression.png',img2)

img = cv2.imread('../assets2/simple.jpg',0)
# Disable nonmaxSuppression
fast = cv2.FastFeatureDetector_create(nonmaxSuppression=False)
#fast.setBool('nonmaxSuppression',0)
kp = fast.detect(img,None)
print "Total Keypoints without nonmaxSuppression: ", len(kp)
img3 = cv2.drawKeypoints(img, kp, color=(255,0,0),outImage=img)
cv2.imwrite('fast_without_nonmaxSuppression.png',img3)
