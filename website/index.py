from flask import Blueprint, render_template, request, redirect, url_for
import os

homePage = Blueprint('homePage', __name__)

@homePage.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        contact_msg = request.form.get('contact_msg')
        return f"{name} \n{email} \n{contact_msg}"
    return render_template("index.html")

@homePage.route("/movies")
def movies():
    return render_template("movies.html")