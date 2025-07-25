# import cv2

# cap = cv2.VideoCapture(1)

# ret , frame = cap.read()
# if not ret:
#     print("failed to grab frame")
#     exit()


# bbox = cv2.selectROI("Tracking",frame,fromCenter=False,showCrosshair=True)

# tracker = cv2.TrackerCSRT_create()

# tracker.init(frame,bbox)

# while True:
#     ret,frame = cap.read()
#     if not ret:
#         break

# success , bbox = tracker.update(frame)

# if success:

#     x, y, w, h = [int(i) for i in bbox]
#     cv2.rectangle(frame ,(x,y),(x+w,y+h),(0,255,0),2)
#     cv2.putText(frame,"Tracking",(x ,y-10),
#     cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

# else:
#     cv2.putText(frame,"lost tracking",(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

#     cv2.imshow("Tracking",frame)

#     key = cv2.waitKey(1)
#     if key == 27:
    
#       break
# cap.release()
# cv2.destroyAllWindows()



import cv2

# Initialize video capture from the webcam
cap = cv2.VideoCapture(0)

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Failed to grab frame")
    exit()

# Select the object to track (draw a rectangle)
bbox = cv2.selectROI("Tracking", frame, fromCenter=False, showCrosshair=True)

# Create the tracker (you can use KCF, MIL, MOSSE, etc.)
tracker = cv2.TrackerMIL_create()

# Initialize tracker with first frame and bounding box
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Update tracker and get new position
    success, bbox = tracker.update(frame)

    if success:
        # Tracking success: draw bounding box
        x, y, w, h = [int(i) for i in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    else:
        # Tracking failure
        cv2.putText(frame, "Lost Tracking", (75, 75),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Show result
    cv2.imshow("Tracking", frame)

    # Exit on pressing ESC
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()