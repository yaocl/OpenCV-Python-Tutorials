# -*- coding: utf-8 -*-

import cv2
import numpy as np

####################
# Convexity Defects

img = cv2.imread('../assets/star3.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
newimg, contours,hierarchy = cv2.findContours(thresh,2,1)

#for cnt in contours:
cnt = contours[0]
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

####################
# Point Polygon Test

print ""
print "Point Polygon Test"
dist = cv2.pointPolygonTest(cnt,(50,50),True)

print "\tdist=", dist

####################
# Match Shapes

print ""
print "Match Shapes"
img1 = cv2.imread('../assets/star1.jpg',0)
img2 = cv2.imread('../assets/star3.jpg',0)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
newimg1, contours1, hierarchy1 = cv2.findContours(thresh,2,1)
#cnt1 = contours[0]
newimg2, contours2, hierarchy2 = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]

for cnt in contours1:
    ret = cv2.matchShapes(cnt,cnt2,1,0.0)
    print "\tmatch result=",ret
