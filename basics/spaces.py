import cv2 as cv
import matplotlib.pyplot as plt


### Read Image
img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Cat',img)

### If you want to show it in RGB
img_ = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img_)
plt.show()

# ### BGR to GRAYSCALE
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Cat Gray',gray)

# ### BGR to HSV
# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('Cat HSV',hsv)

# ### BGR to L*A*B
# lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('Cat LAB',lab)


### WE COULD INVERSE ALL THE IMAGE from a -> b or b -> a
cv.waitKey(0)