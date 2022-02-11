from sqlalchemy import exc
from app.application import data_base as db
from validate import errors


class BaseModelMixin:
    @staticmethod
    def commit():
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadLuck

    @classmethod
    def get(cls, obj_id):
        obj = cls.query.get(obj_id)
        if obj:
            return obj
        raise errors.NotFound

    def add(self):
        db.session.add(self)
        self.commit()

    def delete(self):
        db.session.delete(self)
        self.commit()

    def update(self, attrs: dict):
        for key, value in attrs.items():
            setattr(self, key, value)
        self.commit()