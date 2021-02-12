#-*- coding = utf-8 -*-
#@Time : 2021/2/11 下午2:30
#@Author : 小方
#@File :16-直方图.py
#@Software : PyCharm
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cat = cv.imread("./image/cat.jpeg", 0)  # 灰度图

# 直方图
hist = cv.calcHist([cat], [0], None, [256], [0, 256])

plt.figure(figsize=(10, 8)) # 画布
plt.plot(hist)

# plt.imshow(cat, cmap=plt.cm.gray)
plt.show()
