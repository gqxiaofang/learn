#-*- coding = utf-8 -*-
#@Time : 2021/2/7 下午1:12
#@Author : 小方
#@File :03.图像基础处理.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 创建图像
img = np.zeros((256, 256, 3), np.uint8)

# plt.imshow(img[:,:,::-1])
print(img[100, 100])
print(img[100, 100, 0])
img[100, 100] = (0, 0, 255)
plt.imshow(img[:,:,::-1])

print(img[100, 100])
print(img.shape)
print(img.dtype)
print(img.size)


# plt.show()