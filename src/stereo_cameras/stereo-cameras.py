import cv2 as cv
import numpy as np
import datetime

ply_header = '''ply
format ascii 1.0
element vertex %(vert_num)d
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
end_header
'''


def write_ply(fn, verts, colors):
    verts = verts.reshape(-1, 3)
    colors = colors.reshape(-1, 3)
    verts = np.hstack([verts, colors])
    with open(fn, 'w') as f:
        f.write(ply_header % dict(vert_num=len(verts)))
        np.savetxt(f, verts, '%f %f %f %d %d %d')


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

    imgL = frame1
    imgR = frame0

    # disparity range is tuned for 'aloe' image pair
    #TODO: Investigate these variables
    window_size = 3
    min_disp = 16
    num_disp = 112-min_disp
    stereo = cv.StereoSGBM_create(minDisparity = min_disp,
        numDisparities = num_disp,
        blockSize = 16,
        P1 = 8*3*window_size**2,
        P2 = 32*3*window_size**2,
        disp12MaxDiff = 1,
        uniquenessRatio = 10,
        speckleWindowSize = 100,
        speckleRange = 32
    )


    print('computing disparity...')
    disp = stereo.compute(imgL, imgR).astype(np.float32) / 16.0

    cv.imshow('disparity', (disp-min_disp)/num_disp)

    key_press = cv.waitKey(100) & 0xFF
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
