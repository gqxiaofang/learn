#-*- coding = utf-8 -*-
#@Time : 2021/2/11 下午2:40
#@Author : 小方
#@File :17-掩膜的应用.py
#@Software : PyCharm
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

cat = cv.imread("./image/cat.jpeg", 0)  # 灰度图

# 创建掩膜
mask = np.zeros(cat.shape[:2], np.uint8)
mask[400:650, 200:500] = 1

# 直方图
# hist = cv.calcHist([cat], [0], None, [256], [0, 256])

# plt.figure(figsize=(10, 8)) # 创
# plt.plot(hist)

mask_cat = cv.bitwise_and(cat, cat, mask=mask)
# plt.imshow(mask_cat, cmap=plt.cm.gray)
mask_hist = cv.calcHist([cat], [0], mask, [256], [0, 256])
plt.plot(mask_hist)
plt.show()
