class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions
        self.answer = ''
        self.score = 0

    def next_question(self):
        question = self.questions[self.question_number]
        self.question_number += 1
        self.answer = question.answer
        return f"Q.{self.question_number}: {question.text}"
        # user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        # self.check_answer(question.answer, user_answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def check_answer(self, user_answer):
        correct = self.answer.lower() == user_answer.lower()

        if correct:
            self.score += 1

        return correct
