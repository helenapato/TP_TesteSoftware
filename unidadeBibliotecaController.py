from flask import render_template, request, redirect
from app import app
import livroBibliotecaController
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
        return -1
    biblioteca_para = UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID_para).first()
    if not biblioteca_para:
        return -1
    livro = livroBibliotecaController.LivroBiblioteca.query.filter_by(unidadeID=unidadeID_de, ISBN=ISBN)
    if not livro:
        return -1
    
    retVal = livroBibliotecaController.doarLivros(unidadeID_de, ISBN, quantidade)
    if(retVal == 1):
        return 'livros insuficientes para transferir'
    livroBibliotecaController.setNovosParametrosLivroBiblioteca(unidadeID_de, ISBN, novoUnidadeID=unidadeID_para)
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

@app.route('/unidades/deletar/' , methods = ['GET','POST'])
def deletarUnidadeBibliotecaManual():
    if request.method == 'GET':
        return render_template('deletarUnidadeBiblioteca.html')
 
    if request.method == 'POST':
        unidadeID = request.form['unidadeID']
        deletarUnidadeBiblioteca(unidadeID)
        return redirect('/unidades/')