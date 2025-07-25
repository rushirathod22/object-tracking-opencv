import cv2

image = cv2.imread("image.jpg")
if image is None :
    print("Error")

else:
   print("loaded")
   cv2.circle(image ,(650,150),100,(0,255,255), -1)
   cv2.imshow("Circle",image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()