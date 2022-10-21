import cv2 as cv
import numpy as np

img = cv.imread("/Users/abilfad/Documents/CODE/MLDS/opencv/Resources/Photos/cat.jpg")
cv.imshow("Cats",img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("Black",blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


#cv.imshow("Cats gray",gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow("Cats Canny",canny)

ret, thresh = cv.threshold(gray,123,255,cv.THRESH_BINARY)
cv.imshow('Threshold',thresh)

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.waitKey(0)