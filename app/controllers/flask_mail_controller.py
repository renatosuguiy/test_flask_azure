from flask_mail import Mail, Message
from flask import current_app

import os
from app.services.mail_generate import return_graph
from app.services.storage_services import download_graph


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
    file = download_graph()

    if file:
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

        msg.attach(
            "fig1.png",
            "image/png",
            file,
            "inline",
            headers=[
                ["Content-ID", "<Myimage>"],
            ],
        )
        mail.send(msg)
        return "sent"

    return "Problem"
