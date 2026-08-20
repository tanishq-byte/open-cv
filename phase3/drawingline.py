import cv2
image = cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/phase3/imageresizing.jpeg")

if image is not None:
    print("image loaded successfully")


else:
    print("error in loading image")

pt1= (10,80)
pt2= (80,80)
color =(255,0,0)
thickness = 4

cv2.imshow("orginal image",image)
line_image=cv2.line(image,pt1,pt2,color,thickness)
cv2.imshow("line drawn image ", line_image)
cv2.waitKey(0)
cv2.destroyAllwindows()
cv2.imwrite("lined_image.png",line_image)
