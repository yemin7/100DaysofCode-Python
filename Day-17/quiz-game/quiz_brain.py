class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        quiz_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ")
        self.check_answer (quiz_answer, current_question.answer)


    def still_has_question (self):
        return (self.question_number < len(self.question_list))


    def check_answer (self, quiz_answer, correct_answer):
        if quiz_answer.lower() == correct_answer.lower():
            self.score += 1
        else: print("That's wrong.")
        print (f"The correct answer is {correct_answer}")
        print(f"You got it right!\nYour current score is: {self.score}/{self.question_number}\n")
