#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import time

filename = time.strftime("%m-%d-%H-%M-%S") + '.avi'
fps = 20

cap = cv2.VideoCapture(0)

# Get the width and height of frame
#size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
#        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

size = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))

# Define the codec and create VideoWriter object
# https://gist.github.com/takuma7/44f9ecb028ff00e2132e
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter(filename,fourcc, fps, size, True)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # vertical direction flip
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()