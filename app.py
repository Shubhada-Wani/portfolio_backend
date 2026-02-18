from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # allows Netlify frontend to call API

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    subject = data.get("subject")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"message": "All fields are required"}), 400

    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    try:
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

        return jsonify({"message": "Message sent successfully!"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"message": f"Something went wrong: {str(e)}"}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render provides the PORT env
    app.run(host="0.0.0.0", port=port)
