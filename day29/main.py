import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    return 'a'

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open('data.txt', mode="a") as file:
        file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)

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

website_entry = tkinter.Entry(width=44)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = tkinter.Entry(width=44)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'steve.gagne@nasdaq.com')
password_entry = tkinter.Entry(width=24)
password_entry.grid(row=3, column=1)

generate_password = tkinter.Button(text='Generate Password', command=generate_password)
generate_password.grid(row=3, column=2)
add_button = tkinter.Button(text='Add', command=save_password, width=41)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
