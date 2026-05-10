from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = "rightmoves_secret_key"

# ==========================
# CONFIGURE EMAIL SETTINGS
# ==========================


# MAIL CONFIGURATION

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rightmoveschess@gmail.com'
app.config['MAIL_PASSWORD'] = 'xgzu cndz nygf xxzv'

mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        msg = Message(
            subject="New Contact Form Submission",
            sender='rightmoveschess@gmail.com',
            recipients=['unniloveschess@gmail.com']
        )

        msg.body = f"""
New Contact Request

Name: {name}

Email: {email}

Phone: {phone}

Message:
{message}
"""

        mail.send(msg)

        return """
<div style='
font-family:Poppins,sans-serif;
max-width:700px;
margin:100px auto;
padding:50px;
text-align:center;
background:white;
border-radius:20px;
box-shadow:0 5px 20px rgba(0,0,0,0.1);
'>

<h1 style='color:#0b2b5c;'>
♟ Thank You!
</h1>

<p style='
font-size:20px;
color:#555;
line-height:1.8;
margin-top:20px;
'>
Your enquiry has been submitted successfully.<br>

Our coaching team will contact you shortly.
</p>

<a href='/'
style='
display:inline-block;
margin-top:30px;
padding:14px 28px;
background:#0b2b5c;
color:white;
text-decoration:none;
border-radius:10px;
font-weight:600;
'>
Back to Home
</a>

</div>
"""

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

