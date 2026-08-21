import cv2

image=cv2.i("/Users/tanishqkhetwal/Desktop/open-cv/phase5/images.jpeg")

gaussain_blur = cv2.GaussianBlur(image,(7,7),0)

cv2.imshow("original image",image)
cv2.imshow("blured image",gaussain_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
