import cv2
import numpy as np
import datetime


camera_list = [1, 2]
window_name = "Camera_%s" % str(0)
cv2.namedWindow(window_name)
#TODO: Initialize cameras with empty so everything can be done in loop
cameras = [[cv2.VideoCapture(0), window_name]]

#initialize cameras
for cam_int in camera_list:
    capture = cv2.VideoCapture(cam_int)
    window_name = "Camera %s" % str(cam_int)
    cv2.namedWindow(window_name)
    cameras = np.append(cameras, [[capture, window_name]], axis = 0)

display_video = True
img_counter = 0

print(cameras[1][1])

while display_video:
    for cam_int in cameras:
        img_counter += 1
        ret, frame = cam_int[0].read()
        if not ret:
            continue
        cv2.imshow(cam_int[1], frame)
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            display_video = False
            break
        elif k%256 == ord('s'):
            #TODO: Either add functionality for frame specific frame saving or save all 3
            print("saving image")
            datetime_now = str(datetime.datetime.now()).replace(' ', '_')
            img_name = "{}-{}.png".format(str(cam_int[1]), datetime_now)

            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            # img_counter += 1

for cam_int in cameras:
    cam_int[0].release()

cv2.destroyAllWindows()
