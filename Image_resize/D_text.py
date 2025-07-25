import cv2

image = cv2.imread("image.jpg")
if image is None :
    print("Error")

else:
   print("loaded")

   cv2.putText(image , "Rushikesh",(450,200),cv2.FONT_HERSHEY_SIMPLEX ,1.2,(0,255,255),3)
   cv2.imshow("Text ",image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()