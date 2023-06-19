import tkinter
import pandas
import random

def pick_random_word(valid_words):
    # import ipdb; ipdb.set_trace()
    word_dict = random.choice(valid_words)
    jp_word = word_dict['jp']
    canvas.itemconfig(word, text=jp_word)

def right():
    pick_random_word(words)

def wrong():
    pick_random_word(words)

words = pandas.read_csv('data/japanese_words.csv')
words = words.to_dict(orient='records')

BACKGROUND_COLOR = "#B1DDC6"
FONT_SMOL = ("Arial", 32, "normal")
FONT_BEEG = ("Arial", 60, "normal")

window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

right_image = tkinter.PhotoImage(file='images/right.png')
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=right)

wrong_image = tkinter.PhotoImage(file='images/wrong.png')
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=wrong)

card_back_image = tkinter.PhotoImage(file='images/card_back.png')
card_front_image = tkinter.PhotoImage(file='images/card_front.png')

canvas = tkinter.Canvas(width=800, height=600)
canvas.create_image(400, 300, image=card_front_image)
language = canvas.create_text(400, 150, text='Japanese', font=FONT_SMOL)
word = canvas.create_text(400, 285, text='何', font=FONT_BEEG)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=1, column=0)
wrong_button.grid(column=1, row=1)

window.mainloop()
