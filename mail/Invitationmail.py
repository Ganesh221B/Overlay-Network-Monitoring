from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os
# Flask-Mail parameters
DEBUG = True
SECRET_KEY = 'hidden'
USERNAME = 'secret'
PASSWORD = 'secret'
app.config('MAIL_SERVER')='smtp.gmail.com'
app.config('MAIL_PORT')=465
app.config('MAIL_USE_TLS') = False
app.config('MAIL_USE_SSL')= True
app.config('MAIL_USERNAME') = 'bandhavi.hani@gmail.com'
app.config('MAIL_PASSWORD') = 'ivahdnabv333'
# Setting up flask config
app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)
@app.route("/")
def send_mail(to,subject,body):
    msg = Message(
        subject,
        recipients=[to],
        body= "Welcome to SmartNet!!!",
        sender=app.config['MAIL_DEFAULT_SENDER']
    mail.send(msg)
    return "Sent"