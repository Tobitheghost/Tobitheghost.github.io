from flask import Blueprint, render_template, request
import os

homePage = Blueprint('homePage', __name__)

@homePage.route("/")
def home():
    return render_template("index.html")