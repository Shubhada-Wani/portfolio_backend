from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
# Allow your Netlify frontend to call this API
CORS(app, origins=["https://shubhada-portfolio.netlify.app"], methods=["POST","OPTIONS"], supports_credentials=True)
  # replace with your Netlify URL

@app.route("/send_message", methods=["POST"])
def send_message():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        subject = data.get("subject")
        message = data.get("message")

        if not name or not email or not message:
            return jsonify({"message": "All fields are required"}), 400

        EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
        EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            return jsonify({"message": "Email credentials not set"}), 500

        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = f"Portfolio Contact Form: {subject} from {name}"
        msg.attach(MIMEText(f"Name: {name}\nEmail: {email}\nMessage:\n{message}", 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        return jsonify({"message": "Message sent successfully!"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "Something went wrong."}), 500
    
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "https://shubhada-portfolio.netlify.app")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
    return response



if __name__ == "__main__":
    # Use Render's PORT env variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
