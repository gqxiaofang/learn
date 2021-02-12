#-*- coding = utf-8 -*-
#@Time : 2021/2/12 下午6:39
#@Author : 小方
#@File :32-视频保存.py
#@Software : PyCharm
import numpy as np
import cv2 as cv

cap = cv.VideoCapture("image/DOG.wmv")

width = int(cap.get(3))
height = int(cap.get(4))

out = cv.VideoWriter("out.avi", cv.VideoWriter_fourcc("M", "J", "P", "G"), 10, (width, height))

while(True):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()