import cv2
import sys
import numpy as np

def resize(img):
  (height, width, colors) = img.shape
  if (width >= height):
    height = int(500.0 * height / width)
    width = 500
  else:
    width = int(500.0 * width / height)
    height = 500
  return cv2.resize(img, (width, height))

img = cv2.imread(sys.argv[1])
img = resize(img)
(height, width, _) = img.shape
img2 = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.equalizeHist(gray)
cv2.imshow('gray', gray)
cv2.moveWindow('gray', 100, 0)

ret, thresh = cv2.threshold(gray, 100, 255, 0)
cv2.imshow('threshold', thresh)
cv2.moveWindow('threshold', 600, 0)

contours, hier = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

resultcnt = None
hull = None

for cnt in contours:
    hull = cv2.convexHull(cnt)    # find the convex hull of contour
    cv2.drawContours(img2, [hull], 0, (0, 255, 0), 1)
    hull = cv2.approxPolyDP(hull, 0.1 * cv2.arcLength(hull, True), True)
    if cv2.contourArea(cnt) > 10000:  # remove small areas like noise etc
        if len(hull) == 4:
            resultcnt = cnt
            cv2.drawContours(img, [hull], 0, (0, 255, 0), 2)
            break

# box = np.int32(cv2.cv.BoxPoints(cv2.minAreaRect(resultcnt)))
# cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# src = np.float32(np.reshape(hull, (4, 2)))
# # src = np.float32(hull)
# dst = np.float32(box)
# mat = cv2.getPerspectiveTransform(src, dst)
# newimg = cv2.warpPerspective(img, mat, (width, height))

cv2.imshow('contour', img2)
cv2.moveWindow('contour', 100, height + 50)
cv2.imshow('img', img)
cv2.moveWindow('img', 600, height + 50)

# cv2.imshow('newimg', newimg)

cv2.waitKey(0)
cv2.destroyAllWindows()