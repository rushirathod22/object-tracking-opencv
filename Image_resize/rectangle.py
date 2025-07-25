import cv2

image = cv2.imread("image.jpg")
if image is None :
    print("Error")

else:
    print("loaded")
    pt1 = (200,200)
    pt2 = (450, 500)

    color = (0,0, 255)
    thickness = 3
    cv2.rectangle(image , pt1, pt2, color,thickness)
    cv2.imshow("rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   