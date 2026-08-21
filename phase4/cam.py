import cv2

cap=cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    if not ret:
        print("could not read frames")
        break
    cv2.imshow("caputred feed", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        print("quitting")
        break

cap.release()
cv2.destroyAllWindows()
