

```markdown
# 🎯 Object Tracking using OpenCV

This project demonstrates real-time object tracking from a webcam using OpenCV in Python. You can interactively select a region of interest (ROI), and the tracker will follow the object frame-by-frame using the MIL (Multiple Instance Learning) tracking algorithm.

---

## 🧠 Features

* ✅ **Real-time webcam tracking:** High-speed processing for smooth visual feedback.
* ✅ **Interactive object selection:** Select any object manually using your mouse.
* ✅ **On-screen Statistics:**
    * **FPS (Frames Per Second):** Monitor performance in real-time.
    * **Tracking Status:** Clear "Tracking" or "Lost" indicators.
* ✅ **Simple Controls:** Press `ENTER` to start and `ESC` to exit instantly.

---

## 📦 Requirements

Ensure you have Python installed, then install the necessary OpenCV library:

```bash
pip install opencv-contrib-python
```

---

## 🚀 How to Run

1.  **Launch the script:**
    ```bash
    python tracker.py
    ```
2.  **Select Object:** When the webcam window opens, click and drag to draw a box around the object you want to track.
3.  **Confirm:** Press `ENTER` or `SPACE` to lock the target.
4.  **Exit:** Press `ESC` to stop tracking and close the window.

---

## 🔧 Tracker Configuration

The project currently utilizes the **MIL tracker**:

```python
tracker = cv2.TrackerMIL_create()
```

If you need different performance characteristics, you can swap it for:

| Tracker | Best For... |
| :--- | :--- |
| **CSRT** | High accuracy (but slower) |
| **KCF** | High speed (but struggles with overlaps) |
| **MOSSE** | Extreme speed (purely for simple shapes) |



---

## 📸 Console Output

```text
🟩 Select object to track and press ENTER or SPACE
✅ Tracking started... Press ESC to exit
🛑 Tracking stopped by user.
```

---

## 📁 File Structure

```text
Projects/
└── tracker.py        # Main object tracking script
└── README.md         # Project documentation
```
```

**Would you like me to generate a `requirements.txt` file for you as well so others can install everything with one command?**
