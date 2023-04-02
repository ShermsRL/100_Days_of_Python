import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)

        self.score_label = tkinter.Label(text="Score:", background=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, pady=20)

        self.question_window = tkinter.Canvas(height=250, width=300)
        self.question_text = self.question_window.create_text(150, 100, text="Questions", font=FONT, width=280)
        self.question_window.grid(column=0, row=1, columnspan=2, pady=20, padx=20)

        tick_image = tkinter.PhotoImage(file="./images/true.png")
        self.tick_btn = Button(image=tick_image, highlightthickness=0, command=self.correct)
        self.tick_btn.grid(column=0, row=2)

        cross_image = tkinter.PhotoImage(file="./images/false.png")
        self.cross_btn = Button(image=cross_image, highlightthickness=0, command=self.wrong)
        self.cross_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_window.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_window.itemconfig(self.question_text, text=q_text)
        else:
            self.question_window.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.tick_btn.config(state="disabled")
            self.cross_btn.config(state="disabled")

    def correct(self):
        print("Hello")
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong(self):
        print("Bye")
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.window.after(1000, func=self.get_next_question)
        if is_right:
            self.question_window.config(background="green")
        else:
            self.question_window.config(background="red")
