import cv2

image = cv2.imread("image.jpg")

if image is not None:
    print("loaded")
    croped = image[100:200 , 100:150]
    cv2.imshow("Original",image)
    cv2.imshow("Croped",croped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")