"""This is a introduction program to SQLite"""
import sqlite3

#   ----------------------------   FUNCTIONS   -----------------------------   #

def create_table(filename):
    """Function that initialize SQL table"""
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store( item TEXT, quantity INTEGER, \
    price REAL)")
    conn.commit()

    return conn

def insert(item, quantity, price, conn):
    """Function that insert SQL values"""
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()

def view(conn):
    """Function that returns SQL array values"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")

    return cur.fetchall()

def delete(item, conn):
    """Function that delete from SQL defined value"""
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()

def update(item, quantity, price, conn):
    """Function that updates from SQL defined value"""
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()

#   ------------------------------   MAIN   --------------------------------   #

CONN = create_table('../output/lite.db')
insert('Bread', 30, 1, CONN)
insert('Water Glass', 10, 5, CONN)
insert('Coffe Cup', 13, 7, CONN)
print('Before delete:\n', view(CONN))
delete('Coffe Cup', CONN)
print('After delete:\n', view(CONN))
update('Bread', 25, 3, CONN)
print('After update:\n', view(CONN))

CONN.close()

#   ------------------------------   EOF   ---------------------------------   #
