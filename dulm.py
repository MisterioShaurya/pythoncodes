from tkinter import *
import time

def yesbtn():
    global love_confirm
    love_confirm = True
    lbl = Label(win, text="I Love You Too...")
    lbl.pack()

def nobtn():
    win.destroy()  # Destroy the first window
    global love_confirm
    love_confirm = False

love_confirm = False

while not love_confirm:
    win = Tk()
    win.title("Title pe mt dhyan de yrr!")
    win.iconbitmap('D:/icons/Slogografientnobgico.ico')
    win.maxsize(500, 500)
    win.minsize(500, 500)
    lbl = Label(win, text="Do you love me?")
    lbl.pack()
    btn_yes = Button(win, text="Yes", command=yesbtn)
    btn_yes.pack()
    btn_no = Button(win, text="No", command=nobtn)
    btn_no.pack()
    win.mainloop()
