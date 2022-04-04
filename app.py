from flask import Flask, render_template

App = Flask(__name__)


@App.route("/")
def welcome():
    return render_template("welcome.html")

@App.route("/contact")
def contact():
    return render_template("contact.html")


@App.route("/home")
def home():
    return "Home Page"


@App.route("/gallery")
def gallery():
    return "Gallery Page"


if __name__ == "__main__":
    App.run()