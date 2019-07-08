import cv2
import os, time
import numpy as np

# Load two images
img1 = cv2.imread('images/Screenshot_2019-06-06-17-03-34.png')
img2 = cv2.imread('images/Screenshot_2019-06-07-21-29-39.png')
n = 10

#while(1):

#img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

for i in range (n) :
	j=(i+1)/10
	dst = cv2.addWeighted(img1,j,img2,1-j,0)
	time.sleep(0.5)
	cv2.imshow('image',dst)
	print(j)

cv2.waitKey(0)
cv2.destroyAllWindows()