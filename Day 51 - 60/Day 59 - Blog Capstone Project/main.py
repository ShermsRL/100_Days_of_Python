from datetime import datetime
from flask import Flask, render_template, request
import requests
import smtplib

# Email details
TO_ADDR = "shermantaymk@gmail.com"
TO_ADDR_PASS = "password"

# Blog API data
BLOG_DATA_URL = "https://api.npoint.io/e904b61af23dc79d86c3"
response = requests.get(BLOG_DATA_URL).json()

# datetime
today_date = datetime.today().strftime("%B %w, %Y")

# Author
author = "Sherman Tay"

# flask rerouting
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", today_date=today_date, response=response, author=author)


@app.route("/about.html")
def about():
    return render_template("about.html")


# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")


@app.route("/<int:num>")
def post(num):
    return render_template("post.html", response=response, num=num, author=author, today_date=today_date)


@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        print(request.form["name"])
        print(request.form["email"])
        print(request.form["phone"])
        print(request.form["message"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(TO_ADDR, TO_ADDR_PASS)
            connection.sendmail(from_addr=request.form["email"],
                                to_addrs=TO_ADDR,
                                msg=f"Subject: Hello!\n\n"
                                    f"Name: {request.form['name']}\n"
                                    f"Email: {request.form['email']}\n"
                                    f"Phone: {request.form['phone']}\n"
                                    f"Message: {request.form['message']}")
        return render_template("contact.html")
    else:
        return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)