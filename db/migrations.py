from app.application import flask_app, data_base
from flask_migrate import Migrate
import db.models

migrate = Migrate(flask_app, data_base)
