import numpy as np
import cv2 as cv

events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)

def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEWHEEL:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x, y), (x + 50, y + 75), (100, 255, 100), -1)


# black image
img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
win_name = "img_with_shapes"
cv.namedWindow(winname=win_name)
cv.setMouseCallback(win_name, draw_circle)

while True:
    # show img
    cv.imshow(winname=win_name, mat=img)
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break

# cleanup
cv.destroyAllWindows()
