import cv2 as cv
import numpy as np
import datetime


camera_list = [0,1,2]
cameras = {}

#initialize cameras
for cam_int in camera_list:
    capture = cv.VideoCapture(cam_int)
    window_name = "Camera %s" % str(cam_int)
    cv.namedWindow(window_name)
    cameras[window_name] = capture
    # cameras = np.append(cameras, [[capture, window_name]], axis = 0)

display_video = True
recording = False

while display_video:
    for win_name, vid_cap in cameras.items():
        ret, frame = vid_cap.read()
        if not ret:
            continue
        cv.imshow(win_name, frame)
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
            img_name = "{}-{}.png".format(win_name, datetime_now)

            cv.imwrite(img_name, frame)
            print("{} written!".format(img_name))
        #TODO: Add recording option

for win_name, vid_cap in cameras.items():
    vid_cap.release()

cv.destroyAllWindows()
