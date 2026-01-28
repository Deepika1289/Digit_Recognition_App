# 🧠 Handwritten Digit Recognition Web App

A **CNN-based Handwritten Digit Recognition System** built using **TensorFlow, Flask, and HTML Canvas**.
The application allows users to **draw digits** or **upload digit images** and get **real-time predictions**.

---

## 🚀 Features

* ✍️ Draw digits using an interactive canvas
* 📤 Upload handwritten digit images (PNG/JPG)
* 🧠 Deep Learning model trained on **MNIST dataset**
* ⚡ Real-time prediction using Flask backend
* 🎨 Clean and user-friendly UI
* 📊 Accurate image preprocessing

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask
* **Deep Learning:** TensorFlow, Keras
* **Image Processing:** PIL
* **Dataset:** MNIST
* **Language:** Python

---

## 📂 Project Structure

```
AI_INTERNSHIP/
├── app.py
├── model.h5
├── templates/
│   └── index.html
└── static/
    └── script.js
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Deepika1289/Digit-recognition-App.git
cd Digit-recognition-App
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install tensorflow flask numpy pillow
```

### 4️⃣ Run Application

```bash
python app.py
```

### 5️⃣ Open Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 How It Works

### ✍️ Draw Digit

1. Draw a digit (0–9) on the canvas
2. Click **Predict**
3. Model predicts the digit in real time

### 📤 Upload Image

1. Upload a handwritten digit image
2. Image is resized, inverted, normalized
3. CNN predicts the digit

---

## 🧠 Model Details

* **Model:** Convolutional Neural Network (CNN)
* **Input Size:** 28 × 28 × 1
* **Dataset:** MNIST
* **Accuracy:** ~98%
* **Output:** Digit (0–9)

---

## 👩‍💻 Author

**Deepika**
AI & Machine Learning Intern

---

## ⭐ Support

If you like this project, please **star ⭐ the repository**.
