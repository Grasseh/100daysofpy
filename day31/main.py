import tkinter
import pandas
import random
import os
import json

en_word = ''
known_words = []

def pick_random_word(valid_words):
    global en_word, card_front_image, flip_timer
    window.after_cancel(flip_timer)
    word_dict = random.choice(valid_words)
    jp_word = word_dict['jp']
    en_word = word_dict['en']
    canvas.itemconfig(language, text='Japanese')
    canvas.itemconfig(word, text=jp_word)
    canvas.itemconfig(image, image=card_front_image)
    flip_timer = window.after(3000, flip_to_back)

def right():
    global known_words, en_word, words
    known_words.append(en_word)
    with open('data/known_words.json', mode="w") as file:
        json.dump({ "words" : known_words }, file, indent=4)

    words = [i for i in words if not in_known_words(i['en'])]
    # import ipdb; ipdb.set_trace()
    pick_random_word(words)

def wrong():
    pick_random_word(words)

def flip_to_back():
    canvas.itemconfig(image, image=card_back_image)
    canvas.itemconfig(language, text='English')
    canvas.itemconfig(word, text=en_word)

def initialize_words():
    global known_words
    if not os.path.isfile('data/known_words.json'):
        with open('data/known_words.json', mode="w") as file:
            json.dump({ "words" : known_words }, file, indent=4)
    else:
        with open('data/known_words.json', mode="r") as file:
            known_words = json.load(file)['words']

    words = pandas.read_csv('data/japanese_words.csv')
    words = words.to_dict(orient='records')

    # import ipdb; ipdb.set_trace()
    words = [i for i in words if not in_known_words(i['en'])]
    return words

def in_known_words(word):
    global known_words
    return word in known_words


words = initialize_words()

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
image = canvas.create_image(400, 300, image=card_front_image)
language = canvas.create_text(400, 150, text='', font=FONT_SMOL)
word = canvas.create_text(400, 285, text=' ', font=FONT_BEEG)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=1, column=0)
wrong_button.grid(column=1, row=1)
flip_timer = window.after(3000, flip_to_back)
pick_random_word(words)

window.mainloop()
