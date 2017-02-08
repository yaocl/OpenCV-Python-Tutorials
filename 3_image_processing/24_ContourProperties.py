# -*- coding: utf-8 -*-

import cv2
import numpy as np

##################################
# Aspect Ratio

img = cv2.imread('../assets/star1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

newimg2, contours2,hierarchy2 = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_NONE)

rect = [cv2.boundingRect(cnt) for cnt in contours]

print ""
print "Aspect Ratio:"
for c in rect:
	x = c[0]
	y = c[1]
	w = c[2]
	h = c[3]
	#print c[0], c[1], c[2], c[3]
	aspect_ratio = float(w)/h
	print "\tw=",w,",h=",h,", ratio= ", aspect_ratio

##################################
# Extent

print ""
print "Extent:"
for cnt in contours:
	area = cv2.contourArea(cnt)
	rect = cv2.boundingRect(cnt)
	x = rect[0]
	y = rect[1]
	w = rect[2]
	h = rect[3]

	rect_area = w*h
	extent = float(area)/rect_area
	print "\tarea=", area,",w=",w,",h=",h,", extent= ", extent

##################################
# Solidity

print ""
print "Solidity:"
for cnt in contours:
	area = cv2.contourArea(cnt)
	hull = cv2.convexHull(cnt)
	hull_area = cv2.contourArea(hull)
	solidity = float(area)/hull_area

	print "\tarea=", area,", hull_area=",hull_area,", solidity=",solidity

##################################
# Equivalent Diameter

print ""
print "Equivalent Diameter:"

for cnt in contours:
	area = cv2.contourArea(cnt)
	equi_diameter = np.sqrt(4*area/np.pi)

	print "\tarea=", area,", equi_diameter=",equi_diameter


##################################
# Orientation

print ""
print "Orientation:"
for cnt in contours2:
	(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

	print "\t(x,y)=", x, y,", (MA,ma)=",MA,ma, ", angle=",angle


##################################
# Mask and Pixel Points

print ""
print "Mask and Pixel Points:"

for cnt in contours2:
	mask = np.zeros(gray.shape,np.uint8)
	cv2.drawContours(mask,[cnt],0,255,-1)
	pixelpoints = np.transpose(np.nonzero(mask))
	#pixelpoints = cv2.findNonZero(mask)

	#print "\tpixelpoints=",pixelpoints


##################################
# Mean Color or Mean Intensity

print ""
print "Mean Color:"

# 在每一個 contours 用白色畫在 mask image 上面
for h,cnt in enumerate(contours):
    mask = np.zeros(gray.shape,np.uint8)
    cv2.drawContours(mask,[cnt],0,255,-1)
    mean = cv2.mean(img,mask = mask)

    print "\tmean=",mean

##################################
# Extreme Points

print ""
print "Extreme Points:"

for cnt in contours:
	leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
	rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
	topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
	bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

	print "\tleftmost, rightmost, topmost, bottommost=",leftmost, rightmost, topmost, bottommost

##################################
# Maximum Value, Minimum Value and their locations

print ""
print "Maximum Value, Minimum Value and their locations:"

#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray,mask = mask)

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../assets/messi.png',0)
img2 = img.copy()
template = cv2.imread('../assets/messiface.png',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
