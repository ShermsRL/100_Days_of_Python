import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

text = turtle.Turtle()
text.penup()
text.hideturtle()

correct_guess = []
all_states = pandas.read_csv("50_states.csv")

while len(correct_guess) < 50:
    answer = screen.textinput(title=f"{len(correct_guess)}/{len(all_states)} States Correct",
                              prompt="What's another State name?").title()

    if answer == "Exit":
        break

    for state in all_states.state:
        if answer == state:
            data_of_state = all_states[all_states.state == state]
            text.setpos(int(data_of_state.x), int(data_of_state.y))
            text.write(f"{answer}", align="center")
            correct_guess.append(answer)
            print(correct_guess)



# States_to_learn . csv
state_list = all_states.state.to_list()
for guess in correct_guess:
    state_list.remove(guess)
states_to_learn = pandas.DataFrame(state_list)
states_to_learn.to_csv("states_to_learn.csv")


