from flask import render_template, request, redirect
from app import app
import livroBibliotecaController
import livroController
from models.unidadeBiblioteca import db_unidadeBiblioteca, UnidadeBiblioteca

# TODO Criar interface para todos

def criarUnidadeBiblioteca(unidadeID, endereco):
    biblioteca = UnidadeBiblioteca(unidadeID, endereco)
    db_unidadeBiblioteca.session.add(biblioteca)
    db_unidadeBiblioteca.session.commit()

def deletarUnidadeBiblioteca(unidadeID):
    biblioteca = UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if biblioteca:
        db_unidadeBiblioteca.session.delete(biblioteca)
        db_unidadeBiblioteca.session.commit()
    else:
        return -1

def setNovosParametrosBiblioteca(unidadeID, novoUnidadeID=None, novoEndereco=None):
    biblioteca = UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if biblioteca:
        if novoUnidadeID is not None:
            biblioteca.setUnidadeID(novoUnidadeID)
        if novoEndereco is not None:
            biblioteca.setEndereco(novoEndereco)
                
        db_unidadeBiblioteca.session.commit()       
    else:
        return -1

def transferirLivroUnidade(unidadeID_de, unidadeID_para, ISBN, quantidade):
    biblioteca_de = UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID_de).first()
    if not biblioteca_de:
        return 1 # Biblioteca de origem não existe
    biblioteca_para = UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID_para).first()
    if not biblioteca_para:
        return 2 # Biblioteca de destino não existe
    livro = livroBibliotecaController.LivroBiblioteca.query.filter_by(unidadeID=unidadeID_de, ISBN=ISBN)
    if not livro:
        return 3 # Livro não existe na biblioteca de origem
    
    retVal = livroBibliotecaController.doarLivros(unidadeID_de, ISBN, quantidade)
    if(retVal == 1):
        return 4 # Livros insuficientes para transferir
    livroBibliotecaController.adquirirLivros(unidadeID_para, ISBN, quantidade)

def comprarLivrosUnidade(unidadeID, ISBN, quantidade):
    biblioteca = UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if not biblioteca:
        return -1
    livroBibliotecaController.adquirirLivros(unidadeID, ISBN, quantidade)

@app.route('/unidades/')
def listarUnidadesBiblioteca():
    unidades = UnidadeBiblioteca.query.all()
    return render_template('listarUnidadesBiblioteca.html', unidades=unidades)

@app.route('/unidades/criar/' , methods = ['GET','POST'])
def criarUnidadeBibliotecaManual():
    if request.method == 'GET':
        return render_template('criarUnidadeBiblioteca.html')
 
    if request.method == 'POST':
        unidadeID = request.form['unidadeID']
        endereco = request.form['endereco']
        criarUnidadeBiblioteca(unidadeID, endereco)
        return redirect('/unidades/')

@app.route('/unidades/<int:unidadeID>/deletar/' , methods = ['GET','POST'])
def deletarUnidadeBibliotecaManual(unidadeID):
    biblioteca = UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if biblioteca:
        if request.method == 'GET':
            return render_template('deletarUnidadeBiblioteca.html', biblioteca=biblioteca)
    
        if request.method == 'POST':
            deletarUnidadeBiblioteca(unidadeID)
            return redirect('/unidades/')

@app.route('/unidades/<int:unidadeID>/livros/')
def listarLivrosBiblioteca(unidadeID):
    biblioteca = UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if biblioteca:
        livros = livroBibliotecaController.LivroBiblioteca.query.filter_by(unidadeID=unidadeID)
        if livros:
            lista_livros = {}
            for livro in livros:
                # Buscar as demais informações do livro na classe livro
                newLivro = livroController.Livro.query.filter_by(ISBN=livro.getISBN()).first()
                if newLivro:
                    lista_livros[livro.getISBN()] = [newLivro.getTitulo(), newLivro.getAutor()]
            return render_template('listarLivrosUnidadeBiblioteca.html', livros=livros, lista_livros=lista_livros, unidadeID=unidadeID)

@app.route('/unidades/<int:unidadeID>/livros/criar/' , methods = ['GET','POST'])
def criarLivroUnidadeBibliotecaManual(unidadeID):
    if request.method == 'GET':
        return render_template('criarLivroUnidadeBiblioteca.html')
 
    if request.method == 'POST':
        ISBN = request.form['ISBN']
        copiasDisponiveis = request.form['copiasDisponiveis']
        copiasEmprestadas = request.form['copiasEmprestadas']
        if copiasEmprestadas:
            livroBibliotecaController.criarLivroBiblioteca(unidadeID, ISBN, copiasDisponiveis, copiasEmprestadas)
        else:
            livroBibliotecaController.criarLivroBiblioteca(unidadeID, ISBN, copiasDisponiveis)
        return redirect(f'/unidades/{unidadeID}/livros/')