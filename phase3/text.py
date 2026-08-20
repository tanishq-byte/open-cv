import cv2
image = cv2.imread("/Users/tanishqkhetwal/Desktop/open-cv/phase3/imageresizing.jpeg")

if image is not None:
    print("image loaded successfully")


else:
    print("error in loading image")

text="I am tanishq "
color =(255,255,0)
thickness = 2
scalefactor=1.2
org=(125,250)

cv2.imshow("orginal image",image)
text_image=cv2.putText(image,text,org,cv2.FONT_HERSHEY_SIMPLEX,scalefactor,color,thickness)
cv2.imshow("texted image ",text_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("text.png",text_image)
