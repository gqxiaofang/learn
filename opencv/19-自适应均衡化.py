#-*- coding = utf-8 -*-
#@Time : 2021/2/11 下午3:05
#@Author : 小方
#@File :19-自适应均衡化.py
#@Software : PyCharm
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

cat = cv.imread("./image/cat.jpeg", 0)  # 灰度图

cl = cv.createCLAHE(2.0, (8, 8))

clahe = cl.apply(cat)

# dst = cv.equalizeHist(cat)
# plt.imshow(dst, cmap=plt.cm.gray)
plt.imshow(clahe, cmap=plt.cm.gray)
plt.show()