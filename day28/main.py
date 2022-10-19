import tkinter
import math

reps = 0
global_timer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT=(FONT_NAME, 35, "bold")

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    reps = 0
    title.config(text="Timer", fg=GREEN)
    checkmarks.config(text="", fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    window.after_cancel(global_timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    timer = short_break_min

    if reps % 2 == 1:
        if reps == 1:
            checkmarks.config(text="", fg=PINK)
        timer = work_sec
        title.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        timer = long_break_min
        checkmarks.config(text="✓✓✓✓", fg=PINK)
        title.config(text="Break", fg=RED)
    else:
        checks = ''.join(["✓" for i in range(0, int(reps % 8 / 2))])
        checkmarks.config(text=checks)
        title.config(text="Break", fg=PINK)

    countdown(timer)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps

    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    time_text=f"{math.floor(count / 60)}:{seconds}"
    canvas.itemconfig(timer, text=time_text)

    if count > 0:
        global_timer = window.after(1000, countdown, count - 1)
    else:
        global_timer = window.after(1000, start_timer)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodor")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer = canvas.create_text(100, 130, text='00:00', fill='white', font=FONT)
canvas.grid(column=1, row=1)

title = tkinter.Label(text='Timer', fg=GREEN, bg=YELLOW, font=FONT)
title.grid(row=0, column=1)
checkmarks = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=FONT)
checkmarks.grid(row=3, column=1)
start_button = tkinter.Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)
reset_button = tkinter.Button(text='Reset', command=reset)
reset_button.grid(row=2, column=2)
window.mainloop()
