from flask import render_template, request, redirect
from app import app
from models.usuario import db_usuario, Usuario
import unidadeBibliotecaController
import livroBibliotecaController
import reservaController
import emprestimoController

from datetime import datetime

# TODO Criar interface para todos

def criarUsuario(CPF, nome, email):
    usuario = Usuario(CPF, nome, email)
    db_usuario.session.add(usuario)
    db_usuario.session.commit()

def deletarUsuario(CPF):
    usuario = Usuario.query.filter_by(CPF=CPF).first()
    if usuario:
        db_usuario.session.delete(usuario)
        db_usuario.session.commit()
    else:
        return -1

def setNovosParametrosUsuario(CPF, novoCPF=None, novoNome=None, novoEmail=None):
    usuario = Usuario.query.filter_by(CPF=CPF).first()
    if usuario:
        if novoCPF is not None:
            usuario.setCPF(novoCPF)
        if novoNome is not None:
            usuario.setNome(novoNome)
        if novoEmail is not None:
            usuario.setEmail(novoEmail)            
                
        db_usuario.session.commit()       
    else:
        return -1

def emprestarLivroUnidadeBiblioteca(CPF, unidadeID, ISBN):
    usuario = Usuario.query.filter_by(CPF=CPF).first()
    if not usuario:
        return -1
    biblioteca = unidadeBibliotecaController.UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if not biblioteca:
        return -1
    livro = livroBibliotecaController.LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN)
    if not livro:
        return -1
    
    retVal = livroBibliotecaController.livroFoiEmprestado(unidadeID, ISBN)
    if(retVal == 1):
        return 'não há cópias disponíveis'
    if(retVal == 2):
        return 'essa unidade não tem esse livro'
    emprestimoController.criarEmprestimo(ISBN, CPF, unidadeID, datetime.now())

def devolverLivroUnidadeBiblioteca(CPF, unidadeID, ISBN):
    usuario = Usuario.query.filter_by(CPF=CPF).first()
    if not usuario:
        return -1
    biblioteca = unidadeBibliotecaController.UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if not biblioteca:
        return -1
    livro = livroBibliotecaController.LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN)
    if not livro:
        return -1
    
    livroBibliotecaController.livroFoiDevolvido(unidadeID, ISBN)
    emprestimoController.deletarEmprestimo(ISBN, CPF, unidadeID)

def reservarLivroUnidadeBiblioteca(CPF, unidadeID, ISBN):
    usuario = Usuario.query.filter_by(CPF=CPF).first()
    if not usuario:
        return -1
    biblioteca = unidadeBibliotecaController.UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if not biblioteca:
        return -1
    livro = livroBibliotecaController.LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN)
    if not livro:
        return -1
    reservaController.criarReserva(unidadeID, ISBN, CPF)

@app.route('/usuarios/')
def listarUsuarios():
    usuarios = Usuario.query.all()
    return render_template('listarUsuarios.html', usuarios=usuarios)

@app.route('/usuarios/cadastrar/', methods=['GET', 'POST'])
def cadastrarUsuario():
    if request.method == 'GET':
        return render_template('cadastrarUsuario.html')
    
    if request.method == 'POST':
        CPF = request.form['CPF']
        nome = request.form['nome']
        email = request.form['email']
        criarUsuario(CPF, nome, email)
        return redirect('/usuarios/')
