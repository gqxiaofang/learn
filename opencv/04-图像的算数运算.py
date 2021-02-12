#-*- coding = utf-8 -*-
#@Time : 2021/2/7 下午9:08
#@Author : 小方
#@File :04-图像的算数运算.py
#@Software : PyCharm

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

rain = cv.imread("./image/rain.jpg")
view = cv.imread("./image/view.jpg")

plt.imshow(rain[:, :, ::-1])
plt.show()

plt.imshow(view[:, :, ::-1])
plt.show()

#
img1 = cv.add(rain, view)
plt.imshow(img1[:, :, ::-1])
plt.show()
#
img2 = rain + view
plt.imshow(img2[:, :, ::-1])
plt.show()

