from flask_mail import Message
from App import mail, App
from threading import Thread
from flask import render_template
from flask_babel import _

def send_async_email(App, msg):
    with App.App_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(App, msg)).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Artemis] Reset Your Password',
                sender=App.config['ADMINS'][0],
                recipients=[user.email],
                text_body=render_template('email/reset_password.txt', user=user, token=token),
                html_body=render_template('email/reset_password.html', user=user, token=token))
