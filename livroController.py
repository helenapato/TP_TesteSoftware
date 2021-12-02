from flask import render_template,request,redirect
from app import app
from models.livro import db,Livro

@app.route('/livros/create' , methods = ['GET','POST'])
def createLivro():
    if request.method == 'GET':
        return render_template('createLivro.html')
 
    if request.method == 'POST':
        isbn = request.form['isbn']
        titulo = request.form['titulo']
        autor = request.form['autor']
        livro = Livro(isbn, titulo, autor)
        db.session.add(livro)
        db.session.commit()
        return redirect('/livros')

