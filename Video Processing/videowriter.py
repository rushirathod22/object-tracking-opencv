import cv2

camera = cv2.VideoCapture(1)  # 1 is for youcam open


frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorded = cv2.VideoWriter("my_video.avi",codec,20,(frame_width, frame_height))

while True:
    success , frame = camera.read() # ret= true/false frame= image

    if not success:
        print("not load ")
        break
    recorded.write(frame)
    cv2.imshow("Recording Feed ", frame)

    if cv2.waitKey(1)& 0xFF  == ord('q'):
        print("Quiting....")
        break

camera.release
cv2.destroyAllWindows()