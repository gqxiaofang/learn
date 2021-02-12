#-*- coding = utf-8 -*-
#@Time : 2021/2/7 下午9:19
#@Author : 小方
#@File :05-图像的混合.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

rain = cv.imread("./image/rain.jpg")
view = cv.imread("./image/view.jpg")

img3 = cv.addWeighted(view, 0.3, rain, 0.7, 0)

plt.imshow(img3[:, :, ::-1])
plt.show()