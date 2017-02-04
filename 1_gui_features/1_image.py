#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

# cv2.IMREAD_COLOR 1 : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE 0: Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED -1: Loads image as such including alpha channel
img = cv2.imread('../assets/lena.jpg',cv2.IMREAD_GRAYSCALE)


# cv2.WINDOW_AUTOSIZE: 預設值，無法改變視窗大小
# cv2.WINDOW_NORMAL: 可以自由改變視窗大小
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)

# 如果是 64bits 機器，這一行要改成 k = cv2.waitKey(0) & 0xFF
k = cv2.waitKey(0) & 0xFF

if k == 27: # wait for ESC key to exit
	# 按下 ESC 就把所有視窗關掉
	cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
	# 按下 s 存 png 檔
	cv2.imwrite('lena_gray.png',img)
	cv2.destroyAllWindows()
