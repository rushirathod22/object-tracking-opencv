import cv2

image = cv2.imread("image.jpg")
if image is not None:
    print("loaded")
    # image convert into gray
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY ", gray)
    cv2.imwrite("GRAY.jpg",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error:")