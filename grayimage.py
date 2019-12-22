import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('/home/dev/Dev/FaceDetection/LTJ/jonas.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('jonas.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

cv2.imwrite('/home/dev/Dev/FaceDetection/LTJ/grayimage.jpg'.img)
