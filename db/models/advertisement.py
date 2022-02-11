import hashlib
from app.application import data_base as db
from db import config
from db.models.mixins import BaseModelMixin
from db.models.user import User


class Advertisement(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __str__(self):
        return f'<Title: {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.user_id,
            "title": self.title,
            "text": self.text
        }