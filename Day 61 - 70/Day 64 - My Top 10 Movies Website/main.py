import sqlalchemy.orm
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

# Variables for TMDB
TMDB_API_KEY = "key"

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'key'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top_movies.db"
db = SQLAlchemy(app)
Bootstrap(app)


# Database Table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), unique=True, nullable=False)


# Forms
class RateMovieForm(FlaskForm):
    new_rating = FloatField('Your Rating out of 10 e.g. 7.5')
    new_review = StringField('Your Review')
    submit = SubmitField("Done")
    class Meta:
        csrf = False


class AddMovieForm(FlaskForm):
    add_movie = StringField("Movie Title")
    add_button = SubmitField("Add Movie")
    class Meta:
        csrf = False


# Website links
@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating.desc()).all()
    print(movies)
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = RateMovieForm()
    if request.method == "POST":
        movie_to_update = Movie.query.get(id)
        movie_to_update.rating = form.new_rating.data
        movie_to_update.review = form.new_review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/delete/<int:id>")
def delete(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if request.method == "POST":
        # TMDB Parameters
        params = {
            "api_key": TMDB_API_KEY,
            "query": form.add_movie.data,

        }
        print(form.add_movie.data)
        # Requests
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=params).json().get("results")
        return render_template("select.html", response=response)

    return render_template("add.html", form=form)


@app.route("/select")
def select():
    id = request.args["id"]
    print(id)
    params = {
        "api_key": TMDB_API_KEY,

    }
    response = requests.get(f"https://api.themoviedb.org/3/movie/{id}", params=params).json()
    print(response)
    new_movie = Movie(
        title=response["original_title"],
        year=response["release_date"],
        description=response["overview"],
        img_url=f"https://www.themoviedb.org/t/p/w300_and_h450_bestv2/{response['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()

    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()


