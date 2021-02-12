#-*- coding = utf-8 -*-
#@Time : 2021/2/11 下午3:18
#@Author : 小方
#@File :20-Sobel.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

horse = cv.imread("./image/letter.png", 0)

x = cv.Sobel(horse, cv.CV_16S, 1, 0)
y = cv.Sobel(horse, cv.CV_16S, 0, 1)

# Sobel算法
absx = cv.convertScaleAbs(x)
absy = cv.convertScaleAbs(y)

# Schaar

x = cv.Sobel(horse, cv.CV_16S, 1, 0, ksize=-1)
y = cv.Sobel(horse, cv.CV_16S, 0, 1, ksize=-1)

absx = cv.convertScaleAbs(x)
absy = cv.convertScaleAbs(y)
res = cv.addWeighted(absx, 0.5, absy, 0.5, 0)

plt.imshow(res, cmap=plt.cm.gray)
plt.show()
