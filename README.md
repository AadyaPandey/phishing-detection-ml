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
    

<img width="958" height="428" alt="image" src="https://github.com/user-attachments/assets/29a7dcc8-5abe-48a6-b8f5-b787bc05a394" />
<img width="957" height="424" alt="image" src="https://github.com/user-attachments/assets/0237980b-f17d-4fc8-b14e-b21dcac5c4ed" />
<img width="959" height="422" alt="image" src="https://github.com/user-attachments/assets/87ec95b3-4964-4e06-b521-f29d3ea434b9" />


