import cv2
image = cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/phase3/imageresizing.jpeg")

if image is not None:
    print("image loaded successfully")


else:
    print("error in loading image")

pt1= (10,10)
pt2= (80,80)
color =(255,0,0)
thickness = 3

cv2.imshow("orginal image",image)
rectangle_image=cv2.rectangle(image,pt1,pt2,color,thickness)
cv2.imshow("line drawn image ",rectangle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("rectangle.png",rectangle_image)
