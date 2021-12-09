from flask_sqlalchemy import SQLAlchemy

db_livroBiblioteca = SQLAlchemy()

class LivroBiblioteca(db_livroBiblioteca.Model):

    __tablename__ = 'livroBiblioteca_tb'

    unidadeID = db_livroBiblioteca.Column(db_livroBiblioteca.Integer, primary_key=True)
    ISBN = db_livroBiblioteca.Column(db_livroBiblioteca.Integer, primary_key=True)
    copiasDisponiveis = db_livroBiblioteca.Column(db_livroBiblioteca.Integer)
    copiasEmprestadas = db_livroBiblioteca.Column(db_livroBiblioteca.Integer)

    def __init__(self, unidadeID, ISBN, copiasDisponiveis, copiasEmprestadas=None):
        
        if(not self.checaValidadeISBN(ISBN)):
            raise Exception('ISBN inválido: deve ter exatamente 13 dígitos de 0 a 9')
        
        self.unidadeID = unidadeID
        self.ISBN = ISBN
        self.copiasDisponiveis = copiasDisponiveis

        if(copiasEmprestadas is None):
            self.copiasEmprestadas = 0
        else:
            self.copiasEmprestadas = copiasEmprestadas

    def checaValidadeISBN(self, ISBN):
        # ISBN deve conter apenas dígitos de 0 a 9
        if(not str(ISBN).isdecimal()):
            return False
        # ISBN deve conter 13 dígitos
        if(len(str(ISBN)) != 13):
            return False
        return True

    def getUnidadeID(self):
        return self.unidadeID
    
    def getISBN(self):
        return self.ISBN

    def getCopiasDisponiveis(self):
        return self.copiasDisponiveis

    def getCopiasEmprestadas(self):
        return self.copiasEmprestadas

    def getCopiasTotal(self):
        return self.copiasDisponiveis + self.copiasEmprestadas

    def setUnidadeID(self, novoID):
        self.unidadeID = novoID
    
    def setISBN(self, novoISBN):
        if(self.checaValidadeISBN(novoISBN)):
            self.ISBN = novoISBN

    def setCopiasDisponiveis(self, copiasNovo):
        self.copiasDisponiveis = copiasNovo

    def setCopiasEmprestadas(self, copiasNovo):
        self.copiasEmprestadas = copiasNovo

    def adquirirLivros(self, quantidade):
        self.copiasDisponiveis += quantidade

    def doarLivros(self, quantidade):
        if self.copiasDisponiveis >= quantidade:
            self.copiasDisponiveis -= quantidade
            return True
        else:
            return False

    def livroFoiEmprestado(self):
        if self.copiasDisponiveis > 0:
            self.copiasDisponiveis -= 1
            self.copiasEmprestadas += 1
            return True
        else:
            return False

    def livroFoiDevolvido(self):
        if self.copiasEmprestadas > 0:
            self.copiasDisponiveis += 1
            self.copiasEmprestadas -= 1
            return True
        else:
            return False
