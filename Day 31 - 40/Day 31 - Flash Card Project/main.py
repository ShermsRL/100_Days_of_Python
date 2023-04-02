import tkinter
import pandas
import random
import os.path
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
TOP_TEXT_STYLE = ("Ariel", 40, "italic")
BOTTOM_TEXT_STYLE = ("Ariel", 60, "bold")

# CSV files -------------------------------------------------------------------------------------------------------
header = ['English', 'Mandarin']
chinese_list = []
english_list = []
words_to_learn_dict = {}
try:
    if os.path.exists("./data/words_to_learn.csv"):
        pass
    else:
        raise FileNotFoundError
except FileNotFoundError:
    words_to_learn_csv = pandas.DataFrame.from_dict(words_to_learn_dict).to_csv("./data/words_to_learn.csv",
                                                                                index=False)
    english_csv = pandas.read_csv("./data/english_word.csv")
    english_dict = pandas.DataFrame.to_dict(english_csv, "records")
else:
    words_to_learn_csv = pandas.read_csv("./data/words_to_learn.csv")
    english_dict = pandas.DataFrame.to_dict(words_to_learn_csv, "records")


# Random word function --------------------------------------------------------------------------------------------
def translation():
    canvas.itemconfig(language_text, text="Chinese", fill="white")
    canvas.itemconfig(canvas_image, image=translated_flashcard_image)
    canvas.itemconfig(word_text, text=rand_word['Mandarin'], fill="white")


def random_word():
    global rand_word, flip_timer
    window.after_cancel(flip_timer)
    try:
        rand_word = english_dict[random.randint(0, len(english_dict) - 1)]
    except ValueError:
        messagebox.showinfo(title="Error", message="You have come to the end of the word list")
        window.destroy()
    canvas.itemconfig(language_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=rand_word['English'], fill="black")
    canvas.itemconfig(canvas_image, image=flashcard_image)
    flip_timer = window.after(3000, translation)


def correct_word():
    random_word()
    english_dict.remove(rand_word)


def wrong_word():
    for k, v in rand_word.items():
        if k == 'English':
            english_list.append(v)
            words_to_learn_dict['English'] = english_list
        else:
            chinese_list.append(v)
            words_to_learn_dict['Mandarin'] = chinese_list
    random_word()
    english_dict.remove(rand_word)
    print(words_to_learn_dict)


def on_closing():
    pandas.DataFrame.from_dict(words_to_learn_dict).to_csv("./data/words_to_learn.csv", index=False)
    window.destroy()


# User Interface --------------------------------------------------------------------------------------------------
window = tkinter.Tk()
window.title("Flashy")
window.config(width=900, height=726, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, translation)

# Flashcard
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_image = tkinter.PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=flashcard_image)
canvas.grid(column=0, row=0, padx=50, pady=50, columnspan=2)

translated_flashcard_image = tkinter.PhotoImage(file="./images/card_back.png")

language_text = canvas.create_text(400, 150, text="", font=TOP_TEXT_STYLE)
word_text = canvas.create_text(400, 263, text="", font=BOTTOM_TEXT_STYLE)

# Buttons
tick_image = tkinter.PhotoImage(file="./images/right.png")
tick_button = tkinter.Button(image=tick_image, highlightthickness=0, command=correct_word)
tick_button.grid(column=1, row=1)

cross_image = tkinter.PhotoImage(file="./images/wrong.png")
cross_button = tkinter.Button(image=cross_image, highlightthickness=0, command=wrong_word)
cross_button.grid(column=0, row=1)

random_word()
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
