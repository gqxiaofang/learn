#-*- coding = utf-8 -*-
#@Time : 2021/2/10 上午11:33
#@Author : 小方
#@File :14-黑帽礼貌.py
#@Software : PyCharm
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

open = cv.imread("./image/letteropen.png")
close = cv.imread("./image/letterclose.png")

kernel = np.ones((10, 10), np.uint8)

top = cv.morphologyEx(open, cv.MORPH_TOPHAT, kernel)
black = cv.morphologyEx(close, cv.MORPH_BLACKHAT, kernel)

plt.imshow(black[:,:,::-1])
plt.show()