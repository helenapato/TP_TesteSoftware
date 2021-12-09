from flask import render_template,request,redirect
from app import app
from models.livro import db,Livro

@app.route('/livros/create/' , methods = ['GET','POST'])
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
        return redirect('/livros/')

@app.route('/livros/')
def listaLivros():
    livros = Livro.query.all()
    print(livros)
    return render_template('listaLivros.html',livros = livros)

@app.route('/livros/<int:id>/')
def showLivro(id):
    livro = Livro.query.filter_by(id=id).first()
    if livro:
        return render_template('showLivro.html', livro = livro)
    return f"Livro with id ={id} Doenst exist"

@app.route('/livros/<int:id>/update/',methods = ['GET','POST'])
def update(id):
    livro = Livro.query.filter_by(id=id).first()
    if livro:
        if request.method == 'POST':
        
            isbn = request.form['isbn']
            livro.setISBN(isbn)
        
            titulo = request.form['titulo']
            livro.setTitulo(titulo)

            autor = request.form['autor']
            livro.setAutor(autor)

            db.session.commit()
            return redirect(f'/livros/{id}/')
        return render_template('updateLivro.html', livro = livro)
    return f"Livro with id = {id} Does not exist"
 
@app.route('/livros/<int:id>/delete/', methods=['GET','POST'])
def delete(id):
    livro = Livro.query.filter_by(id=id).first()
    if livro:
        if request.method == 'POST':
            db.session.delete(livro)
            db.session.commit()
            return redirect('/livros/')
        return render_template('deleteLivro.html', livro = livro)
    
    return f"Livro with id = {id} Does not exist"