import cv2
import numpy as np

# Define the color range for detection (e.g., blue object)
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

# Create a blank canvas to draw on
canvas = None

# Start webcam
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror the image
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask for blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None

    if contours:
        largest = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest) > 1000:
            ((x, y), radius) = cv2.minEnclosingCircle(largest)
            M = cv2.moments(largest)
            if M["m00"] > 0:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                cv2.circle(frame, center, 8, (0, 255, 0), -1)

                # Draw on canvas
                cv2.circle(canvas, center, 8, (255, 0, 0), -1)

    # Overlay the drawing canvas onto the frame
    output = cv2.add(frame, canvas)

    # Show everything
    cv2.imshow("Air Drawing - Press 'c' to clear", output)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros_like(frame)

cap.release()
cv2.destroyAllWindows()