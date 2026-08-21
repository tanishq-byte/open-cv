import cv2
import numpy as np
image=cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/phase5/Screenshot 2026-08-21 at 12.30.50 PM.png")
sharp=np.array([
    [0,-1,0],
    [-1,5,0],
    [0,-1,0]
    ])
sharpend= cv2.filter2D(image,-1,sharp)
cv2.imshow("original image",image)
cv2.imshow("sharpend image",sharpend)
cv2.waitKey(0)
cv2.destriyAllWindows()