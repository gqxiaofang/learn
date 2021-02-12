#-*- coding = utf-8 -*-
#@Time : 2021/2/12 下午6:16
#@Author : 小方
#@File :30-ORB.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./image/tv.jpg")

orb = cv.ORB_create(nfeatures=5000)

kp, des = orb.detectAndCompute(img, None)

img2 = cv.drawKeypoints(img, kp, None, flags=0)
plt.imshow(img2[:, :, ::-1])
plt.show()