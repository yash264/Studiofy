# Studiofy – Smart Portrait Enhancement

Studiofy is a lightweight backend system that converts raw human portrait images into studio-style portraits using a combination of classical image processing and efficient pre-trained vision models.  
It focuses on realism, speed, and identity preservation while avoiding heavy generative AI models.

---

## ✨ Key Features

### 1. Face Detection & Analysis
- Uses a combination of:
  - **YOLO-based face detection**
  - **MediaPipe face analysis**
- Provides stable and accurate face localization
- Helps guide face-focused enhancement without altering identity

---

### 2. Human Body Detection
- Uses a lightweight **YOLO-based person detector**
- Detects the full human body region
- Ensures the **entire person (face + body)** remains sharp

---

### 3. Realistic Background Blur (Portrait Mode)
- Applies DSLR-style background blur
- Keeps:
  - Face
  - Neck
  - Shoulders
  - Upper body
  clear and natural
- Uses **soft elliptical masks** instead of hard rectangular masks
- Smooth blur falloff avoids cut-out artifacts

---

### 4. Adaptive Blur Strength
- Background blur strength adapts automatically based on:
  - Subject size
  - Distance from camera
- Prevents excessive blur when the subject is small in the frame

---

### 5. Noise Reduction & Image Cleanup
- Reduces:
  - Sensor noise
  - Compression artifacts
- Designed for mobile-camera and low-light images
- Preserves important edges and textures

---

### 6. Face-Focused Enhancement
- Enhances facial clarity using:
  - Bilateral filtering
  - Edge-aware sharpening
- Guided by MediaPipe face analysis
- Preserves:
  - Natural skin texture
  - Facial structure
  - Original identity

---

### 7. Studio-Grade Color & Contrast Enhancement
Uses professional photography techniques:
- LAB-based automatic white balance
- Soft contrast enhancement (CLAHE on luminance channel)
- Vibrance boost (not raw saturation)
- Luminance-only sharpening (avoids color halos)

Result:
- Natural skin tones
- Balanced highlights and shadows
- Clean studio-style appearance

---

## 📂 Processing Pipeline
```
Input Image
↓
Noise Reduction
↓
Face Detection & MediaPipe Analysis
↓
Face Enhancement
↓
Human Body Detection
↓
Realistic Background Blur
↓
Color & Contrast Enhancement
↓
Studio-Style Portrait Output
```

## 🧠 Design Philosophy

- Avoid heavy generative models
- Prefer:
  - Classical computer vision
  - Lightweight pre-trained detectors
- Emphasis on:
  - Speed
  - Predictable output
  - Engineering clarity

---

## 🛠️ Tech Stack

- **Python**
- **Flask** – backend API
- **OpenCV** – image processing
- **YOLO** – face and human body detection
- **MediaPipe** – face analysis & stability
- Classical image processing techniques

---

---

## 🎯 What This Project Achieves

✔ Studio-style portrait enhancement  
✔ Realistic background blur  
✔ Whole body preserved  
✔ Fast inference  
✔ No heavy generative AI models  

---

## 🚀 Future Improvements

- Multi-person handling
- User-controlled blur strength
- Smart portrait cropping
- Lighting condition detection

---
