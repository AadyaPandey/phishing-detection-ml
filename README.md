# 🔐 Phishing URL Detection Web App

A full-stack machine learning web application that detects whether a given URL is **legitimate** or **phishing**. Built with React, Express.js, and a Python-trained ML model (Random Forest Classifier), this project combines modern web development with practical machine learning.

---

## 🚀 Features

- ✅ Real-time URL prediction: Safe or Phishing
- 🧠 Trained on 500k+ real-world phishing URLs
- 💻 Full-stack implementation:
  - React frontend
  - Node.js + Express backend
  - Python + scikit-learn ML model
- 🔁 Seamless integration via REST API
- 💾 Model saved using `pickle` for reuse

---

## ⚙️ Tech Stack

| Layer        | Tech Used              |
|--------------|------------------------|
| Frontend     | React.js               |
| Backend      | Node.js, Express.js    |
| Machine Learning | Python, scikit-learn |
| Communication| Axios                  |
| Model Format | `phishing_model.pkl`   |

---

## 📦 Project Structure

```bash
phishing-detection/
│
├── train_model/           # Python ML training
│   ├── main.py
│   └── phishing_model.pkl
│
├── backend/               # Node.js + Python backend
│   ├── index.js
│   ├── phishing_model.pkl
│   └── python/
│       └── predictor.py
│
├── frontend/              # React frontend
│   ├── src/
│   └── App.js
│
└── README.md

```
🚀 Getting Started
Follow these steps to run the project locally:

1. Train the Model (Python)
- cd train_model
- python main.py

2. Start the Backend Server

- cd backend
- npm install
- node server.js
    

3. Start the Frontend (React)
- cd frontend
- npm install
- npm start
    
## 🌍 Live Demo
Check the Hugging Face Space here:  
👉 [Phishing URL Detector](https://AadyaPandey-phishing-url-detector.hf.space)
<img width="957" height="434" alt="image" src="https://github.com/user-attachments/assets/0660c61e-4f42-4b70-88b4-dbc8178db652" />
<img width="954" height="433" alt="image" src="https://github.com/user-attachments/assets/5984ac21-8863-4081-8412-2ea80d1f5151" />




