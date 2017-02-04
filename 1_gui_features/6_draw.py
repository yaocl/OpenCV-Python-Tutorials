# -*- coding: utf-8 -*-

'Draw a line,rectangle,circle,ellipse'

import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8) #empty color image

# 在 img ，起點 (0,0) 終點 (420,420)，顏色 (255,0,0)，thickness 3 畫線
cv2.line(img,(0,0),(420,420),(255,0,0),3) #line

# thickness -1 表示為 closed figure
cv2.circle(img, (450, 70), 70, (0,0,255), -1) #circle

cv2.rectangle(img,(385,0),(510,120),(0,255,0),3) #rectangle

cv2.ellipse(img,(255,255),(100,50),0,0,180,255,-1) #ellipse

# ROWSx1x2
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
# True -> closed figure
img = cv2.polylines(img,[pts],True,(0,255,255))

# 字型
font = cv2.FONT_HERSHEY_SIMPLEX
# 4: Font Scale, cv2.LINE_AA gives anti-aliased line
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('Draw', img)
cv2.waitKey(0)
cv2.destroyWindow('Draw')