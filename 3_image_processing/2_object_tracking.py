# -*- coding: utf-8 -*-
import cv2
import numpy as np


def rot90(img, angle):
        if(angle == 270 or angle == -90):
            img = cv2.transpose(img)
            img = cv2.flip(img, 0)  # transpose+flip(0)=CCW
        elif (angle == 180 or angle == -180):
            img = cv2.flip(img, -1)  # transpose+flip(-1)=180
        elif (angle == 90 or angle == -270):
            img = cv2.transpose(img)
            img = cv2.flip(img, 1)  # transpose+flip(1)=CW
        elif (angle == 360 or angle == 0 or angle == -360):
            pass
        else :
            raise Exception("Unknown rotation angle({})".format(angle))
        return img

cap = cv2.VideoCapture(0)

while(1):
    # 由 camera 取得 frame
    _, frame = cap.read()

    # macbook pro 的 camera 預設影像轉了 90度，以下把畫面逆時針轉 90度，同時長與寬縮小一半
    frame = rot90(frame, -90)
    w, h = frame.shape[:2]
    frame = cv2.resize(frame, (h/2,w/2), interpolation = cv2.INTER_AREA)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定義 HSV 的藍色區間
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # bitwaise AND mask
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()