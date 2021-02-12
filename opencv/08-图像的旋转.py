#-*- coding = utf-8 -*-
#@Time : 2021/2/7 下午9:38
#@Author : 小方
#@File :08-图像的旋转.py
#@Software : PyCharm

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

kids = cv.imread("./image/kids.jpg")
rows, cols = kids.shape[:2]

M = cv.getRotationMatrix2D((cols/2, rows/2), 45, 0.5)

res3 = cv.warpAffine(kids, M, (cols, rows))

plt.imshow(res3[:,:,::-1])
plt.show()
