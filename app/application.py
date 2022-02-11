from flask import Flask
from db import config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL

flask_app = Flask(__name__)
if config.IS_DEBUG:
    flask_app.config.from_mapping(SQLALCHEMY_DATABASE_URI=config.SQLITE_URL)
else:
    flask_app.config.from_mapping(SQLALCHEMY_DATABASE_URI=URL(**config.DATABASE))
data_base = SQLAlchemy(flask_app)

