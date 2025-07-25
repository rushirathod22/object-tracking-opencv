import cv2

image = cv2.imread("image.jpg")

if image is not None:
    suc = cv2.imwrite("output.jpg",image)
    if suc :
       print("Image as 'output.jpg'")

    else:
        print("Failed")
else:
    print("Error : ")