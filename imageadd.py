import cv2
import numpy as np

img1 = cv2.imread('/home/dev/Dev/FaceDetection/LTJ/jonas.jpg')
img2 = cv2.imread('/home/dev/Dev/FaceDetection/LTJ/jonas2.jpg')

# add = img1 + img2
add = cv2.add(img1, img2)  #straight up adds the pixel values 

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) #0 is gamma value, to be left alone

cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()