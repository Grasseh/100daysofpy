from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
LABEL_COLOR = "#FFFFFF"
FONT = ("Arial", 20, "italic")

class QuizUI:
    def __init__(self, brain: QuizBrain):
        self.brain = brain

        self.window = Tk()
        self.window.title("Quizzes")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        true_image = PhotoImage(file='images/true.png')
        true_button = Button(image=true_image, highlightthickness=0, command=self.check_true)

        false_image = PhotoImage(file='images/false.png')
        false_button = Button(image=false_image, highlightthickness=0, command=self.check_false)

        true_button.grid(row=2, column=0)
        false_button.grid(row=2, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas.config(highlightthickness=0, bg='white')

        self.question = self.canvas.create_text(
            150,
            125,
            width=230,
            text='abc',
            font=FONT,
            fill=THEME_COLOR
        )

        self.score = 0
        self.score_text = Label(text='Score: 0', bg=THEME_COLOR, fg=LABEL_COLOR)
        self.score_text.grid(row=0, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if not self.brain.still_has_questions():
            self.end_game()
            return

        question_text = self.brain.next_question()
        self.canvas.itemconfig(self.question, text=question_text)
        self.canvas.config(bg='white')
        self.check_answer_mutex = False

    def check_false(self):
        self.check_answer('false')

    def check_true(self):
        self.check_answer('true')

    def check_answer(self, answer):
        if self.check_answer_mutex:
            return

        self.check_answer_mutex = True
        correct = self.brain.check_answer(answer)
        color = "white"

        if correct:
            color = "green"
        else:
            color = "red"

        self.canvas.config(bg=color)
        self.score_text.config(text=f"Score: {self.brain.score}")

        self.flip_timer = self.window.after(1000, self.get_next_question)

    def end_game(self):
        self.check_answer_mutex = True
        score = self.brain.score
        self.canvas.itemconfig(self.question, text=f"Game Over! You scored {score}/10")
        self.canvas.config(bg='white')

