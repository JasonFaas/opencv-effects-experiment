import cv2 as cv
import numpy as np
import datetime


window_name = "Camera_%s" % str(0)
cv.namedWindow(window_name)
camera = [cv.VideoCapture(0), window_name]

flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)

while True:
    ret, frame = camera[0].read()
    if not ret:
        continue
    cv.imshow(camera[1], frame)
    key_press = cv.waitKey(1) & 0xFF


    # Convert BGR to HSV
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv_frame, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('mask',mask)
    cv.imshow('res',res)

    if key_press == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif key_press == ord('s'):
        print("saving image")
        datetime_now = str(datetime.datetime.now()).replace(' ', '_')
        img_name = "{}-{}.png".format(str(camera[1]), datetime_now)

        cv.imwrite(img_name, frame)
        print("{} written!".format(img_name))

camera[0].release()
cv.destroyAllWindows()
