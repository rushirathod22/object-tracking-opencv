



````markdown
# 🎯 Object Tracking using OpenCV

This project demonstrates real-time object tracking from a webcam using OpenCV in Python. You can interactively select a region of interest (ROI), and the tracker will follow the object frame-by-frame using the MIL tracking algorithm.

---

## 🧠 Features

- ✅ Real-time webcam tracking
- ✅ Interactive object selection (ROI)
- ✅ Displays:
  - FPS (Frames Per Second)
  - Tracking box
  - "Tracking" or "Lost Tracking" messages
- ✅ ESC key to stop tracking and exit

---

## 📦 Requirements

- Python 3.x
- OpenCV

Install dependencies using:

```bash
pip install opencv-python
````

---

## 🚀 How to Run

```bash
python tracker.py
```

1. A webcam window will open.
2. Use your mouse to select the object to track.
3. Press `ENTER` or `SPACE` to begin tracking.
4. Press `ESC` to stop and close the window.

---

## 🔧 Tracker Used

The project uses OpenCV's **MIL tracker**:

```python
tracker = cv2.TrackerMIL_create()
```

You can easily switch to other trackers like:

* `cv2.TrackerKCF_create()`
* `cv2.TrackerCSRT_create()`
* `cv2.TrackerMOSSE_create()`

---

## 📸 Sample Output

```
🟩 Select object to track and press ENTER or SPACE
✅ Tracking started... Press ESC to exit
🛑 Tracking stopped by user.
```

---

## 📁 File Structure

```
Projects/
└── tracker.py        # Main object tracking script
```


