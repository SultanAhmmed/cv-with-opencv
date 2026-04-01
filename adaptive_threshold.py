import os
import cv2


# img = cv2.imread(os.path.join('.','data','hadwritten.jpg'))
img = cv2.imread(os.path.join('.','data','cat.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)

thresh_adaptive = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('img',img)
cv2.imshow('thresh',thresh)
cv2.imshow('thresh_adaptive',thresh_adaptive)
cv2.waitKey(0)