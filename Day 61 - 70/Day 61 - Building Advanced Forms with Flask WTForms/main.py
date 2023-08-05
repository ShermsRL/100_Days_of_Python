from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)
Bootstrap(app)


class MyForm(FlaskForm):
    email = StringField(label="Email", validators=[Email(message="Invalid Email")])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")


class QuickForm(FlaskForm):
    quickform1 = StringField()
    quickform2 = StringField()
    quickform3 = StringField()


app.secret_key = "Hello"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
            return render_template("success.html", form=form)
        else:
            return render_template("denied.html", form=form)
    return render_template("login.html", form=form)


@app.route("/quick")
def quick_form_test():
    quickform = QuickForm()
    return render_template("quickform.html", form=quickform)


if __name__ == '__main__':
    app.run(debug=True)
