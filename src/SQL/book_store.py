"""
    This program stores book informations as: title, author, year and ISBN
"""
import tkinter
import __book_store

#   ----------------------------   FUNCTIONS   -----------------------------   #

def view_command():
    """Function that returns all the data from SQL server"""
    LIST.delete(0, END)
    for row in __book_store.view(CONN):
        LIST.insert(END, row)

def search_commmand():
    """Function that returns given the data from SQL server"""
    LIST.delete(0, END)
    for row in __book_store.search(CONN, TITLE.get(), AUTHOR.get(), YEAR.get(), ISBN.get()):
        LIST.insert(END, row)

def add_commmand():
    """Function that inserts given the data into SQL server"""
    LIST.delete(0, END)
    __book_store.insert(CONN, TITLE.get(), AUTHOR.get(), YEAR.get(), ISBN.get())
    LIST.insert(END, (TITLE.get(), AUTHOR.get(), YEAR.get(), ISBN.get()))

def get_select_row(event):
    # pylint: disable=W0612,W0613,global-statement,global-variable-undefined
    """Function that select the desired book"""
    global SELECTED_TUPLE
    SELECTED_TUPLE = LIST.get(LIST.curselection()[0])
    ENTRY1.delete(0, END)
    ENTRY2.delete(0, END)
    ENTRY3.delete(0, END)
    ENTRY4.delete(0, END)
    ENTRY1.insert(END, SELECTED_TUPLE[1])
    ENTRY2.insert(END, SELECTED_TUPLE[2])
    ENTRY3.insert(END, SELECTED_TUPLE[3])
    ENTRY4.insert(END, SELECTED_TUPLE[4])

def delete_command():
    """Function that deletes given the data from SQL server"""
    __book_store.delete(CONN, SELECTED_TUPLE[0])
    LIST.delete(0, END)

def update_command():
    """Function that updates given the data from SQL server"""
    __book_store.update(CONN, SELECTED_TUPLE[0], TITLE.get(), AUTHOR.get(), YEAR.get(), ISBN.get())
    search_commmand()

def close_command():
    """Terminate connection"""
    CONN.close()
    WINDOW.destroy()

#   ------------------------   GLOBAL VARIABLES   --------------------------   #

CONN = __book_store.connect('../output/book_store.db')

END = tkinter.END
WINDOW = tkinter.Tk()
FRAME = tkinter.LabelFrame(WINDOW, text="Info", padx=0, pady=0)

LABEL1 = tkinter.Label(FRAME, text="Title")
LABEL2 = tkinter.Label(FRAME, text="Author")
LABEL3 = tkinter.Label(FRAME, text="Year")
LABEL4 = tkinter.Label(FRAME, text="ISBN")

YEAR = tkinter.StringVar()
ISBN = tkinter.StringVar()
TITLE = tkinter.StringVar()
AUTHOR = tkinter.StringVar()

SB = tkinter.Scrollbar(FRAME)
LIST = tkinter.Listbox(FRAME, height=6, width=50)

ENTRY1 = tkinter.Entry(FRAME, textvariable=TITLE, width=50)
ENTRY2 = tkinter.Entry(FRAME, textvariable=AUTHOR, width=50)
ENTRY3 = tkinter.Entry(FRAME, textvariable=YEAR, width=50)
ENTRY4 = tkinter.Entry(FRAME, textvariable=ISBN, width=50)

B1 = tkinter.Button(FRAME, text="View all", width=12, command=view_command)
B2 = tkinter.Button(FRAME, text="Search entry", width=12, command=search_commmand)
B3 = tkinter.Button(FRAME, text="Add entry", width=12, command=add_commmand)
B4 = tkinter.Button(FRAME, text="Update selected", width=12, command=update_command)
B5 = tkinter.Button(FRAME, text="Delete selected", width=12, command=delete_command)
B6 = tkinter.Button(FRAME, text="Close", width=12, command=close_command)

#   ------------------------------   MAIN   --------------------------------   #

WINDOW.wm_title("Book Store")
WINDOW.grid_rowconfigure(0, weight=1)
WINDOW.grid_columnconfigure(0, weight=1)

FRAME.grid(row=0, column=0, sticky="nsew")
FRAME.grid_columnconfigure(1, weight=0)
FRAME.grid_rowconfigure(1, weight=0)

LABEL1.grid(row=0, column=0)
LABEL2.grid(row=1, column=0)
LABEL3.grid(row=2, column=0)
LABEL4.grid(row=3, column=0)

ENTRY1.grid(row=0, column=1)
ENTRY2.grid(row=1, column=1)
ENTRY3.grid(row=2, column=1)
ENTRY4.grid(row=3, column=1)

LIST.grid(row=4, column=1, rowspan=1, columnspan=1)
LIST.configure(yscrollcommand=SB.set)
LIST.bind('<<ListboxSelect>>', get_select_row)

SB.grid(row=4, column=2)
SB.configure(command=LIST.yview)

B1.grid(row=14, column=0)
B2.grid(row=14, column=1)
B3.grid(row=14, column=2)
B4.grid(row=15, column=0)
B5.grid(row=15, column=1)
B6.grid(row=15, column=2)

WINDOW.mainloop()

#   ------------------------------   EOF   ---------------------------------   #
