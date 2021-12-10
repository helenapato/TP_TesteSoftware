from flask import render_template, request, redirect
from app import app
from models.emprestimo import db_emprestimo, Emprestimo
from datetime import datetime
# import time

def criarEmprestimo(ISBN, CPF, unidadeID, dataAluguel):
    emprestimo = Emprestimo(ISBN, CPF, unidadeID, dataAluguel)
    db_emprestimo.session.add(emprestimo)
    db_emprestimo.session.commit()

def deletarEmprestimo(ISBN, CPF, unidadeID):
    emprestimo = Emprestimo.query.filter(ISBN=ISBN, CPF=CPF, unidadeID=unidadeID).first()
    if emprestimo:
        db_emprestimo.session.delete(emprestimo)
        db_emprestimo.session.commit()
    else:
        return -1

def setDataDevolucaoReal(ISBN, CPF, unidadeID, dataDevolucaoReal):
    emprestimo = Emprestimo.query.filter(ISBN=ISBN, CPF=CPF, unidadeID=unidadeID).first()
    if emprestimo:
        emprestimo.setDataDevolucaoReal(dataDevolucaoReal)
    else:
        return -1

def calcularMulta(ISBN, CPF, unidadeID, dataCalculo):
    emprestimo = Emprestimo.query.filter(ISBN=ISBN, CPF=CPF, unidadeID=unidadeID).first()
    if emprestimo:
        return emprestimo.calcularMulta(dataCalculo)
    else:
        return -1

@app.route('/emprestimos/')
def listEmprestimos():
    emprestimos = Emprestimo.query.all()
    print(emprestimos)
    return render_template('listaEmprestimos.html', emprestimos=emprestimos)

@app.route('/emprestimos/create/', methods=['GET', 'POST'])
def criarEmprestimoManual():
    if request.method == 'GET':
        return render_template('createEmprestimo.html')
    
    if request.method == 'POST':
        ISBN = request.form['ISBN']
        CPF = request.form['CPF']
        unidadeID = request.form['unidadeID']
        # dataAluguel = request.form['dataAluguel']
        dataAluguel = datetime.now()
        emprestimo = Emprestimo(ISBN, CPF, unidadeID, dataAluguel)
        db_emprestimo.session.add(emprestimo)
        db_emprestimo.session.commit()
    return redirect('/emprestimos/')