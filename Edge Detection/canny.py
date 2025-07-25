import cv2

img = cv2.imread(r"C:\Personal campus\Airtificial Intelligence\OpenCV\Edge Detection\Rushi.png",cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img,50,150)

cv2.imshow("original",img)
cv2.imshow("Edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()