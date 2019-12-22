import numpy as np
import cv2

img = cv2.imread('/home/dev/Dev/FaceDetection/LTJ/jonas.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (300, 300), (255, 255, 255), 5) #start end color width

cv2.rectangle(img, (10, 10), (300, 300), (255, 255, 255), 5)

cv2.circle(img, (150, 150), 30, (266, 255, 255), -1)  #-1 causes the circle to fill with color, other number will be width

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)  #data type object in numpy
cv2.polylines(img, [pts], False, (255, 255, 255), 5)

font = cv2.FONT_HERSHEY_COMPLEX
font =  cv2.putText(img, 'Jonas', (100,100), font, 1, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
