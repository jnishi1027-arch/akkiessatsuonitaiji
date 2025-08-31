from . import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_productions = con.execute('SELECT * FROM productions').fetchall()
    con.close()
    
    productions = []
    for row in db_productions:
        productions.append({'arrival_day': row[0], 'title': row[1], 'price': row[2]})
          
    return render_template(
        'index.html',
        productions=productions
    )
    
    
@app.route('/form')
def form():
    return render_template(
        'form.html'
    )
    
@app.route('/register', methods=['POST'])    
def register():
    arrival_day = request.form['arrival_day']
    title = request.form['title']
    price = request.form['price']
    
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO productions VALUES (?, ?, ?)',
                [arrival_day, title, price])
    con.commit()
    con.close()
    return redirect(url_for('index'))
