import numpy as np
import cv2



img = np.zeros((512,512,3),np.uint8)
line = cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow('changshi',img);cv2.waitKey(0);
