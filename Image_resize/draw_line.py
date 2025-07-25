import cv2

image = cv2.imread("image.jpg")
if image is None :
    print("Error")

else:
   print("loaded")


   pt1 = (50 , 100)
   pt2 = (300,100)
   color = (0, 255, 0)
   thickness = 4

   cv2.line(image , pt1, pt2, color , thickness)
   cv2.imshow("line image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()