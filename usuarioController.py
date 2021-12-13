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
        return 1
    biblioteca = unidadeBibliotecaController.UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if not biblioteca:
        return 2
    livro = livroBibliotecaController.LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN)
    if not livro:
        return 3
    
    retVal = livroBibliotecaController.livroFoiEmprestado(unidadeID, ISBN)
    if(retVal == 1):
        return 4
    if(retVal == 2):
        return 5
    emprestimoController.criarEmprestimo(ISBN, CPF, unidadeID, datetime.now())
    return 0

def devolverLivroUnidadeBiblioteca(CPF, unidadeID, ISBN):
    usuario = Usuario.query.filter_by(CPF=CPF).first()
    if not usuario:
        return 1
    biblioteca = unidadeBibliotecaController.UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if not biblioteca:
        return 2
    livro = livroBibliotecaController.LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN)
    if not livro:
        return 3
    
    livroBibliotecaController.livroFoiDevolvido(unidadeID, ISBN)
    emprestimoController.deletarEmprestimo(ISBN, CPF, unidadeID)

def reservarLivroUnidadeBiblioteca(CPF, unidadeID, ISBN):
    usuario = Usuario.query.filter_by(CPF=CPF).first()
    if not usuario:
        return 1
    biblioteca = unidadeBibliotecaController.UnidadeBiblioteca.query.filter_by(unidadeID=unidadeID).first()
    if not biblioteca:
        return 2
    livro = livroBibliotecaController.LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN)
    if not livro:
        return 3
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

@app.route('/usuarios/deletar/<int:CPF>/', methods=['GET', 'POST'])
def deletarUsuarioManual(CPF):
    usuario = Usuario.query.filter_by(CPF=CPF).first()
    if usuario:
        if request.method == 'GET':
            return render_template('deletarUsuario.html', usuario=usuario)
        
        if request.method == 'POST':
            deletarUsuario(CPF)
            return redirect('/usuarios/')

@app.route('/usuarios/emprestar/', methods=['GET', 'POST'])
def fazerEmprestimo():
    if request.method == 'GET':
        return render_template('fazerEmprestimo.html')
    
    if request.method == 'POST':
        CPF = request.form['CPF']
        unidadeID = request.form['unidadeID']
        ISBN = request.form['ISBN']
        resultadoEmprestimo = emprestarLivroUnidadeBiblioteca(CPF, unidadeID, ISBN)

        if resultadoEmprestimo == 1:
            return 'Não foi possível encontrar um usuário com este CPF'
        elif resultadoEmprestimo == 2:
            return 'Não foi possível encontrar esta biblioteca'
        elif resultadoEmprestimo == 3:
            return 'Não foi possível encontrar este livro'
        elif resultadoEmprestimo == 4:
            return 'Não há cópias deste livro disponíveis nesta biblioteca'
        elif resultadoEmprestimo == 5:
            return 'Não foi possível encontrar este livro nesta biblioteca'
        return redirect('/emprestimos/')

@app.route('/usuarios/reservar/', methods=['GET', 'POST'])
def fazerReserva():
    if request.method == 'GET':
        return render_template('fazerReserva.html')
    
    if request.method == 'POST':
        CPF = request.form['CPF']
        unidadeID = request.form['unidadeID']
        ISBN = request.form['ISBN']
    
    resultadoReserva = reservarLivroUnidadeBiblioteca(CPF, unidadeID, ISBN)
    if resultadoReserva == 1:
        return 'Não foi possível encontrar um usuário com este CPF'
    elif resultadoReserva == 2:
        return 'Não foi possível encontrar esta biblioteca'
    elif resultadoReserva == 3:
        return 'Não foi possível encontrar este livro'
    return redirect('/livros/')

@app.route('/usuarios/devolver/', methods=['GET', 'POST'])
def fazerDevolucao():
    if request.method == 'GET':
        return render_template('fazerDevolucao.html')
    
    if request.method == 'POST':
        CPF = request.form['CPF']
        unidadeID = request.form['unidadeID']
        ISBN = request.form['ISBN']
    
        resultadoDevolucao = devolverLivroUnidadeBiblioteca(CPF, unidadeID, ISBN)
        if resultadoDevolucao == 1:
            return 'Não foi possível encontrar um usuário com este CPF'
        elif resultadoDevolucao == 2:
            return 'Não foi possível encontrar esta biblioteca'
        elif resultadoDevolucao == 3:
            return 'Não foi possível encontrar este livro'
        return redirect('/livros/')