import tkinter as tk
from tkinter import ttk

def printMsg():
    print("Ok")

root = tk.Tk()
frame = tk.Frame(root)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame.grid(row=0, column=0, sticky="nsew")
frame.grid_columnconfigure(3, weight=1)
frame.grid_rowconfigure(1, weight=1)

label1 = tk.Label(frame, text="Label here")
button1 = tk.Button(frame, text="Yes", width=2, command=printMsg)
button2 = tk.Button(frame, text="No", width=2, command=printMsg)

label1.grid(row=0, column=0, columnspan=1)
button1.grid(row=0, column=1)
button2.grid(row=0, column=2)

root.mainloop()
