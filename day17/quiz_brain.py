class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions
        self.score = 0

    def next_question(self):
        question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(question.answer, user_answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def check_answer(self, correct_answer, user_answer):
        correct = correct_answer.lower() == user_answer.lower()
        if correct:
            self.score += 1
            print("You are correct!")
        else:
            print("Nope!")
        print(f"The answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("")
