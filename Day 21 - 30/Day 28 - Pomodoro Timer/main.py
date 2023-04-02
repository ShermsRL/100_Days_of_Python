import tkinter
from tkinter import messagebox
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=("Arial", 30, "normal"))
    cycle_completed_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If it's the 8th rep:
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=PINK)
        messagebox.showinfo(title='Short Break!', message='Hey! HEY! Time to take a long break! You Deserve it!')
    # #If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Rest", fg=RED)
        messagebox.showinfo(title='Long Break!', message='Time to freshen up!')
    # If it's the 1st/3/5/7th rep:
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        messagebox.showinfo(title='Work', message='Alright lads, back to work!')
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = round(count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check_mark = ""
        for _ in range(math.floor(reps/2)):
            check_mark += "✔"
        cycle_completed_label.config(text=check_mark)

# ---------------------------- UI SETUP ------------------------------- #
# colorhunt.com to look at color palette

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Arial", 30, "normal"))
timer_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = tkinter.Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = tkinter.Button(text="Reset", command=reset)
reset_btn.grid(column=2, row=2)

cycle_completed_label = tkinter.Label(bg=YELLOW, fg=GREEN)
cycle_completed_label.grid(column=1, row=3)












window.mainloop()