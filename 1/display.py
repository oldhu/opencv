#!/usr/bin/env python

import cv
import sys

if len(sys.argv) != 2:
  print 'Usage: display.py ImageToLoadAndDisplay'
  exit(1)

img = cv.LoadImage(sys.argv[1])
cv.NamedWindow("Display window")
cv.ShowImage("Display window", img)
cv.WaitKey()
