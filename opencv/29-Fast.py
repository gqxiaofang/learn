#-*- coding = utf-8 -*-
#@Time : 2021/2/12 下午5:23
#@Author : 小方
#@File :29-Fast.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./image/tv.jpg")

fast = cv.FastFeatureDetector_create(threshold=30)

kp = fast.detect(img, None)

img2 = cv.drawKeypoints(img, kp, None, color=(0, 0, 255))

fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)
img3 = cv.drawKeypoints(img, kp, None, color=(0, 0, 255))

plt.imshow(img3[:, :, ::-1])
plt.show()