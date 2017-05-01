"""This program implements book store functions"""
import sqlite3

#   ----------------------------   FUNCTIONS   -----------------------------   #

def connect(filename):
    """Function that initialize SQL table"""
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title \
    text, author text, year integer, isbn integer)")
    conn.commit()

    return conn

def insert(conn, title, author, year, isbn):
    """Function that inserts SQL values"""
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()

def view(conn):
    """Function that returns SQL array values"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")

    return cur.fetchall()

def search(conn, title='', author='', year='', isbn=''):
    """Function that searches SQL by given keys"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR \
    isbn =?", (title, author, year, isbn))

    return cur.fetchall()

def delete(conn, id):
    """Function that deletes from SQL defined value"""
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()

def update(conn, id, title, author, year, isbn):
    """Function that updates from SQL defined value"""
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()

#   ------------------------------   EOF   ---------------------------------   #
