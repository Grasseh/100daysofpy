from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain

question_bank = []

for question in question_data['results']:
    question_bank.append(QuestionModel(question['question'], question['correct_answer']))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("That's it for the quiz!")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")
