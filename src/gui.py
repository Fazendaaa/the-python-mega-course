"""This a simple program to convert minutes to seconds -- vice-versa"""
# pylint: disable=unused-import
from tkinter import *

#   ------------------------   GLOBAL VARIABLES   --------------------------   #

WINDOW = Tk()
FLAG = True
TEXT1 = StringVar()
TEXT2 = StringVar()
VALUE = StringVar()
TEXT1.set("Minutes:")
TEXT2.set("Seconds:")

#   ----------------------------   FUNCTIONS   -----------------------------   #

def change():
    """This function updates the Label of the entry convertion"""
    global FLAG, TEXT1, TEXT2

    FLAG = not FLAG
    tmp = TEXT1.get()
    TEXT1.set(TEXT2.get())
    TEXT2.set(tmp)

def convert():
    """This function does the convertion given user input"""
    global FLAG
    value = int(VALUE.get())

    if FLAG:
        value *= 60
    else:
        value /= 60

    #   cleans up the screen then print it
    TEXT.replace('1.0', END, value)

#   ------------------------------   MAIN   --------------------------------   #

LABEL_1 = Label(WINDOW, textvariable=TEXT1)
LABEL_1.grid(row=0, column=0)

LABEL_2 = Label(WINDOW, textvariable=TEXT2)
LABEL_2.grid(row=0, column=2)

BUTTON_1 = Button(WINDOW, text="<=>", command=change)
BUTTON_1.grid(row=0, column=1)

ENTRY = Entry(WINDOW, textvariable=VALUE)
ENTRY.grid(row=1, column=0)

BUTTON_2 = Button(WINDOW, text="Execute", command=convert)
BUTTON_2.grid(row=1, column=1)

TEXT = Text(WINDOW, height=1, width=20)
TEXT.grid(row=1, column=2)

WINDOW.mainloop()

#   ------------------------------   EOF   ---------------------------------   #
