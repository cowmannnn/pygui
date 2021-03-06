# import everything from tkinter so we can make a gui
from tkinter import *
#imports python inbuilt image library
from PIL import ImageTk, Image

# creates a reference variable to the Tkinter library
# so that we can access its methods
root = Tk()

# e used as reference variable for entry method that
# displays a text box for user input
e = Entry(root, width=50, bg="pink")
e.grid(row=0, column=0)


# function defined to run code when button is clicked
def aClick():
    label = Label(root, text=e.get())
    label.grid(row=1, column=0)


# call a function with the button using command parameter,
# padding functions similarly to html padding
button1 = Button(root, text="enter your name",
                 padx=50, pady=10, command=aClick)
button1.grid(row=1, column=0)

# event loop
root.mainloop()
