from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
all_turtles = []

y= -100
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x= -230, y=y)
    y += 50
    all_turtles.append(new_turtle)

print(all_turtles)
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost. The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)











# def move_forward():
#     turt.forward(10)
#
#
# def move_backwards():
#     turt.back(10)
#
#
# def turn_left():
#     turt.left(10)
#
#
# def turn_right():
#     turt.right(10)
#
#
# def clear_screen():
#     turt.clear()
#     turt.penup()
#     turt.home()
#     turt.pendown()
#
#
# screen.listen()
# screen.onkeypress(key="w", fun=move_forward)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=turn_left)
# screen.onkeypress(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()