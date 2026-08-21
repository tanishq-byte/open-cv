import cv2

image=cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/phase6/images (1).jpeg",cv2.IMREAD_GRAYSCALE)

greyscale= cv2.Canny(image,20,200)

cv2.imshow("origina image",image)
cv2.imshow("canny image",greyscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
