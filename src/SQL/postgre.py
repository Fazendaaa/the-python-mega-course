"""This is a introduction program to Postgre -- see this video for more info: \
https://www.youtube.com/watch?v=YyAEho7sDro -- ps: mute this video and watch it\
 with two times velocity"""
import psycopg2

#   ----------------------------   FUNCTIONS   -----------------------------   #

def create_table(filename):
    """Function that initialize SQL table"""
    conn = psycopg2.connect(filename)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store( item TEXT, quantity INTEGER,\
     price REAL)")
    conn.commit()

    return conn

def insert(item, quantity, price, conn):
    """Function that insert SQL values"""
    cur = conn.cursor()
    #   do not use "'%s'" % (variable) -- this mean that the DB could be open to
    #   SQL injections
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()

def view(conn):
    """Function that returns SQL array values"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")

    return cur.fetchall()

def delete(item, conn):
    """Function that delete from SQL defined value"""
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()

def update(item, quantity, price, conn):
    """Function that delete from SQL defined value"""
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()

#   ------------------------------   MAIN   --------------------------------   #

FILENAME = "dbname='postgres' "
USER = "user='postgres' "
PASSWORD = "password='postgres123' "
HOST = "host='localhost' "
PORT = "port='5432'"
CONN = create_table(FILENAME+USER+PASSWORD+HOST+PORT)

insert('Apple', 50, 1, CONN)
insert('Orange', 40, 2, CONN)
insert('Banana', 20, 3, CONN)
print('After insertions:\n', view(CONN))
delete('Orange', CONN)
print('After delete:\n', view(CONN))
update('Banana', 15, 3, CONN)
print('After update:\n', view(CONN))

CONN.close()

#   ------------------------------   EOF   ---------------------------------   #
