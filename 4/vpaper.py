import cv2
import numpy


def resize(img):
  max = 400.0
  (height, width, colors) = img.shape
  if (width >= height):
    height = int(max * height / width)
    width = int(max)
  else:
    width = int(max * width / height)
    height = int(max)
  return cv2.resize(img, (width, height))

vc = cv2.VideoCapture(0)
cv2.namedWindow("bw",1);
cv2.moveWindow('bw', 100, 0)
cv2.namedWindow("v",1);
cv2.moveWindow('v', 600, 0)

while True:
  ret, img = vc.read()
  img = resize(img)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray = cv2.equalizeHist(gray)
  ret, thresh = cv2.threshold(gray, 110, 255, 0)
  cv2.imshow('bw', thresh)
  contours, hier = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  for cnt in contours:
      if cv2.contourArea(cnt) > 10000:  # remove small areas like noise etc
          hull = cv2.convexHull(cnt)    # find the convex hull of contour
          hull = cv2.approxPolyDP(hull, 0.1 * cv2.arcLength(hull, True), True)
          if len(hull) == 4:
              cv2.drawContours(img, [hull], 0, (0, 255, 0), 2)
  cv2.imshow('v', img)


