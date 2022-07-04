import json
import os
from flask import jsonify
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# sending a email using sendgrip api
def send_email():
    message = Mail(
        from_email="renato.suguiy@pucpr.edu.br",
        to_emails="renatosuguiy@gmail.com",
        subject="Sending with Twilio SendGrid is Fun",
        html_content="<strong>and easy to do anywhere, even with Python</strong>",
    )

    sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return jsonify({"msg": "Sent"})
