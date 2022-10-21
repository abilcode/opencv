import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# Paint the image for a certain colour (BGR)

blank[:] = 0,255,0 ## ALl green
blank[200:400, 300:400] = 0,0,255 ## red for certain area
cv.imshow("Green",blank)

## Draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=2) ### automaticaly filled if thickness = -1
cv.imshow('Reactangle',blank)

### Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3) ## 40 is the radius of the circle
cv.imshow('Circle',blank)

### Draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=1)

cv.imshow('Line',blank)
cv.putText(blank,"hello",(300,300),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv.imshow('Text',blank)
cv.waitKey(0)