import cv2

image = cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/images.jpeg")
if image is None:
    print("error")
else:
    print("successfully loaded image")
    h, w, c=image.shape
    print(f"image shape is \n height:{h}\n width: {w}\n channel:{c} " )

