import cv2

image = cv2.imread("image.jpg")

if image is  None:
    print("error")
else:
    print("loaded")

    resized = cv2.resize(image ,(300,300))
    # width ,height

    cv2.imshow("original Image",image)
    cv2.imshow("resized ",resized)

    cv2.imwrite("resized_output.jpg",resized)