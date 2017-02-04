# -*- coding: utf-8 -*-

import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
	# 在 EVENT_LBUTTONUP 時，畫上 circle
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
# 設定 setMouseCallback 為 draw_circle
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
