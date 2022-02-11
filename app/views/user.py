from flask import request, jsonify
from flask.views import MethodView
from db.models import User
from app.application import flask_app
from validate.schemas.user import USER_CREATE, USER_UPDATE
from validate.validator import validate


class UserView(MethodView):
    def get(self, user_id):
        user = User.get(user_id)
        return jsonify(user.to_dict())

    @validate('json', USER_CREATE)
    def post(self):
        user = User(**request.json)
        user.set_password(request.json['password'])
        user.add()
        return jsonify(user.to_dict())

    def delete(self, user_id):
        user = User.get(user_id)
        user.delete()
        return jsonify({'status': 'OK'})

    @validate('json', USER_UPDATE)
    def patch(self, user_id):
        user = User.get(user_id)
        user.update(request.json)
        return jsonify(user.to_dict())


flask_app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users_get'), methods=['GET', ])
flask_app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users_delete'), methods=['DELETE', ])
flask_app.add_url_rule('/users/', view_func=UserView.as_view('users_create'), methods=['POST', ])
flask_app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users_update'), methods=['PATCH', ])
