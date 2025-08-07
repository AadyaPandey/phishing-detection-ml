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
- 🌐 Deployed on Vercel (frontend) and Render (backend)

---

## ⚙️ Tech Stack

| Layer        | Tech Used              |
|--------------|------------------------|
| Frontend     | React.js               |
| Backend      | Node.js, Express.js    |
| Machine Learning | Python, scikit-learn |
| Communication| Axios                  |
| Model Format | `phishing_model.pkl`   |
| Deployment   | Vercel + Render        |

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
