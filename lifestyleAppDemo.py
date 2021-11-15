# import everything from tkinter so we can make a gui
from tkinter import *
from tkinter import ttk
# imports python inbuilt image library
from PIL import ImageTk, Image
# importing strftime function to retrieve system time
from time import strftime, time

# creates a reference variable to the Tkinter library
# so that we can access its methods
root = Tk()
# creates a reference variable to the Style methods
style = ttk.Style()
# window size is set
root.geometry("350x500")
# title and icon of app changed
root.title("WorkLife App v0.2")
root.iconbitmap(r"icons\rating.ico")

# class created for the main window


class Window():
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    #
    canvas = Canvas(root, width=200, height=200)
    canvas.place(x=0, y=0)
    rating_img = ImageTk.PhotoImage(Image.open(r"icons\rating.png"))
    canvas.create_image(20, 20, anchor=NW, image=rating_img)
    #


# class which holds the buttons and places them on the gui
class Buttons():
    tasks_button = Button(root, width=11, height=4)
    tasks_button.place(x=0, y=430,)

    insights_button = Button(root, width=12, height=4)
    insights_button.place(x=85, y=430)

    mindfulness_button = Button(root, width=12, height=4)
    mindfulness_button.place(x=172, y=430)

    exercise_button = Button(root, width=12, height=4)
    exercise_button.place(x=262, y=430)

# class which holds the methods that allow the clock to
# display system time, refresh method WIP


class clock():
    def __init__(self):
        time_str = strftime("%H:%M:%S")
        self.time_label = Label(root, font=("calibri", 20, "bold"),
                                foreground="black")
        self.time_label.config(text=time_str)
        self.time_label.place(x=0, y=90)
        self.seconds = 0

    def refresh(self):
        self.seconds += 1
        self.time_label.after(1000, self.__init__)


# clock is defined and called
refresh = clock()
refresh.refresh

# event loop
root.mainloop()
