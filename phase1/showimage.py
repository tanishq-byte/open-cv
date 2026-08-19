import cv2

image= cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/images.jpeg")
if image is not None:
    cv2.imshow("image",image )
    cv2.waitKey(0)
    cv2.destroyALLwindows()
else :
    print("error in loading  image ")



