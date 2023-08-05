from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3


# Database using sqllite3 directly-------------------------------------------------------------------------------------
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books "
#                "(id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL,"
#                "rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K.Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


# class Books(db.Model):
#     # id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False)
#
#
# db.create_all()
# book = Books(title="Immunity", author="Forgot", rating=9.5)
# db.session.add(book)
# db.session.commit()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# all_books = []


# Read a particular record
# book = Books.query.filter_by(title="Harry Potter").first()


@app.route('/')
def home():
    # Read all records
    all_books = db.session.query(Books).all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        db.create_all()
        new_book = Books(
            title=request.form.get("title"),
            author=request.form.get("author"),
            rating=request.form.get("rating"))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    book = Books.query.filter_by(id=id).first()
    if request.method == "POST":
        book_to_update = book
        book_to_update.rating = request.form.get("new_rating")
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", book=book)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    book = Books.query.filter_by(id=id).first()
    if request.method == "GET":
        book_to_delete = book
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)
    # Create a new record
    # db.create_all()
    # new_book = Books(title="qwerty", author="98765", rating=9.9)
    # db.session.add(new_book)
    # db.session.commit()

    # Update a particular record by query
    # book_to_update = Books.query.filter_by(title="Harry Potter").first()
    # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit()

    # Update a record by primary key
    # book_id = 1
    # book_to_update = Books.query.get(book_id)
    # book_to_update.title = "Harry Potter and the Goblet of Fire"
    # db.session.commit()

    # Delete a particular record by primary key
    # book_id = 1
    # book_to_delete = Books.query.get(book_id)
    # db.session.delete(book_to_delete)
    # db.session.commit()


