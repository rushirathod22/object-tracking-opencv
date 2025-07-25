import cv2

image = cv2.imread("image.jpg")

if image is not None:
    h, w, c =image.shape
    print(f"image loaded: \nheight:{h}\nwidth:{w}\nchanel:{c}" )
else:
    print("not load image")    