#-*- coding = utf-8 -*-
#@Time : 2021/2/12 下午12:52
#@Author : 小方
#@File :22-Canny.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

horse = cv.imread("./image/horse.jpg", 0)

res = cv.Canny(horse, 0, 100)

plt.imshow(res, cmap=plt.cm.gray)
plt.show()
