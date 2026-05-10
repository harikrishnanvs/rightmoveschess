from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "rightmoves_secret_key"

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
    return render_template("thankyou.html") 
    
if __name__ == "__main__":
    app.run(debug=True)

