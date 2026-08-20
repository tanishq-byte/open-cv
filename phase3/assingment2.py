import cv2

image = cv2.imread(input("enter the file location "))
if image is not None:
    print("successfully loaded image ")
else:
    print("error in loading image")


def line(image):
    a = int(input("inputx1"))
    b = int(input("inputy1"))
    c = int(input("input x2"))
    d = int(input("input y2"))
    pt1 = (a, b)
    pt2 = (c, d)
    thickness = int(input("thickness="))
    color = (255, 255, 0)
    lined_image = cv2.line(image, pt1, pt2, color, thickness)
    cv2.imshow("lined image", lined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    choice = input("1.save the image \n 2.delete the image ")
    if choice == "1":
        cv2.imwrite("lined.png", lined_image)
    elif choice == "2":
        print("image deleted")
    else:
        print("invalid statement ")


def rectangle(image):
    a = int(input("inputx1"))
    b = int(input("inputy1"))
    c = int(input("input x2"))
    d = int(input("input y2"))
    pt1 = (a, b)
    pt2 = (c, d)
    thickness = int(input("thickness="))
    color = (255, 255, 0)
    rectangle_image = cv2.rectangle(image, pt1, pt2, color, thickness)
    cv2.imshow("rectangle image", rectangle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    choice = input("1.save the image \n 2.delete the image ")
    if choice == "1":
        cv2.imwrite("rectangle.png", rectangle_image)
    elif choice == "2":
        print("image deleted")
    else:
        print("invalid statement ")


def circle(image):
    a = int(input("inputx1"))
    b = int(input("inputy1"))
    centre = (a, b)
    radius = int(input("input radius"))
    thickness = int(input("thickness (-1 for filled and 1 for hollow )="))
    color = (255, 255, 0)
    circle_image = cv2.circle(image, centre, radius, color, thickness)
    cv2.imshow("circle image", circle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    choice = input("1.save the image \n 2.delete the image ")
    if choice == "1":
        cv2.imwrite("circle.png", circle_image)
    elif choice == "2":
        print("image deleted")
    else:
        print("invalid statement ")


def text(image):
    txt = input("enter the text to add")
    thickness = int(input("thickness="))
    color = (255, 255, 0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    a = int(input("inputx1"))
    b = int(input("inputy1"))
    org = (a, b)
    text_image = cv2.putText(image, txt, org, font, 1.2, color, thickness)
    cv2.imshow("text image", text_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    choice = input("1.save the image \n 2.delete the image ")
    if choice == "1":
        cv2.imwrite("text.png", text_image)
    elif choice == "2":
        print("image deleted")
    else:
        print("invalid statement ")


def main():
    a = input("editing the image \n 1.add line \n 2.add rectangle \n 3.add circle \n4.add text ")
    if a == "1":
        line(image)
    elif a == "2":
        rectangle(image)
    elif a == "3":
        circle(image)
    elif a == "4":
        text(image)
    else:
        print("invalid choice exiting")


main()