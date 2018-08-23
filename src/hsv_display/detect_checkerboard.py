import cv2 as cv
import numpy as np
import datetime


window_name = "Camera_%s" % str(0)
cv.namedWindow(window_name)
camera = [cv.VideoCapture(0), window_name]

flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)

input_percent = 0.1
input_percent_reverse = 1.0 - input_percent

while True:
    ret, frame = camera[0].read()
    if not ret:
        continue
    cv.imshow(camera[1], frame)
    key_press = cv.waitKey(1) & 0xFF


    # Convert BGR to HSV
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_black_checkerboard = np.array([0, 0, 0])
    upper_black_checkerboard = np.array([180, 40, int(255 * 0.3)])
    lower_white_checkerboard = np.array([0, 0, int(255 * 0.3)])
    upper_white_checkerboard = np.array([180, 40, 255])
    # Threshold the HSV image to get only blacks and white
    black_mask = cv.inRange(hsv_frame, lower_black_checkerboard, upper_black_checkerboard)
    white_mask = cv.inRange(hsv_frame, lower_white_checkerboard, upper_white_checkerboard)

    mask = cv.max(black_mask, white_mask)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask=mask)
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
    elif key_press >= ord('0') and key_press <= ord('9'):
        input_percent = (key_press - ord('0')) * 0.1
        input_percent_reverse = 1.0 - input_percent
        print("input_percent:{}".format(int(100* input_percent)))
    elif key_press == ord('+'):
        input_percent += 0.01
        input_percent_reverse = 100.0 - input_percent
        print("input_percent:{}".format(int(100* input_percent)))
    elif key_press == ord('-'):
        input_percent -= 0.01
        input_percent_reverse = 100.0 - input_percent
        print("input_percent:{}".format(int(100* input_percent)))

camera[0].release()
cv.destroyAllWindows()
