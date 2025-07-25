import cv2

img = cv2.imread(r"C:\Personal campus\Airtificial Intelligence\OpenCV\Edge Detection\Rushi.png",cv2.IMREAD_GRAYSCALE)

ret , thresh_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("original",img)
cv2.imshow("Thereshold ",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()