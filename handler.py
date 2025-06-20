import json
import smtplib
from email.mime.text import MIMEText

def send_email(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        receiver = body.get("receiver_email")
        subject = body.get("subject")
        message = body.get("body_text")

        if not receiver or not subject or not message:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing required fields"})
            }

        sender = "motgharebhavesh@gmail.com"
        app_password = "jbhu tujo uufu kppl"  # Gmail app password

        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, app_password)
            server.sendmail(sender, receiver, msg.as_string())

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully!"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to send email", "details": str(e)})
        }
