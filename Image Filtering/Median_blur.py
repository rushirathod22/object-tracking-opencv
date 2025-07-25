import cv2
image = cv2.imread(" image.jpg")

if image is None:
    print("Error:")
else:
 blurred = cv2.medianBlur(image,5)

cv2.imshow("original",image)
cv2.imshow("clean image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()