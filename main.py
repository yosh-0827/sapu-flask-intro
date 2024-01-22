from flask import Flask, request
from flask import render_template, redirect, url_for  #HTMLを使ってビジュを描画する

app = Flask(__name__)

import db
db.create_books_table()
import sqlite3
DATABASE = 'books.db'

@app.route('/')  #トップにアクセスしたらこのindex関数が呼ばれるようにする
def index():  # トップ画面にアクセスした時に実行される
    con = sqlite3.connect(DATABASE)
    db_books = con.execute('SELECT * FROM books').fetchall()    #fetchallでSELECTしたデータをpythonのリストオブジェクトとして取得する
    con.close()

    books = []
    for row in db_books:
        books.append({'title': row[0], 'price': row[1], 'arrival_day': row[2]})

    return render_template(
        'index.html',
        books=books      # 定義したbookオブジェクトをHTML側に渡す
    )

@app.route('/form')
def form():
    return render_template(
    'form.html'
)

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']     # requestにはPOSTで送られたHTMLで設定したinputの情報が入ってる
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?, ?, ?)',
                [title, price, arrival_day])
    con.commit()
    con.close()
    # 登録が終わったらトップに戻るようにする
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)