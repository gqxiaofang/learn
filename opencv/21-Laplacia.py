#-*- coding = utf-8 -*-
#@Time : 2021/2/12 下午12:50
#@Author : 小方
#@File :21-Laplacia.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

horse = cv.imread("./image/horse.jpg", 0)

res = cv.Laplacian(horse, cv.CV_16S)

res = cv.convertScaleAbs(res)

plt.imshow(res, cmap=plt.cm.gray)
plt.show()
