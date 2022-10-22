from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz_question = QuizBrain(question_bank)
while quiz_question.still_has_questions():
    quiz_question.next_question()
else:
  print("You have completed the quiz")
  print(f"Your final score is {quiz_question.score}/{quiz_question.question_number}")


