from flask import Flask
App = Flask(__name__)


@App.route("/")
def welcome():
    return "Welcome to my website"


if __name__ == "__main__":
    App.run()