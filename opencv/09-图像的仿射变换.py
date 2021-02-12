#-*- coding = utf-8 -*-
#@Time : 2021/2/8 下午5:52
#@Author : 小方
#@File :09-图像的仿射变换.py
#@Software : PyCharm

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

kids = cv.imread("./image/kids.jpg")
rows, cols = kids.shape[:2]

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[100, 100], [200, 50], [100, 250]])

M = cv.getAffineTransform(pts1, pts2)

# print(M)
res4 = cv.warpAffine(kids, M, (cols, rows))

plt.imshow(res4[:,:,::-1])
plt.show()