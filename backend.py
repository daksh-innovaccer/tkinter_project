import sqlite3


def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, price INTEGER)")
    conn.commit()
    conn.close()


def backendInsert(title, author, year, price):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(null, ?,?,?,?)",
                (title, author, year, price))
    conn.commit()
    conn.close()


# connect()
# insert('ABC', 'author',2022, 1000)

def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * from book")
    rows=cur . fetchall()
    conn.close()
    return rows

print(view())

def search(title="", author="", year="", price=""):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book where title=? OR author=? OR year=? OR price=?", (title, author, year, price))
    rows=cur . fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE from book where id=?",(id, ))
    conn.commit()
    conn.close()

def update(title, author, year, price, id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE book set title=?, author=?, year=?, price=? where id=?", (title, author, year, price, id))
    conn.commit()
    conn.close()
