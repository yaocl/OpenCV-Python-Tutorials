# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('../assets/lena.jpg',0)
rows,cols = img.shape

# 以 np.float32 為資料型別產生 array，傳送給 cv2.warpAffine()，就可以移動到 (100,50)
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()