import cv2
image = cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/phase3/imageresizing.jpeg")

if image is not None:
    print("image loaded successfully")


else:
    print("error in loading image")

centre=(160,250)
color =(255,0,0)
thickness = -1
radius=100

cv2.imshow("orginal image",image)
circle_image=cv2.circle(image,centre,radius,color,thickness)
cv2.imshow("circle image ",circle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("circle.png",circle_image)
