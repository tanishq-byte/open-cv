import cv2

image=cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/phase6/images (1).jpeg",cv2.IMREAD_GRAYSCALE)

rev,greyscale= cv2.threshold(image,120,255,cv2.THRESH_BINARY)

cv2.imshow("origina image",image)
cv2.imshow("thresholded  image",greyscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
