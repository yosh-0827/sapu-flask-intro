import sqlite3

DATABASE = 'books.db'

def create_books_table():
    con = sqlite3.connect(DATABASE)    # conはコネクションオブジェクト（DBへのアクセス）
    con.execute("CREATE TABLE IF NOT EXISTS books (title, price, arrival_day)")       # 実行SQLを書く
    con.close()
