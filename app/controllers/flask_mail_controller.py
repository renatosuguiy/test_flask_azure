from flask_mail import Mail, Message
from flask import current_app


def flask_email():
    mail = Mail(current_app)
    print(current_app.config["MAIL_USERNAME"])
    print(current_app.config["MAIL_PASSWORD"])
    msg = Message(
        "Hello",
        sender="renato.suguiy@pucpr.edu.br",
        recipients=["renatosuguiy@gmail.com"],
    )
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"
