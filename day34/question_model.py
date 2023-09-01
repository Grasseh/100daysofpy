import html

class QuestionModel:
    def __init__(self, text, answer):
        self.text = html.unescape(text)
        self.answer = html.unescape(answer)
