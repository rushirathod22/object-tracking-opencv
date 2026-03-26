
# 🎯 Object Tracking using OpenCV

🚀 **Real-time Computer Vision** | High-performance object tracking from a webcam using Python and the MIL (Multiple Instance Learning) algorithm.

![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 🧠 Features

* ✅ **Real-time Webcam Tracking:** High-speed processing for smooth visual feedback.
* ✅ **Interactive ROI Selection:** Select any object manually using your mouse.
* ✅ **On-screen HUD (Heads-Up Display):**
    * **FPS Counter:** Monitor performance in real-time.
    * **Tracking Status:** Clear "Tracking" or "Lost" indicators.
* ✅ **Simple Controls:** Press `ENTER` to lock and `ESC` to exit instantly.



---

## 🛠 Tech Stack

* **Language:** Python 3.x
* **Library:** OpenCV (cv2)
* **Algorithm:** MIL (Multiple Instance Learning)

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed, then install the required OpenCV library:

```bash
pip install opencv-contrib-python
```

### 2. How to Run
Launch the script from your terminal or command prompt:

```bash
python tracker.py
```

### 3. Usage Instructions
1. **Select Object:** When the webcam window opens, click and drag your mouse to draw a box around the object you want to track.
2. **Confirm:** Press **ENTER** or **SPACE** to lock the target.
3. **Exit:** Press **ESC** at any time to stop tracking and close the window.

---

## 🔧 Tracker Configuration

The project currently utilizes the **MIL tracker** for its balance of speed and reliability:

```python
tracker = cv2.TrackerMIL_create()
```

### Alternative Trackers
If you need different performance characteristics, you can swap the tracker in the code:

| Tracker | Best For... |
| :--- | :--- |
| **CSRT** | High accuracy (but slightly slower) |
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

## 📂 File Structure

```text
Object-Tracking-Project/
├── tracker.py        # Main object tracking script
├── README.md         # Project documentation
└── requirements.txt  # List of dependencies
```

---

## 👨‍💻 Contributing

1. Fork the repo.
2. Create a branch (`git checkout -b feature/new-tracker`).
3. Commit changes (`git commit -m "Added CSRT support"`).
4. Push to the branch (`git push origin feature/new-tracker`).
5. Open a Pull Request.

---

4. **Step-by-Step:** Clear instructions on which keys to press (`ENTER`, `SPACE`, `ESC`).

**Would you like me to create a `requirements.txt` file for this so users can install everything with one command?**
