import cv2
import numpy as np

camera_list = [1, 2]
window_name = "Camera %s" % str(0)
cv2.namedWindow(window_name)
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
            print("saving image")
            img_name_0 = "opencv_frame_{}_0.png".format(img_counter)
            cv2.imwrite(img_name_0, frame)
            print("{} written!".format(img_name_0))
            # img_counter += 1

for cam_int in cameras:
    cam_int[0].release()

cv2.destroyAllWindows()
