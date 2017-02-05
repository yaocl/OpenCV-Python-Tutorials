# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 列印所有 color space 的 flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags

# 想找到藍色的 HSV value，可以直接用 cv2.cvtColor 將藍色傳進去

green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green
#[[[ 60 255 255]]]