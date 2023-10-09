from flask import Blueprint, render_template, request, redirect, url_for
import os

homePage = Blueprint('homePage', __name__)

@homePage.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@homePage.route("/disp/<content>", methods=['GET', 'POST'])
def display(content):
    print(content)
    image = 'maxresdefault.jpg'
    video = 'istockphoto-463918882-640_adpp_is.mp4'
    if content == 'Russ':
        return render_template("display.html", image = image)
    if content == 'Bathroom':
        return render_template("display.html", image = image)
    if content == 'Loading_1':
        return render_template("display.html", image = 'truck-loading-goods.1.1.jpg')
    if content == 'Loading_2':
        return render_template("display.html", image = '19710556_m.jpg')
    if content == 'Loading_3':
        return render_template("display_video.html", video = 'istockphoto-1366683418-640_adpp_is.mp4')
    if content == 'New_Pick':
        return render_template("display.html", image = 'maxresdefault.jpg')
    if content == 'Damage':
        return render_template("display.html", image = image)
    if content == 'Charging':
        return render_template("display_video.html", video = 'istockphoto-1400033393-640_adpp_is.mp4')
    if content == 'Office':
        return render_template("display_video.html", video = 'istockphoto-1201224615-640_adpp_is.mp4')
    if content == 'Break':
        return render_template("display_video.html", video = 'istockphoto-463918882-640_adpp_is.mp4')
    if content == 'Forklift':
        return render_template("display.html", image = image)
    if content == 'Wrapping':
        return render_template("display_video.html", video = 'istockphoto-1166568867-640_adpp_is.mp4')
    if content == 'Amazon':
        return render_template("display_video.html", video = 'istockphoto-1334942634-640_adpp_is.mp4')
    if content == 'Unloading':
        return render_template("display.html", image = 'Manc-Airport-PR-image-3.jpg')
    return render_template("display.html", image = image)

@homePage.route("/close", methods=['GET', 'POST'])
def close():
    return render_template("close.html")

@homePage.route("/outline_visible", methods=['GET', 'POST'])
def outline_visible():
    return render_template("outline_visible.html")

@homePage.route("/outline_invisible", methods=['GET', 'POST'])
def outline_invisible():
    return render_template("outline_invisible.html")