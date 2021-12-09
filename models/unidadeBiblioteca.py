from flask_sqlalchemy import SQLAlchemy

TAM_MAX_STR = 50

db_unidadeBiblioteca = SQLAlchemy()

class UnidadeBiblioteca(db_unidadeBiblioteca.Model):

    __tablename__ = 'unidadeBiblioteca_tb'

    unidadeID = db_unidadeBiblioteca.Column(db_unidadeBiblioteca.Integer, primary_key=True)
    endereco = db_unidadeBiblioteca.Column(db_unidadeBiblioteca.String(TAM_MAX_STR))

    def __init__(self, unidadeID, endereco):
        self.unidadeID = unidadeID
        self.endereco = endereco

    def getUnidadeID(self):
        return self.unidadeID

    def getEndereco(self):
        return self.endereco

    def setUnidadeID(self, novoID):
        self.unidadeID = novoID

    def setEndereco(self, novoEndereco):
        self.endereco = novoEndereco
