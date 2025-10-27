# aiqgen
A full-stack AI-powered question generator that automatically creates educational questions from any text or PDF.

A simple web app built using **Flask** and **Streamlit**, deployed on [Render](https://render.com).  
This project demonstrates how to combine a backend API (Flask) with a data dashboard or UI (Streamlit).

---

## 🚀 Features
- Flask backend for data handling or APIs  
- Streamlit frontend for interactive visualization  
- Easy to deploy on Render  
- Responsive and lightweight  

---

## 🧰 Tech Stack
- Python 3.x  
- Flask  
- Streamlit  
- Gunicorn (for production)

---

## ⚙️ Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/flask-streamlit-app.git
cd flask-streamlit-app

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run locally
streamlit run app.py
# or if using Flask
python app.py
