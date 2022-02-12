from app.views.user import *
from app.views.advertisement import *
from flask import jsonify
from validate import errors
from db.models import User
from app.application import data_base as db
from app.application import auth


@flask_app.route('/health/', methods=['GET', ])
def health():
    if request.method == 'GET':
        return jsonify({'status': 'OK'})

    return {'status': 'OK'}


@auth.verify_password
def verify_password(username, password):
    user = db.session.query(User).filter(User.username == username).first()
    if user is None or not user.check_password(password):
        raise errors.BadLuck

    return user


@auth.error_handler
def auth_error(status):
    return "Access Denied", status