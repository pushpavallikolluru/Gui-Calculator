import tkinter as tk
from tkinter import messagebox

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        try:
            value = eval(scvalue.get())
            scvalue.set(value)
            screen.update()
        except Exception as e:
            scvalue.set("Error")
            screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

scvalue = tk.StringVar()
scvalue.set("")
screen = tk.Entry(root, textvar=scvalue, font="lucida 20 bold")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", ".", "C", "+", "-", "*", "/", "="
]

i = 0
for btn in buttons:
    button = tk.Button(frame, text=btn, font="lucida 15 bold", padx=20, pady=15)
    button.grid(row=i//4, column=i%4)
    button.bind("<Button-1>", click)
    i += 1

root.mainloop()
