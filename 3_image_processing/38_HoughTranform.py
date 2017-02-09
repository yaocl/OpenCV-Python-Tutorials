# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../assets/dave2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
#edges = cv2.Canny(gray,50,200,apertureSize = 3)

plt.subplot(1,3,1)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.title("original")
plt.xticks([]), plt.yticks([])

# void HoughLines(InputArray image, OutputArray lines, double rho, double theta, int threshold, double srn=0, double stn=0)
#  rho：距離解析度，越小表示定位要求越準確，但也較易造成應該是同條線的點判為不同線。
#  theta：角度解析度，越小表示角度要求越準確，但也較易造成應該是同條線的點判為不同線。

lines = cv2.HoughLines(edges, 0.5, np.pi/180, 100)

for x in range(0, len(lines)):
    for rho,theta in lines[x]:
        #print "(rho, theta)=",rho,theta
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

#cv2.imwrite('houghlines3.jpg',img)
plt.subplot(1,3,2)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.title("HoughLines")
plt.xticks([]), plt.yticks([])


img = cv2.imread('../assets/dave2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
#edges = cv2.Canny(gray,100,200,apertureSize = 3)

# minLineLength - Minimum length of line. Line segments shorter than this are rejected.
# maxLineGap - Maximum allowed gap between line segments to treat them as single line.
minLineLength = 30
maxLineGap = 10
lines = cv2.HoughLinesP(edges,0.5,np.pi/180,15,minLineLength,maxLineGap)

for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

#cv2.imwrite('houghlines5.jpg',img)
plt.subplot(1,3,3)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.title("HoughLinesP")
plt.xticks([]), plt.yticks([])

plt.show()