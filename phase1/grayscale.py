import cv2

image= cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/images.jpeg")
if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    print("successfully converted to grayscale")
    cv2.imshow("gray",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("not loaded image")

cv2.imwrite("gray.jpg",gray)