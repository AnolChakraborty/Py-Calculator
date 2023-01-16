import math
import tkinter as tk
from tkinter.constants import COMMAND, CURRENT, END, INSERT
from typing import Text


class Button(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


ui = tk.Tk()
ui.title("Calculator")

# ui.geometry("287x350") # Enabling this may not show full ui of the calculator in different screen sizes, so better keep it disabled
ui.attributes('-topmost', True)

photo = tk.PhotoImage(file = "res/icon.png")
ui.iconphoto(False, photo)

def lab(val):
    tk.Label(ui, text=str(val), width=5, borderwidth=3).grid(row=0, column=4, pady=8, columnspan=2)

lab(": )")

e = tk.Entry(ui, font=("default, 11"), insertontime=0, bd=5, width=21, borderwidth=10, foreground="#ff0000", highlightthickness=5, highlightcolor="#f5d0d0", highlightbackground="#f5d0d0")
e.grid(row=0, rowspan=2, column=0, columnspan=4, padx=5, pady=5)
e.bind("<Key>", lambda e: "break")

def view(val):
    tk.Label(ui, borderwidth=3, relief="sunken", text=str(val), width=34, bg="#f5d0d0", fg="#000000").grid(row=2, column=0, columnspan=5, pady=5)

view("Calculations here")

global flag
flag = 0

def insrt(number):
    global flag
    if flag == 1:
        e.delete(0, END)
        view("Calculations here")
        lab(": )")
        flag = 0
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def addition(s):
    lab(s)
    global stat
    stat = str(s)
    global num
    num = e.get()
    e.delete(0, END)

def substraction(s):
    lab(s)
    global stat
    stat = str(s)
    global num
    num = e.get()
    e.delete(0, END)

def multiplication(s):
    lab(s)
    global stat
    stat = str(s)
    global num
    num = e.get()
    e.delete(0, END)

def division(s):
    lab(s)
    global stat
    stat = str(s)
    global num
    num = e.get()
    e.delete(0, END)

def root(s):
    lab(s)
    global num
    num = e.get()
    e.delete(0, END)
    e.insert(0, str("Root of: "))
    global flag
    flag = 0
    global stat
    stat = str(s)
    res(s)

def power(s):
    lab(s)
    global num
    num = e.get()
    e.delete(0, END)
    e.insert(0, str("Power of: "))
    global flag
    flag = 0
    global stat
    stat = str(s)
    res(s)

def res(s):
    lab(s)
    global stat
    num2 = e.get()
    if stat == "+":
        ans1 = float(num) + float(num2)
        ans = ans1
    elif stat == "-":
        ans1 = float(num) - float(num2)
        ans = ans1
    elif stat == "x":
        ans1 = float(num) * float(num2)
        ans = ans1
    elif stat == "/":
        ans1 = float(num) / float(num2)
        ans = "{:.3f}".format(ans1)
    elif stat == "root":
        num2 = str(num2[9:])
        ans1 = float(math.pow(float(num), float(1/int(num2))))
        ans = "{:.2f}".format(ans1)
    elif stat == "pow":
        num2 = str(num2[10:])
        ans1 = float(math.pow(float(num), int(num2)))
        ans = "{:.2f}".format(ans1)
    e.delete(0, END)
    e.insert(0, ans)
    global flag
    flag = 1
    if stat == "root":
        view(str(num2) + " root of " + str(num) + " = " + str(ans1))
    elif stat == "pow":
        view(str(num) + " power " + str(num2) + " = " + str(ans1))
    else:
        view(str(num) + " " + str(stat) + " " + str(num2) + " = " + str(ans1))


def clear():
    lab(": |")
    view("Calculations here")
    global flag
    flag = 1
    e.delete(0, END)


sub = Button(ui,activebackground='#ffe46b', bg="#d0c6f5", text="-", padx=18, pady=15, command=lambda: substraction("-")).grid(row=5, column=3)
mul = Button(ui,activebackground='#ffe46b', bg="#d0c6f5", text="x", padx=17, pady=15, command=lambda: multiplication("x")).grid(row=4, column=3)
div = Button(ui,activebackground='#ffe46b', bg="#d0c6f5", text="/", padx=19, pady=8, command=lambda: division("/")).grid(row=3, column=3)
cls = Button(ui,activebackground='#ff4d4d',bg="#6699ff", text="cls", padx=15, pady=8, command= clear).grid(row=3, column=0)

b7 = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text="7", padx=20, pady=15, command=lambda: insrt("7")).grid(row=4, column=0)
b8 = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text="8", padx=20, pady=15, command=lambda: insrt("8")).grid(row=4, column=1)
b9 = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text="9", padx=20, pady=15, command=lambda: insrt("9")).grid(row=4, column=2)
add = Button(ui,activebackground='#ffe46b', bg="#d0c6f5", text="+", padx=15, pady=42, command=lambda: addition("+")).grid(row=6, column=3, rowspan=2)

b4 = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text="4", padx=20, pady=15, command=lambda: insrt("4")).grid(row=5, column=0)
b5 = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text="5", padx=20, pady=15, command=lambda: insrt("5")).grid(row=5, column=1)
b6 = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text="6", padx=20, pady=15, command=lambda: insrt("6")).grid(row=5, column=2)

b1 = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text="1", padx=20, pady=15, command=lambda: insrt("1")).grid(row=6, column=0)
b2 = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text="2", padx=20, pady=15, command=lambda: insrt("2")).grid(row=6, column=1)
b3 = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text="3", padx=20, pady=15, command=lambda: insrt("3")).grid(row=6, column=2)
equall = Button(ui,activebackground='#6dff6b', bg="#c6f5ea", text="=", padx=18, pady=115, command=lambda: res("=")).grid(row=3, column=4, rowspan=5)

bdot = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text=".", padx=22, pady=15, command=lambda: insrt(".")).grid(row=7, column=2)
b0 = Button(ui,activebackground='#73f5d7', bg="#f5f0f0", text="0", padx=50, pady=15, command=lambda: insrt("0")).grid(row=7, column=0, columnspan=2)

rt = Button(ui,activebackground='#ffe46b', bg="#d0c6f5", text="\u221A", padx=19, pady=8, command=lambda: root("root")).grid(row=3, column=1)
pow = Button(ui,activebackground='#ffe46b', bg="#d0c6f5", text="pow", padx=10, pady=8, command=lambda: power("pow")).grid(row=3, column=2)


ui.resizable(False, False)
ui.mainloop()
