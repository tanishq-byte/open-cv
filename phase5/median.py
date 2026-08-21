import cv2

image=cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/phase5/images3.jpeg")

blured_image = cv2.medianBlur(image,5)
gaussain_blur = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("original image",image)
cv2.imshow("medioan blured image",blured_image)



# cv2.imshow("blured image",gaussain_blur) 
cv2.waitKey(0)
cv2.destroyAllWindows()