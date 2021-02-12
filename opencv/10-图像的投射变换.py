#-*- coding = utf-8 -*-
#@Time : 2021/2/8 下午6:19
#@Author : 小方
#@File :10-图像的投射变换.py
#@Software : PyCharm

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

kids = cv.imread("./image/kids.jpg")
rows, cols = kids.shape[:2]

pst1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pst2 = np.float32([[100, 145], [300, 100], [80, 290], [310, 300]])

T = cv.getPerspectiveTransform(pst1, pst2)

res5 = cv.warpPerspective(kids, T, (cols, rows))

plt.imshow(res5[:,:,::-1])
plt.show()