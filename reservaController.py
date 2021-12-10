from models.reserva import db_reserva, Reserva

def criarReserva(unidadeID, ISBN, CPF):
        lista = Reserva(unidadeID, ISBN, CPF)
        db_reserva.session.add(lista)
        db_reserva.session.commit()

def deletarReserva(unidadeID, ISBN, CPF):
    reserva = Reserva.query.filter_by(unidadeID=unidadeID, ISBN=ISBN, CPF=CPF).first()
    if reserva:
        db_reserva.session.delete(reserva)
        db_reserva.session.commit()
    else:
        return -1

def mudarDisponibilidade(unidadeID, ISBN):
    reserva = Reserva.query.filter_by(unidadeID=unidadeID, ISBN=ISBN).first()
    if reserva:
        reserva.setDisponivel()
        db_reserva.session.commit()
    else:
        return -1

def setNovosParametrosReserva(unidadeID, ISBN, CPF, novoUnidadeID=None, novoISBN=None, novoCPF=None):
    reserva = Reserva.query.filter_by(unidadeID=unidadeID, ISBN=ISBN, CPF=CPF).first()
    if reserva:
        if novoUnidadeID is not None:
            reserva.setUnidadeID(novoUnidadeID)
        if novoISBN is not None:
            reserva.setISBN(novoISBN)    
        if novoCPF is not None:
            reserva.setCPF(novoCPF) 
                
        db_reserva.session.commit()       
    else:
        return -1



