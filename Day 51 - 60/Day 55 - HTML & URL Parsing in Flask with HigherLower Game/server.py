from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 to 9</h1>"\
           "<img src= 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:num>")
def number_check(num):
    if num < random_num:
        return "<h3 style='color:red; font-size:50px;'>Too low, try again!</h3>"
    elif num > random_num:
        return "<h3 style='color:blue; font-size:50px;'>Too high, try again!</h3>"
    else:
        return "<h3 style='color:green; font-size:50px;'>Correct!</h3>"

if __name__ == "__main__":
    app.run(debug=True)