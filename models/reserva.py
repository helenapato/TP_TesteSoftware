from flask_sqlalchemy import SQLAlchemy

db_reserva = SQLAlchemy()

class Reserva(db_reserva.Model):

    __tablename__ = 'Reserva_tb'

    unidadeID = db_reserva.Column(db_reserva.Integer, primary_key=True)
    ISBN = db_reserva.Column(db_reserva.Integer, primary_key=True)
    CPF = db_reserva.Column(db_reserva.Integer, primary_key=True)
    disponivel = db_reserva.Column(db_reserva.Boolean)

    def __init__(self, unidadeID, ISBN, CPF):

        self.checaValidadeParametrosReserva(ISBN, CPF)

        self.unidadeID = unidadeID
        self.ISBN = ISBN
        self.CPF = CPF
        self.disponivel = False

    def checaValidadeParametrosReserva(self, ISBN, CPF):
        if(not self.checaValidadeISBN(ISBN)):
            raise Exception('ISBN inválido: deve ter exatamente 13 dígitos de 0 a 9')
        
        if(not self.checaValidadeCPF(CPF)):
            raise Exception('CPF inválido: deve ter exatamente 11 dígitos de 0 a 9')

    def checaValidadeISBN(self, ISBN):
        # ISBN deve conter apenas dígitos de 0 a 9
        if(not str(ISBN).isdecimal()):
            return False
        # ISBN deve conter 13 dígitos
        if(len(str(ISBN)) != 13):
            return False
        return True

    def checaValidadeCPF(self, CPF):
        # CPF só pode conter dígitos de 0 a 9
        if(not str(CPF).isdecimal()):
            return False
        # Tamanho do CPF deve ser de exatamente 11 dígitos
        if(len(str(CPF)) != 11):
            return False
        return True

    def getUnidadeID(self):
        return self.unidadeID

    def getISBN(self):
        return self.ISBN

    def getCPF(self):
        return self.CPF

    def getDisponivel(self):
        return self.disponivel

    def setUnidadeID(self, novoUnidadeID):
        self.unidadeID = novoUnidadeID

    def setISBN(self, novoISBN):
        if(self.checaValidadeISBN(novoISBN)):
            self.ISBN = novoISBN

    def setCPF(self, novoCPF):
        if(self.checaValidadeCPF(novoCPF)):
            self.CPF = novoCPF

    def setDisponivel(self):
        self.disponivel = not self.disponivel
