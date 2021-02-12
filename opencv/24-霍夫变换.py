#-*- coding = utf-8 -*-
#@Time : 2021/2/12 下午1:51
#@Author : 小方
#@File :24-霍夫变换.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./image/rili.jpg")
edges = cv.Canny(img, 50, 150)

lines = cv.HoughLines(edges, 0.8, np.pi/180, 150)
for line in lines:
    # print(lines)
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = rho*a
    y0 = rho*b
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*a)
    x2 = int(x0-1000*(-b))
    y2 = int(y0-1000*a)
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0))

# plt.imshow(edges, cmap=plt.cm.gray)
plt.imshow(img[:,:,::-1])
plt.show()