from flask import render_template, request, redirect
from app import app
from models.livro import db_livro, Livro

def criarLivro(ISBN, titulo, autor):
    livro = Livro(ISBN, titulo, autor)
    db_livro.session.add(livro)
    db_livro.session.commit()

def deletarLivro(ISBN):
    livro = Livro.query.filter_by(ISBN=ISBN).first()
    if livro:
        db_livro.session.delete(livro)
        db_livro.session.commit()
    else:
        return -1

def setNovosParametrosLivro(ISBN, novoISBN=None, novoTitulo=None, novoAutor=None):
    livro = Livro.query.filter_by(ISBN=ISBN).first()
    if livro:
        if novoISBN is not None:
            livro.setISBN(novoISBN)
        if novoTitulo is not None:
            livro.setTitulo(novoTitulo)    
        if novoAutor is not None:
            livro.setAutor(novoAutor)
                
        db_livro.session.commit()       
    else:
        return -1

@app.route('/livros/create/' , methods = ['GET','POST'])
def createLivro():
    if request.method == 'GET':
        return render_template('createLivro.html')
 
    if request.method == 'POST':
        isbn = request.form['isbn']
        titulo = request.form['titulo']
        autor = request.form['autor']
        criarLivro(isbn, titulo, autor)
        return redirect('/livros/')

@app.route('/livros/')
def listaLivros():
    livros = Livro.query.all()
    return render_template('listaLivros.html',livros = livros)

@app.route('/livros/<int:ISBN>/')
def showLivro(ISBN):
    livro = Livro.query.filter_by(ISBN=ISBN).first()
    if livro:
        return render_template('showLivro.html', livro = livro)
    return f"Livro with ISBN ={ISBN} Doenst exist"

@app.route('/livros/<int:ISBN>/update/', methods = ['GET','POST'])
def update(ISBN):
    livro = Livro.query.filter_by(ISBN=ISBN).first()
    if livro:
        if request.method == 'POST':
        
            novoISBN = request.form['isbn']
            novoTitulo = request.form['titulo']
            novoAutor = request.form['autor']

            setNovosParametrosLivro(ISBN, novoISBN=novoISBN, novoTitulo=novoTitulo, novoAutor=novoAutor)
            return redirect(f'/livros/{ISBN}/')
        return render_template('updateLivro.html', livro = livro)
    return f"Livro with ISBN = {ISBN} Does not exist"
 
@app.route('/livros/<int:ISBN>/delete/', methods=['GET','POST'])
def deletarLivroManual(ISBN):
    livro = Livro.query.filter_by(ISBN=ISBN).first()
    if livro:
        if request.method == 'GET':
            return render_template('deleteLivro.html', livro = livro)
    
        if request.method == 'POST':
            deletarLivro(ISBN)
            return redirect('/livros/')
    return f"Livro com ISBN = {ISBN} não existe"