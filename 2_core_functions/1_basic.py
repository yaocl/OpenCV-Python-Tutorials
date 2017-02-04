# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('../assets/lena.jpg')

# 列印 (100,100) 位置的 BGR 顏色: [ 88  78 185]
px = img[100,100]
print px

# 只取得 B 的色碼: 88
blue = img[100,100,0]
print blue

# 把 [100,100] 改成白色
img[100,100] = [255,255,255]
print img[100,100]

######

#accessing RED value
print img.item(10,10,2)

#modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)
# 100

####

# img.shape 是 a tuple of number of rows, columns and channels (if image is color)
# (512, 512, 3)
print img.shape

# 圖片大小: 786432
print img.size

# 資料型別 uint8
print img.dtype

########

roi = img[280:340, 330:390]
img[273:333, 100:160] = roi

cv2.imshow('image',img)

# 如果是 64bits 機器，這一行要改成 k = cv2.waitKey(0) & 0xFF
k = cv2.waitKey(0) & 0xFF

if k == 27: # wait for ESC key to exit
	# 按下 ESC 就把所有視窗關掉
	cv2.destroyAllWindows()

#####

# 用 split 將圖片分成 b, g, r 三個 array
b,g,r = cv2.split(img)

# 再將剛剛的 b,g,r 整合成圖片
img = cv2.merge((b,g,r))

# 將 r 的部分都設定為 0
img[:,:,2] = 0

cv2.imshow('image',img)

# 如果是 64bits 機器，這一行要改成 k = cv2.waitKey(0) & 0xFF
k = cv2.waitKey(0) & 0xFF

if k == 27: # wait for ESC key to exit
	# 按下 ESC 就把所有視窗關掉
	cv2.destroyAllWindows()

