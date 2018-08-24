import numpy as np
import cv2 as cv

# black image
img = np.zeros(shape=(256, 256, 3), dtype=np.uint8)

# draw red line
cv.line(img=img, pt1=(10,10), pt2=(20,40), color=(100, 100, 255), thickness=3)

cv.rectangle(img=img, pt1=(20,40), pt2=(40,80), color=(255, 100, 100))

cv.circle(img=img, center=(140,80), radius=100, color=(200,200,200), thickness=3)

cv.ellipse(img=img, center=(140,80), axes=(50,100), angle=50, startAngle=0, endAngle=270, color=(250, 250, 100), thickness=-1)

# polygon
pts = np.array([[10, 200], [20, 150], [60, 200], [150, 50]], np.int32)
cv.polylines(img, [pts], True, (0, 255, 255), thickness=5)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Drawing Images',(150,200), font, 2,(150,150,255),2,cv.LINE_AA)


# show img
cv.imshow(winname="img_with_shapes", mat=img)
cv.waitKey(-1)

# cleanup
cv.destroyAllWindows()
