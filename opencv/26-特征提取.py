#-*- coding = utf-8 -*-
#@Time : 2021/2/12 下午4:25
#@Author : 小方
#@File :26-特征提取.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./image/chessboard.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img = cv.medianBlur(gray_img, 7)
gray = np.float32(gray_img)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
img[dst>0.001*dst.max()]=[0, 0, 255]

plt.figure(figsize=(10, 10))
# plt.imshow(gray_img, cmap=plt.cm.gray)
plt.imshow(img[:,:,::-1])
plt.show()