#-*- coding = utf-8 -*-
#@Time : 2021/2/7 下午9:32
#@Author : 小方
#@File :07-图像的平移.py
#@Software : PyCharm

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

kids = cv.imread("./image/kids.jpg")
rows, cols = kids.shape[:2]
# print(rows, cols)
M = np.float32([[1, 0, 100], [0, 1, 50]])
res1 = cv.warpAffine(kids, M, (2*cols, 2*rows))

plt.imshow(res1[:,:,::-1])
plt.show()