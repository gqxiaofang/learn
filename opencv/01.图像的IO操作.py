#-*- coding = utf-8 -*-
#@Time : 2021/2/7 上午11:49
#@Author : 小方
#@File :01.图像的IO操作.pywo
#@Software : PyCharm

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread("image/tree.jpg", 0)     # 途径问题
# print(cv.__version__)

# opencv中显示
# cv.imshow("tree", img)         # 显示
# cv.waitKey(0)
# cv.destroyWindow()

# matplotlib展示
# plt.imshow(img[:,:,::-1])
plt.imshow(img, cmap=plt.cm.gray)
plt.show()

# k = cv.waitKey(0)

# 保存图像
cv.imwrite("image/treedouble.png", img)
