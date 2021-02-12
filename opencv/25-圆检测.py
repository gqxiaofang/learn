#-*- coding = utf-8 -*-
#@Time : 2021/2/12 下午2:33
#@Author : 小方
#@File :25-圆检测.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

star = cv.imread("./image/star.jpeg")
gray_img = cv.cvtColor(star, cv.COLOR_BGR2GRAY)
img = cv.medianBlur(gray_img, 7)

circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 200, param1=100, param2=50, minRadius=0, maxRadius=100)
for i in circles[0,:]:
    cv.circle(star, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv.circle(star, (i[0], i[1]), 2, (0, 255, 0), -1)

# plt.imshow(img, cmap=plt.cm.gray)
plt.imshow(star[:,:,::-1])
plt.show()