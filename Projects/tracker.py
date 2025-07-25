import cv2
import time

# Initialize webcam
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print(" Error: Could not open webcam.")
    exit()

# Read first frame
ret, frame = cap.read()
if not ret:
    print(" Failed to grab initial frame.")
    cap.release()
    exit()

# Select ROI
print("🟩 Select object to track and press ENTER or SPACE")
bbox = cv2.selectROI("Tracking", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Tracking")

# Create tracker
tracker = cv2.TrackerMIL_create()
tracker.init(frame, bbox)

# Colors and font
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
FONT = cv2.FONT_HERSHEY_SIMPLEX

# Start time for FPS calculation
start_time = time.time()
frame_count = 0

print(" Tracking started... Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        print(" Failed to grab frame.")
        break

    success, bbox = tracker.update(frame)
    frame_count += 1
    fps = frame_count / (time.time() - start_time)

    if success:
        x, y, w, h = [int(i) for i in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, 2)
        cv2.putText(frame, "Tracking", (x, y - 10), FONT, 0.7, GREEN, 2)
    else:
        cv2.putText(frame, "Lost Tracking!", (75, 75), FONT, 0.9, RED, 2)

    # Draw FPS on top-left
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), FONT, 0.7, BLUE, 2)

    # Display tracker info
    cv2.rectangle(frame, (5, 5), (170, 70), (0, 0, 0), -1)
    cv2.putText(frame, "ESC to Exit", (10, 60), FONT, 0.5, (200, 200, 200), 1)

    # Show the frame
    cv2.imshow("Object Tracking", frame)

    # Exit on ESC
    key = cv2.waitKey(1)
    if key == 27:
        print(" Tracking stopped by user.")
        break

cap.release()
cv2.destroyAllWindows()
