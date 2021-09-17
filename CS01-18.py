from tkinter import *

root = Tk()
root.title("First GUI")
myText = Label(text="Khunasin",fg="green",font=150).grid(row=0,column=0)
myText = Label(text="Sooksri",fg="blue",font=150).grid(row=0,column=1)
root.geometry("600x300")
root.mainloop()