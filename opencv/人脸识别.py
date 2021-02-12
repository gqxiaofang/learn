#-*- coding = utf-8 -*-
#@Time : 2021/2/13 下午2:49
#@Author : 小方
#@File :人脸识别.py
#@Software : PyCharm
import cv2 as cv
import matplotlib.pyplot as plt

# print(cv.__file__)

img = cv.imread("./image/yangzi.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 实例化检测器
face_cas = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cas.load("haarcascade_frontalface_default.xml")

eyes_cas = cv.CascadeClassifier("haarcascade_eye.xml")
eyes_cas.load("haarcascade_eye.xml")

# 人脸检测
face_rects = face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
# 绘制人脸　检测眼睛
for facerect in face_rects:
    x,y,w,h = facerect
    cv.rectangle(img, (x,y),(x+w, y+h),(0, 255, 0),3)
    roi_color = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]
    eyes = eyes_cas.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0, 255, 0), 3)

plt.imshow(img[:,:,::-1])
plt.show()