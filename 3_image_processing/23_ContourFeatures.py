# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('../assets/star.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

###################################
# Moments
cnt = contours[0]
M = cv2.moments(cnt)
#print M

# Centroid 計算第一個輪廓的中心點：Cx = M10/M00, Cy = M01/M00
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
# contours[0] Centroid: (cx,cy)= 199 349
print "contours[0] Centroid: (cx,cy)=",cx,cy

# loop over the contours
for c in contours:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

	# draw the contour and center of the shape on the image
	cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
	cv2.circle(img, (cX, cY), 7, (0, 0, 255), -1)
	cv2.putText(img, "C", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

cv2.imwrite('star1_Centroid.jpg',img)

###################################
# Countour Area, 可利用 countourArea() 或是由 M['m00'] 得到區塊面積
area = cv2.contourArea(cnt)
# Countour Area  contourArea= 1567.5
print "Countour Area  contourArea=",area

###################################
# Contour Perimeter, 計算弧長, 可利用 cv2.arcLength(), 第二個參數 True: closed contour, False: curve
perimeter = cv2.arcLength(cnt,True)
# Contour Perimeter  arcLength= 156.953317404
print "Contour Perimeter  arcLength=",perimeter

###################################
# Contour Approximation

img = cv2.imread('../assets/star2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

imgres = img.copy()

#epsilon = 0.1*cv2.arcLength(cnt,True)
#approx = cv2.approxPolyDP(cnt,epsilon,True)
approx = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours]
#print "Contour Approximation  approx=",approx
for c in approx:
	cv2.drawContours(imgres, [c], -1, (0, 255, 0), 2)
cv2.imwrite('star4_ContourApproximation1.jpg',imgres)

imgres = img.copy()

epsilon = 0.1*cv2.arcLength(cnt,True)
#approx = cv2.approxPolyDP(cnt,epsilon,True)
approx = [cv2.approxPolyDP(cnt, epsilon, True) for cnt in contours]
#print "Contour Approximation  approx=",approx
for c in approx:
	cv2.drawContours(imgres, [c], -1, (0, 255, 0), 2)
cv2.imwrite('star4_ContourApproximation2.jpg',imgres)

###################################
# Convex Hull

img = cv2.imread('../assets/star1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

hull = [cv2.convexHull(cnt) for cnt in contours]

#print hull

for c in hull:
	cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
cv2.imwrite('star5_ConvexHull.jpg',img)

##################################
# Checking Convexity 檢查是否為 凸狀區塊

convex = [cv2.isContourConvex(cnt) for cnt in contours]
#Checking Convexity isContourConvex= [False, False, False, True, False, False]
print "Checking Convexity isContourConvex=", convex

##################################
# Straight Bounding Rectangle

img = cv2.imread('../assets/star1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

rect = [cv2.boundingRect(cnt) for cnt in contours]

imgres = img.copy()
for c in rect:
	x = c[0]
	y = c[1]
	w = c[2]
	h = c[3]
	#print c[0], c[1], c[2], c[3]
	imgres = cv2.rectangle(imgres,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imwrite('star7_StraightBoundingRectangle.jpg',imgres)

# Rotated Rectangle

rect = [cv2.minAreaRect(cnt) for cnt in contours]

imgres = img.copy()
for c in rect:
	#print c
	box = cv2.boxPoints(c)
	box = np.int0(box)
	imgres = cv2.drawContours(imgres,[box],0,(0,0,255),2)

cv2.imwrite('star7_RotatedRectangle.jpg',imgres)

##################################
# Minimum Enclosing Circle
img = cv2.imread('../assets/star1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

circle = [cv2.minEnclosingCircle(cnt) for cnt in contours]

imgres = img.copy()
for c in circle:
	x=c[0][0]
	y=c[0][1]
	radius = c[1]

	center = (int(x),int(y))
	radius = int(radius)
	imgres = cv2.circle(imgres,center,radius,(0,255,0),2)

cv2.imwrite('star8_MinimumEnclosingCircle.jpg',imgres)

##################################
# Fitting an Ellipse

img = cv2.imread('../assets/star1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
newimg, contours,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_NONE)

ellipses = [cv2.fitEllipse(cnt) for cnt in contours]

imgres = img.copy()
for c in ellipses:
	#print c
	imgres = cv2.ellipse(imgres, c, (0,255,0),2)

cv2.imwrite('star9_FittingEllipse.jpg',imgres)

##################################
# Fitting a Line

img = cv2.imread('../assets/star1.jpg')

rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

cv2.imwrite('starA_FittingLine.jpg',img)
