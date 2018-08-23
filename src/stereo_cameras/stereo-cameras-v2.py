import cv2 as cv
import numpy as np
import datetime
from matplotlib import pyplot as plt

camera_list = [2]
window_name = "Camera_%s" % str(0)
cv.namedWindow(window_name)
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
    ret0, frame0 = cameras[0][0].read()
    ret1, frame1 = cameras[1][0].read()
    if not ret0 or not ret1:
        continue
    cv.imshow(cameras[0][1], frame0)
    cv.imshow(cameras[1][1], frame1)

    imgL = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    imgR = cv.cvtColor(frame0, cv.COLOR_BGR2GRAY)

    stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(imgL, imgR)
    plt.imshow(disparity, 'gray')
    plt.show()


    key_press = cv.waitKey(1000) & 0xFF
    break
    if key_press == 27:
        # ESC pressed
        print("Escape hit, closing...")
        display_video = False
        break
    # elif key_press == ord('s'):
        # print("saving image")
        datetime_now = str(datetime.datetime.now()).replace(' ', '_')
        img_name = "{}-{}.png".format(str(cam_int[1]), datetime_now)

        # cv.imwrite(img_name, frame)
        # print("{} written!".format(img_name))

for cam_int in cameras:
    cam_int[0].release()

cv.destroyAllWindows()
