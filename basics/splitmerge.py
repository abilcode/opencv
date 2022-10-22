import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../Resources/Photos/cat.jpg')
blank = np.zeros(img.shape[:2],dtype='uint8')
b,g,r = cv.split(img)
### Inverse
# img_merged = cv.merge([b,g,r])

### Grayscale concentration
# cv.imshow('b',b)

# cv.imshow('g',g)

# cv.imshow('r',r)

### Showing only blue, (Blue filter)
img_blue = cv.merge([b,blank,blank]) ## Format : BGR
img_blue = cv.cvtColor(img_blue,cv.COLOR_BGR2RGB)

plt.imshow(img_blue)
plt.show()

#cv.waitKey(0)