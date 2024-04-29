from tkinter import *

def btnfun():
    x = textinput.get()
    lbl = Label(win,text=f"Nice to meet you {x}!")
    lbl.grid()

win = Tk()
textinput = StringVar()
win.title("Shaurya deep's tkinter window")
win.iconbitmap('D:/icons/Slogografientnobgico.ico')
win.geometry('600x500')
lbl = Label(win,text="Enter your name here:")
lbl.grid(pady=5,padx=10)
ent = Entry(win,textvariable=textinput)
ent.grid(row=2,pady=10)
btn = Button(win,text="Click here!",command=btnfun)
btn.grid(padx=10)
win.mainloop()