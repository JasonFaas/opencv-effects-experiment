import cv2 as cv

cap = cv.VideoCapture("../resourses/opencv_video_2018-08-21_14:47:23.408106_0.mkv")
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv.destroyAllWindows()
