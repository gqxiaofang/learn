#-*- coding = utf-8 -*-
#@Time : 2021/2/9 上午10:23
#@Author : 小方
#@File :11-图像金字塔.py
#@Software : PyCharm

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

kids = cv.imread("./image/kids.jpg")

imgup = cv.pyrUp(kids)
imgup2 = cv.pyrUp(imgup)

imgdown = cv.pyrDown(kids)
imgdown2 = cv.pyrDown(imgdown)

plt.imshow(imgdown2[:,:,::-1])
plt.show()