import cv2 as cv


def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

### Only work on live video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


img = cv.imread('../Resources/Photos/cat_large.jpg')
img_rs = rescaleFrame(img,0.2)
cv.imshow("Cat",img)
cv.imshow("Cat_rs",img_rs)
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
while True :
    isTrue, frame = capture.read()
    frame_rs = rescaleFrame(frame,0.2)
    
    cv.imshow("Video",frame)
    cv.imshow("Video_rs",frame_rs)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
