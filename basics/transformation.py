import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('cat',img)

### Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension) ## - val to left or up, + right or down

translated = translate(img, 100,100)
cv.imshow('translated',translated)

### Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension = (height,width)

    return cv.warpAffine(img,rotMat,dimension)
    

rotated = rotate(img, 45) ## -angle for clockwise rotation
cv.imshow('rotated',rotated)

### Fliping
fliped = cv.flip(img,0) # 1 for flipping vertically and horizontally
cv.imshow('flip',fliped)

cv.waitKey(0)