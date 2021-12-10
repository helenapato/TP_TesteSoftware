from flask_sqlalchemy import SQLAlchemy
from datetime import date, timedelta

PERIODO_EMPRESTIMO = 15
VALOR_MULTA = 10

db_emprestimo = SQLAlchemy()

class Emprestimo(db_emprestimo.Model):

    __tablename__ = 'emprestimo_tb'
    ISBN = db_emprestimo.Column(db_emprestimo.Integer, primary_key=True)
    CPF = db_emprestimo.Column(db_emprestimo.Integer, primary_key=True)
    unidadeID = db_emprestimo.Column(db_emprestimo.Integer, primary_key=True)
    dataAluguel = db_emprestimo.Column(db_emprestimo.Date)
    dataDevolucaoPrevista = db_emprestimo.Column(db_emprestimo.Date)
    dataDevolucaoReal = db_emprestimo.Column(db_emprestimo.Date)

    def __init__(self, ISBN, CPF, unidadeID, dataAluguel):
        
        # self.checaValidadeParametrosEmprestimo(dataAluguel)

        self.ISBN = ISBN
        self.CPF = CPF
        self.unidadeID = unidadeID
        self.dataAluguel = dataAluguel
        self.dataDevolucaoPrevista = dataAluguel + timedelta(days=PERIODO_EMPRESTIMO)
        # self.dataDevolucaoPrevista = dataAluguel
        self.dataDevolucaoReal = None
    
    def checaValidadeParametrosEmprestimo(self, dataAluguel):
        if(not isinstance(dataAluguel, date)):
            raise Exception('A data do aluguel deve ser do tipo Data')
    
    def getISBN(self):
        return self.ISBN

    def getCPF(self):
        return self.CPF
    
    def getUnidadeID(self):
        return self.unidadeID
    
    def getDataAluguel(self):
        return self.dataAluguel
    
    def getDataDevolucaoPrevista(self):
        return self.dataDevolucaoPrevista

    def getDataDevolucaoReal(self):
        return self.dataDevolucaoReal
    
    def setDataDevolucaoReal(self, dataDevolucaoReal):
        if(not isinstance(dataDevolucaoReal, date)):
            raise Exception('A data real de devolução deve ser do tipo Data')

        if(dataDevolucaoReal < self.dataAluguel):
            raise Exception('A data real de devolução deve ser maior ou igual a data do aluguel')

        self.dataDevolucaoReal = dataDevolucaoReal
    
    def calcularMulta(self, dataCalculo):
        if(not isinstance(dataCalculo, date)):
            raise Exception('A data deve ser do tipo Data')

        if(dataCalculo <= self.dataDevolucaoPrevista):
            return 0
        else:
            atraso = (dataCalculo - self.dataDevolucaoPrevista).days
            return (atraso/10 * VALOR_MULTA)