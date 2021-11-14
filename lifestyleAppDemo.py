# import everything from tkinter so we can make a gui
from tkinter import *
from tkinter import ttk
# imports python inbuilt image library
from PIL import ImageTk, Image

# creates a reference variable to the Tkinter library
# so that we can access its methods
root = Tk()
# creates a reference variable to the Style methods
style = ttk.Style()
# window size is set
root.geometry("350x500")
# title of app changed
root.title("WorkLife App v0.1")

# class created for the main window


class Window():
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    #
    canvas = Canvas(root, width=100, height=100)
    canvas.place(x=490, y=20)
    clock_img = ImageTk.PhotoImage(Image.open(r"icons\clock.png"))
    canvas.create_image(20, 20, anchor=NW, image=clock_img)
    #
    tasks_button = Button(root, width=12, height=4)
    tasks_button.place(x=0, y=430,)

    insights_button = Button(root, width=12, height=4)
    insights_button.place(x=95, y=430)


# event loop
root.mainloop()
