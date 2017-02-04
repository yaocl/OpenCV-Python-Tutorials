#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

# 讀取 index 0 的camera
cap = cv2.VideoCapture(0)

print "frame width=",cap.get(3),", height=",cap.get(4)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here，由 BGR 轉換為 gray-scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()