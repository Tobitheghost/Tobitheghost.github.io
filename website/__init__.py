from flask import Flask
from flask_mail import Mail
from .utils import mailUsername, mailPassword

app = Flask(__name__)

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = mailUsername
app.config['MAIL_PASSWORD'] = mailPassword
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def create_app():
    from .index import homePage
    app.register_blueprint(homePage, url_prefix='/')
    return app