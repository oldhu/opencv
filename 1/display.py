#!/usr/bin/env python

import cv2
import sys

if len(sys.argv) != 2:
  print 'Usage: display.py ImageToLoadAndDisplay'
  exit(1)

img = cv2.imread(sys.argv[1])
cv2.namedWindow("Display window")
cv2.imshow("Display window", img)
cv2.waitKey(0)
