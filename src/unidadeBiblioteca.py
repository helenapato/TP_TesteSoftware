class UnidadeBiblioteca:

    def __init__(self, unidadeID, endereco, livros={}):
        self.unidadeID = unidadeID
        self.endereco = endereco
        # Livros será um dicionário cuja chave será o ISBN do livro e o valor será uma lista
        # a posição 0 da lista indica quantas cópias estão disponíveis e a posição 1 quantas estão alugadas
        self.livros = livros

    def getUnidadeID(self):
        return self.unidadeID

    def getEndereco(self):
        return self.endereco

    def getLivros(self):
        return self.livros

    def getCopiasDisponiveisLivro(self, ISBN):
        if(self.livroExisteUnidade(ISBN)):
            return self.livros[ISBN][0]
        return 0

    def getCopiasAlugadasLivro(self, ISBN):
        if(self.livroExisteUnidade(ISBN)):
            return self.livros[ISBN][1]
        return -1

    def setLivros(self, livrosNovo):
        self.livros = livrosNovo

    def livroExisteUnidade(self, ISBN):
        if(ISBN in self.livros):
            return True
        return False

    def adquirirLivro(self, ISBN, quantidade):
        if(self.livroExisteUnidade(ISBN)):
            self.livros[ISBN][0] += quantidade
        else:
            self.livros[ISBN] = [quantidade, 0]

    def atualizaContagemLivroAlugado(self, ISBN):
        self.livros[ISBN][0] -= 1
        self.livros[ISBN][1] += 1

    def atualizaContagemLivroDevolvido(self, ISBN):
        self.livros[ISBN][0] += 1
        self.livros[ISBN][1] -= 1

    def checaLivroDisponivel(self, ISBN):
        if(not self.livroExisteUnidade(ISBN)):
            return False
        if(self.livros[ISBN][0] > 0):
            return True
        return False

    def listaLivrosDisponiveis(self):
        livrosDisponiveis = []
        for ISBN in self.livros:
            if(self.checaLivroDisponivel(ISBN)):
                livrosDisponiveis.append(ISBN)
        return livrosDisponiveis


    def transferirLivroUnidade(self, ISBN, unidadeID, quantidade):
        #TODO
        print('TODO')

    def notificarUsuarioReservaDisponivel(self, ISBN, usuario):
        #TODO
        print('TODO')