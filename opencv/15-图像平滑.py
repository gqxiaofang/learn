#-*- coding = utf-8 -*-
#@Time : 2021/2/10 上午11:45
#@Author : 小方
#@File :15-图像平滑.py
#@Software : PyCharm
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

dogsp = cv.imread("./image/dogsp.jpeg")
doggau = cv.imread("./image/dogGauss.jpeg")

# 均值滤波
dog = cv.blur(doggau, (5, 5))

# 高斯滤波
dog = cv.GaussianBlur(doggau, (3, 3), 1)

# 中值滤波
dog = cv.medianBlur(dogsp, 3)

plt.imshow(dog[:,:,::-1])
plt.imshow(dogsp[:,:,::-1])
plt.show()
