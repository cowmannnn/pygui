#import everything from tkinter so we can make a gui
from tkinter import *

#creates a reference variable to the Tkinter library
#so that we can access its methods
root = Tk()

label = Label(root, text="my name jeff")

label.grid(row=0, column=0)

button1 = Button(root, text="click me!", padx=50,pady=10)

button1.grid(row=1, column=0)



root.mainloop()