# Portfolio Backend (Flask)

This is the Flask backend for the portfolio contact form. It handles form submissions from your Netlify frontend and sends emails via Gmail SMTP.

---

## Features

- Receives contact form data (`name`, `email`, `subject`, `message`) via POST request
- Sends email to your Gmail account
- CORS enabled so Netlify frontend can communicate
- Environment variables for email credentials

---

## Project Structure

portfolio_backend/
├─ app.py # main Flask app
├─ requirements.txt # Python dependencies
├─ .env # environment variables (not committed)
├─ runtime.txt # optional: Python version for deployment
├─ .gitignore
└─ README.md



---

## Setup Instructions (Local)

1. **Clone the repo:**
   ```bash
   git clone https://github.com/<your-username>/portfolio_backend.git
   cd portfolio_backend

2.Create a virtual environment:

python -m venv venv

3.Activate virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


4.Install dependencies:

pip install -r requirements.txt


5.Set up environment variables:
Create a .env file in the root folder:

EMAIL_ADDRESS=yourgmail@gmail.com
EMAIL_PASSWORD=yourapppassword


6.Run the app locally:

python app.py


--API endpoint: POST http://127.0.0.1:5000/send_message

--Deployment (Render)

--Push repo to GitHub.

--Go to Render
 → New → Web Service.

--Connect GitHub repo.

--Set Environment: Python.

--Build command:

pip install -r requirements.txt


--Start command:

python app.py


A--dd Environment Variables on Render:

EMAIL_ADDRESS = yourgmail@gmail.com
EMAIL_PASSWORD = yourapppassword


--Deploy → get public URL → use in Netlify frontend fetch.

--Frontend Integration

--Update your Netlify frontend JS fetch:

const res = await fetch("https://your-backend.onrender.com/send_message", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(formData)
});