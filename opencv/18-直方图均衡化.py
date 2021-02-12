#-*- coding = utf-8 -*-
#@Time : 2021/2/11 下午2:47
#@Author : 小方
#@File :18-直方图均衡化.py
#@Software : PyCharm
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

cat = cv.imread("./image/cat.jpeg", 0)  # 灰度图

dst = cv.equalizeHist(cat)
# plt.imshow(dst, cmap=plt.cm.gray)
plt.imshow(cat, cmap=plt.cm.gray)
plt.show()