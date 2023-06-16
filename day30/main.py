import tkinter
import random
import pyperclip
import json
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_len = random.randint(8, 10)
    number_len = random.randint(2, 4)
    symbol_len = random.randint(2, 4)

    password = ""
    character_list = []
    character_list += [random.choice(letters) for _ in range(letter_len)]
    character_list += [random.choice(numbers) for _ in range(number_len)]
    character_list += [random.choice(symbols) for _ in range(symbol_len)]

    random.shuffle(character_list)

    for character_to_pick in character_list:
        list_len = len(character_to_pick)
        password += character_to_pick[random.randint(0, list_len - 1)]

    pyperclip.copy(password)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()

    if email == '':
        messagebox.showinfo(
            title="Oops",
            message="You left the email empty!"
        )

        return

    if password == '':
        messagebox.showinfo(
            title="Oops",
            message="You left the password empty!"
        )

        return

    if website == '':
        messagebox.showinfo(
            title="Oops",
            message="You left the website empty!"
        )

        return

    if not messagebox.askokcancel(
        title=website_entry.get(),
        message=f"These are the details you entered:\n"
                f"Email: {email}\n"
                f"Password: {password}\n"
                f"Are these okay to save?"
    ):
        return

    data = {}

    # This is for academic purposes since it should just check if
    # the file exists instead
    try:
        with open('data.json', mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open('data.json', mode="w") as file:
            json.dump(data, file, indent=4)

    data[website] = {
        'email': email,
        'password': password
    }

    with open('data.json', mode="w") as file:
        json.dump(data, file, indent=4)
        website_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)

def search():
    data = {}

    try:
        with open('data.json', mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    result = ""

    website = website_entry.get()

    try:
        email = data[website]['email']
        password = data[website]['password']
        result=f"Website: {website}\nEmail: {email}\nPassword: {password}\n"
    except KeyError:
        result=f"No entry found"

    messagebox.showinfo(
        title="Information",
        message=result
    )

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website = tkinter.Label(text='Website')
website.grid(row=1, column=0)
username = tkinter.Label(text='Username/Email')
username.grid(row=2, column=0)
password = tkinter.Label(text='Password')
password.grid(row=3, column=0)

website_entry = tkinter.Entry(width=24)
website_entry.grid(row=1, column=1)
email_entry = tkinter.Entry(width=44)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'steve.gagne@nasdaq.com')
password_entry = tkinter.Entry(width=24)
password_entry.grid(row=3, column=1)

search_button = tkinter.Button(text='Search', command=search)
search_button.grid(row=1, column=2)
generate_password = tkinter.Button(text='Generate Password', command=generate_password)
generate_password.grid(row=3, column=2)
add_button = tkinter.Button(text='Add', command=save_password, width=41)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
