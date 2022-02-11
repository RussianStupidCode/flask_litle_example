from flask import request, jsonify
from flask.views import MethodView
from db.models import Advertisement, User
from app.application import flask_app
from validate.schemas.advertisement import ADVT_CREATE, ADVT_UPDATE
from validate.validator import validate


class AdvertisementView(MethodView):
    def get(self, advt_id):
        advt = Advertisement.get(advt_id)
        return jsonify(advt.to_dict())

    @validate('json', ADVT_CREATE)
    def post(self):
        advt = Advertisement(**request.json)
        advt.add()
        return jsonify(advt.to_dict())

    def delete(self, advt_id):
        advt = Advertisement.get(advt_id)
        advt.delete()
        return jsonify({'status': 'OK'})

    @validate('json', ADVT_UPDATE)
    def patch(self, advt_id):
        advt = Advertisement.get(advt_id)
        advt.update(request.json)
        return jsonify(advt.to_dict())


flask_app.add_url_rule('/advts/<int:advt_id>', view_func=AdvertisementView.as_view('advts_get'), methods=['GET', ])
flask_app.add_url_rule('/advts/<int:advt_id>', view_func=AdvertisementView.as_view('advts_delete'), methods=['DELETE', ])
flask_app.add_url_rule('/advts/', view_func=AdvertisementView.as_view('advts_create'), methods=['POST', ])
flask_app.add_url_rule('/advts/<int:advt_id>', view_func=AdvertisementView.as_view('advts_update'), methods=['PATCH', ])
