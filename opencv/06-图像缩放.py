#-*- coding = utf-8 -*-
#@Time : 2021/2/7 下午9:24
#@Author : 小方
#@File :06-图像缩放.py
#@Software : PyCharm
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

kids = cv.imread("./image/kids.jpg")

# 绝对尺寸
rows, cols = kids.shape[:2]
# print(rows, cols)
res = cv.resize(kids, (2*cols, 2*rows))

# 相对尺寸
res1 = cv.resize(kids, None, fx=0.5, fy=0.5)


plt.imshow(res1[:,:,::-1])
plt.show()
