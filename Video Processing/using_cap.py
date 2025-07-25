import cv2

cap = cv2.VideoCapture(1)  # 1 is for youcam open

while True:
    ret , frame = cap.read() # ret= true/false frame= image

    if not ret:
        print("not load ")
        break

    cv2.imshow("Webcam Feed ", frame)

    if cv2.waitKey(1)& 0xFF  == ord('q'):
        print("Quiting....")
        break

cap.release
cv2.destroyAllWindows()