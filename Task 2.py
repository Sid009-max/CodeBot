from tkinter import *

# calculator app
expression = ""   # stores the current input

def press(key):
    """append key to expression"""
    global expression
    expression += str(key)
    equation.set(expression)

def equalpress():
    """evaluate the expression"""
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = ""   # reset after showing result
    except:
        equation.set("error")
        expression = ""

def clear():
    """clear the entry field"""
    global expression
    expression = ""
    equation.set("")


# main gui code
root = Tk()
root.title("Calculator")
root.geometry("300x350")
root.configure(bg="lightgray")

equation = StringVar()

# entry field
entry = Entry(root, textvariable=equation, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# buttons layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, r, c) in buttons:
    if text == "=":
        b = Button(root, text=text, width=7, height=2,
                   bg="green", fg="white",
                   command=equalpress)
    else:
        b = Button(root, text=text, width=7, height=2,
                   command=lambda t=text: press(t))
    b.grid(row=r, column=c, padx=5, pady=5)

# clear button at the bottom
clear_btn = Button(root, text="C", width=31, height=2,
                   bg="red", fg="white",
                   command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
