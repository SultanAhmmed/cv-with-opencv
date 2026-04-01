import os
import cv2

img = cv2.imread(os.path.join('.','data','cat.jpg'))

k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussianblur = cv2.GaussianBlur(img, (k_size,k_size), 3)
img_meanblur = cv2.medianBlur(img, k_size)
img_bilateralblur = cv2.bilateralFilter(img, k_size, 75, 75)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussianblur', img_gaussianblur)
cv2.imshow('img_meanblur', img_meanblur)
cv2.imshow('img_bilateralblur', img_bilateralblur)
cv2.waitKey(0)