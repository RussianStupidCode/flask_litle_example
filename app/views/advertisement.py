from flask import request, jsonify
from flask.views import MethodView
from db.models import Advertisement, User
from app.application import flask_app
from validate.schemas.advertisement import ADVT_CREATE, ADVT_UPDATE
from validate.validator import validate
from app.application import auth
from validate import errors


class AdvertisementView(MethodView):
    def get(self, advt_id):
        advt = Advertisement.get(advt_id)
        return jsonify(advt.to_dict())

    @validate('json', ADVT_CREATE)
    @auth.login_required
    def post(self):
        advt = Advertisement(**request.json)
        user = auth.current_user()
        advt.owner_id = user.id
        advt.add()
        return jsonify(advt.to_dict())

    @auth.login_required
    def delete(self, advt_id):
        user = auth.current_user()
        advt = Advertisement.get(advt_id)
        if user.id != advt.owner_id:
            errors.AuthError

        advt.delete()
        return jsonify({'status': 'OK'})

    @validate('json', ADVT_UPDATE)
    @auth.login_required
    def patch(self, advt_id):
        user = auth.current_user()
        advt = Advertisement.get(advt_id)
        if user.id != advt.owner_id:
            errors.AuthError

        advt.update(request.json)
        return jsonify(advt.to_dict())


flask_app.add_url_rule('/advts/<int:advt_id>', view_func=AdvertisementView.as_view('advts_get'), methods=['GET', ])
flask_app.add_url_rule('/advts/<int:advt_id>', view_func=AdvertisementView.as_view('advts_delete'), methods=['DELETE', ])
flask_app.add_url_rule('/advts/', view_func=AdvertisementView.as_view('advts_create'), methods=['POST', ])
flask_app.add_url_rule('/advts/<int:advt_id>', view_func=AdvertisementView.as_view('advts_update'), methods=['PATCH', ])
