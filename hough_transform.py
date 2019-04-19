import cv2
import numpy as np

img = cv2.imread('square.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150)
minLineLength = 100
maxLineGap = 0


cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
