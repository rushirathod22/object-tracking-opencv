import cv2

image = cv2.imread("image.jpg")
if image is None :
    print("Error")

else:
   filpped_horizontaL = cv2.flip(  image,1)
   flipped_vertical  = cv2.flip(image,0)
   flipped_both = cv2.flip(image,-1)

cv2.imshow("original",image)
cv2.imshow("horizontal", filpped_horizontaL)
cv2.imshow("vertical",  flipped_vertical )
cv2.imshow("both", flipped_both)
cv2.waitKey(0)
cv2.destroyAllWindows()

              