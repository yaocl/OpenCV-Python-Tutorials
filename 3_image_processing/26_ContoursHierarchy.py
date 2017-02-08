# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('../assets/hierarchy.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST,
	cv2.CHAIN_APPROX_SIMPLE)

imgres = img.copy()
print ""
print "RETR_LIST:"
index=1
for c in contours:
	print "\tRETR_LIST contour ",index, ", pos=", c[0][0]
	cv2.drawContours(imgres, [c], -1, (0, 255, 0), 2)
	cv2.putText(imgres, str(index), tuple(c[0][0]),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	index =index+1

cv2.imwrite('hierarchy_RETR_LIST.jpg',imgres)

#rint contours
print "\tRETR_LIST hierarchy=",hierarchy

##############

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

imgres = img.copy()
print ""
print "RETR_EXTERNAL:"
index=1
for c in contours:
	print "\tRETR_EXTERNAL contour ",index, ", pos=", c[0][0]
	cv2.drawContours(imgres, [c], -1, (0, 255, 0), 2)
	cv2.putText(imgres, str(index), tuple(c[0][0]),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	index =index+1

cv2.imwrite('hierarchy_RETR_EXTERNAL.jpg',imgres)

#rint contours
print "\tRETR_EXTERNAL hierarchy=",hierarchy

##############

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_CCOMP,
	cv2.CHAIN_APPROX_SIMPLE)

imgres = img.copy()
print ""
print "RETR_CCOMP:"
index=1
for c in contours:
	print "\tRETR_CCOMP contour ",index, ", pos=", c[0][0]
	cv2.drawContours(imgres, [c], -1, (0, 255, 0), 2)
	cv2.putText(imgres, str(index), tuple(c[0][0]),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	index =index+1

cv2.imwrite('hierarchy_RETR_CCOMP.jpg',imgres)

#rint contours
print "\tRETR_CCOMP hierarchy=",hierarchy

##############

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE,
	cv2.CHAIN_APPROX_SIMPLE)

imgres = img.copy()
print ""
print "RETR_TREE:"
index=1
for c in contours:
	print "\tRETR_TREE contour ",index, ", pos=", c[0][0]
	cv2.drawContours(imgres, [c], -1, (0, 255, 0), 2)
	cv2.putText(imgres, str(index), tuple(c[0][0]),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	index =index+1

cv2.imwrite('hierarchy_RETR_TREE.jpg',imgres)

#rint contours
print "\tRETR_TREE hierarchy=",hierarchy
