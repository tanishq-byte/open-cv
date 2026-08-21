import cv2

camera=cv2.VideoCapture(1)
frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'mp4v')
recoder=cv2.VideoWriter("myvedio.mp4",codec,20,(frame_width,frame_height))

while True:
    success,image=camera.read()
    if not success:
        break
    recoder.write(image)
    cv2.imshow("showing vedio",image)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.release()
recoder.release()
cv2.destroyAllWindows()
