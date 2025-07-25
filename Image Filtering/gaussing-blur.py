import cv2
image = cv2.imread("C:\Personal campus\Airtificial Intelligence\OpenCV\Image Filtering\image.jpg")

blurred = cv2.GaussianBlur(image,(7,7),3)

cv2.imshow("original",image)
cv2.imshow("blured",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()  