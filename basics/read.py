import cv2 as cv
# img = cv.imread('../Resources/Photos/cat_large.jpg')
# cv.imshow("Cat",img)


## Init Video Object
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

## Playing Video by showing image per frame
while True :
    isTrue, frame = capture.read()
    cv.imshow("Video",frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)