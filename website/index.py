from flask import Blueprint, render_template, request, redirect, url_for
import os

homePage = Blueprint('homePage', __name__)

@homePage.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@homePage.route("/movies")
def movies():
    return render_template("movies.html")