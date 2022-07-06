import base64
from flask_mail import Mail, Message
from flask import current_app, render_template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.services.mail_generate import return_graph


def flask_email():
    mail = Mail(current_app)
    msg = Message(
        "Hello",
        sender="<renato.suguiy@pucpr.edu.br>",
        recipients=["<renatosuguiy@gmail.com>"],
    )
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "<h1>Sent</h1>"


def mail_graph():
    return_graph()
    with open("fig1.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    template = (
        ""
        '<img src="cid:Myimage">'
        "{caption}"  # Optional caption to include below the graph
        "<br>"
        "<hr>"
        ""
    )

    mail = Mail(current_app)
    msg = Message(
        "Teste",
        sender="renato.suguiy@pucpr.edu.br",
        recipients=["renatosuguiy@gmail.com"],
    )
    _ = template.format(caption="Gráfico de exemplo")
    msg.html = _
    with current_app.open_resource("fig1.png") as fp:
        msg.attach(
            "fig1.png",
            "image/png",
            fp.read(),
            "inline",
            headers=[
                ["Content-ID", "<Myimage>"],
            ],
        )
    mail.send(msg)
    return "sent"
