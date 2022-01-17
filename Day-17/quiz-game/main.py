from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{len(question_bank)}")