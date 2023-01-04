from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

#PERFECTED IMPLEMENTATION OF API IF YOU FORGET HOW THE CODE WORKS CONVERT EVERY INSTANCE OF BOOK TABLE TO BOOKI IN BOTH SCRIPTS

def db_connection():
    conn=None
    try:
        conn=pymysql.connect(host='sql7.freesqldatabase.com',database='sql7580274',user='sql7580274',password='fJXubzwYfd', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    except pymysql.Error as e:
        print(e)
    return conn


@app.route("/books", methods=['GET','POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()
    books=None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM book")
        books = [
            dict( id=row['id'], author= row['author'], language = row['language'], title=row['title'])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
        else:
            "No books found", 404
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        sql="""INSERT INTO book (author, language, title) VALUES (%s,%s,%s)"""
        cursor.execute(sql,(new_author,new_lang,new_title))
        conn.commit()
        return f"Book with the id: {cursor.lastrowid} created sucessfully",201 #

@app.route('/books/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book=None
    if request.method=="GET":
        cursor.execute("SELECT * FROM book WHERE id=%s",(id,))
        rows = cursor.fetchall()
        for r in rows:
            book=r
        if book is not None:
            return jsonify(book),200
        else:
            return "Something went wrong", 404
    if request.method=="PUT":
        sql="""UPDATE book SET title=%s,author=%s,language=%s WHERE id=%s"""
        updated_author = request.form['author']
        updated_lang = request.form['language']
        updated_title = request.form['title']
        updated_book={
            "id":id,
            "author":updated_author,
            "language":updated_lang,
            "title":updated_title
        }
        cursor.execute(sql,(updated_author,updated_lang,updated_title,id))
        conn.commit()
        return jsonify(updated_book)
    if request.method=="DELETE":
        sql="""DELETE FROM book WHERE id=%s"""
        cursor.execute(sql,(id,))
        conn.commit()
        return "The book with id: {} has been deleted".format(id),200
if __name__== "__main__":
    app.run()