# -*- coding: utf-8 -*-

import cv2
import numpy as np

# Load two images
img1 = cv2.imread('../assets/lena.jpg')
img2 = cv2.imread('../assets/opencv-logo.png')

# 要將 logo 放在 img1 的左上角，先以 img2 的大小，在 img1 設定 ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# 產生 img2 的 mask 及 inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 把 img1 中，剛剛的 img2 的 mask 放上去，把那些地方的圖像挖空
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# 取得 img2 需要的圖像處
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# 把 img1_bg 跟 img2_fg 相加起來
dst = cv2.add(img1_bg,img2_fg)
# 將 結果 dst 放回 img1
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()