from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        form_name = request.form.get("name")
        form_email = request.form.get("email")
        if User.query.filter_by(email=form_email).first() != None:
            flash("You've already signed up with that email, Please log in instead.")
            return redirect(url_for("login"))
        hashed_password = generate_password_hash(password=request.form.get("password"),
                                                 method='pbkdf2:sha256'[7:], salt_length=8)
        new_user = User(email=form_email,
                        name=form_name,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        account = User.query.filter_by(email=request.form.get("email")).first()
        if account != None:
            form_password = request.form.get("password")
            if check_password_hash(account.password, form_password):
                login_user(account)
                return redirect(url_for("secrets"))
            else:
                flash("Password Incorrect, Please try again.")
        else:
            flash("That email does not exist, please try again")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download/<path:filename>')
@login_required
def download(filename):
    return send_from_directory(app.config['static/files'], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
