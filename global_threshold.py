import os
import cv2

img = cv2.imread(os.path.join('.','data','cat.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = img_threshold = cv2.threshold(img_gray, 110, 255, cv2.THRESH_BINARY)
thresh = cv2.blur(thresh, (10,10))
ret, thresh = img_threshold = cv2.threshold(thresh, 110, 255, cv2.THRESH_BINARY)


cv2.imshow("Image", img)
cv2.imshow("thresh", thresh)
print(ret)
cv2.waitKey(0)