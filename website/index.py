from flask import Blueprint, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from .utils import mailUsername
from website import mail


homePage = Blueprint('homePage', __name__)

@homePage.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        contact_msg = request.form.get('contact_msg')
        msg = Message(subject=f"ContactWebpage: {name} at {email}", body=contact_msg, recipients=[mailUsername], sender=email)
        mail.send(msg)
        msg2 = Message(subject=f"Thank You for Contacting Me!", body="Thank you for getting in contact with me. I will read your message asap!", recipients=[email], sender=mailUsername)
        mail.send(msg2)
        return render_template("index.html", success=True)
    return render_template("index.html")

@homePage.route("/movies")
def movies():
    return render_template("movies.html")

@homePage.route("/TexasToms")
def texas():
    return render_template('texas toms.html')