import cv2 as cv
import numpy as np
import datetime


camera_list = [1, 2]
window_name = "Camera_%s" % str(0)
cv.namedWindow(window_name)
#TODO: Initialize cameras with empty so everything can be done in loop
cameras = [[cv.VideoCapture(0), window_name]]

#initialize cameras
for cam_int in camera_list:
    capture = cv.VideoCapture(cam_int)
    window_name = "Camera %s" % str(cam_int)
    cv.namedWindow(window_name)
    cameras = np.append(cameras, [[capture, window_name]], axis = 0)

display_video = True
recording = False

while display_video:
    for cam_int in cameras:
        ret, frame = cam_int[0].read()
        if not ret:
            continue
        cv.imshow(cam_int[1], frame)
        key_press = cv.waitKey(1) & 0xFF

        if key_press == 27:
            # ESC pressed
            print("Escape hit, closing...")
            display_video = False
            break
        elif key_press == ord('s'):
            #TODO: Either add functionality for frame specific frame saving or save all 3
            print("saving image")
            datetime_now = str(datetime.datetime.now()).replace(' ', '_')
            img_name = "{}-{}.png".format(str(cam_int[1]), datetime_now)

            cv.imwrite(img_name, frame)
            print("{} written!".format(img_name))
        #TODO: Add recording option

for cam_int in cameras:
    cam_int[0].release()

cv.destroyAllWindows()
