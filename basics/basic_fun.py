import cv2 as cv 

img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Cat',img)

### Gray Scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

### Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

### Edge Cascade
canny = cv.Canny(img,123,175) ### We can reduced the edges by using the blured img
cv.imshow('Canny Edges',canny)

### Dilating the image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

### Eroding the image
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

### Resized
resized = cv.resize(img, (500,500),interpolation=cv.INTER_AREA)
cv.imshow("resized",resized)
cv.waitKey(0)