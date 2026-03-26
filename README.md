# ⚖️ LegalEase AI-G & 🎯 Object Tracking Hub

🚀 **Hackathon Edition** | A multi-utility repository featuring AI-powered Legal Guidance and Real-time Computer Vision Tracking.

![GitHub repo size](https://img.shields.io/github/repo-size/rushirathod22/object-tracking-opencv)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

---

## 📌 Project 1: LegalEase AI-G (AI Assistant)

An **AI-powered legal platform** designed to simplify access to legal knowledge using Natural Language Processing.

### ✨ AI Features
* 🧠 **Legal Q&A:** Get simplified answers to complex legal questions.
* 📄 **Smart Drafting:** Generate agreements and contracts instantly.
* 🌍 **Plain English:** Translates "Legalese" into understandable summaries.
* ⚠️ *Disclaimer: For educational purposes only; not professional legal advice.*

### 🛠 Tech Stack
* **Frontend:** React / Next.js, Tailwind CSS
* **Backend:** Node.js / Express
* **AI:** OpenAI API / LLM Integration

---

## 📌 Project 2: OpenCV Object Tracking

A high-performance Python tool for real-time object tracking from a webcam using the **MIL (Multiple Instance Learning)** algorithm.



### 🧠 Tracking Features
* ✅ **Real-time Processing:** Smooth visual feedback from your webcam.
* ✅ **Interactive Selection:** Manually select any Object of Interest (ROI) with your mouse.
* ✅ **Live HUD:** On-screen FPS counter and "Tracking/Lost" status indicators.
* ✅ **Simple Controls:** `ENTER` to lock target, `ESC` to exit instantly.

### 🚀 How to Run (Tracking)
1. **Install Requirements:**
   ```bash
   pip install opencv-contrib-python
   Launch Script:
```
Bash
python tracker.py
```
```
Controls:

Click & Drag: Draw a box around the object.

ENTER / SPACE: Confirm selection.

ESC: Close the application.
```
```

📂 File Structure
Plaintext
LegalEase-AI-G-ai-Hackthon/
├── frontend/         # Next.js UI (LegalEase)
├── backend/          # Node.js API & AI Logic
├── tracking_tool/    # Python Object Tracker
│   └── tracker.py    # Main CV Script
├── README.md         # Project Documentation
└── LICENSE           # MIT License
```
```
⚙️ Configuration & Environment
Legal Assistant (.env)
Create a file in the /backend folder:
```
```
Tracker Options
You can swap the tracker in tracker.py for different performance:

cv2.TrackerKCF_create(): Faster, but struggles with overlaps.

cv2.TrackerCSRT_create(): More accurate, but slightly slower.
```

#👨‍💻 Team & Contributing
*Rushikesh Rathod – GitHub Profile*

**Feel free to Fork this repo, create a feature branch, and submit a Pull Request!**
