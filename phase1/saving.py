import cv2

image= cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/images.jpeg")
if image is not  None:
    success = cv2.imwrite("output.jpg", image)
    if success:
        print("image saved successfully")
    else:
        print("error in saving image")
else :
    print("error in loading image ")

