# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the data, converters convert the letter to a number
# letter-recognition.data 裡面有 20000 筆資料，前 10000 筆是 training samples
# 後 10000 筆是 test samples
# 每一行第一個是 letter，後面是 UCI Machine Learning Repository http://archive.ics.uci.edu/ml/ 的 features
data= np.loadtxt('../assets4/letter-recognition.data', dtype= 'float32', delimiter = ',', converters= {0: lambda ch: ord(ch)-ord('A')})

# split the data to two, 10000 each for train and test
# 把資料分成兩段，各 10000 筆
train, test = np.vsplit(data,2)

# split trainData and testData to features and responses
responses, trainData = np.hsplit(train,[1])
labels, testData = np.hsplit(test,[1])

# Initiate the kNN, classify, measure accuracy.
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, result, neighbours, dist = knn.findNearest(testData, k=5)

correct = np.count_nonzero(result == labels)
accuracy = correct*100.0/10000
print accuracy

# 最後的正確率為 93.06，如果想要增加正確率，必須 iteratively add error data in each level
