import cv2 

a = input("enter file location")
image= cv2.imread(a)
if image is not None:
    print("successfully loaded ")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

else:
    print("error in loading the image ")

print("enter your choice\n 1. to save the image \n 2. to show the image ")
choice = input("")
if choice == "1":
     print("converted to gray scale ")
     cv2.imwrite("assingment1.jpg",gray)
     print("image saved successfully")
elif choice == "2":
    
    print("converted to gray scale ")
    b= input("name for output file ")
    cv2.imshow(b, gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else :
    print("invalid choice")
