from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import UnmappedInstanceError
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


def to_dict(self):
    d = {}
    for column in self.__table__.columns:
        d[column.name] = str(getattr(self, column.name))

    return d


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    # Return random Cafe of selected field ------------------------------------------------------------------------
    cafe = db.session.query(Cafe)[random.randint(0, len(db.session.query(Cafe).all()))]
    return jsonify(
        id=cafe.id,
        name=cafe.name,
        map_url=cafe.map_url,
        img_url=cafe.img_url,
        location=cafe.location,)


@app.route("/all")
def get_all_cafe():
    list = []
    all_cafe = db.session.query(Cafe).all()
    for cafe in all_cafe:
        list.append(to_dict(cafe))
    return jsonify(all_cafe=list)


@app.route("/search")
def search_cafe():
    location = request.args.get("loc").title()
    cafe_in_loc = Cafe.query.filter_by(location=location).first()
    print(type(cafe_in_loc))
    try:
        return jsonify(to_dict(cafe_in_loc))
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    if request.method == "POST":
        new_cafe_data = request.form.to_dict()
        new_cafe = Cafe(
            name=new_cafe_data["name"],
            map_url=new_cafe_data["map_url"],
            img_url=new_cafe_data["img_url"],
            location=new_cafe_data["location"],
            seats=new_cafe_data["seats"],
            has_toilet=bool(new_cafe_data["has_toilet"]),
            has_wifi=bool(new_cafe_data["has_wifi"]),
            has_sockets=bool(new_cafe_data["has_sockets"]),
            can_take_calls=bool(new_cafe_data["can_take_calls"]),
            coffee_price=new_cafe_data["coffee_price"],
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"Success": "Successfully added the new cafe!"})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH", "GET"])
def update_price(cafe_id):
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    new_price = request.args.get("new_price")
    try:
        cafe.coffee_price = new_price
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
    db.session.commit()
    return jsonify({"Success": "Successfully updated the price."}), 200


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["GET", "DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    if api_key == "TopSecretAPIKey":
        try:
            db.session.delete(cafe)
        except UnmappedInstanceError:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
        else:
            return jsonify({"Success": "We are sorry that your favourite cafe closed down"}), 200
    elif api_key != "TopSecretAPIKey":
        return jsonify({"error": "Sorry. That's not allowed. Make sure you have the correct api key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
