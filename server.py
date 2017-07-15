from flask import Flask, request, redirect
from models import db
from models import Place
from flask.json import jsonify

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/my_database'
db.init_app(app)
db.app = app

@app.route("/")
def main():
    return '<h1>Welcome to the RC task</h1>'


def get_json_for_place(place):
    return {
        'name': place.name,
        'lat': place.lat,
        'lng': place.lng,
    }


@app.route('/post_location', methods=['GET', 'POST'])
def post_location():
    json = request.get_json()
    if request.method=='POST':
        name = json['name']
        lat = json['latitude']
        lng = json['longitude']
        new_place = Place(name=name, lat=lat, lng=lng)
        db.session.add(new_place)
        db.session.commit()
        return jsonify({'place': get_json_for_place(new_place)})
    else:
        return '<h1>Add the values for name, latitude and longitude</h1>'

@app.route('/get_using_self',methods=['GET', 'POST'])
def get_using_self():
    json = request.get_json()
    if request.method=='POST':
        distance = json['distance']
        lat = json['latitude']
        lng = json['longitude']
        expression = (acos(sin(1.3963) * sin(Lat) + cos(1.3963) * cos(Lat) * cos(Lon - (-0.6981))) * 6371) <= distance
        places = Place.query.filter_by(expression)
        all_places = []
        for each in places:
            place_obj={}
            place_obj['name']= each.name
            place_obj['lat']= each.lat
            place_obj['lng'] = each.lng
            all_place.append(place_obj)
        return jsonify(all_places)
    else:
        return "<h1>Add the values for distance, latitude and longitude</h1>"


if __name__ == '__main__':
    app.run()

