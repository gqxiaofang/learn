#-*- coding = utf-8 -*-
#@Time : 2021/2/9 下午2:12
#@Author : 小方
#@File :13-开闭运算.py
#@Software : PyCharm
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

open = cv.imread("./image/letteropen.png")
close = cv.imread("./image/letterclose.png")

kernel = np.ones((10, 10), np.uint8)
cvopen = cv.morphologyEx(open, cv.MORPH_OPEN, kernel)
cvclose = cv.morphologyEx(close, cv.MORPH_CLOSE, kernel)

plt.imshow(cvclose[:,:,::-1])
plt.show()