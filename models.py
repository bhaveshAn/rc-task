from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Place(db.Model):
    __tablename__ = 'place'

    name = db.Column(db.String, primary_key=True)
    lat = db.Column(db.String, primary_key=True)
    lng = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return "%s - %s" % (self.name, self.lat, self.lng)

