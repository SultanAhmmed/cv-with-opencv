import os
import cv2
import numpy as np



img = cv2.imread(os.path.join(".","data","cat.jpg"))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img_gray, (5,5), 0)
img_edge = cv2.Canny(blur, 50, 200)
img_edge_di = cv2.dilate(img_edge, np.ones((5,5), dtype=np.int8))
img_edge_er = cv2.erode(img_edge_di, np.ones((5,5), dtype=np.int8))

cv2.imshow('Img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_di', img_edge_di)
cv2.imshow('img_edge_er', img_edge_er)
cv2.waitKey(0)