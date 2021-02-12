#-*- coding = utf-8 -*-
#@Time : 2021/2/9 下午2:01
#@Author : 小方
#@File :12-腐蚀和膨胀.py
#@Software : PyCharm
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 腐蚀膨胀
letter = cv.imread("./image/letter.png")
# 创建核结构
kernel = np.ones((5, 5), np.uint8)
letter2 = cv.erode(letter, kernel)

letter3 = cv.dilate(letter, kernel)

plt.imshow(letter3[:,:,::-1])
plt.show()