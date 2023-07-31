import cv2
import matplotlib.pyplot as plt
import pandas as pd
import os 
from vision2 import Vision 

cascade_coral = cv2.CascadeClassifier('cascade/params.xml')
vision_coral = Vision(None)
testImagePath= "EDRSegment10.5_2022.12.16_AfterLeft/G0016252.JPG"

rectangles = cascade_coral.detectMultiScale(testImagePath)
detection_image = vision_coral.draw_rectangles(testImagePath, rectangles)
cv2.imshow('matches', detection_image)

cv2.waitKey(0)
  
# closing all open windows
cv2.destroyAllWindows()
