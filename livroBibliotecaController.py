from models.livroBiblioteca import db_livroBiblioteca, LivroBiblioteca
import livroController
import reservaController

def criarLivroBiblioteca(unidadeID, ISBN, copiasDisponiveis, copiasEmprestadas=None):
        if copiasEmprestadas is None:
            livro = LivroBiblioteca(unidadeID, ISBN, copiasDisponiveis, 0)
        else:
            livro = LivroBiblioteca(unidadeID, ISBN, copiasDisponiveis, copiasEmprestadas)

        db_livroBiblioteca.session.add(livro)
        db_livroBiblioteca.session.commit()

def deletarLivroBiblioteca(unidadeID, ISBN):
    livro = LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN).first()
    if livro:
        db_livroBiblioteca.session.delete(livro)
        db_livroBiblioteca.session.commit()
    else:
        return -1   

def setNovosParametrosLivroBiblioteca(unidadeID, ISBN, novoUnidadeID=None, novoISBN=None, novoCopiasDisponiveis=None, novoCopiasEmprestadas=None):
    livro = LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN).first()
    if livro:
        if novoUnidadeID is not None:
            livro.setUnidadeID(novoUnidadeID)
        if novoISBN is not None:
            livro.setISBN(novoISBN)    
        if novoCopiasDisponiveis is not None:
            livro.setCopiasDisponiveis(novoCopiasDisponiveis) 
        if novoCopiasEmprestadas is not None:
            livro.setCopiasEmprestadas(novoCopiasEmprestadas) 
                
        db_livroBiblioteca.session.commit()       
    else:
        return -1    

def adquirirLivros(unidadeID, ISBN, quantidade):
    livro = LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN).first()
    if livro:
        livro.adquirirLivros(quantidade)
        db_livroBiblioteca.session.commit()
    else:
        livroNovo = LivroBiblioteca(unidadeID, ISBN, quantidade)
        db_livroBiblioteca.session.add(livroNovo)
        db_livroBiblioteca.session.commit()

def doarLivros(unidadeID, ISBN, quantidade):
    livro = LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN).first()
    if livro:
        retValue = livro.doarLivros(quantidade)
        if(retValue):
            db_livroBiblioteca.session.commit()
            return 0
        else:
            return 1
    else:
        return 2

def livroFoiEmprestado(unidadeID, ISBN):
    livro = LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN).first()
    if livro:
        retValue = livro.livroFoiEmprestado()
        if(retValue):
            db_livroBiblioteca.session.commit()
            return 0
        else:
            return 1
    else:
        return 2

def livroFoiDevolvido(unidadeID, ISBN):
    livro = LivroBiblioteca.query.filter_by(unidadeID=unidadeID, ISBN=ISBN).first()
    if livro:
        retValue = livro.livroFoiDevolvido()
        if(retValue):
            db_livroBiblioteca.session.commit()
            reserva = reservaController.Reserva.query.filter_by(unidadeID=unidadeID, ISBN=ISBN).first()
            if reserva:
                reservaController.mudarDisponibilidade(unidadeID, ISBN)
            return 0
        else:
            return 1
    else:
        return 2
