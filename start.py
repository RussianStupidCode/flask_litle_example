from app.application import flask_app, data_base
from flask import Flask
import app.views.app


def start():
    flask_app.run()


if __name__ == "__main__":
    start()
