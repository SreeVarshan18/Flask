from flask import Flask
App = Flask(__name__)


@App.route("/")
def welcome():
    return "Welcome to my website"

@App.route("/contact")
def contact():
    return "Contact Page"


@App.route("/home")
def home():
    return "Home Page"


@App.route("/gallery")
def gallery():
    return "Gallery Page"


if __name__ == "__main__":
    App.run()