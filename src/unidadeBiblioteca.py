import sys

sys.path.insert(0, '../src')
from livroBiblioteca import LivroBiblioteca

class UnidadeBiblioteca:

    def __init__(self, unidadeID, endereco, livros={}):
        self.unidadeID = unidadeID
        self.endereco = endereco
        # Livros será um dicionário cuja chave será o ISBN do livro e o valor será um objeto livroBiblioteca
        self.livros = livros

    def getUnidadeID(self):
        return self.unidadeID

    def getEndereco(self):
        return self.endereco

    def getLivros(self):
        return self.livros

    def livroExisteUnidade(self, ISBN):
        if(ISBN in self.livros):
            return True
        return False

    def getCopiasDisponiveisLivro(self, ISBN):
        if(self.livroExisteUnidade(ISBN)):
            return self.livros[ISBN].getCopiasDisponiveis()
        return 0

    def getCopiasEmprestadasLivro(self, ISBN):
        if(self.livroExisteUnidade(ISBN)):
            return self.livros[ISBN].getCopiasEmprestadas()
        return -1

    def setLivros(self, livrosNovo):
        self.livros = livrosNovo

    def adquirirLivro(self, ISBN, quantidade):
        if(self.livroExisteUnidade(ISBN)):
            self.livros[ISBN].adquirirLivros(quantidade)
        else:
            self.livros[ISBN] = LivroBiblioteca(ISBN, quantidade)

    def livroFoiEmprestado(self, ISBN):
        self.livros[ISBN].livroFoiEmprestado()

    def livroFoiDevolvido(self, ISBN):
        self.livros[ISBN].livroFoiDevolvido()

    def checaLivroDisponivel(self, ISBN):
        if(not self.livroExisteUnidade(ISBN)):
            return False
        if(self.livros[ISBN].livroEstaDisponivel()):
            return True
        return False

    def listaLivrosDisponiveis(self):
        livrosDisponiveis = []
        for ISBN in self.livros:
            if(self.checaLivroDisponivel(ISBN)):
                livrosDisponiveis.append(ISBN)
        return livrosDisponiveis


    def transferirLivroUnidade(self, ISBN, unidade, quantidade):
        if(not self.livroExisteUnidade(ISBN)):
            raise Exception('Livro não existe nesta unidade')
        self.livros[ISBN].doarLivros(quantidade)
        unidade.adquirirLivro(ISBN, quantidade)

    def notificarUsuarioReservaDisponivel(self, ISBN, usuario):
        #TODO
        print('TODO')