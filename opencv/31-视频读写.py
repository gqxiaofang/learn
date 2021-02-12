#-*- coding = utf-8 -*-
#@Time : 2021/2/12 下午6:33
#@Author : 小方
#@File :31-视频读写.py
#@Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

cap = cv.VideoCapture("image/DOG.wmv")

# 判断是否读取成功
while(cap.isOpened()):
    # 获取每一帧图像
    ret, frame = cap.read()
    # 是否获取成功
    if ret == True:
        cv.imshow("frame", frame)
    if cv.waitKey(25)&0xFF==ord("q"):
        break

cap.release()
cv.destroyWindow()