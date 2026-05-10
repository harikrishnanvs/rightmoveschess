from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = "rightmoves_secret_key"

# ==========================
# CONFIGURE EMAIL SETTINGS
# ==========================


# MAIL CONFIGURATION

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  

mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/thankyou")
def thankyou():
    return """
    <h1 style='text-align:center;margin-top:100px;'>
    ✅ Thank You!<br><br>
    Our coaching team will contact you shortly.
    </h1>
    """
    
if __name__ == "__main__":
    app.run(debug=True)

