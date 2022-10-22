import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def show_img(img):
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    plt.imshow(img)
    
    plt.show()

### Test 
img = cv.imread('../Resources/Photos/cats 2.jpg')
### Average Blur
average = cv.blur(img,(3,3))
### Gaussian Blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gauss',gauss)
### Median Blur
median = cv.medianBlur(img,3)
cv.imshow('Median',median)
### Bilateral Blur
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',median)

#show_img(img)
show_img(average)
