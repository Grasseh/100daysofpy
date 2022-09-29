import tkinter

def button_clicked():
    celcsius = int(entry_input.get())
    freedom = celcsius * 1.8 + 32
    answer_label.config(text=str(round(freedom, 1)))

window = tkinter.Tk()
window.title("My first GUIEWWWWWW C to F")
window.minsize(100, 100)
label = tkinter.Label(text='is equal to')
label.grid(row=1, column=0)
label = tkinter.Label(text='Celcius')
label.grid(row=0, column=2)
label = tkinter.Label(text='Freedom Unit')
label.grid(row=1, column=2)
answer_label = tkinter.Label(text='0')
answer_label.grid(row=1, column=1)
entry_input = tkinter.Entry(width = 10)
entry_input.grid(row=0, column=1)
button = tkinter.Button(text='Convert', command=button_clicked)
button.grid(row=2, column=1)
window.mainloop()
