import cv2
import numpy as np


image = cv2.imread(r"C:\Personal campus\Airtificial Intelligence\OpenCV\Image Filtering\image.jpg")
sharpen_kernal = np.array([
    [0 , -2 , 0],
    [-1 , 5 ,-1],
    [0 , -1 , 0]
])

sharpened = cv2.filter2D(image,-1,sharpen_kernal)
cv2.imshow("original",image)
cv2.imshow("sharpened",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()