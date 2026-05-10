from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = "rightmoves_secret_key"

# ==========================
# CONFIGURE EMAIL SETTINGS
# ==========================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"     # sender
EMAIL_PASSWORD = "your_app_password"       # app password
RECEIVER_EMAIL = "academy_email@gmail.com" # where messages go


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        msg = EmailMessage()
        msg["Subject"] = "New Contact – Right Moves Chess Academy"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = RECEIVER_EMAIL
        msg.set_content(
            f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

            flash("Message sent successfully!", "success")
        except Exception as e:
            flash("Error sending message. Please try again.", "error")

        return redirect(url_for("contact"))

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

